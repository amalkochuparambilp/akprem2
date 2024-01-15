import streamlit as st
from rembg import remove
from PIL import image

def removebg(img):
    input = Image.open(img)
    return remove(input)

def main():
    st.title("AKP BG REM | UNDEVELOPMENT")
    uploaded_file = st.file_uploader("Choose an image",type=["png","JPG"])

    
    if uploaded_file is not None:
        st.image(uploaded_file)
        result=removebg(uploaded_file)
        st.image(result)

if __name__ == '__main__':
    main()