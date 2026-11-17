import streamlit as st
from itertools import islice

def exp(dict, n):
    i, j = next(islice(dict.items(), n, n + 1))
    with st.expander(i):
        st.markdown(j)
def mar(txt):
    st.markdown(txt)
st.title('Hello')
st.sidebar.selectbox('', ['q1', 'q2', 'q3', 'q4'])
with q1:
    st.write('lk')


