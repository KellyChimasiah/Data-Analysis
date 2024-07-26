import pandas as pd

geospartial_data = pd.read_csv(r"C:\Users\user\Desktop\py. test\synthetic_geospatial_data.csv")
distribution_data= pd.read_csv(r"C:\Users\user\Desktop\py. test\synthetic_ev_distribution_data.csv")
#print(geospartial_data['Substation_Location'].head())
#print(distribution_data['EV_Charging_Station_Location'].head())

#geospartial_data[['Location_Part1', 'Location_Part2']] = geospartial_data['Substation_Location'].str.split(',', expand=True)
#geospartial_data['Location_Part1'] = geospartial_data['Location_Part1'].str.strip().str.strip('(')
#geospartial_data['Location_Part2'] = geospartial_data['Location_Part2'].str.strip().str.strip('(')
#print(geospartial_data.head())
geospartial_data[['latitude', 'longitude']] = geospartial_data['Substation_Location'].str.strip('()').str.split(',', expand=True)


distribution_data[['latitude', 'longitude']] = distribution_data['EV_Charging_Station_Location'].str.strip('()').str.split(',', expand=True)

distribution_data.drop(columns=['EV_Charging_Station_Location'])
geospartial_data.drop(columns=['Substation_Location'] )

print(distribution_data.info())
print(geospartial_data.head())