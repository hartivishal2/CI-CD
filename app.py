import streamlit as st

#stream lit 

st.title("Power Calculator")
st.write("Enter a number to calculate the square , cube , fifth number")

n = st.number_input("Enter a Integer " , value=1 , step=1)

square = n ** 2 
cube = n ** 3
fifthNumber = n ** 5 

st.write(f"The square is {square}")
st.write(f"The cube is {cube}")
st.write(f"The fifthSquare is {fifthNumber}")