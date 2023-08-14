import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

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

gI = clean_data.Good_Income
correlation_gI_dP   =   np.corrcoef(gI,dP)
print(correlation_gI_dP)

plt.figure()
plt.scatter(gI,dP)
plt.xlabel('Good Income')
plt.ylabel('Divorce Probability')
plt.legend
plt.show

X_love = df['Love'].values.reshape(-1,1)
Y_dP = df['Divorce_Probability'].values

model = LinearRegression()
model.fit(X_love,Y_dP)

slope = model.coef_[0]
intercept   =   model.intercept_
plt.figure()
plt.scatter(X_love,Y_dP)
plt.plot(X_love,slope * X_love + intercept, color='red',label='Linear Regression Line')
plt.xlabel('Love')
plt.ylabel('Divorce Probability')
plt.show()

X_gI = df['Good_Income'].values.reshape(-1,1)
Y_dP = df['Divorce_Probability'].values

model = LinearRegression()
model.fit(X_gI,Y_dP)

slope = model.coef_[0]
intercept   =   model.intercept_
plt.figure()
plt.scatter(X_gI,Y_dP)
plt.plot(X_gI,slope * X_gI + intercept, color='red',label='Linear Regression Line')
plt.xlabel('Good Income')
plt.ylabel('Divorce Probability')
plt.show()
 
correlation_gI_Love = np.corrcoef(gI,Love)
print(correlation_gI_Love)

X_Inc = df["Good_Income"].values.reshape(-1,1)
Y_love= df["Love"].values
model =  LinearRegression()

model.fit(X_Inc,Y_love)
slope = model.coef_[0]
intercept = model.intercept_

plt.figure
plt.scatter(Love,gI, label="Good Income vs Love")
plt.plot(X_gI,slope*X_gI+intercept, color='red', label="Linear Regression Line")
plt.xlabel('Good Income')
plt.ylabel('Love')
plt.show()

from causalinference.causal import CausalModel
causal_dPgI = CausalModel(gI,dP)

causal_dPgI.est_via_ols()
print(causal_dPgI.estimates)



'''from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)
'''

