# Natural language processing course: `Translation assistant for legal terminology`

ReadMe (submission 2)
This project aims to improve legal text translation, using the Facebook NLLB-2000 translation model and  RAG.

Progress so far:

-Downloaded a folder from the DGT corpus, containing .tmx files.
-Converted them to one .csv file, keeping only ENG-SLO pairs.
-In Google Colab imported the .csv file and the Facebook NLLB-200 model.
-The model translated the English sentences into Slovenian.
-These translations were evaluated with BLEU, using the already
 existing Slovenian translations from the DGT legal corpus as a Gold standard.
-It scored 36.17 on the BLEU score, which clearly shows that
 there's space for improvement.

Link to the Google Colab Notebook: https://colab.research.google.com/drive/1WZ29Dq1oOFWCtlmHFMygo4PA-74L7Di_?usp=sharing

Files added:
- dgt_all.csv - the .csv file with ENG-SLO pairs
- Google_colab_notebook_(cells_not_run).ipynb - conversion pipeline (clean, non-executed version)
- tmx_to_csv_conversion.py - the code used to convert the .tmx files into "dgt_all.csv".

To be done:
- Use Retrieval Augmented Generation (RAG) to improve the quality of the model's translation
- Compare RAG-enhanced model to baseline BLEU score.
