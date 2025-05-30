import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Chai is being prepared!")
    
    
add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Ginger is being added to your chai!")

tea_type = st.radio("Pick you chai base:", ["Milk", "water", "White", "Sugar"])
st.write(f"You have selected {tea_type} as your chai base.")
flavour = st.selectbox("Select a flavour:", ["Cardamom", "Cinnamon", "Tulsi", "Adrak"])
st.write(f"Selected flavour is {flavour}.")
sugar = st.slider("Sugar level:", 0, 10, 5)
cups = st.number_input("How many cups of chai do you want?", min_value=1, max_value=10, step=1)
st.write(f"Selected chai {cups}.")
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}, your chai is being prepared!")
    
dob = st.date_input("Enter your date of birth")
st.write(f"Your date of birth is {dob}.")


