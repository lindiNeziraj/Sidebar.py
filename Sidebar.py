import streamlit as st
st.title("Rregjistrimi")
st.write("Hyrja ne te dhena!")


Emri = st.text_input("Emri: ")
Mbiemri = st.text_input("Mbiemri: ")
Mosha = st.number_input("Mosha: ", min_value=0, max_value=100)
Te_dhena = st.button("Shtyp per te dhena!")
st.success("Urime!")

st.write(f"Emri: {Emri}")
st.write(f"Mbiemri: {Mbiemri}")
st.write(f"Mosha: {Mosha}")
st.write(f"Te dhena: {Te_dhena}")