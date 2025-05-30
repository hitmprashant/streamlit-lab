import streamlit as st
st.title("Streamlit Lab")
st.header("Welcome to the Streamlit Lab!")
st.text("This is a simple Streamlit application to demonstrate basic functionality.")
st.write("Choose your favorite chai")
chai = st.selectbox("Your Fav. chai", ["Ginger", "Masala", "Lemon", "Green", "Black"])
st.write(f"You choose {chai} chai. Excelent choice!")
st.success("Your chai have been brewed and is ready to be served!")


