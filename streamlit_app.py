from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

def send_prompt(prompt):
    headers = {
        'authority': 'api.popai.pro',
        'accept': 'text/event-stream',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJiNTlkY2NmYi03YWU3LTQ0MDMtODk1MS1hMzJlY2UyNmI0ODQiLCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5ODY1NDg1LCJpYXQiOjE2OTgzMjk0ODV9.4kt7y6ZrdhPxehhSFks021rgs4wR1awJVMPwMXGJjys5PCrzNROs_VwQxZBKCqUEeuMZLM8e0P1l-s1czvLAkw',
        'content-type': 'application/json',
        'origin': 'https://www.popai.pro',
        'referer': 'https://www.popai.pro/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'isGetJson': True,
        'channelId': '218d8710-facd-4c4d-82f0-077ba1259b65',
        'message': prompt,
        'model': 'GPT-3.5',
        'messageIds': [],
        'improveId': None,
        'richMessageId': None,
        'isImprove': False,
        'isNewChat': False,
        'action': None,
    }

    response = requests.post('https://api.popai.pro/api/v1/chat/send', headers=headers, json=json_data)
    return response.text

"""
# Welcome to CanonPDF!
"""

text = st.text_input("Enter PDF URL")

if st.button("Go!"):
    st.write(send_prompt("Summarise the main points of the article in a list format:"))



