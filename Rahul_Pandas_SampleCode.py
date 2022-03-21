'''
Sample code given by by Dr. Rahul Sharma 
about using pandas to read csv/tsv files and 
some basic manipulations
'''

import pandas as pd
df = pd.read_csv(“path/to/file.tsv”, sep=‘\t’)
df=pd.read_csv(‘path/to/filetsv’,sep=“\t’ encoding="the encoding that was returned")
df[‘column_nam”].head()
df.head()
df1 = df[df[‘col_name’]==‘GBM’]
df1.to_csv(‘path/tofile/nameoffie.csv’, index=False)
