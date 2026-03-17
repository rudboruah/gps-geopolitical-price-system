import streamlit as st
import pandas as pd

st.set_page_config(page_title="Geopolitical Price System", layout="wide")

st.title("🌍 Geopolitical Price System (GPS)")
st.subheader("Market Pricing of Global Stability")

st.metric("Global Stability Index", "62", "-4 this week")

st.markdown("### Live Geopolitical Risk Markets")

data = {
    "Event": [
        "Taiwan Conflict by 2030",
        "New Iran Sanctions (12m)",
        "Strait of Hormuz Closure",
        "Global Food Shock Event"
    ],
    "Probability": ["18%", "42%", "9%", "27%"],
    "7d Change": ["+2.1%", "+5.4%", "+1.3%", "+3.8%"]
}

df = pd.DataFrame(data)

st.table(df)

st.markdown("### Country Exposure")

country = st.selectbox(
    "Select Country",
    ["Indonesia", "Singapore", "Brazil", "Germany"]
)

if country == "Indonesia":
    st.write("Climate + Supply Chain Exposure: HIGH")
    st.write("Suggested Hedges: Maritime Disruption Contracts")

if country == "Singapore":
    st.write("Trade Exposure: HIGH")
    st.write("Suggested Hedges: Supply Chain Stability Index")

st.markdown("### AI Risk Explanation")

st.info("""
Recent increase in geopolitical risk is driven by:

• Shipping disruptions  
• Rising sanctions probability  
• Energy supply volatility
""")
