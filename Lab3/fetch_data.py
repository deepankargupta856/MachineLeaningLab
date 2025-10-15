from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
spambase = fetch_ucirepo(id=94) 
  
# data (as pandas dataframes) 
X = spambase.data.features 
y = spambase.data.targets 
  
X.to_csv('features.csv', index=True)
y.to_csv('targets.csv', index=True)

# metadata 
print(spambase.metadata) 
  
# variable information 
print(spambase.variables) 

