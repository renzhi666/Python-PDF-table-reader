import tabula
import time
import pandas as pd
import numpy as np
import os
import glob
key_word = "keyword"
column_name ="name"
outputdata = pd.DataFrame([])
mylist = [f for f in glob.glob("*.pdf")]
for alist in mylist:

    print(alist)


    path = os.path.join(os.getcwd(), alist)
    df = tabula.read_pdf(path, encoding='utf-8', pages='all')

    outputdata = outputdata.append(df.loc[lambda df: df.column_name ==key_word, :])
  
    
print(outputdata)

outputdata.to_csv(os.path.join(os.getcwd(), "output.csv"))
