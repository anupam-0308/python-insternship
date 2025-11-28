import streamlit as st
import pandas as pd

st.title("Hello ANUPAM")
st.text("welcome to Dashboard")
st.header("I am a header")
st.write("you can write ",10+5)
         
name = st.text_input("Enter your name : ")
age = st.number_input("Enter your age: ")
st.write("Your name is :",name, "Your age is : ",age)
st.selectbox("Enter your course : " ,["BCA","BTECH","BBA"])
if st.button("CLICK ME"):
    st.success("Clicked Button")
file = st.file_uploader("Upload your file")
if file:
    content = file.read()
    st.write("File Uploaded Successfully !!!!")

data = {"Name": ["TOM","JACK","POP","HARRY"],"Marks" :[10,10,20,10]}
df = pd.DataFrame(data)

st.dataframe(df)

data = pd.DataFrame({
    "Marks" : [10,10,20,10]
})
st.line_chart(data)
st.bar_chart(data)




