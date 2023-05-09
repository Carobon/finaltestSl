import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st

##

st.title('Analyse de corrélation et de distribution dataset voitures')

link ="C:/Users/33668/Project_2/quete_streamlit/new_df_cars.csv"
df_cars = pd.read_csv(link)

def filter_by_continent(continent):
    filtered_data = data[data["Continent"] == continent]
    return filtered_data
continents = ['US.', 'Europe.' ,'Japan.']
selected_continent = st.sidebar.selectbox("Select a continent", continents)
if st.sidebar.button("Filter"):
    filtered_data = filter_by_continent(selected_continent)
else:
    filtered_data = df_cars

# Display the filtered data
st.write(filtered_data)

st.title('Heatmap dataset voitures')
st.write("La correlation est forte entre year et mpg, et time-to-60")
heatmap_col = ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60', 'year']
fig, ax = plt.subplots()
sns.heatmap(df_cars[heatmap_col].corr(), ax=ax)
st.write(fig)

st.write("La distribution des différentes series du dataframe est inégale dans le temps")
if st.checkbox("Seaborn Pairplot",value=True):
	import seaborn as sns
	fig = sns.pairplot(df_cars, hue="year") 
	st.pyplot(fig)
