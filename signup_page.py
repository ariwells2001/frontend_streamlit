import streamlit as st
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from tokenonly import dummy
from devices_page import devices


end_point = 'signup/'
update_point = 'myupdate/'


# except Exception as e:
#     print(type(e))
#     print("The accesstoken had already been requested. You do not have to apply for it again")
username=""
location= "http://localhost:8000/backend/"

def signup(location):
    
    # username = st.text_input("User Name")
    # password = st.text_input("Password", type="password")
    # loginButton = st.button("Login")
    print(location)
    placeholder1 = st.sidebar.empty()
    placeholder2 = st.sidebar.empty()
    placeholder3 = st.sidebar.empty()


 #   with st.sidebar.form("Login"):
    with placeholder1.form("Signup"):
        account = st.text_input("Account")
        password = st.text_input("Password", type="password")
        email = st.text_input("Aqara Email Account")
        # loginButton = placeholder3.selectbox("Login",("Choose a Login menu","Login"))
        # loginButton = placeholder3.button("Login")
        # numberOfDataRetrieved = st.slider("Number of Data To Be Retrieved",min_value=1,max_value=100,value=50,step=10)
        # numberOfRowsInTable = st.slider("Number of Rows in a Table",min_value=1,max_value=20,value=5,step=1)
        submitButton = st.form_submit_button("Submit")
       

    if submitButton:
        st.subheader("Registration of Aqara Account")
        
        headers = {
                    'Content-Type': 'application/json'
                    }
        data = {
            'username':account,
            'password':password,
            'email':email
        }

        data = json.dumps(data)

        # response = requests.post(url=end_point,data=data)
        # data = json.loads(response.text)
        # status = response

        # print('token is {} and status is {}'.format(data,status))

        # # try:
        response = requests.post(url=(location + end_point),headers=headers,data=data)
        data = json.loads(response.text)
        status = response
        TOKEN = data['token']
        st.write(TOKEN)
        
        headers = {
                    'Authorization': 'Token {}'.format(TOKEN),
                    'Content-Type': 'application/json;charset=UTF-8',
                    'DN':'1'
                        }
        response = requests.get(url=(location + update_point),headers=headers)
        data = json.loads(response.text)
        status = response

        st.write('data is {} and status is {}'.format(data,status))


        # st.write('token is {} and status is {}'.format(data,status))
        st.write("Your account has been registered Successfully.")
        st.write("Please refresh a web browser")

        # if logoffButton:
        #     st.write("Logged off")
        # #dummy()
        # data = {
        #     'username': username,
        #     'password': password
        #     }

        # data = json.dumps(data)
        # # placeholder1.empty()
        # # placeholder2.empty()
        # # placeholder3.empty()
        
        # response = requests.post(url=(location + login_point),data=data)
        # data = json.loads(response.text)
        # TOKEN = data['token']
        # status = response

        # dataLogs1 =[]
        # dataLogs2 =[]
        # full_list = []
        # DN = 100

        # st.write("Logged as {}".format(username))
        
        # # DN=st.number_input(label="Retrieved Data",value=10)
        # headers = {
        #     'Authorization': 'Token {}'.format(TOKEN),
        #     'Content-Type': 'application/json;charset=UTF-8',
        #     'DN':str(DN),
        #     'ORDERING':'-id'
        # }

        # response = requests.get(url= (location + weather_point),headers=headers)
        # data = json.loads(response.text)
        # status = response

        # #print('data is {} and status is {}'.format(data[0]['modelName'],status))
        # if data !=[]:
        #     #print(data[0])
        #     df = pd.DataFrame.from_dict(data)
        #     df[['temperature']] = df[['temperature']]/100
        #     df[['humidity']] = df[['humidity']]/100
        #     df[['airpressure']] = df[['airpressure']]/100
        #     st.write(weather_point)
        #     st.write(df[['temperature','humidity','airpressure','datetime']].head(1))
        #     full_list.append(weather_point[30:-1])
        
        # # st.write("""### Pair Grid Chart for Correlation""")
        # # g = sns.PairGrid(df[['temperature','humidity','airpressure']])
        # # g.map_diag(sns.histplot)
        # # g.map_offdiag(sns.scatterplot)
        # # g.add_legend()
        # # g.savefig("output.png")
        # # st.pyplot(g)

        #     fig = plt.figure(figsize=(10,4))
        #     sns.lineplot(data=df[['datetime','temperature']])
        #     sns.lineplot(data=df[['datetime','humidity']])
        #     st.pyplot(fig)
        #     #fig = plt.figure(figsize=(10,4))
            
        #     #st.pyplot(fig)
        #     fig = plt.figure(figsize=(10,4))
        #     sns.lineplot(data=df[['datetime','airpressure']])
        #     st.pyplot(fig)
        # i = 0
        # for endpoint1 in endpoints1:
        #     response = requests.get(url=(location + endpoint1),headers=headers)
        #     dataLogs1.append(json.loads(response.text))
        #     status = response

        #     #print('data is {} and status is {}'.format(dataLogs[i][0]['modelName'],status))
        #     print(dataLogs1[i])
        #     df = pd.DataFrame.from_dict(dataLogs1[i])
        #     if dataLogs1[i]!=[]:
        #         st.write(endpoint1)
        #         st.write(df[["modelName","deviceId","value","datetime"]].head(1))
        #         full_list.append(endpoint1[30:-1])
        #         fig = plt.figure(figsize=(10,4))
        #         sns.lineplot(data=df[['datetime','value']])
        #         st.pyplot(fig)
        #     i=i+1
        
        # j = 0
        # for endpoint2 in endpoints2:
        #     response = requests.get(url=(location + endpoint2),headers=headers)
        #     dataLogs2.append(json.loads(response.text))
        #     status = response

        #     #print('data is {} and status is {}'.format(dataLogs[i][0]['modelName'],status))
        #     print(dataLogs2[j])
        #     df = pd.DataFrame.from_dict(dataLogs2[j])
        
        #     if dataLogs2[j]!=[]:
        #         st.write(endpoint2)
        #         st.write(df[["modeName","deviceId","value1","value2","datetime"]].head(1))
        #         full_list.append(endpoint2[30:-1])
        #         fig = plt.figure(figsize=(10,4))
        #         sns.lineplot(data=df[['datetime','value1']])
        #         sns.lineplot(data=df[['datetime','value2']])
        #         st.pyplot(fig)
        #     j=j+1
        #     # df[['temperature']] = df[['temperature']]/100
        #     # df[['humidity']] = df[['humidity']]/100
        #     # df[['airpressure']] = df[['airpressure']]/100
        #     # st.write(df[['temperature','humidity','airpressure','datetime']])
        #     # st.sidebar.button("Test")
        #     # st.write("""### Pair Grid Chart for Correlation""")
        #     # g = sns.PairGrid(df[['temperature','humidity','airpressure']])
        #     # g.map_diag(sns.histplot)
        #     # g.map_offdiag(sns.scatterplot)
        #     # g.add_legend()
        #     # g.savefig("output.png")
        #     # st.pyplot(g)

        #     # fig = plt.figure(figsize=(10,4))
        #     # sns.lineplot(data=df[['datetime','temperature']])
        #     # st.pyplot(fig)
        
        # page = st.sidebar.selectbox("Devices List",full_list)
        
        
        

if __name__ == '__main__':
	signup(location)