## Manuscript
[Integrated transcriptional and spatial profiling identifies CTHRC1+ fibroblasts as fibrogenic signaling hubs in human lung fibrosis](https://www.biorxiv.org/content/10.64898/2026.04.08.717092v1)
Authors: Natalia-Del Pilar Vanegas, Hu Chen, Jack Wellmerling, Ahmed Ghobashi, Mahnoor Hamid, Victor Peters, Chandani Sen, Brenda F. Reader, Konstantin Shilo, Brigitte N. Gomperts, Qin Ma, Ana Mora, Daniel Tschumperlin, Mauricio Rojas. Vanegas and Chen contributed equally; Rojas is the corresponding author.


## Abstract
Lung mesenchymal cells are key regulators of tissue homeostasis and extracellular matrix (ECM) remodeling, and their aberrant activation drives the progressive parenchymal scarring characteristic of idiopathic pulmonary fibrosis (IPF), a fatal disease with limited therapeutic options. Despite their central pathogenic role, lung mesenchymal cells are difficult to isolate due to their embedded position within the ECM, and standard in vitro culture conditions may lead to the loss of their native functional and transcriptional characteristics, hampering the study of mesenchymal behavior in disease. The transcriptional heterogeneity of lung mesenchymal subtypes and the extent to which culture-induced alterations diverge from native tissue signatures remain poorly understood. Here, we integrated single-cell RNA sequencing (scRNA-seq) and spatial transcriptomics of native lung tissue from IPF patients and age-matched healthy donors with transcriptomic profiling of cultured mesenchymal cells collected at passages 1 and 6 after isolation using three optimized protocols: whole lung cell suspension (WLCS), negative fraction enrichment, and outgrowth.

Native tissue-based analysis identified six transcriptionally distinct mesenchymal subtypes: alveolar, adventitial, inflammatory, peribronchial, CTHRC1+ and smooth muscle cell (SMC). The fibroblast subtype CTHRC1+ represented the most transcriptionally activated pro-fibrotic subtype, showing the greatest upregulation of ECM biosynthesis genes, a prominent role in intercellular communication, and preferential enrichment within fibroblastic foci in IPF lung tissue. Pseudotime trajectory analysis supported a directional transcriptional continuum from alveolar and inflammatory fibroblasts toward the CTHRC1+ state, driven by coordinated activation of pro-fibrotic transcription factors, including RUNX2, CREB3L1, and NFATC1. In vitro culture progressively reshaped mesenchymal transcriptional identity relative to native tissue, with increased collagen and matrix metalloproteinase (MMP) expression during passaging, loss of distinct CTHRC1+ fibroblasts, and gain of alveolar fibroblasts displaying pro-fibrotic activation across all isolation protocols.

These findings provide a high-resolution transcriptional map of lung mesenchymal heterogeneity in IPF and highlight critical limitations of standard in vitro culture systems for recapitulating native mesenchymal diversity, with important implications for the development and evaluation of mesenchymal-targeted therapeutic strategies in IPF.

## Repository contents

- `code/`: Jupyter notebooks and R Markdown scripts for the figure analyses, plus their rendered HTML reports and `helper.py`, a shared plotting function. Each script is listed in the figure map below.
- `data/`: input data for the analysis code, uploaded to Code Ocean.
- `results/`: generated figures, organized into a folder for each figure or supplementary figure.

## Data download

The study data are associated with GEO accessions [GSE283885](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE283885), [GSE331286](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE331286), [GSE331144](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE331144), and [GSE334010](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE334010). Open each series page and download the available processed files using its **Supplementary files** links. For raw sequencing data, follow any SRA links on the series or sample pages.

## Software environment

The analyses use R 4.5.2 and Python 3.10.8. The Python packages are listed in `requirements.txt` and can be installed with `pip install -r requirements.txt`.

To install the R packages, run the following command from the repository root:

```bash
Rscript install-requirements.R
```

## Script-to-figure map

Paths are relative to `code/`; panel labels follow the scripts. HTML files with matching names are rendered versions of the R Markdown reports.

| Script | Figure panels |
| --- | --- |
| `Fig_1.ipynb` | Figure 1b–g |
| `Fig_2.Rmd` | Figure 2a–f |
| `Fig_4.Rmd` | Figure 4a–d |
| `Fig_5.ipynb` | Figure 5b–e |
| `Fig_6.ipynb` | Figure 6b–d |
| `Fig_6f.Rmd` | Figure 6f |
| `Fig_7a.ipynb` | Figure 7a |
| `Fig_7bc_Supplementary_8.Rmd` | Figure 7b–c and Supplementary Figure 8 |
| `Fig_8.ipynb` | Figure 8a–c |
| `Fig_9.ipynb` | Figure 9a–c |
| `Supplementary_Fig_1.Rmd` | Supplementary Figure 1a–d |
| `Supplementary_Fig_2abc.Rmd` | Supplementary Figure 2a–c |
| `Supplementary_Fig_2de.ipynb` | Supplementary Figure 2d–e |
| `Supplementary_Fig_3.Rmd` | Supplementary Figure 3a–f |
| `Supplementary_Fig_4.Rmd` | Supplementary Figure 4a–b |
| `Supplementary_Fig_4c.ipynb` | Supplementary Figure 4c |
| `Supplementary_Fig_5.Rmd` | Supplementary Figure 5a–c |
| `Supplementary_Fig_6.Rmd` | Supplementary Figure 6a–c |
| `Supplementary_Fig_7.Rmd` | Supplementary Figure 7 |
| `Supplementary_Fig_7.ipynb` | Supplementary Figure 7 |

## Run order

1. Download the raw datasets from GEO using the accessions above.
2. Annotate cell lineages and fibroblast subtypes using the markers shown in Figure 1 and `code/Fig_1.ipynb`, see the manuscript for details of the analysis and annotation process.
3. Run the notebook cells or R Markdown chunks in order for the desired figures.

## Citation
If you use this code, please cite the manuscript:

Integrated transcriptional and spatial profiling identifies CTHRC1+ fibroblasts as fibrogenic signaling hubs in human lung fibrosis. bioRxiv (2026). https://www.biorxiv.org/content/10.64898/2026.04.08.717092v1
