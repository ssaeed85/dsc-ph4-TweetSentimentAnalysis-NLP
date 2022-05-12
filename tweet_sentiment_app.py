import streamlit as st
import pickle
from src.documentParser import  doc_preparer


f=open('model/final_model.sav' , 'rb')
final_model=pickle.load(f)

decoder ={
    0: 'Negative',
    1: 'Neutral',
    2: 'Positive'
}
st.title("Twitter Sentiment stuff")

tweet = st.text_input("Input potential tweet here", 
max_chars=280)
# unhide_output = st.button('Tweet!', key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False)
pred = final_model.predict([doc_preparer(tweet,stem=True)])
st.write(decoder[pred[0]])
# if unhide_output:
#     pred = final_model.predict([doc_preparer(tweet,stem=True)])
#     st.write(type(pred))

