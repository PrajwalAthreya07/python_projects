#importing the packages
import pandas as pd
import plotly.express as px

#creating a variable and assigning the url(json file) to it
url = 'http://api.open-notify.org/iss-now.json'

#creating a data frame to obtain real-time latitude and longitude of the iss
df = pd.read_json(url)
print(df)

df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)
print(df)

#dropping(deleting) the index and message from the data frame
df = df.drop(['index','message'], axis = 1)
print(df)

#plotting the exact location of the iss using the co-ordinates obtained
figure = px.scatter_geo(df,lat='latitude',lon='longitude')
figure.show()