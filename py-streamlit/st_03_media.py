import streamlit as st
 
## Show image
## PIL : Python Image Library
from PIL import Image
img = Image.open("files/example_cat.jpeg")
st.image(img, width=400, caption="Image example: Cat")
 
## Show videos
vid_file = open("files/example_vid_cat.mp4", "rb").read()
st.video(vid_file, start_time=2)
 
## Play audio file.
audio_file = open("files/loop_w_bass.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3", start_time=10)