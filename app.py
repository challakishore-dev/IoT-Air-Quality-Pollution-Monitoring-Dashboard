
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="IoT Air Quality Dashboard", layout="wide")
st.title("🌍 IoT Air Quality & Pollution Monitoring Dashboard")

aq = st.slider("Air Quality Sensor Value", 0, 500, 120)
temp = st.slider("Temperature (°C)", 0, 50, 28)
hum = st.slider("Humidity (%)", 0, 100, 60)

if aq <= 50:
    status = "Good"
elif aq <= 100:
    status = "Moderate"
elif aq <= 200:
    status = "Poor"
else:
    status = "Hazardous"

st.metric("Air Quality", aq)
st.metric("Temperature", temp)
st.metric("Humidity", hum)
st.success(f"Status: {status}")

data = pd.DataFrame({
    "Time": pd.date_range(end=datetime.now(), periods=30),
    "AQI": np.random.randint(20, 300, 30)
})
st.line_chart(data.set_index("Time"))
