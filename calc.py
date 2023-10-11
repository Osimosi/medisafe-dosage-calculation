import pandas as pd
import numpy as np

# ask file name from user

print("name dat file boah: ")
file_name = input() + '.csv'

# read csv file
df = pd.read_csv(file_name)

#cleaning data

# drop columns
df.drop(['Notes'] , axis = 1 , inplace = True)
df.drop(['Type'] , axis = 1 , inplace = True)
df.drop(['Recorded on'] , axis = 1 , inplace = True)
df.drop(['Scheduled for'] , axis = 1 , inplace = True)

df.rename(columns = {'Name' : 'Dosage (mg)' , 'Value' : 'Status'} , inplace = True)


#drop entire nan rows

df.dropna(how = 'all' , inplace = True)

#throw error for any nan values in the cleaned dataframe

if df.isnull().values.any():
    raise ValueError('Null values found in the dataframe, gimme clean data you peasant. *whip whip*\n\n')


# encoding string to int

# status column, replace skipped & missed with 0, taken with 1
df['Status'].replace('Skipped' , 0 , inplace = True)
df['Status'].replace('Missed' , 0 , inplace = True)
df['Status'].replace('Taken' , 1 , inplace = True)

# dosage column
df['Dosage (mg)'].replace('Isotretinoin 40' , 40 , inplace = True)
df['Dosage (mg)'].replace('Isotretinoin 20' , 20 , inplace = True)


print("\nTotal dosage supposed to be taken = 6 months = 180 days\n")
print("60mg per day = 180 * 60 = 10800 mg\n\n")

# Total dosage taken (where status = 1)
taken = df.drop(df[df.Status == 0].index)






#----------Final outputs---------#


print('Total pills popped (mg) = ' , taken['Dosage (mg)'].sum() , 'mg' , '\n')

# Total dosage skipped (where status = 0)
skipped = df.drop(df[df.Status == 1].index)
print('Total pills skipped tsk tsk tsk = ' , skipped['Dosage (mg)'].sum() , 'mg' , '\n')




print ("gotta pop " , (10800 - taken['Dosage (mg)'].sum()) / 40 , "more pills of 40mg or " , (10800 - taken['Dosage (mg)'].sum()) / 20 , "more pills of 20mg"  , '\n')

#print number of pills left to pop (60mg a day, 40mg + 20mg a day)


print( (10800 - taken['Dosage (mg)'].sum()) / 60 , "more days to go .-. " , '\n')


# show simple bar in terminal to show progress
print("\n\n")
print("Progress bar")
print("------------")
print("[" , end = '')
for i in range(int((taken['Dosage (mg)'].sum() / 10800) * 50)):
    print("#" , end = '')
for i in range(50 - int((taken['Dosage (mg)'].sum() / 10800) * 50)):
    print(" " , end = '')
print("]")
print("\nPercentage of dosage taken = " , (taken['Dosage (mg)'].sum() / 10800) * 100 , "%")
print("\n\n")
