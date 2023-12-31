import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px


# get the data:

dataset = pd.read_csv('https://github.com/lzsheppard/Bico_Sound_Map/blob/main/query-result.csv', delimiter='\t')

# Example assuming the file is in the same directory as the notebook
full_data = pd.read_csv('https://github.com/lzsheppard/Bico_Sound_Map/blob/main/Bi-Co%20Sound%20Map%20Locations.csv', delimiter='\t')


# helper function to create popup data
def _makeMessage(df, indx):

    message = "<br><br>Recording information: <br><br> Description: <br>>" + dataset["description"][indx] # Provides description of the sound
    message += "<br> Date Recorded: <br>>" + dataset["date"][indx] # Provides date it was recorded
    message += "<br> Location: " + str(dataset["location"][indx])
    return message

def _makeMessage_2(df, indx):

    
    message = "<br><br>Recording information: <br><br> Description: <br>>" + full_data["Sound"][indx] # Provides description of the sound
    message += "<br> Time Recorded: <br>>" + full_data["Time"][indx] # Provides time of day it was recorded
    message += "<br> Date Recorded: <br>>" + full_data["Date"][indx] # Provides date it was recorded
    message += "<br> Recorded by: <br>>" + full_data["Recorder"][indx] # Provides recorder
    message += "<br> Recorded on: <br>>" + full_data["Device"][indx] # Provides recorded device
    message += "<br><br> Stats: <br><br> Original sound emitted for: "+ full_data["Purpose"][indx] #Purpose
    message += "<br> Volume, from 1-10: " + str(full_data["Volume"][indx])
    message += "<br> Distractability, from 1-10: " + str(full_data["Distractability"][indx])
    message += "<br> Rowdiness, from 1-10: " + str(full_data["Rowdiness"][indx])
    message += "<br> Pitch, from 1-10: " + str(full_data["Pitch"][indx])
    message += "<br> Multiplicity, from 1-10: " + str(full_data["Multiplicity"][indx])
    message += "<br> Repetition, from 1-10: " + str(full_data["Repetition"][indx])
    message += "<br> Persistence, from 1-10: " + str(full_data["Persistence"][indx])
    return message

# this is the map, with pins for each row of the dataset
#Used this post for help with tooltip formatting https://stackoverflow.com/questions/65524514/how-can-we-get-tooltips-and-popups-to-show-in-folium
st.header('Bi-Co Sound Survey Computational Essay')
st.markdown('By Logan Griffin, Luke Sheppard, Reed Solomon, and Jade Yu')
st.markdown('Sounds of Silence: A Sound Survey of the Bi-Co During Finals Week')



# here is the sidebar button to show the map
show_map = st.sidebar.checkbox('Show Map of Sound Events with Special data', value=False)

if show_map:
    #Used this post for help with tooltip formatting https://stackoverflow.com/questions/65524514/how-can-we-get-tooltips-and-popups-to-show-in-folium
    m = folium.Map(location=[40.012831, -75.30926273234793],zoom_start=13)
    tooltip = "Click me!"
    
    for indx in full_data.index:
        lon1 = full_data["Longitude"][indx]
        lat1 = full_data["Latitude"][indx]
        message = makeMessage(full_data, indx)
        folium.Marker([lon1,lat1], popup=message, tooltip=tooltip).add_to(m)
    
        folium_static(m)

show_map2 = st.sidebar.checkbox('Show Map of Sound Events', value=False)

if show_map2:

    fig = px.scatter_mapbox(full_data,
                        lat2 = full_data["Longitude"],
                        lon2 = full_data["Latitude"],
                        hover_name="description",
                        color = "Campus",
                        zoom=13)
    fig.show()

show_map3 = st.sidebar.checkbox('Show Map of Sound Event LOD', value=False)

if show_map3:
    
    m = folium.Map(location=[40.009395, -75.305613],zoom_start=13)
    tooltip = "Click me!"

    for indx in dataset.index:
        lon3 = dataset["longitude"][indx]
        lat3 = dataset["latitude"][indx]
        marker = folium.Marker(location=[lon3, lat3], 
                       tooltip=tooltip, 
                       popup=_makeMessage(dataset, indx))
        marker.add_to(m)
    m
