from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to CanonPDF!

Enter your PDF URL to get started :)
"""


text = st.text_input("Enter PDF URL")

st.button("Go!")

