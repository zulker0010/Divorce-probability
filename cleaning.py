import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',-1)
clean_data = pd.read_excel(r'F:\Data Analytics\Divorce probability\Divorce-probability\Marriage_Divorce_DB.xlsx', sheet_name='Marriage_Divorce_DB')

print(clean_data)
clean_data.head()