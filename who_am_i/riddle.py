
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#print("Column headings:")
#print(df.columns)
#print(df['Computer Parts'])

#iterating through parts
#for i in df.index:
    #print(df['Computer Parts'][i])
    #print(df['Soaps'][i])

#saving in a list
df = pd.read_excel('C:\\Users\\anush\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\riddleAssign\\indian name.xlsx') #sheetname='Sheet1')
inames = df['Indian Names']
print(inames)

df = pd.read_excel('C:\\Users\\anush\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\riddleAssign\\CompParts.xlsx')
compParts = df['Computer Parts']
print(compParts)

df = pd.read_excel('C:\\Users\\anush\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\riddleAssign\\designSoftware.xlsx')
designSoft = df['Design Software']
print(designSoft)

df = pd.read_excel('C:\\Users\\anush\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\riddleAssign\\waterStorage.xlsx')
waterStore = df['Water Storage']
print(waterStore)

df = pd.read_excel('C:\\Users\\anush\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\riddleAssign\\AllSoapNames.xlsx')
soaps = df['Soaps1']
print(soaps)
for i in df.index:
    if inames[1] and inames[4] and inames[5] and inames[7] and inames[10]==df['Soaps1']:
        a=inames
        print(a)
df = pd.read_excel('C:\\Users\\anush\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\riddleAssign\\Companies.xlsx')
companyN = df['Company Name']
print(companyN)

#iterating through lists
