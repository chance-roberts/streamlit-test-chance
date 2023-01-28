import streamlit as st
import pandas as pd
from PIL import Image

#Container located at top of UI.
con = st.container()
con.write("Inside container")

#Designer function to memorize dataframe display.
#@st.experimental_memo #(show_spinner=True)
def load_data():
    return pd.read_csv("data/TeamInformation(Test).csv")

#Save load_data function into df var. access df in streamlit.
#df = load_data()
about_us = {'Name': [], 'Major': [], 'Picture': []}
abt = pd.DataFrame(about_us)
about = st.dataframe(data=abt)

#Side bar area.
scrbd = st.expander("Score breakdown")
comp = st.expander("Comparison")
scrbd.write("Something")
comp.write("Else")

abt = st.expander("About the Team")
#about_us = {'Picture': [],'Name': [], 'Major': []}
abt = load_data()
about = st.dataframe(data=abt)

def load_images(dataframe):
    for i in about_us:
        image = Image.open(about_us[0:i])
        st.image(image, caption = about_us[1:i])


abt.write(load_images(abt))
#st.sidebar.button("Enter", on_click=st.dataframe(df))
#st.text_input()


#def hide_data():
    #return st.button("Show grid", on_click=load_data(df))

#def button_check():
#   print("this button works!")

#btn_chk = button_check()

#test
