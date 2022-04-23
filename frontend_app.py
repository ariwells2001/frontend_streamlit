
import streamlit as st
from login_page import login
from registration_page import registration
from signup_page import signup
from PIL import Image

image = Image.open("aqaralogo.png")
st.sidebar.title ("Test App for Backend API")

st.sidebar.image(image,width = 200)
placeholder1= st.sidebar.empty()
placeholder2 = st.sidebar.empty()
placeholder3 = st.sidebar.empty()
placeholder4 = st.sidebar.empty()
placeholder5 = st.sidebar.empty()

        
# with placeholder1.form("Basic Settings"):

#     server = st.selectbox("Server",("Localhost","Aqara Korea","Ariwells"))
#     httpsOK = st.checkbox("HTTPS",value=False)
#     eight000 = st.checkbox("Port 8000",value=True)
#     page = st.selectbox("Login/out-Signup",("Aqara Account Registration","Login","Signup"))
#     settingButton = st.form_submit_button("Submit")

# with st.form("Basic Settings"):

server = placeholder1.selectbox("Server",("Localhost","Aqara Korea","Ariwells"))
httpsOK = placeholder2.checkbox("HTTPS",value=False)
eight000 = placeholder3.checkbox("Port 8000",value=True)
page = placeholder4.selectbox("Login/out-Signup",("Please select a menu","Login","Aqara Account Registration","Signup"))
messageOnly = placeholder5.write("If you are a new user, please register an Aqara Account and sign up first")
    # settingButton = st.form_submit_button("Submit")
#settingButton = placeholder5.button("Submit")

if page=="Login":
    
    placeholder1.empty()
    placeholder2.empty()
    placeholder3.empty()
    placeholder4.empty()
    placeholder5.empty()
    

    if server == "Localhost":
        serverIP = "localhost"
    elif server == "Aqara Korea":
        serverIP = "aqarakorea.kr"
    elif server == "Ariwells":
        serverIP = "ariwells.kr"


    if httpsOK == False:
        headValue = "http://"
    else:
        headValue = "https://"

    if eight000 == True:
        portValue=":8000/backend/"
    else:
        portValue="/backend/"

    location = headValue + serverIP + portValue
    login(location)

elif page=="Aqara Account Registration":
    
    placeholder1.empty()
    placeholder2.empty()
    placeholder3.empty()
    placeholder4.empty()
    #placeholder5.empty()
    

    if server == "Localhost":
        serverIP = "localhost"
    elif server == "Aqara Korea":
        serverIP = "aqarakorea.kr"
    elif server == "Ariwells":
        serverIP = "ariwells.kr"


    if httpsOK == False:
        headValue = "http://"
    else:
        headValue = "https://"

    if eight000 == True:
        portValue=":8000/backend/"
    else:
        portValue="/backend/"

    location = headValue + serverIP + portValue

    registration(location)

elif page=="Signup":
    
    placeholder1.empty()
    placeholder2.empty()
    placeholder3.empty()
    placeholder4.empty()
    #placeholder5.empty()
    

    if server == "Localhost":
        serverIP = "localhost"
    elif server == "Aqara Korea":
        serverIP = "aqarakorea.kr"
    elif server == "Ariwells":
        serverIP = "ariwells.kr"


    if httpsOK == False:
        headValue = "http://"
    else:
        headValue = "https://"

    if eight000 == True:
        portValue=":8000/backend/"
    else:
        portValue="/backend/"

    location = headValue + serverIP + portValue

    signup(location)