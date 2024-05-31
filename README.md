ISS Tracker in Real Time
This project provides a simple implementation for tracking the International Space Station (ISS) in real time using Python. The script fetches data from an API and visualizes the current position of the ISS on a world map using the pandas and plotly packages.

Installation
Before you run the code, ensure you have the required packages installed. You can install them using pip:


pip install pandas plotly
Usage
To track the ISS in real-time, you can use the provided script. Here is a step-by-step guide:

Import the necessary libraries:


import pandas as pd
import plotly.express as px
Fetch the ISS location data from the API:


url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)
Process the data to extract latitude and longitude:


df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)
df = df.drop(['index', 'message'], axis=1)
Visualize the ISS position on a world map:


fig = px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()


Here is the complete code for tracking the ISS in real-time:


import pandas as pd
import plotly.express as px

url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)

df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)
df = df.drop(['index', 'message'], axis=1)

fig = px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()

Explanation:
Fetching Data: The script uses the open-notify API to get the current position of the ISS in JSON format.
Data Processing: The JSON data is converted into a pandas DataFrame, and the latitude and longitude values are extracted and organized.
Visualization: Using plotly.express, the current position of the ISS is plotted on a geographical scatter plot, which is then displayed.

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.
