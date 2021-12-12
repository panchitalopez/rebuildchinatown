#creating smaller CSV file because my original CSV file had a lot of columns that were unncecessary

inputfile = input('Enter inputfile name: ')
outputfile = input('Enter outputfile name: ')
df = pd.read_csv(inputfile)
new = df[['Name','Cuisine', 'Type', 'Borough', 'ZIP', 'Lat','Long']]
new.to_csv(outputfile)

