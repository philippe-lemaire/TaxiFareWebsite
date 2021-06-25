import streamlit as st
import datetime
import requests

"""
# The Pikmin Taxi Company
"""
st.image("https://images.nintendolife.com/561b53fd662d9/pikmin-3-banner.original.jpg")

date = st.date_input(
    label="Please select a date",
    value=datetime.date.today(),
    min_value=None,
    max_value=None,
    key=None,
    help=None,
)
time = st.time_input(label="Please select a time", value=datetime.time())

pickup_longitude = st.number_input(label="pickup longitude")
pickup_latitude = st.number_input(label="pickup latitude")
dropoff_longitude = st.number_input(label="dropoff longitude")
dropoff_latitude = st.number_input(label="dropoff latitude")
passenger_count = st.slider(
    label="Passengers, it really does not matter",
    min_value=1,
    max_value=5,
    value=1,
)


url = "https://phil-benkklhp2a-ew.a.run.app/predict"

params = {
    "key": "whatever",
    "pickup_datetime": "2001-12-26 12:12:00",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
}

if st.button("push me"):

    response = requests.get(url, params)

    pred = response.json()["prediction"]
    pred = round(pred, 2)

    ## Here is the result

    f" Your fare should be about {pred} dollar"

else:
    "What are you waiting for, push that button!"
