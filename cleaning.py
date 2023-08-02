import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',None)
clean_data = pd.read_excel(r'F:\Data Analytics\Divorce probability\Divorce-probability\Marriage_Divorce_DB.xlsx', sheet_name='Marriage_Divorce_DB')

pd.DataFrame(clean_data)

print(clean_data)
##clean_data.head()
##clean_data.median()

x   =  clean_data.Divorce_Probability.values.reshape(-1,1)
y   =  clean_data.Love.values
#plt.scatter(x,y)
#plt.show

##np.corrcoef(x,y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
model   =   LinearRegression()
model.fit(x,y)
slope=model.coef_(0)
intercept   =   model.intercept_
plt.scatter(x,y,label="Linear Regression of Divorce Probability vs Love")
plt.plot(x, slope * x + intercept, color='black', label="Regression line")
plt.xlabel('Divorce Probability')
plt.ylabel('Love')


