import streamlit as st
from PIL import Image
import os
import generative_engine
import time

@st.cache_data
def foodIdentifierEngine(file):
    with open(os.path.join("temp",file.name),"wb") as f:
        f.write(file.getbuffer())
    #processing text    
    img = Image.open('./temp/'+file.name)   
    response = generative_engine.generate_recipe(img)
    
    return response



st.markdown("<h1 style='text-align:center; font-family: garamond; font-size: 45px'>Let Him Cook!</h1>", unsafe_allow_html=True)   
st.divider()
st.subheader("Upload an image of the dish you want to cook")
file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if file is None:
    st.caption("Please upload the image in .jpg, .jpeg or .png format")

if file is not None:
    try:
        placeholder = st.empty()
        with placeholder.container():
            st.caption("Please wait while we analyze the image and generate the recipe...")
            
            response = foodIdentifierEngine(file)
        
        placeholder.empty()
        st.write(response["recipe"])
        st.divider()
        st.caption("This recipe was brought to you in "+str(response["prompt_generation_time"])+" seconds")
        if (st.download_button("Download this recipe",data=response["recipe"],file_name="recipe.txt")):
            st.snow()
            st.success("File downloaded", icon='✅')
    except:
        st.write("Some unexpected error occured, Please try again!!")

    