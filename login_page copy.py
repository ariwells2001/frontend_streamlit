import streamlit as st
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from tokenonly import dummy


##### Backend URL Endpoints ######
signup_point = 'sighup/'
login_point = 'login/'
hubm2_point = 'hubm2/'
smartplug_point = 'smartplug/'
rollershade_point = 'rollershade/'
curtain_point = 'curtain/'
relay_point = 'relay/'
motion_point = 'motion/'
door_point = 'door/'
weather_point = 'weather/'
illuminance_point = 'illuminance/'
cube_point = 'cube/'
miniswitch_point = 'miniswitch/'
wallswitch1_point = 'wallswitch1/'
wallswitch2_point = 'wallswitch2/'
wirelessswitch1_point = 'wirelessswitch1/'
wirelessswitch2_point = 'wirelessswitch2/'

endpoints1 = [hubm2_point,smartplug_point,relay_point,motion_point,
            door_point,illuminance_point,cube_point,miniswitch_point,wallswitch1_point,wirelessswitch1_point
             ]
endpoints2 = [rollershade_point,curtain_point,wallswitch2_point,wirelessswitch2_point]



TOKEN=""
username=""
location= "http://localhost:8000/backend/"

def login(location):
    
    username = st.text_input("User Name")
    password = st.text_input("Password", type="password")
    loginButton = st.button("Login")
       
    # placeholder1 = st.empty()
    # placeholder2 = st.empty()
    # placeholder3 = st.empty()


    with st.form("Login"):
         username = st.text_input("User Name")
         password = st.text_input("Password", type="password")
         loginButton = st.form_submit_button("Login")
       

    if loginButton:
        #dummy()
        data = {
            'username': username,
            'password': password
            }

        data = json.dumps(data)
        # placeholder1.empty()
        # placeholder2.empty()
        # placeholder3.empty()
        
        response = requests.post(url=(location + login_point),data=data)
        data = json.loads(response.text)
        TOKEN = data['token']
        status = response

        dataLogs1 =[]
        dataLogs2 =[]
        full_list = []
        DN = 100

        st.write("Logged as {}".format(username))
        
        # DN=st.number_input(label="Retrieved Data",value=10)
        headers = {
            'Authorization': 'Token {}'.format(TOKEN),
            'Content-Type': 'application/json;charset=UTF-8',
            'DN':str(DN),
            'ORDERING':'-id'
        }

        response = requests.get(url= (location + weather_point),headers=headers)
        data = json.loads(response.text)
        status = response

        #print('data is {} and status is {}'.format(data[0]['modelName'],status))
        if data !=[]:
            #print(data[0])
            df = pd.DataFrame.from_dict(data)
            df[['temperature']] = df[['temperature']]/100
            df[['humidity']] = df[['humidity']]/100
            df[['airpressure']] = df[['airpressure']]/100
            st.write(weather_point)
            st.write(df[['temperature','humidity','airpressure','datetime']].head(1))
            full_list.append(weather_point[30:-1])
        
        # st.write("""### Pair Grid Chart for Correlation""")
        # g = sns.PairGrid(df[['temperature','humidity','airpressure']])
        # g.map_diag(sns.histplot)
        # g.map_offdiag(sns.scatterplot)
        # g.add_legend()
        # g.savefig("output.png")
        # st.pyplot(g)

            fig = plt.figure(figsize=(10,4))
            sns.lineplot(data=df[['datetime','temperature']])
            sns.lineplot(data=df[['datetime','humidity']])
            st.pyplot(fig)
            #fig = plt.figure(figsize=(10,4))
            
            #st.pyplot(fig)
            fig = plt.figure(figsize=(10,4))
            sns.lineplot(data=df[['datetime','airpressure']])
            st.pyplot(fig)
        i = 0
        for endpoint1 in endpoints1:
            response = requests.get(url=(location + endpoint1),headers=headers)
            dataLogs1.append(json.loads(response.text))
            status = response

            #print('data is {} and status is {}'.format(dataLogs[i][0]['modelName'],status))
            print(dataLogs1[i])
            df = pd.DataFrame.from_dict(dataLogs1[i])
            if dataLogs1[i]!=[]:
                st.write(endpoint1)
                st.write(df[["modelName","deviceId","value","datetime"]].head(1))
                full_list.append(endpoint1[30:-1])
                fig = plt.figure(figsize=(10,4))
                sns.lineplot(data=df[['datetime','value']])
                st.pyplot(fig)
            i=i+1
        
        j = 0
        for endpoint2 in endpoints2:
            response = requests.get(url=(location + endpoint2),headers=headers)
            dataLogs2.append(json.loads(response.text))
            status = response

            #print('data is {} and status is {}'.format(dataLogs[i][0]['modelName'],status))
            print(dataLogs2[j])
            df = pd.DataFrame.from_dict(dataLogs2[j])
        
            if dataLogs2[j]!=[]:
                st.write(endpoint2)
                st.write(df[["modeName","deviceId","value1","value2","datetime"]].head(1))
                full_list.append(endpoint2[30:-1])
                fig = plt.figure(figsize=(10,4))
                sns.lineplot(data=df[['datetime','value1']])
                sns.lineplot(data=df[['datetime','value2']])
                st.pyplot(fig)
            j=j+1
            # df[['temperature']] = df[['temperature']]/100
            # df[['humidity']] = df[['humidity']]/100
            # df[['airpressure']] = df[['airpressure']]/100
            # st.write(df[['temperature','humidity','airpressure','datetime']])
            # st.sidebar.button("Test")
            # st.write("""### Pair Grid Chart for Correlation""")
            # g = sns.PairGrid(df[['temperature','humidity','airpressure']])
            # g.map_diag(sns.histplot)
            # g.map_offdiag(sns.scatterplot)
            # g.add_legend()
            # g.savefig("output.png")
            # st.pyplot(g)

            # fig = plt.figure(figsize=(10,4))
            # sns.lineplot(data=df[['datetime','temperature']])
            # st.pyplot(fig)
        
        page = st.sidebar.selectbox("Devices List",full_list)
        return 0
        
        

if __name__ == '__main__':
	login(location)