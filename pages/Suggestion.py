import smtplib
import streamlit as st
from PIL.ImageQt import toqimage
from openpyxl.styles.alignment import horizontal_alignments
from reportlab.lib.pdfencrypt import padding

import utils.Common_header as ch
import utils.Common_footer as cf
import smtplib as sb
import email.message as em

st.set_page_config(page_title="Welcome to Project Name",
                   page_icon="images/saleslg.png",
                   layout="wide")
ch.print_header()
st.divider()
st.markdown("""<p style='text-align:center;background-color:blue;color:white;font:weight:bold;font-size:35px'><u>Suggestion</u>""",unsafe_allow_html=True)

with st.container(border=True):
    st.subheader("Share Your suggestion📝")
    st.markdown("**We value your idease.Please share your Suggestion for improvement below.**")
col1,col2,col3=st.columns([1,5,1],gap="large")
with col2:
    with st.form(""):
        name=st.text_input("**Name**",placeholder="Enter Your Full Name");
        email=st.text_input("**Email Id📧**",placeholder="email.com");
        mob=st.text_input("**Mobile No📱:**",placeholder="+91");
        select=st.selectbox("**Topic of the Suggestion🔽**",["Select a Topic..",
                                                      "Product Features",
                                                      "Website Usability",
                                                      "Content Ideas"])
        sugg=st.text_area("**detailed Suggestion Message💬**",placeholder="Share your Detailed thoughts,ideas, or feedback here..",
                          height=100,max_chars=2100)
        b1,b2=st.columns([5,5])
        with b1:
         if st.button("Submit Suggestion✅"):
            sender_email = "mydreamme733@gmail.com"
            sender_app_pass = "mxme ftrf ebch yirh"
            msg = em.EmailMessage()
            msg["To"] = sender_email
            msg["Subject"] = "A new Suggestion Received"
            msg.set_content(f"""
 Hello admin,
            
              Your have ha received a new sms  from a user of Data 
              analysis
            
              Topic of Suggestion:{sugg}         
              please find below details-      
            - Name of Person: {name}     
            - email of person: {email}          
            - mobile number of person: {mob}
            - Suggestion Message:-   {msg}
            """)
            smtp = smtplib.SMTP("smtp.gmail.com", 587)
            smtp.starttls()
            smtp.login(sender_email, sender_app_pass)
            smtp.send_message(msg)
            smtp.quit()
            st.success("Email Sent successfully!")
        with b2:
            reset=st.button("Reset🔄")
cf.print_footer()