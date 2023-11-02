
import streamlit
import pandas
import requests


streamlit.title("My Parents new healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled eggs')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

myFruitList = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Please select a fruit:",list(myFruitList.Fruit))
streamlit.dataframe(myFruitList)

streamlit.header('FruityVice fruit advice')

fruit_choice = streamlit.textinput('Please select a fruit of your choice','kiwi')
streamlit.write(fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
