import streamlit as st

st.title('SREAMLIT TUTORIAL')
st.write("This is new APP")

button1 = st.button("Click Me!!")
if button1:
    st.write("Has clicat el botó")

st.markdown("""---""")
st.header("CHECKBOX")
like = st.checkbox("T'agrada aquesta APP?")
button2 = st.button("Envia")
if button2:
    if like:
        st.write("Gracies, l'he feta jo")
    else:
        st.write("Ets un CAP DE FAVA!!!")

st.markdown("""---""")
st.header("RADIO BUTTON")
animal = st.radio("Quin és el teu animal preferit?", ("Lleó","Tigre","Os"))
button3 = st.button("Envia animal preferit")
if button3:
    st.write("El teu animal preferit és: ",animal)
    if animal == "Lleó":
        st.write("ROAR!!!")

st.markdown("""---""")
st.header("SELECTBOX")
animal2 = st.selectbox("Quin és el teu animal preferit?", ("Lleó","Tigre","Os"))
button4 = st.button("Torna enviar animal preferit")
if button4:
    st.write("El teu animal preferit és: ",animal2)
    if animal2 == "Lleó":
        st.write("ROAR!!!")

st.markdown("""---""")
st.header("MULTISELECT")
options = st.multiselect("Quins son els tesu animals preferits", ["Lleó","Tigre","Os","Elefant"])
button5 = st.button("Envia animals preferits")
if button5:
    st.write("Has elegit: ",options)

st.markdown("""---""")
st.header("SLIDER")
qualificacio = st.slider("Indica la nota", 0,10)
button6 = st.button("Envia la nota")
if button6:
    st.write("Qualificació: ",qualificacio)


st.markdown("""---""")
st.header("TEXT INPUT")
user_text = st.text_input("Quina és la teva pelicula favorita?", "STAR WARS!!!")
button7 = st.button("Envia pelicula")
if button7:
    st.write("PELICULA FAVORITA: ",user_text)

st.markdown("""---""")
st.header("NUMBER INPUT")
user_number = st.number_input("Quin és el teu numero favorit?")
button8 = st.button("Envia numero")
if button8:
    st.write("NUMERO FAVORIT: ",user_number)


def run_sentiment_analysis(txt):
    st.write(f"ANALISI FETA!!! {txt}")

st.markdown("""---""")
st.header("TEXT AREA")
text = st.text_area("Introdueix el text que vols analitzar", '''As you learned in Streamlit fundamentals, Streamlit runs a server that clients connect to. That means viewers of your app don't have direct access to the files which are local to your app. Most of the time, this doesn't matter because Streamlt commands handle that for you.''')
st.write('SENTIMENT: ',run_sentiment_analysis(text))
