import streamlit as st
import pandas as pd

st.title("Zomato Data Analysis Dashboard")

df = pd.read_csv("zomato.csv", encoding='ISO-8859-1')

st.write(df.head())

city = st.selectbox("Select City", df['City'].unique())

filtered_df = df[df['City'] == city]

st.write(filtered_df.head())

st.subheader("Rating Distribution")

st.bar_chart(filtered_df['Aggregate rating'].value_counts())

df['Cuisines'] = df['Cuisines'].fillna('Unknown')
df['Cuisines'] = df['Cuisines'].str.split(', ')
df_exploded = df.explode('Cuisines')

top_cuisines = df_exploded['Cuisines'].value_counts().head(10)

st.subheader("Top Cuisines")
st.bar_chart(top_cuisines)