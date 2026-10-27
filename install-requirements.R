options(repos = c(CRAN = "https://cloud.r-project.org"))

if (!requireNamespace("remotes", quietly = TRUE)) install.packages("remotes")

versions <- c(
  scCustomize = "3.0.1", Seurat = "5.1.0", SeuratObject = "5.1.0",
  ggpubr = "0.6.3", RApiSerialize = "0.1.4", stringfish = "0.16.0",
  Rcpp = "1.1.1-1.1", BH = "1.90.0-1", RcppParallel = "5.1.11-2",
  devtools = "2.4.5", pheatmap = "1.0.13", reshape2 = "1.4.5",
  tibble = "3.3.1", ggrepel = "0.9.8", readxl = "1.5.0"
)
for (package in names(versions)) {
  remotes::install_version(package, version = versions[[package]], upgrade = "never")
}

if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")
BiocManager::install(c("BiocNeighbors", "ComplexHeatmap", "Biobase"), ask = FALSE, update = FALSE)
remotes::install_version("qs", version = "0.27.3", upgrade = "never")
install.packages("registry")
remotes::install_version("pkgmaker", version = "0.32.10", upgrade = "never")
install.packages("NMF")
remotes::install_github("jinworks/CellChat", upgrade = "never")
remotes::install_version("ggplot2", version = "3.5.2", upgrade = "never")
