import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai Lovers")
    st.image("https://media.istockphoto.com/id/614533094/photo/indian-masala-chai-tea.jpg?s=612x612&w=0&k=20&c=0P-npS30JIBX0FA9csLyB0WYtkEU7gWkNE7nSnvXlSE=", width=300)
    vote1 = st.button("Vote for Masala Chai Lovers")
    
    
with col2:
    st.header("Adrak Chai Lovers")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLNkTTuD6qNzuMLYxaQ-MSuy8jOwSa-MnjCQ&s", width=300)
    vote2 = st.button("Vote for Adrak Chai Lovers")
    

if vote1:
    st.success("Thank you for voting for Masala Chai Lovers!")
elif vote2:
    st.success("Thank you for voting for Adrak Chai Lovers!")
    
name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Select your favorite tea", ["Masala Chai", "Adrak Chai", "Lemon Chai", "Green Tea", "Black Tea"])
st.write(f"Thank you {name} for voting! You selected {tea} as your favorite tea.")
with st.expander("Show Team Making Instructions"):
    st.write("""
    1. Boil water in a pot.
    2. Add tea leaves and spices.
    3. Let it simmer for a few minutes.
    4. Strain the tea into cups.
    5. Add milk and sugar to taste.
    6. Serve hot and enjoy your chai! 
""")
    
st.markdown('### Welcome to the Chai Taste Poll!')
st.markdown('> Blockquote: "Chai is not just a drink, it’s an emotion."')



