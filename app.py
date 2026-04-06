import streamlit as st
import pandas as pd
import os
from src.generate_data import generate_dummy_data
from src.analysis import confidence_interval
from src.report_generator import generate_pdf_report

# =========================
# Load / Generate Data
# =========================
if os.path.exists("data/dummy_data.csv"):
    df = pd.read_csv("data/dummy_data.csv")
else:
    df = generate_dummy_data()

st.title("Digital User Analysis Dashboard")
st.dataframe(df.head())

# =========================
# Confidence Interval
# =========================
ci_age = confidence_interval(df["Umur"])
ci_interest = confidence_interval(df["Skor Minat Digital"])

st.subheader("Confidence Interval")
st.write(ci_age)
st.write(ci_interest)

# =========================
# Generate PDF & Download
# =========================
pdf_filename = "report_mufti.pdf"

if st.button("Generate PDF Report"):
    generate_pdf_report(df, ci_age, ci_interest, filename=pdf_filename)
    st.success("Report berhasil dibuat!")

    # Tambahkan tombol download
    with open(pdf_filename, "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name=pdf_filename,
            mime="application/pdf"
        )
