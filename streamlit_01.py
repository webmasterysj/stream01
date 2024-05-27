# pip install streamlit
# streamlit run 파일명
import streamlit as st
import pandas as pd

st.write("# chart view")
st.write("## raw data")
view = [100, 150, 30]
st.bar_chart(view)
sview = pd.Series(view)
st.write(sview)
