import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

dummy_text = """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. 
Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate
"""
st.write(dummy_text)

st.subheader("Our Team")

df = pandas.read_csv("self-paced-project/data.csv", sep=",")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])
with col1:
    for index, row in df[:4].iterrows():
        name = row['first name'] + " " + row['last name']
        name = name.title()
        st.subheader(name)
        st.write(row['role'])
        st.image(f"self-paced-project/images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        name = row['first name'] + " " + row['last name']
        name = name.title()
        st.subheader(name)
        st.write(row['role'])
        st.image(f"self-paced-project/images/"+row['image'])

with col3:
    for index, row in df[8:].iterrows():
        name = row['first name'] + " " + row['last name']
        name = name.title()
        st.subheader(name)
        st.write(row['role'])
        st.image(f"self-paced-project/images/" + row['image'])
