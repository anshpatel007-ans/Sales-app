import streamlit as st
import pandas as pd
def print_footer():
     #Footer section
     cur_dt=pd.Timestamp.now()
     st.markdown(f"""
            <div style='width:100%;background-color:#27272A;color:white;text-align:center;
                   min-height:100px;padding-top:10px;'>
             
             
             <div style='width:50%;float:left;><p>📧 <b>Email:</b> <a href="mailto:ansh9519@gmail.com">anshptel956@gmail.com</a></p></div>
              <div style='width:50%;float:left;> <p>▶️ <b>YouTube:</b> <a href="https://www.youtube.com/@anshlive007" target="_blank">www.youtube.com/@anshlive007</a></p></div>
               <div style='width:50%;float:left;> <p>ⓕ Facebook<b>:</b> <a href="https://www.facebook.com/profile.php?id=61577510685849&sfnsn=wiwspmo&mibextid=RUbZ1f"target="_blank">www.facebook.com/Harsh Shukla</a></p></div>
              <div style='width:50%;float:left;> <p><b>🅾 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦:</b> <a href="https://www.youtube.com/redirect?event=channel_header&redir_token=QUM4Zm9rUnVZRjU5dXZYaHJMNnlXX3VIcnY3ZXxBR3JiS2FtbU5qWEI1VC1SWlpSNlhoelhCT1ZUTzVhRVZQTnBGLTZlWnQ4NUZrbXpjSXZXODNVWmg2VUQzOC00bW43V2Y4NmVHa3NlTGFzU01FOEQzTThHdlhFZS13TjlOdURw&q=https%3A%2F%2Fwww.instagram.com%2Fansh_007patel%3Figsh%3DMWVjYzVmdmFuem5saw%3D%3D" target="_blank">www.instagram.com/ansh007</a></p></div>
            <div style='width:50%;float:left;'>&copy; Copyright {cur_dt.year} to Sales Analytics App</div>
            <div style='width:50%;float:left;'>Developed By: Er. Govind Verma</div>
            </div>
               """, unsafe_allow_html=True)

