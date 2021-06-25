import streamlit as st
import datetime
import requests

"""
# TaxiFareModel front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
"""
)

"""
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:

"""
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
    step=None,
    format=None,
    key=None,
    help=None,
)

"""

"""
## Once we have these, let's call our API in order to retrieve a prediction
"""
See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
"""

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

response = requests.get(url, params)

pred = response.json()["prediction"]
pred = round(pred, 2)

## Here is the result

f" Your fare should be about {pred} dollar"
