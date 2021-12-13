#creating smaller CSV file because my original CSV file had a lot of columns that were unncecessary
inputfile = input('Enter inputfile name: ')
outputfile = input('Enter outputfile name: ')
df = pd.read_csv(inputfile)
new = df[['Name','Cuisine', 'Type', 'Borough', 'ZIP', 'Lat','Long']]
new.to_csv(outputfile)

#Analysis 1: to find count and percentage of cuisine (General). 
outputfile = input('Enter outputfile name: ')
df = pd.read_csv('ult.csv') 
x = df.Cuisine_General.value_counts(dropna=False)
y = df.Cuisine_General.value_counts(dropna=False, normalize=True)
z = pd.concat([x,y], axis=1, keys= ['counts', '%'])
print (z) 
    
