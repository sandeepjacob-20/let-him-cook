import streamlit as st
from PIL import Image
import os
import generative_engine


st.markdown("<h1 style='text-align:center; font-family: garamond;'>Let Him Cook</h1>", unsafe_allow_html=True)   
file = st.file_uploader("Upload file", type=["jpg", "jpeg", "png"])
if file is None:
    st.caption("Please upload an image of the dish you want to cook")
if file is not None:
    with open(os.path.join("temp",file.name),"wb") as f:
        f.write(file.getbuffer())

    img = Image.open('./temp/'+file.name)
    
    response = generative_engine.generate_recipe(img)
    st.write(response["receipe"])
    st.caption("This receipie was brought to you in "+str(response["prompt_generation_time"])+" seconds")
    os.remove('./temp/'+file.name)
    st.divider()
    if (st.download_button("Download this receipie",data=response["receipe"],file_name="receipie.docx")):
        st.success("File downloaded", icon='✅')

    