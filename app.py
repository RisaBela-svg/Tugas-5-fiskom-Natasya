import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Analisis Nilai Siswa", layout="wide")

st.title("📊 Dashboard Analisis Data Nilai Siswa")

# Upload file
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("📋 Data Mentah")
    st.dataframe(df)

    # Statistik Deskriptif
    st.subheader("📈 Statistik Deskriptif")
    st.write(df.describe())

    # Pilih kolom numerik
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:

        # ===============================
        # Histogram
        # ===============================
        st.subheader("📊 Histogram Distribusi Nilai")
        selected_col = st.selectbox("Pilih Kolom untuk Histogram", numeric_cols)

        fig1, ax1 = plt.subplots()
        ax1.hist(df[selected_col], bins=10)
        ax1.set_title(f"Histogram {selected_col}")
        ax1.set_xlabel("Nilai")
        ax1.set_ylabel("Frekuensi")
        st.pyplot(fig1)

        # ===============================
        # Rata-rata per Soal
        # ===============================
        st.subheader("📌 Rata-rata Nilai per Soal")

        mean_scores = df[numeric_cols].mean()

        fig2, ax2 = plt.subplots()
        mean_scores.plot(kind='bar', ax=ax2)
        ax2.set_title("Rata-rata Nilai per Soal")
        ax2.set_ylabel("Rata-rata")
        st.pyplot(fig2)

        # ===============================
        # Boxplot
        # ===============================
        st.subheader("📦 Boxplot Distribusi Nilai")

        fig3, ax3 = plt.subplots(figsize=(10,5))
        sns.boxplot(data=df[numeric_cols], ax=ax3)
        plt.xticks(rotation=90)
        st.pyplot(fig3)

        # ===============================
        # Heatmap Korelasi
        # ===============================
        st.subheader("🔥 Heatmap Korelasi Antar Soal")

        fig4, ax4 = plt.subplots(figsize=(10,8))
        sns.heatmap(df[numeric_cols].corr(), annot=False, cmap="coolwarm", ax=ax4)
        st.pyplot(fig4)

        # ===============================
        # Distribusi Total Nilai Siswa
        # ===============================
        st.subheader("🏆 Distribusi Total Nilai Siswa")

        df["Total_Nilai"] = df[numeric_cols].sum(axis=1)

        fig5, ax5 = plt.subplots()
        ax5.hist(df["Total_Nilai"], bins=10)
        ax5.set_title("Distribusi Total Nilai Siswa")
        ax5.set_xlabel("Total Nilai")
        ax5.set_ylabel("Frekuensi")
        st.pyplot(fig5)

        # Download data
        st.subheader("⬇️ Download Data dengan Total Nilai")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='hasil_analisis.csv',
            mime='text/csv'
        )

else:
    st.info("Silakan upload file Excel terlebih dahulu.")