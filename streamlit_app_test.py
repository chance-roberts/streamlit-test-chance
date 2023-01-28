import streamlit as st
import pandas as pd

#Container located at top of UI.
con = st.container()
con.write("Inside container")

#Designer function to memorize dataframe display.
#@st.experimental_memo #(show_spinner=True)
def load_data():
    return pd.read_csv("data/reddit_comments.csv")

#Save load_data function into df var. access df in streamlit.
df = load_data()


#Side bar area.
scrbd = st.expander("Score breakdown")
comp = st.expander("Comparison")

scrbd.write("Something")
comp.write("Else")
