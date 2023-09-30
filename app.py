import sys
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from PIL import Image 
import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage" , page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
local_css("style\style.css")

with st.container():
   
    st.subheader("Hi I am Aarush Simlot aka Romer The Gamer :wave:")
    st.title("A Football Lover from UK")
    st.write("I am very Passionate about football.")
    st.write("[Learn More>](https://www.google.com)")

#--- LOAD ASSETS
lottie_coding= "https://lottie.host/be9fb69d-0658-4d8e-8b72-9f4c58286a78/0UhfEnPfIJ.json"
img_right = Image.open("images/1.jpg")
img_left = Image.open("images/2.jpg")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(""" To be Edited LAter""")
        st.write ("[Linked In Profile >](https://www.linkedin.com/in/abhisheksimlot/)")


    with right_column:
        st_lottie(lottie_coding,height =300, key="coding")

with st.container():
    st.write("---")
    st.header("My Pics")
    st.write("##")
    image_column_left,image_column_right = st.columns((1,2))
    
    with image_column_left:
        st.image(img_left)
    with image_column_right:
        st.image(img_right)


with st.container():
    st.write("---")
    st.header("Get in touch with Me..!!")
    st.write("##")
    # Documemtation formsubmit.co
    contact_form = """<form action="https://formsubmit.co/abhishek.simlot@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value=false required>
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <Textarea name= "message" placeholder="Your Message Here" required> </Textarea>
     <button type="submit">Send</button>
    </form> """

    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


