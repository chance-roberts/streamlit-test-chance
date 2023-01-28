import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#Container located at top of UI.
con = st.container()
con.write("Inside container")

#Designer function to memorize dataframe display.
#@st.experimental_memo #(show_spinner=True)
def load_data():
    return pd.read_csv("data/TeamInformation.csv")

#Save load_data function into df var. access df in streamlit.
#df = load_data()
about_us = {'Name': [], 'Major': [], 'Picture': []}
abt = np.array(about_us)
about = st.dataframe(data=abt)


add_selectbox = st.sidebar.image(
    "Meet the Team"
)


#Side bar area.
scrbd = st.expander("Score breakdown")
comp = st.expander("Comparison")
scrbd.write("Something")
comp.write("Else")

abt = st.expander("About the Team")
#about_us = {'Picture': [],'Name': [], 'Major': []}
abtdf = load_data()
about = st.dataframe(data=abtdf)

def load_images(dataframe):
    for i in about_us:
        image = Image.open(about_us[0:i])
        st.image(image, caption = about_us[1:i])


abt.write(load_images(abtdf))
#st.sidebar.button("Enter", on_click=st.dataframe(df))
#st.text_input()


#def hide_data():
    #return st.button("Show grid", on_click=load_data(df))

#def button_check():
#   print("this button works!")

#btn_chk = button_check()

#test
