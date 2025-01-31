---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Running on Command Line
For parallel training of multiple models on a cluster, the interactive MOGDx notebook was modularised and optimised. The setup between the R and Python workflows differ slightly, thus two command line interfaces are provided. 

## Setup from R Workflow
Ensure all expression and meta files for all modalities are in a single folder with naming convention `modality_datExpr.csv`/`modality_datMeta.csv` e.g. `mRNA_datExpr.csv`/`mRNA_datMeta.csv`. 

Ensure all graph/network files are in a single folder with naming convention `modality_graph.csv` e.g. `mRNA_graph.csv`

If performing an analysis on integrated modalities ensure all expression and meta files for the integrated modalities are in the folder. 

e.g. if analysing mRNA & miRNA, ensure mRNA_miRNA_graph.csv , datMeta_mRNA.csv, datMeta_miRNA.csv, datExpr_mRNA.csv and datExper_miRNA.csv are in the same folder. 

This process will have been done automatically by the creation of the raw folder and running of SNF.R and it is easiest to retain this folder.

## Setup from Python Workflow
Ensure all pkl files are in a single folder with naming convention `{modality}_processed.pkl` e.g. `mRNA_processed.pkl`. 

Ensure all graph/network files are in a single folder with naming convention `{modality}_graph.csv` e.g. `mRNA_graph.csv`. 

If performing an analysis on integrated modalities ensure all expression and meta files for the integrated modalities are in the correct folder. 

## Execution Command

MOGDx is a command line tool. A sample command is : \
`python MOGDx.py -i "/raw_data/raw_BRCA" -o "./Output/BRCA/"  -mod "mRNA" "miRNA" --R  --n-splits 5 -ld 32 16 --target "paper_BRCA_Subtype_PAM50" --index-col "patient" --epochs 2000 --lr 0.001 --h-feats 64 --decoder-dim 64`

-i is the location of the raw data containing all datExpr, datMeta and graph.csv files \
-o is the location where the output will be printed \
-mods is the modalities to include in the integration  \
--R specifies that the data was generated using the R workflow (default Python) \
--n-splits is the number of cross validation splits \
-ld is the latent dimension per modality. It is order alphabetically thus, mRNA will be compressed to dim of 32 and miRNA to 16  \
--target is the phenotype being classified \
--index-col is the column containing the patient ids  

All other arguments are related to the Graph Convolutional Network with Multi Modal Encoder