# comparable_corpus_Wablieft_deStandaard

This repo contains the relevant notebooks for my master's dissertation on the creation of the comparable corpora between easy-to-read Dutch Wablieft and De Standaard.

create_dataframes.ipynb creates the dataframe used by the other notebooks.
ScoreArticles.ipynb is the notebook used to manually score Wablieft articles and their 3 most similar de Standaard articles 
RobBERT_finetune.ipynb fine-tunes the existing two models on the manually scored Wablief - De Standaard data
  The training - dev - test datasets used can be found in the traindevtest folder
  The notebooks fine-tuned in this notebook are:
    
    pdelobelle/robbert-v2-dutch-base (https://huggingface.co/pdelobelle/robbert-v2-dutch-base)
    jegormeister/robbert-v2-dutch-base-mqa-finetuned (https://huggingface.co/jegormeister/robbert-v2-dutch-base-mqa-finetuned)
    
    
RobBERT.ipynb creates sentence embeddings for each model and calculates the similarity
  Here, the first similarity dictionaries (comparable corpora) are created for later reuse
  There is also a print function to print the articles from a similarity dictionary. This is used to manually evaluate article pairs and their similarity scores from the fine-tuned models
data_exploration.ipynb is used to explore the basic dataset and the sentence embeddings obtained from RobBERT.ipynb

logreg.ipynb explores the thresholding and classification models

