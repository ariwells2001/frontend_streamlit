import streamlit as st
import requests
import json



##### Backend URL Endpoints ######
signup_point = 'http://localhost:8000/backend/sighup/'
login_point = 'http://localhost:8000/backend/login/'

#st.title ("Smart Office Dashboard")

def login(token="12345678"):
    
    if token == "12345678":
        placeholder1 = st.empty()
        placeholder2 = st.empty()
        placeholder3 = st.empty()
        username = placeholder1.text_input("User Name")
        password = placeholder2.text_input("Password", type="password")
        loginButton = placeholder3.button("Login")

    
    data = {
        'username': username,
        'password': password
    }

    data = json.dumps(data)

    if loginButton:
        placeholder1.empty()
        placeholder2.empty()
        placeholder3.empty()
        response = requests.post(url=login_point,data=data)
        data = json.loads(response.text)
        token = data['token']
        status = response
    return token

def dummy():
    st.subheader("Success")

if __name__ == '__main__':
	login()