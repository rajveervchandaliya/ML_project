import streamlit as st

# Page title
st.title("🍎 Food Calorie Counter")

# Food calorie data
calories = {
    "apple": 95,
    "banana": 105,
    "orange": 62,
    "egg": 78,
    "rice": 206,
    "roti": 71,
    "chapati": 70,
    "bread": 80,
    "pizza": 285,
    "burger": 295,
    "sandwich": 250,
    "chicken": 165,
    "dal": 120,
    "milk": 103,
    "idli": 58,
    "dosa": 168
}

# Input text
food = st.text_input("Enter a food item:")

# Calculate and display calories
if food:
    food_name = food.lower().strip()

    if food_name in calories:
        st.success(f"{food.title()} contains approximately {calories[food_name]} calories.")
    else:
        st.warning("Sorry, this food item is not in our database.")

# Display available foods
st.subheader("Available Food Items")

st.write(", ".join(food.title() for food in calories.keys()))
