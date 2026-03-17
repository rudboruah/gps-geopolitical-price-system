import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="GPS Terminal", layout="wide")

# ---------- HEADER ----------
st.title("🌍 Geopolitical Price System (GPS)")
st.caption("Real-time market pricing of geopolitical risk")

# ---------- GLOBAL INDEX ----------
st.markdown("## 🌐 Global Stability Index")

col1, col2, col3 = st.columns(3)

col1.metric("Global Stability Score", "62", "-4.2")
col2.metric("Geopolitical Volatility", "High", "+12%")
col3.metric("Systemic Risk Level", "Elevated", "+8%")

# ---------- TIME SERIES ----------
st.markdown("### Stability Trend")

dates = pd.date_range(end=datetime.datetime.today(), periods=30)
values = np.cumsum(np.random.randn(30)) + 65

df_trend = pd.DataFrame({"Date": dates, "Index": values})
df_trend = df_trend.set_index("Date")

st.line_chart(df_trend)

# ---------- MARKET TABLE ----------
st.markdown("## 📊 Live Geopolitical Markets")

market_data = pd.DataFrame({
    "Event": [
        "Taiwan Conflict by 2030",
        "Iran Sanctions Escalation (12m)",
        "Strait of Hormuz Closure",
        "Global Food Shock Event",
        "Red Sea Shipping Disruption"
    ],
    "Probability (%)": [18, 42, 9, 27, 35],
    "7d Change (%)": [2.1, 5.4, 1.3, 3.8, 4.5]
})

st.dataframe(market_data, use_container_width=True)

# ---------- EVENT DETAIL ----------
st.markdown("## 🔍 Event Explorer")

event = st.selectbox("Select Event", market_data["Event"])

selected = market_data[market_data["Event"] == event].iloc[0]

st.write(f"**Probability:** {selected['Probability (%)']}%")
st.write(f"**7d Change:** {selected['7d Change (%)']}%")

st.progress(selected["Probability (%)"] / 100)

# ---------- COUNTRY PANEL ----------
st.markdown("## 🌏 Country Exposure")

country = st.selectbox("Select Country", ["Indonesia", "Singapore", "Brazil", "Germany", "UAE"])

if country == "Indonesia":
    st.warning("High climate + supply chain exposure")
    st.write("Suggested hedge: Maritime disruption contracts")

elif country == "Singapore":
    st.info("High trade dependency")
    st.write("Suggested hedge: Supply chain stability index")

elif country == "Brazil":
    st.info("Commodity exposure")
    st.write("Suggested hedge: Food volatility contracts")

elif country == "Germany":
    st.warning("Energy vulnerability")
    st.write("Suggested hedge: Energy disruption instruments")

elif country == "UAE":
    st.info("Energy exporter advantage")
    st.write("Suggested hedge: Regional instability derivatives")

# ---------- AI ANALYST ----------
st.markdown("## 🧠 AI Risk Analyst")

if st.button("Explain Current Risk Environment"):
    st.success("""
    Key drivers of rising geopolitical risk:

    • Increased sanctions probability across multiple regions  
    • Maritime shipping disruptions impacting global trade  
    • Energy supply volatility due to regional tensions  
    • Climate-related shocks amplifying systemic instability  

    Market sentiment indicates rising concern over supply chain resilience.
    """)

# ---------- NEWS SIMULATION ----------
st.markdown("## 📰 Market Signals")

news = [
    "Shipping disruption risk rises in key trade corridors",
    "Energy markets react to geopolitical tensions",
    "New sanctions discussions increase volatility",
    "Climate events impacting agricultural supply chains"
]

for n in news:
    st.write("•", n)

# ---------- FOOTER ----------
st.caption("GPS v0.1 — Experimental market infrastructure concept")
