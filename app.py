import streamlit as st
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    st.title("Abdullah' Calculator")

    x = st.number_input("Enter the first number:", value=0.0)
    y = st.number_input("Enter the second number:", value=0.0)
    operator = st.selectbox("Select an operator:", ["+", "-", "*", "/"])

    if st.button("Calculate"):
        if operator == '+':
            result = add(x, y)
        elif operator == '-':
            result = subtract(x, y)
        elif operator == '*':
            result = multiply(x, y)
        elif operator == '/':
            result = divide(x, y)
        else:
            result = "Invalid operator"

        st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
