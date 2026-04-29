import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="RVSA Pro", layout="wide")

# -------------------------

# 🔥 PREMIUM CSS

# -------------------------

st.markdown("""

<style>

/* Background */
body {
    background-color: #0a0f1c;
    color: white;
}

/* Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Title */
.main-title {
    font-size: 55px;
    font-weight: bold;
    color: #4f8ef7;
    text-align: center;
}

/* KPI Cards */
.card {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(145deg, #111827, #1f2937);
    box-shadow: 0 0 20px rgba(79,142,247,0.3);
    text-align: center;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0c0f18;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    padding: 10px;
}

.block-container {
    padding-top: 1rem;
}

</style>

""", unsafe_allow_html=True)

# -------------------------

# 📂 LOAD DATA

# -------------------------

@st.cache_data
def load_data():
    return pd.read_csv("india_vehicle_sales_cleaned.csv")

df = load_data()

# -------------------------

# 🚀 HERO SECTION

# -------------------------

st.markdown("<div class='main-title'>RVSA ANALYTICS</div>", unsafe_allow_html=True)
st.caption("Production Level Vehicle Analytics Dashboard")

st.divider()

# -------------------------

# 📊 KPI CARDS

# -------------------------

total = int(df["Units_Sold"].sum())
states = df["State"].nunique()
segments = df["Segment"].nunique()

c1, c2, c3 = st.columns(3)

c1.markdown(f"<div class='card'><h2>{total:,}</h2><p>Total Sales</p></div>", unsafe_allow_html=True)
c2.markdown(f"<div class='card'><h2>{states}</h2><p>States</p></div>", unsafe_allow_html=True)
c3.markdown(f"<div class='card'><h2>{segments}</h2><p>Segments</p></div>", unsafe_allow_html=True)

st.divider()

# -------------------------

# 🎛 FILTERS

# -------------------------

st.sidebar.title("Filters")

year = st.sidebar.multiselect("Year", df["Year"].unique(), df["Year"].unique())
state = st.sidebar.multiselect("State", df["State"].unique(), df["State"].unique())

filtered = df[(df["Year"].isin(year)) & (df["State"].isin(state))]

# -------------------------

# 📑 TABS

# -------------------------

tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🚗 Segments", "⚡ EV", "🤖 Forecast"])

# -------------------------

# OVERVIEW

# -------------------------

with tab1:
    st.subheader("Sales by Region")
region_df = filtered.groupby("Region")["Units_Sold"].sum().reset_index()

fig = px.bar(region_df, x="Region", y="Units_Sold",
             color="Region",
             template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)


# -------------------------

# SEGMENTS

# -------------------------

with tab2:
    st.subheader("Segment Distribution")

seg = filtered.groupby("Segment")["Units_Sold"].sum().reset_index()

fig2 = px.pie(seg, names="Segment", values="Units_Sold",
              hole=0.5,
              template="plotly_dark")

st.plotly_chart(fig2, use_container_width=True)


# -------------------------

# EV

# -------------------------

with tab3:
    st.subheader("EV Growth")

ev = filtered[filtered["Fuel_Type"] == "Electric"]
trend = ev.groupby("Year")["Units_Sold"].sum().reset_index()

fig3 = px.line(trend, x="Year", y="Units_Sold",
               markers=True,
               template="plotly_dark")

st.plotly_chart(fig3, use_container_width=True)


# -------------------------

# FORECAST

# -------------------------

with tab4:
    st.subheader("Sales Forecast")
year_map = {"FY2019":1,"FY2020":2,"FY2021":3,"FY2022":4,"FY2023":5,"FY2024":6}
df["Year_Num"] = df["Year"].map(year_map)

trend = df.groupby("Year_Num")["Units_Sold"].sum().reset_index()

x = trend["Year_Num"]
y = trend["Units_Sold"]

coeffs = np.polyfit(x, y, 2)
poly = np.poly1d(coeffs)

future_x = np.arange(1, 9)
future_y = poly(future_x)

fig4 = px.line(x=future_x, y=future_y,
               markers=True,
               template="plotly_dark")

st.plotly_chart(fig4, use_container_width=True)


st.divider()

