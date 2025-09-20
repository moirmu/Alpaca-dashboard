import streamlit as st
import pandas as pd

st.title("📊 AlpacaBot Dashboard")

try:
    df = pd.read_csv("trade_journal.csv")
    st.write("Laatste trades:")
    st.dataframe(df)

    total_pnl = df["PnL"].sum()
    winrate = (df["PnL"] > 0).mean() * 100
    avg_conf = df["Confidence"].mean()

    st.metric("Totale PnL", f"${total_pnl:.2f}")
    st.metric("Winrate", f"{winrate:.2f}%")
    st.metric("Gem. Confidence", f"{avg_conf:.2f}")

except Exception as e:
    st.error(f"Kon trade_journal.csv niet laden: {e}")
