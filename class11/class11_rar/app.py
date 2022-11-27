import streamlit as st
import pandas as pd
import numpy as np

st.image("https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/NEDUET_logo.svg/1200px-NEDUET_logo.svg.png", width=100)
st.title("Dynamic Data Handling")
# st.text('Fixed width text')
# st.markdown('# Markdown') # see *
# st.code('for i in range(8): foo()')
read_and_cache_csv = st.cache(pd.read_csv)
df = read_and_cache_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# gender = st.selectbox("Sex",df.Sex.unique())

# st.button('Click me')
# st.checkbox('I agree')

# gender = st.sidebar.radio('Select one:', df.Sex.unique())



# st.write(gender,type(gender))


with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    sbt = st.form_submit_button('Login')


if sbt:
    if username=='admin' and password == 'admin':
        st.write("Successfully Login")
        st.line_chart(df,x="Sex",y="Age")
        gender = st.sidebar.multiselect('Select one:', df.Sex.unique())
        st.dataframe(df[df.Sex.isin(gender)])
        st.write("Total Row",len(df[df.Sex.isin(gender)]))  
    else:
        st.write("Invalid username or password")


      
# st.dataframe(df)
# st.table(df.iloc[0:10])
# st.json(df.head(10).to_dict())
# st.metric(label="Temperature", value="70 °F", delta="1.2 °F")