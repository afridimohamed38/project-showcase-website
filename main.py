import streamlit as st

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:  # to open a column use "with" context manager
    st.image("images/mypic.png")  # to create an image

with col2:
    st.title("Mohamed Afridi")
    content = """I'm a fresher who has just entered IT industry who is looking forward to make a positive impact!
                I completed my B.E(Mechanical) in 2020, after that I started looking for jobs and I found that 
                I was more of a computer nerd than a mechanical guy. So I joined in IT.
                I am currently working as an ETL engineer in Tata Consultancy services(TCS) this year. 
                I also have data monitoring support experience before that in the same organization"""
    st.write(content)


content2 = """
    Below you can find some of the apps i have built using python. Feel free to contact me!
"""
st.info(content2)
