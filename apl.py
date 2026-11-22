import streamlit as st
from itertools import islice

def exp(i, j):
    with st.expander(i):
        st.markdown(j)
def mar(txt):
    st.markdown(txt)
def tit(txt):
    st.title(txt)
def hea(txt):
    st.header(txt)
def ima(adr):
    st.image(adr)




#start
st.title('Hello')
#ima('ап/пз.jpg')
with st.expander("ЮРИДИЧЕСКАЯ ИНФОРМАЦИЯ И ПРАВИЛА ПРОЕКТА «APLOVOLIKA»"):
    st.latex(r"E = mc^2")
    
    mar('''• Полная юридическая информация и дисклеймер: [ССЫЛКА НА ДОКУМЕНТ](https://docs.google.com/document/d/1dIQJ9G3hlMnczXa5pik6zBpvlfeCVZ_dBVCGFxuaZD4/edit?usp=drivesdk)

• Политика конфиденциальности: [ССЫЛКА НА ДОКУМЕНТ](https://docs.google.com/document/d/1zqOBbswMuTDWhLwonkuSOTrLEdBuiXbWMzEQ9_9pnU8/edit?usp=drivesdk)

• Договор-оферта на размещение рекламы: [ССЫЛКА НА ДОКУМЕНТ](https://docs.google.com/document/d/12qyCaHJc8QY7mXGVe4vR0YXDRZQVcKjx3HL8BHlFcXA/edit?usp=drivesdk)''')
q = st.selectbox('Выбрать канал', ['', 'Aplovolika', 'WB-Курьер, обучение', 'Банки, обучение', 'Авито перепродажи, обучение'])

def ap1():
    ima('ап/як.jpg')
    mar('''1) WB-КУРЬЕР и ЯНДЕКС-КУРЬЕР
*Лёгкие, хорошо оплачиваемые работы с гибким графиком, который можно настроить под себя*''')
    exp('ПРЕИМУЩЕСТВА WB-курьер:', '''● Официальное трудоустройство.

● Оплата за заказ: ~100₽.

● Средний заработок за день: 1.500₽ - 2.000₽.

● За выполнение 60 заказов с учётом бонуса 3.000₽ можно за 5 дней заработать почти 10.000₽ (при полной нагрузке)

● Свободный график.

● Возраст от 16 лет.''')





if q == 'Aplovolika':
    st.write('adsf')

    
    ta1, ta2 = st.tabs(['qwerty', 'adsfgh'])
    with ta1:
        hea('hello')
        mar('My favourite food is chocolate')

    mar('deftest')
    ap1()






elif q == 'WB-Курьер, обучение':
    hea('Coming soon...')
    mar('Много текста с длинными предложения ми и важными **СЛОВАМИ**')

elif q == 'Банки, обучение':
    hea('Coming soon...')

elif q == 'Авито перепродажи, обучение':
    hea('Coming soon...')





