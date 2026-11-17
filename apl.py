import streamlit as st
from itertools import islice

def exp(dict, n):
    i, j = next(islice(dict.items(), n, n + 1))
    with st.expander(i):
        st.markdown(j)
def mar(txt):
    st.markdown(txt)
def tit(txt):
    st.title(txt)
def hea(txt):
    st.header(txt)
st.title('Hello')
q = st.sidebar.selectbox('', ['1', '2', '3', '4'])
if q == '1':
    st.write('lk')












elif q == '2':
    hea('Coming soon...')

elif q == '3':
    hea('Coming soon...')

elif q == '4':
    hea('Coming soon...')
