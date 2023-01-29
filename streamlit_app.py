import streamlit as st
import pandas as pd
import numpy as np
import os
import urllib.request
import requests
from io import BytesIO
from PIL import Image

#Container located at top of UI.
con = st.container()
con.write("Inside container")

#Designer function to memorize dataframe display.
#@st.experimental_memo #(show_spinner=True)


def load_csv():
    return np.loadtxt("TeamInformation.csv", delimiter= ',', dtype= str)
    
    




#calls csv as nparray
abt = load_csv()


#urllib.request.urlretrieve("https://drive.google.com/file/d/1imkFET1xtuRNesk4uth6G5n1ZMblrVBo","test.jpeg")
#'https://drive.google.com/file/d/1imkFET1xtuRNesk4uth6G5n1ZMblrVBo'
#url = "https://commons.wikimedia.org/wiki/File:Cat03.jpg"
#req_test = requests.get(url)
#comment
#testimg = Image.open((req_test.content))
#Sidebar for Meet the Team
with st.sidebar:
    st.header("Meet the Team")
    #st.caption(abt.shape)
    st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
    #st.markdown("![PLZ]==(https://i.imgur.com/viJ42ZU.jpg)")
    #st.image("https://i.imgur.com/viJ42ZU.jpg")
    
    
    #st.image(testimg)
    
    for i in range(len(abt)):
        url = abt[i:0]
        st.image(url)
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
