import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

#Container located at top of UI.
con = st.container()
con.write("Inside container")

#Designer function to memorize dataframe display.
#@st.experimental_memo #(show_spinner=True)


def load_csv():
    csv = pd.read_csv("TeamInformation.csv")
    st.write(csv)
    




#calls csv as nparray
#abt = np.array(load_csv())



#Sidebar for Meet the Team
with st.sidebar:
    st.header("Meet the Team")
    for i in abt:
        st.image(abt[0:i])
        st.caption("Test")






#Side bar area.
scrbd = st.expander("Score breakdown")
comp = st.expander("Comparison")
scrbd.write("Something")
comp.write("Else")

abt = st.expander("About the Team")
#about_us = {'Picture': [],'Name': [], 'Major': []}

#st.sidebar.button("Enter", on_click=st.dataframe(df))
#st.text_input()


#def hide_data():
    #return st.button("Show grid", on_click=load_data(df))

#def button_check():
#   print("this button works!")

#btn_chk = button_check()

#test
