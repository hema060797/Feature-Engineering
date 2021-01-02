import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
use_cols=['loan_amnt','int_rate','annual_inc','open_acc','loan_status','open_il_12m']
#df=pd.read_csv('G:/Major Project/loan.csv',usecols=use_cols)
#print(df.head())
#print(df.dtypes)

data=pd.read_csv('G:/Major Project/loan.csv',usecols=use_cols).sample(10000,random_state=44)
#sample have 2 parameters one is no of records,second is seed for reproducibility
print(data.head())
print(data.shape)

print('CONTINOUS VARIABLE')
#lets look at the values  of the variable loan_amnt this is amount of money required by borrower in US dollar
print(data.loan_amnt.unique())

#lets make an histogram to get familiar with the distribution of the variable
fig=data.loan_amnt.hist(bins=10)
fig.set_title('Loan amount requested')
fig.set_xlabel('Loan Amount')
fig.set_ylabel('Number of loans')#749 got 5000 rs loan amt


print('Discrete variable')
print(data.open_acc.dropna().unique())
#print(data1)
data.open_acc.hist(bins=10)
plt.set_xlim(0,30)
plt.set_title('No of open accounts')
plt.set_xlabel('No of open accounts')
plt.set_ylabel('Number of customers')



print(data.open_il_12m.unique())

fig=data.open_il_12m.hist(bins=50)
fig.set_title('Number of installment accounts opened in past 12 months')
fig.set_xlabel('Number of installment accounts opened in past 12 months')
fig.set_ylabel('Number of borrowers')
