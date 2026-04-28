ReadMe (submission 2)
This project aims to improve the NLLB translation model with RAG.

Progress so far:

-Downloaded a folder from the DGT corpus, containing .tmx files.
-Converted them to one .csv file, keeping only ENG-SLO pairs.
-In Google Colab imported the .csv file and the NLLB model.
-The model translated the English sentences into Slovenian.
-These translations were evaluated with BLEU, using the already
 existing Slovenian translation as a Gold standard.
-It scored 36.17 on the BLEU score, which clearly shows that
 there's space for improvement.


Files added:
- dgt_all.csv - the .csv file with ENG-SLO pairs
- Google_colab_notebook_(cells_not_run).ipynb - conversion pipeline (clean, non-executed version)
- tmx_to_csv_conversion.py - the code used to convert the .tmx files into "dgt_all.csv".