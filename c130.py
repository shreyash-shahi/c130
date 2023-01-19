import csv
import pandas as pd

df = pd.read_csv("final.csv")
print(df.shape)

del df["hyperlink"]
print(df.shape)
del df["temp_planet_date"]
del df["temp_planet_mass"]
del df["pl_letter"]
del df["pl_name"]
del df["pl_controvflag"]
del df["pl_pnum"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["pl_orbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr2"]

print(df.shape)

df = df.rename({
    'pl_hostname':"solar_system_name",
    'pl_discmethod':"planet_discovery_method"
},axis = 'columns')

df.to_csv('main.csv')
