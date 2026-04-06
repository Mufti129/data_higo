import streamlit as st
import os
from src.generate_data import generate_dummy_data
from src.analysis import confidence_interval
from src.report_generator import generate_pdf_report

# Load 
if os.path.exists("data/dummy_data.csv"):
    import pandas as pd
    df = pd.read_csv("data/dummy_data.csv")
else:
    df = generate_dummy_data()

st.title("Digital User Analysis Dashboard HIGO")
st.dataframe(df.head())

# Confidence Interval
ci_age = confidence_interval(df["Umur"])
ci_interest = confidence_interval(df["Skor Minat Digital"])

st.subheader("Confidence Interval Umur")
st.write(ci_age)

st.subheader("Confidence Interval Minat Didital")
st.write(ci_interest)

# Insights
st.subheader("Key Insights")
umur_mean = df['Umur'].mean()
top_login = df['Kategori Waktu Login'].value_counts().idxmax()
high_interest_pct = (df['Skor Minat Digital'] == 3).mean() * 100
top_loc = df['Tipe Lokasi'].value_counts().idxmax()

st.markdown(f"""
- Mayoritas pengguna usia produktif ({umur_mean:.0f} tahun)
- Login dominan pada {top_login}
- {high_interest_pct:.0f}% user high digital interest → target campaign
- Lokasi terbanyak: {top_loc}
""")

# Generate Report
pdf_filename = "report_mufti_higo.pdf"
if st.button("Generate PDF Report"):
    generate_pdf_report(df, ci_age, ci_interest, filename=pdf_filename)
    st.success("Report berhasil dibuat!")
    with open(pdf_filename, "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name=pdf_filename,
            mime="application/pdf"
        )
