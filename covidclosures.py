#creating smaller CSV file because my original CSV file had a lot of columns that were unncecessary
inputfile = input('Enter inputfile name: ')
outputfile = input('Enter outputfile name: ')
df = pd.read_csv(inputfile)
new = df[['Name','Cuisine', 'Type', 'Borough', 'ZIP', 'Lat','Long']]
new.to_csv(outputfile)

#Analysis 1: to find count and percentage of cuisine (General). 
x = df.Cuisine_General.value_counts(dropna=False)
y = df.Cuisine_General.value_counts(dropna=False, normalize=True)
z = pd.concat([x,y], axis=1, keys= ['counts', '%'])
print (z) 
    
#Analysis 2: find count and percentage of cuisine(specific) 
x = df.Cuisine.value_counts(dropna=False)
y = df.Cuisine.value_counts(dropna=False, normalize=True)
z = pd.concat([x,y], axis=1, keys= ['counts', '%'])
print (z) 

#Graph per Cuisine(specific, with restaurants, cafes, bars) 
df = pd.read_csv('ult.csv') 
x = df.Cuisine.value_counts(dropna=False)
y = df.Cuisine.value_counts(dropna=False, normalize=True)
z = pd.concat([x,y], axis=1, keys= ['Count'])
z = z.plot(kind='barh', color = 'lightseagreen')
plt.title('Closure of Restaurants During Pandemic by Cuisine')
plt.xlabel('Count')
plt.ylabel('Cuisine Type')
plt.show()

#Closures Frequency by ZIP Code  
x = df.groupby(['ZIP']).size()
print(x)


#Returns a dataframe of JUST Chinese restaurants
x = (df.loc[(df.Cuisine == 'Chinese') & (df.Type == "restaurant")])
#Returns a dataframe of JUST American restaurants 
y = df.loc[df.Type == "restaurant"] 
j = x/y*100
print (j) #j = 22.297297% of restaurants closed were Chinese restaurants.





