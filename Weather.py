import requests
import streamlit as st
def weather(city):
    api=st.secrets['api']  
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
    response=requests.get(url)
    data=response.json()
    if data.get('cod')!=404:
        main=data.get('main',{})
        description=data.get('weather',[{}])[0].get('description',"N/A")
        temperature=main.get('temp','N/A')
        st.write('🏙City: ',city)
        st.write('🌡Temperature: ',temperature)
        st.write('📝Desciption: ',description)
        if temperature<10:
            st.snow()
        else:
            st.balloons()    
    else:
        st.error('🚫City not found.')
if __name__=='__main__':
    city=st.text_input("Enter city name here : ")
    weather(city)       
