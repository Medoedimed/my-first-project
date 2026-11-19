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
q = st.selectbox('', ['1', '2', '3', '4'])
ta1, ta2 = st.tabs(['qwerty', 'adsfgh'])
with ta1:
    hea('hello')
    mar('My favourite food is chokolate')
with st.expander("Нажми, чтобы узнать больше"):
    st.latex(r"E = mc^2")
    st.image(r'A1.jpg')






if q == '1':
    st.write('')










elif q == '2':
    hea('Coming soon...')
    mar('Много текста с длинными предложения ми и важными **СЛОВАМИ**')

elif q == '3':
    hea('Coming soon...')

elif q == '4':
    hea('Coming soon...')
