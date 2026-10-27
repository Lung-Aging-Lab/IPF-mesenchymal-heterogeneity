from matplotlib.ticker import FuncFormatter, MaxNLocator
import pandas as pd
import matplotlib.pyplot as plt
def plot_ct_density(adata, group_key='group', groups=None, ct_key='cell_group', show_pct=False, figsize=(10, 6),
                   title='Cell Type Composition per Group', pct_fontsize=10):
    if isinstance(groups, str):
        groups = [groups]

    if groups is not None:
        adata = adata[adata.obs[group_key].isin(groups)].copy()
    else:

        
        
        groups = list(adata.obs[group_key].unique())

    # print(f"Comparison of {groups}")

    # Ensure group_key is categorical with proper order
    if hasattr(adata.obs[group_key], 'cat'):
        group_order = adata.obs[group_key].cat.categories.tolist()
        groups = [g for g in group_order if g in groups]
    else:
        groups = sorted(groups)

    # Keep original category order
    if hasattr(adata.obs[ct_key], 'cat'):
        sorted_cell_types = adata.obs[ct_key].cat.categories.tolist()
    else:
        overall_counts = adata.obs[ct_key].value_counts()
        sorted_cell_types = overall_counts.index.tolist()
        all_cell_types = sorted(adata.obs[ct_key].unique())
        for ct in all_cell_types:
            if ct not in sorted_cell_types:
                sorted_cell_types.append(ct)

    data_pct = {}
    data_count = {}

    for g in groups:
        subset = adata[adata.obs[group_key] == g]
        if len(subset) > 0:
            pct = subset.obs[ct_key].value_counts(normalize=True) * 100
            count = subset.obs[ct_key].value_counts()
            pct = pct.reindex(sorted_cell_types, fill_value=0)
            count = count.reindex(sorted_cell_types, fill_value=0)
        else:
            pct = pd.Series(0, index=sorted_cell_types)
            count = pd.Series(0, index=sorted_cell_types)

        data_pct[g] = pct
        data_count[g] = count

    df_pct = pd.DataFrame(data_pct).T
    df_count = pd.DataFrame(data_count).T

    # Ensure color mapping matches category order
    if f'{ct_key}_colors' in adata.uns:
        color_list = adata.uns[f'{ct_key}_colors']
        if len(color_list) != len(sorted_cell_types):
            if hasattr(adata.obs[ct_key], 'cat'):
                original_order = adata.obs[ct_key].cat.categories.tolist()
                color_dict = dict(zip(original_order, adata.uns[f'{ct_key}_colors']))
                color_list = [color_dict.get(ct, 'gray') for ct in sorted_cell_types]
            else:
                color_list = adata.uns[f'{ct_key}_colors'][:len(sorted_cell_types)]
    else:
        try:
            from scanpy.plotting.palettes import default_20
            color_list = sns.color_palette(default_20, n_colors=len(sorted_cell_types))
        except:
            color_list = sns.color_palette("tab20", n_colors=len(sorted_cell_types))

    # Create figure explicitly
    fig, ax = plt.subplots(figsize=figsize)
    df_pct.loc[groups].plot(kind='barh', stacked=True, color=color_list, width=0.6, ax=ax)
    
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0f}%"))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    ax.set_xlim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0f}%"))

    ax.set_ylabel(group_key)
    ax.set_xlabel('Percentage (%)')
    ax.set_title(title)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    legend = ax.legend(
        title=ct_key,
        loc='center left',
        bbox_to_anchor=(1.0, 0.5), 
        frameon=False
    )
    legend.set_title(None)

    ax.set_xlabel(None)
    ax.set_ylabel(None)

    if show_pct:
        for i, group in enumerate(df_pct.index):
            cumulative_width = 0
            for ct in df_pct.columns:
                pct = df_pct.loc[group, ct]
                n = df_count.loc[group, ct]
                if pct > 5:
                    ax.text(cumulative_width + pct / 2, i, f'{pct:.1f}%\n(n={n})',
                            va='center', ha='center', color='black', fontsize=pct_fontsize)
                cumulative_width += pct

    ax.invert_yaxis()
    plt.tight_layout()

    df_summary = df_pct.round(2).copy()
    for col in df_summary.columns:
        df_summary[col] = df_summary[col].astype(str) + '% (n=' + df_count[col].astype(int).astype(str) + ')'

    return fig, df_summary.loc[groups]