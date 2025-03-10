import streamlit as st
import re

def check_password_strength(password):
    suggestions = []
    
    if len(password) < 6:
        suggestions.append("Use at least 6 characters.")
        return "Weak", suggestions
    
    if not re.search("[a-z]", password):
        suggestions.append("Include at least one lowercase letter.")
    
    if not re.search("[A-Z]", password):
        suggestions.append("Include at least one uppercase letter.")
    
    if not re.search("[0-9]", password):
        suggestions.append("Include at least one digit.")
    
    if not re.search("[@#$%^&+=]", password):
        suggestions.append("Include at least one special character (@, #, $, etc.).")
    
    if len(suggestions) >= 3:
        return "Weak", suggestions
    elif len(suggestions) == 2:
        return "Medium", suggestions
    elif len(suggestions) == 1:
        return "Strong", suggestions
    else:
        return "Very Strong", ["Great! Your password is very strong."]

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter a password", type="password")

if password:
    strength, suggestions = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")

    if suggestions:
        st.write("*****Suggestions to Improve:*****")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

st.button("Check Password Strength")
