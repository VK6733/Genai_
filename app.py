import streamlit as st
import google.generativeai as genai
from PIL import Image


from streamlit.runtime.uploaded_file_manager import UploadedFile
genai.configure(api_key="AIzaSyBDm_ebuvAMkzJjtiYs-oHgugQAFkxST5I")
model=genai.GenerativeModel("gemini-pro-vision")


def get_generated_res(input,image):
 if input !="":
  response=model.generate_content([input,image])
 else:
  response=model.generate_content(image)
 return response.text




st.set_page_config(page_title="Image + Text model")


st.header("Image and text application")


input=st.text_area("Input: ",key="input")
# submit=st.button("ask your question")


# if submit:
#   response=get_gemini_model(input)
#   st.subheader("Response is")
#   st.write(response)


uploaded_file=st.file_uploader("Choose the file....",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None :
 image=Image.open(uploaded_file)
 st.image(image,caption="image_uploaded", use_column_width=True)


submit=st.button("tell me about the image")
if submit:
 response=get_generated_res(input,image)
 st.subheader("The generated reponse is ")
 st.write(response)
