import streamlit as st # to make web app
import pandas as pd
import plotly_express as px
import datetime as dt
import yfinance as yf
import time
import pickle
from prophet import Prophet # for predictitng trends
from prophet.plot import plot_plotly # plotting the graph for predicted values
from plotly import graph_objs as go
from pandas_datareader import data as pdr
from pathlib import Path

yf.pdr_override()

val = False

st.set_page_config(
    page_title="Prophit++",
    page_icon="📈"
)


st.image("jet_img.png", width=400)

st.title("Prediction of the stock chosen")

