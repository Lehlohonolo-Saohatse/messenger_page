# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:41:16 2025

@author: Lehlo
"""

import streamlit as st
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")

def send_email(sender_email, sender_name, subject, message):
    recipient_email = "lehlohonolosaohatse03@gmail.com"  # Your email
    smtp_server = "smtp.gmail.com"  # SMTP server (adjust based on provider)
    smtp_port = 587  # SMTP port
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = f"Collaboration/Recruitment: {subject}"
    
    body = f"Name: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Collaborate with Lehlohonolo Saohatse")
st.write("Fill in the form below to reach out for collaboration or recruitment opportunities.")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.text_input("Subject")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send Message")

    if submit:
        if name and email and subject and message:
            response = send_email(email, name, subject, message)
            st.success(response)
        else:
            st.error("Please fill in all fields before submitting.")
