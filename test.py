from glob import glob
import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getcwd(),'modified_fifa.csv'))
print(df.head(5))