import os
import streamlit as st
import pandas as pd
from src.analysis import confidence_interval
from src.report_generator import generate_pdf_report

from src.generate_data import generate_dummy_data
#df = pd.read_csv("data/dummy_data.csv")

if os.path.exists("data/dummy_data.csv"):
    df = pd.read_csv("data/dummy_data.csv")
else:
    df = generate_dummy_data()
st.title("Digital User Analysis Dashboard")

st.dataframe(df.head())

# CI
ci_age = confidence_interval(df["Umur"])
ci_interest = confidence_interval(df["Skor Minat Digital"])

st.subheader("Confidence Interval")

st.write(ci_age)
st.write(ci_interest)

# Generate report button
if st.button("Generate PDF Report"):
    generate_pdf_report(df, ci_age, ci_interest)
    st.success("Report berhasil dibuat!")
