import nltk
import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import time
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
import gtts
from gtts import gTTS
import os
import requests
import pandas as pd
#__________________________________________________________


class language_ai :

    def process(self):
        st.set_page_config(page_title='TQA Project By Praveen', layout="wide")




        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])

        col2.markdown(
            "<h1 style='font-size: 80px;'><span style='color: cyan;'>Table </span> <span style='color: white;'>Questioning </span><span style='color: white;'>Answering </span><span style='color: cyan;'> System</span> </h1>",
            unsafe_allow_html=True)
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")

        API_URL = "https://api-inference.huggingface.co/models/microsoft/tapex-large-finetuned-wtq"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        data = {
            "name": ["praveen", "thambey", "shabarinath", 'viswanathan', 'anna lakshmi', 'pavan', 'vigesh',
                     'vengatesh', 'nivas'],
            "age": ["21", "30", "38", '21', '45', '25', '25', '25', '26'],
            "height": ["170", "160", "159", '168', '159', '168', '176', '180', '160'],
            "skills": [
                "NLP , Python , Ml", "Ml", "Python", "ML", "DL", "Ml", "Python", "ML", "DL"
            ]
        }
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.table(data)

        col2.markdown(
            "<h1 style='font-size: 40px;'><span style='color: cyan;'></span> <span style='color: white;'>Provide </span><span style='color:cyan;'>Question</span><span style='color: cyan;'></span> </h1>",
            unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 7, 1])
        try:
            with col2:
                input = st.text_input('')
            with col2:
                if st.button("Proceed"):
                    output = query({
                        "inputs": {
                            "query": input,
                            "table": data
                        },
                    })
                    st.markdown(
                        "<h1 style='font-size: 40px;'><span style='color: cyan;'></span> <span style='color: cyan;'>Result </span><span style='color:white;'>:)</span><span style='color: cyan;'></span> </h1>",
                        unsafe_allow_html=True)

                    st.code(f'Question : {input} , Answer : {output["answer"]}')
        except:
            col2.success('Correct Question Words !!!')

#___________________________________________________________________________________________________________________________________________





# Object Creation

object = language_ai()
object.process()