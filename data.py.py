import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

distribution = pd.read_csv (r"C:\Users\user\Desktop\py. test\synthetic_ev_distribution_data.csv")
geospartial = pd.read_csv (r"C:\Users\user\Desktop\py. test\synthetic_geospatial_data.csv")
weather = pd.read_csv (r"C:\Users\user\Desktop\py. test\synthetic_weather_data.csv")

print(distribution.info())
print(distribution.describe())
print(distribution.head())
ev_type_counts = distribution['EV_Type'].value_counts()

# Plot the bar chart
#ev_type_counts.plot(kind='bar', title='Distribution of EV_Type')
#plt.xlabel('EV_Type')
#plt.ylabel('Count')
#plt.show()

geographical_area = distribution['Geographical_Area'].value_counts()
geographical_area.plot(kind="barh" , title="Geographical_area")
plt.show()



#df = pd.read_excel(r'C:\Users\user\Desktop\py. test\merged_data.xlsx')
#df1 = df.dropna(inplace=True)
#print(df.info())








