import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="SUPERSTORE!!!", page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: Sample Superstore EDA")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename=fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\bielalzina_cifpjoant\OneDrive - CIFP JOAN TAIX\Documents\GitHub\tutorial-streamlit\dashboard_files")
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")


# CREAM DUES COLUMNES
col1, col2 = st.columns((2))

# ORDENAM REGISTRES PER DATA
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")

# OBTENIM DATA INICIAL i DATA FINAL
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

# DEMANAM DATA INICIAL I FINAL A L'USUARI
with col1:
    dataInicial = pd.to_datetime(st.date_input("START DATE", startDate, format="DD/MM/YYYY"))

with col2:
    dataFinal = pd.to_datetime(st.date_input("END DATE", endDate, format="DD/MM/YYYY"))

# ACOTAM LES DADES DEL CSV SEGONS LES DATES SELECCIONADES
df = df[(df["Order Date"] >= dataInicial) & (df["Order Date"] <= dataFinal)].copy()

# FILTRES SIDEBAR
st.sidebar.header("Elegeix el teu filtre")

# FILTRE PER REGIÓ
region = st.sidebar.multiselect("Elegeix la Regió", df["Region"].unique())

# SINO ELEGIM REGIÓ
if not region:
    df2=df.copy()
# REGIO/NS SELECCIONADA/ES
else:
    df2=df[df["Region"].isin(region)]

# FILTRE PER ESTAT
state = st.sidebar.multiselect("Elegeix Estat", df2["State"].unique())

# SINO ELEGIM ESTAT
if not state:
    df3=df2.copy()
# ESTAT/S SELECCIONAT/S
else:
    df3=df2[df2["State"].isin(state)]


