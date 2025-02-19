import requests
import streamlit as st
def weather(city):
#     st.markdown(f'''
#         <style>
#     .stApp{{
#         background-image: url("{image}");
#         background-size: cover;
#         background-position: top;
#         background-repeat: no-repeat;
#     }}
# </style>''',unsafe_allow_html=True
#     )
    api=st.secrets['api']  
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
    response=requests.get(url)
    data=response.json()
    if data.get('cod')!=404:
        main=data.get('main',{})
        description=data.get('weather',[{}])[0].get('description',"N/A")
        temperature=float(main.get('temp',0))
        if st.button('Check'):
            st.success(f'🏙City: {city}')
            st.success(f'🌡Temperature:{temperature} ')
            st.success(f'📝Desciption: {description}')
            if temperature<=10:
                st.snow()
            else:
                st.balloons()
    else:
        st.error('🚫City not found.')
if __name__=='__main__':
    city=st.text_input("Enter city name here : ")
    # image='https://github.com/Ghazanfar-G/Weather_checker/blob/main/weather.png?raw=true'
    weather(city)       
