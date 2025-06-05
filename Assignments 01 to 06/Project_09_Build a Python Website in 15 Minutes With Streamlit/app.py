import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")

# --- Header Section ---
st.subheader("Hi, I am Azeezullah :")
st.title("A Web Developer | Digital Marketer | AI Engineer")
# --- Description ---
st.write("I help businesses grow with modern websites and smart ad campaigns.")

# --- Load Image ---
from PIL import Image
img = Image.open("assets/profile.jpg")
st.image(img, width=200)

# --- Contact Form ---
st.write("---")
st.header("📬 Get In Touch With Me!")
contact_form = """
<form action="https://formsubmit.co/azeezullahnoohpoto@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required><br><br>
     <input type="email" name="email" placeholder="Your email" required><br><br>
     <textarea name="message" placeholder="Your message here" required></textarea><br><br>
     <button type="submit">Send</button>
</form>
"""

# Display the form
st.markdown(contact_form, unsafe_allow_html=True)

# Social Links Section
st.write("---")
st.subheader("🌐 Connect with me")

st.markdown("""
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/azeezullah-noohpoto-6499b52a6)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/AZ-AZEEZULLAH)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/923043566873)
""", unsafe_allow_html=True)


# Hide Streamlit Style
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- Footer ---
st.write("---")
st.write("Made with ❤️ by Azeezullah")  
# --- Footer Style ---
footer_style = """
            <style>
            footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                text-align: center;
            }
            </style>
            """
st.markdown(footer_style, unsafe_allow_html=True)
