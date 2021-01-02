import pandas as pd
import datetime
#creating the variable with dates ,and from that extract the week day
#let us create a list of dates  with 20days difference from today and then tranform into a dataframe
df_base=datetime.datetime.today()
df_date_list=[df_base-datetime.timedelta(days=x)for x in range(0,20)]
df=pd.DataFrame(df_date_list)
#print(df)
df.columns=['day']
print(df)
print('EXTRACTING THE WEEK DAY NAME')
df['day_of_week']=df['day'].dt.weekday_name
print(df.head())
#engineering categorical  variable by ordinal  number replacement


weekday_map={'Monday':1,
             'Tuesday':2,
             'Wednesday':3,
             'Thursday':4,
             'Friday':5,
             'Saturday':6,
             'Sunday':7
             }
df['day_ordinal']=df.day_of_week.map(weekday_map)
print(df.head(20))