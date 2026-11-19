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

q = st.selectbox('Выбрать канал', ['', 'Aplovolika', 'WB-Курьер, обучение', 'Банки, обучение', 'Авито перепродажи, обучение'])


with st.expander("Нажми, чтобы узнать больше"):
    st.latex(r"E = mc^2")
    st.image('ап/ал.jpg')






if q == 'Aplovolika':
    st.write('')

    
    ta1, ta2 = st.tabs(['qwerty', 'adsfgh'])
    








elif q == 'WB-Курьер, обучение':
    hea('Coming soon...')
    mar('Много текста с длинными предложения ми и важными **СЛОВАМИ**')

elif q == 'Банки, обучение':
    hea('Coming soon...')

elif q == 'Авито перепродажи, обучение':
    hea('Coming soon...')

with ta1:
    hea('hello')
    mar('My favourite food is chokolate')




