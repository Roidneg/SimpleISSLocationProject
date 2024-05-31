import pandas as pd
import plotly.express as px
import requests

# Fetch data from the API with error handling
url = 'http://api.open-notify.org/iss-now.json'

try:
    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError for bad responses
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f'Error fetching data {e}')
    data = None

if data:
    # Extract latitude and longitude from the API Response
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])

    # Load data into Dataframe
    df = pd.DataFrame({
        'latitude': [latitude],
        'longitude': [longitude]
    })

    # Create scatter plot on a geographical map
    fig = px.scatter_geo(df, lat='latitude', lon='longitude')

    # Add title and customize appearance
    fig.update_layout(
        title='Current Location of the ISS',
        geo=dict(
            showland=True,
            landcolor='rgb(243, 243, 243)',
            subunitwidth=1,
            countrywidth=1
        )
    )

    fig.show()
