import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',None)
clean_data = pd.read_excel(r'F:\Data Analytics\Divorce probability\Divorce-probability\Marriage_Divorce_DB.xlsx', sheet_name='Marriage_Divorce_DB')

df = pd.DataFrame(clean_data)

print(clean_data)
##clean_data.head()
##clean_data.median()

Love = clean_data.Love
dP = clean_data.Divorce_Probability

plt.scatter(Love,dP)
plt.xlabel('Love')
plt.ylabel('Divorce Probability')
plt.legend
plt.show

correlation_Love_dP = np.corrcoef(Love,dP)
print(correlation_Love_dP)

Income = clean_data.Good_Income
correlation_Income_dP   =   np.corrcoef(Income,dP)
print(correlation_Income_dP)

plt.figure()
plt.scatter(Income,dP)
plt.xlabel('Income')
plt.ylabel('Divorce Probability')
plt.legend
plt.show





'''from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)
'''

