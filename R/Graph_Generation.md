# Modality Graph Generation

## Introduction

This R Markdown file generates K Nearest Neighbour graphs for different
modalities in a given dataset.

### Setup - Insert Libraries

    source('~/MOGDx/R/preprocess_functions.R')

### Load Data, Specify Locations, Projects and Modalities

    trait = 'paper_BRCA_Subtype_PAM50'
    dataset = 'TCGA'
    project = 'BRCA'
    for (modality in c( 'mRNA'  )) {
      
      print(modality)
      load(paste0('./../data/',dataset , '/raw/', project ,'/',modality,'_processed.RData'))
        
      if (modality %in% c('miRNA' , 'mRNA')) {
        g <- expr.to.graph(datExpr , datMeta , trait , top_genes , modality)
      } else if (modality == 'DNAm') {
        g <- expr.to.graph(datExpr , datMeta , trait , cpg_sites , modality)
      } else if (modality == 'CNV') {
        g <- expr.to.graph(log(datExpr) , datMeta , trait , cnv_sites , modality)
      } else if (modality == 'RPPA') { 
        g <- expr.to.graph(datExpr , datMeta , trait , protein_sites , modality)
      } else if (modality == 'CSF') { 
        g <- expr.to.graph(datExpr , datMeta , trait , csf_sites , modality)
      } else if (modality == 'MOCA') { 
        g <- expr.to.graph(datExpr , datMeta , trait , q_sites , modality)
      } else if (modality == 'MDS-UPDRS') { 
        g <- expr.to.graph(datExpr , datMeta , trait , p_sites , modality)
      } else if (modality == 'Parkinsonism') {
        g <- expr.to.graph(datExpr , datMeta , trait , park_sites , modality)
      } else if (modality == 'Clinical') {
        g <- expr.to.graph(datExpr , datMeta , trait , clin_sites , modality)
      } else if (modality == 'SNP') {
        g <- expr.to.graph(datExpr , datMeta , trait , snp_sites , modality)
      }
      
      write.csv(g, file = paste0('./../data/',dataset , '/raw/', project , '/output/',modality,'_graph.csv'))
      write.csv(datExpr , file = paste0('./../data/',dataset , '/raw/', project , '/output','/datExpr_', modality , '.csv'))
      write.csv(datMeta , file = paste0('./../data/',dataset , '/raw/', project , '/output','/datMeta_', modality , '.csv'))
      
    }

    ## [1] "mRNA"
    ## [1] 2484 1047

```{image} ./../images/mRNA_graph.png
:alt: fishy
:width: 1200px
:align: center
```
