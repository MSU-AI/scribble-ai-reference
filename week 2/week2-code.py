import streamlit as st

table_dict = {
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [20, 21, 22, 23, 24]
}

# st.image("cat.jpg")

st.title("Hello ! Welcome to the number guessing game")

st.write("Enter any number and we will display a different image depending on whether the number is odd or even")

num = st.number_input("Enter a number", min_value=0)

if num % 2 == 0 and num != 0:
    st.subheader("You win a cat!")
    st.image("cat.jpg")
elif num % 2 != 0 and num != 0:
    st.subheader("You win a dog!")
    st.image("dog.jpg")
else:
    pass
