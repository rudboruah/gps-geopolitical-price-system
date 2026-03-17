import streamlit as st
import pandas as pd
import numpy as np
import datetime
import feedparser
import random

# ---------- CONFIG ----------
st.set_page_config(page_title="GPS Terminal V2", layout="wide")

st.title("🌍 Geopolitical Price System (GPS) — V2")
st.caption("Market infrastructure for pricing global instability")

# ---------- GLOBAL STATE ----------
base_risk = 60 + random.randint(-5, 5)

# ---------- GLOBAL INDEX ----------
st.markdown("## 🌐 Global Stability Index")

col1, col2, col3 = st.columns(3)
col1.metric("Stability Score", base_risk, f"{random.randint(-5,0)}")
col2.metric("Volatility", "High", "+12%")
col3.metric("Systemic Risk", "Elevated", "+8%")

# ---------- TREND ----------
st.markdown("### 30-Day Stability Trend")

dates = pd.date_range(end=datetime.datetime.today(), periods=30)
values = np.cumsum(np.random.randn(30)) + base_risk

df = pd.DataFrame({"Date": dates, "Index": values}).set_index("Date")
st.line_chart(df)

# ---------- LIVE MARKETS ----------
st.markdown("## 📊 Geopolitical Risk Markets")

markets = pd.DataFrame({
    "Event": [
        "Taiwan Conflict",
        "Iran Sanctions Escalation",
        "Hormuz Closure",
        "Global Food Shock",
        "Red Sea Disruption"
    ],
    "Probability (%)": np.random.randint(5, 60, 5),
    "Trend": np.random.choice(["↑", "↓"], 5)
})

st.dataframe(markets, use_container_width=True)

# ---------- EVENT ANALYSIS ----------
st.markdown("## 🔍 Event Analysis")

event = st.selectbox("Select Event", markets["Event"])
prob = int(markets[markets["Event"] == event]["Probability (%)"])

st.progress(prob / 100)
st.write(f"Current Market-Implied Probability: **{prob}%**")

# ---------- AI ANALYST ----------
st.markdown("## 🧠 AI Geopolitical Analyst")

def generate_analysis(event, prob):
    narratives = [
        f"Rising probability of {event} is driven by escalating regional tensions and strategic signaling.",
        f"Market pricing suggests increasing concern around {event}, particularly due to supply chain exposure.",
        f"{event} risk is being repriced due to recent geopolitical developments and economic fragility.",
        f"Participants are hedging against {event}, reflecting heightened uncertainty in global markets."
    ]
    return random.choice(narratives)

if st.button("Generate AI Analysis"):
    st.success(generate_analysis(event, prob))

# ---------- LIVE NEWS ----------
st.markdown("## 📰 Live Market Signals")

feed = feedparser.parse("http://feeds.reuters.com/reuters/worldNews")

for entry in feed.entries[:5]:
    st.write(f"• {entry.title}")

# ---------- SCENARIO SIMULATOR ----------
st.markdown("## 🎯 Scenario Simulator")

scenario = st.selectbox(
    "Select Scenario",
    ["Status Quo", "Regional Conflict", "Global Sanctions Wave", "Supply Chain Collapse"]
)

impact = {
    "Status Quo": -2,
    "Regional Conflict": +10,
    "Global Sanctions Wave": +15,
    "Supply Chain Collapse": +20
}

new_risk = base_risk + impact[scenario]

st.metric("Projected Stability Impact", new_risk, f"{impact[scenario]}")

st.info(f"""
Scenario Impact Analysis:

• Scenario: {scenario}  
• Estimated increase in systemic risk: {impact[scenario]} points  
• Key transmission channels: trade, energy, financial markets  
""")

# ---------- COUNTRY PANEL ----------
st.markdown("## 🌏 Country Exposure")

country = st.selectbox("Country", ["Indonesia", "Singapore", "Brazil", "Germany", "UAE"])

profiles = {
    "Indonesia": "High climate + maritime exposure",
    "Singapore": "Trade hub vulnerability",
    "Brazil": "Commodity volatility exposure",
    "Germany": "Energy dependency risk",
    "UAE": "Energy exporter with regional exposure"
}

st.write(profiles[country])

# ---------- FOOTER ----------
st.caption("GPS Terminal V2 — Experimental prototype of a geopolitical market system")
