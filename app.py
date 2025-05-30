import streamlit as st
import datetime
import datetime
import requests


'''
# TaxiFareModel front
'''
# Fecha y hora
trip_date = st.date_input("Trip date", datetime.date(2019, 7, 6))
trip_time = st.time_input("Trip time", datetime.time(8, 45))

# Combinar fecha y hora en un solo string ISO
pickup_datetime = datetime.datetime.combine(trip_date, trip_time).isoformat()

# Coordenadas y pasajeros
pickup_longitude = st.number_input('Pickup longitude', value=0.0, format="%.6f")
pickup_latitude = st.number_input('Pickup latitude', value=0.0, format="%.6f")
dropoff_longitude = st.number_input('Dropoff longitude', value=0.0, format="%.6f")
dropoff_latitude = st.number_input('Dropoff latitude', value=0.0, format="%.6f")
number_passenger = st.number_input('Passenger count', min_value=1, step=1)



url_api = 'https://taxifare-1054089886272.europe-west1.run.app/predict'
params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': int(number_passenger)
}

# Botón para hacer la solicitud
if st.button('Predict fare'):
    response = requests.get(url_api, params=params)

    if response.status_code == 200:
        st.subheader("Prediction Result:")
        st.json(response.json())
    else:
        st.error(f"API request failed with status code {response.status_code}")
