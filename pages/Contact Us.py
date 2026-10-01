import streamlit as st
from fontTools.varLib.instancer import names
from narwhals._compliant import column
from openpyxl.descriptors import container
from streamlit import columns

import utils.Common_header as ch
import utils.Common_footer as cf
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")

ch.print_header()
st.divider()
st.markdown("<div style='font-size:35px;text-align: center; color: #00B4D8;background-color:blue;color:white;'>Contact Us</div", unsafe_allow_html=True)
st.markdown("---")
col1,col2,co3=columns([1,5,1],gap="large")
with col2:
       with st.container(border=True):
        st.subheader("Contact Details")
        name=st.text_input("Enter your name")
        email=st.text_input("📧 Enter Your Email:")
        feed= st.text_area("Customer feedback")
        btn=st.button("Submit")
        if btn:
            st.success("Thank you! Your message has been submitted.")
            if btn:
                st.text("Your name is: " + name)
                st.text("Your email is :" + email)
                st.text("Your Feedback id : " + feed)

st.title("📞 Contact Us")
with st.container(border=True):
    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("""
                 <div style='background-color:; padding:20px; border-radius:12px; min-height:250px;width:250;'>
                 <h3>📍 Get In Touch</h3>
                 <br>
                 <p><b>Address:</b> Lalganj, Pratapgarh, (U.P)</p>
                 <p>📞 <b>Contact:</b> 8505802432</p>
                 <p>📧 <b>Email:</b> <a href="mailto:ansh9519@gmail.com">anshptel956@gmail.com</a></p>
                 <p>▶️ <b>YouTube:</b> <a href="https://www.youtube.com/@anshlive007" target="_blank">www.youtube.com/@anshlive007</a></p>
                 <p>ⓕ<b>Facebook:</b> <a href="https://www.facebook.com/profile.php?id=61577510685849&sfnsn=wiwspmo&mibextid=RUbZ1f"target="_blank">www.facebook.com/Harsh Shukla</a></p>
                 <p>ⓕ <b>Instagram:</b> <a href="https://www.youtube.com/redirect?event=channel_header&redir_token=QUM4Zm9rUnVZRjU5dXZYaHJMNnlXX3VIcnY3ZXxBR3JiS2FtbU5qWEI1VC1SWlpSNlhoelhCT1ZUTzVhRVZQTnBGLTZlWnQ4NUZrbXpjSXZXODNVWmg2VUQzOC00bW43V2Y4NmVHa3NlTGFzU01FOEQzTThHdlhFZS13TjlOdURw&q=https%3A%2F%2Fwww.instagram.com%2Fansh_007patel%3Figsh%3DMWVjYzVmdmFuem5saw%3D%3D" target="_blank">www.instagram.com/ansh007</a></p>
                 </div>
                 """, unsafe_allow_html=True)



    with col2:
        st.markdown("<h3>🗺️ Our Location</h3>", unsafe_allow_html=True)
        # Google Map Embed for Lalganj, Pratapgarh
        map_html = """
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14456.123!2d81.85!3d25.88!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399a0b0b0b0b0b0b%3A0x0!2sLalganj%2C%20Pratapgarh%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v123456789" 
        width="100%" height="350" style="border:0; border-radius:12px;" allowfullscreen="" loading="lazy"></iframe>
        """
        st.components.v1.html(map_html, height=350)


cf.print_footer()
