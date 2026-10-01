import streamlit as st
import utils.Common_header as hd
import utils.Common_footer as cf
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
hd.print_header()
print()
st.write("---")
st.markdown("""
<div style="color:white;background-color:blue;text-align:center;
font-size:40px;padding-top:10px;border-radius:5px;">
<p><b>About Us</b></p>""",unsafe_allow_html=True)
col1,col2=st.columns([4,6])
with col1:
    with st.container(border=True):
        st.markdown("""
        <div style="background-color:#F8FAFC;border:5px solid #2563EB;box-shadow:0 2px 8px rgba(0,0,0,0.05);.main.block-container:margin:0 auto;max-width:700px;">
        <div[data-testid="stVerticalBlock"]div:hover{box-shadow:0 4px 12px rgba(0,0,0,0.01);>
        <span style="font-size:40px;"></span>
        <span style="font-size:28px; font-weight:bold;"> 📊 Project Name 
        <p style="padding-left:40px;font-size:15px;">
        <b>Sales Analytics Dashboard</b></p>
       
        </span>
        </div>
        </div>
        """,unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
        <div style="background-color:#F8FAFC; border:5px solid #2563EB;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <span style="font-size:40px;"></span>
        <span style="font-size:28px; font-weight:bold;">🏷️ Project Version

        <p style="padding-left:60px;font-size:18px;">
        Version 1.0 </p>
        </span>
        </div>
        """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
        <div style="background-color:#F8FAFC; border:5px solid #2563EB;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <span style="font-size:40px;color:info;"></span>
        <span style="font-size:28px; font-weight:bold;color:info;">⚙️Technology Name

        <p style="padding-left:40px;font-size:20px;">
        Python </p>
        </span>
        </div>
        """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
        <div style="background-color:#F8FAFC; border:5px solid #2563EB;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <span style="font-size:35px;"></span>
        <span style="font-size:28px; font-weight:bold;">🛠️ Used Technology

        <p style="padding-left:10px;font-size:20px;">
         <b>Language:</b> Python</br>
         <b>Framework:</b> Streamlit</br>
         <b>Libraries:</b>Matplotlib
        </span>
        </div>
        """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
        <div style="background-color:#F8FAFC; border:5px solid #2563EB;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <span style="font-size:40px;"></span>
        <span style="font-size:28px; font-weight:bold;">🏢 Training Company
        <p style="padding-left:20px;font-size:15px;" <b>Kamadgiri Software Solutions</b></p>
       
        </span>
        </div>
        """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
        <div style="color:white;background-color:blue;text-align:center;font-weight:bold;
        font-size:28px;padding-top:10px;border-radius:5px;">
        <p><b>🚀Our Mission</b></p>
        </div>
        """, unsafe_allow_html=True)
        m1, m2 = st.columns([3, 7])
        with m1:
            st.image("images/mission.jpg", )
        with m2:
            st.markdown("""
            You can find visual examples and design inspiration for sales analytics such a""",unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
        <div style="color:white;background-color:blue;text-align:center;font-weight:bold;
        font-size:28px;padding-top:10px;border-radius:5px;">
        <p><b>ℹ️Our Details</b></p>
        </div>
        """, unsafe_allow_html=True)
        m1, m2 = st.columns([3, 7])
        with m1:
            st.image("images/1000028982.jpg")
        with m2:
            st.markdown("""
            Name : Er.Ansh Patel
          
            Mob  : +91 8505802432
             
            email: ansh9519@gmail.com 
            """,unsafe_allow_html=True)
with col2:
    with st.container(border=True):
        st.markdown("""
        <div style="color:white;background-color:blue;text-align:center;
        font-size:30px;padding-top:10px;border-radius:5px;">
        <p><b>🎯 Project Objective</b></p>
        </div>
        <p style="font-size:20px;line-height:1.6; text-align:justify;">Project objectives are specific, measurable targets that define what a project must achieve. They guide team decisions, set clear delivery boundaries, and provide a standard for measuring success using frameworks like SMART (Specific, Measurable, Achievable, Relevant, Time-bound).Project objective lines are specific, measurable, and time-bound statements that define what a project will deliver, using frameworks like SMART (Specific, Measurable, Achievable, Relevant, Time-bound) and key performance indicators (KPIs). </p>
        """,unsafe_allow_html=True)
        sm1, sm2, sm3, sm4 = st.columns([2, 2.02, 2, 2])
        with sm1:
            with st.container(border=True):
                st.markdown("""<div style="font-size:17px;background-color:#F8FAFC;text-align:center;border:3px solid blue;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
                ✔️<br>
                Spacific</div>
                """,unsafe_allow_html=True)

        with sm2:
            with st.container(border=True,width=250):
                st.markdown("""<div style="font-size:17px; text-align:center;background-color:#F8FAFC;border:3px solid blue;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
                           ⌛<br>
                           Misurable</div>
                           """, unsafe_allow_html=True)
        with sm3:
            with st.container(border=True):
               st.markdown("""<div style="font-size:17px; text-align:center;background-color:#F8FAFC;border:3px solid blue;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
                           🥇<br>
                           Achivable</div>
                           """, unsafe_allow_html=True)
        with sm4:
            with st.container(border=True):
                st.markdown("""<div style="font-size:17px; text-align:center;background-color:#F8FAFC;border:3px solid blue;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
                           😊<br>
                           Relevent</div>
                           """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<div style='background:#2563EB; color:white;font-size:28px;text-align:center; padding:5px; border-radius:2px;font-weight:bold;'>🔑 Key Features</div>",
                    unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            - 🔑 **Easy CSV Upload**  
              Upload sales data in CSV format with one click
            - 🔑 **Real-time KPIs**  
              Track Total Sales, Total Profit, and Orders instantly
            - 🔑 **Data Cleaning Tools**  
              Remove duplicates and handle missing values easily
            - 🔑 **Interactive Filters**  
              Filter data by Date, Region, and Category
            """)

        with col2:
            st.markdown("""
            - 🔑 **Dynamic Visualizations**  
              Bar, Line, Pie and Area charts for insights
            - 🔑 **Top Performers Analysis**  
              Find Top Products, Customers and Regions
            - 🔑 **Monthly & Yearly Trends**  
              Analyze sales and profit trends over time
            - 🔑 **Export Reports**  
              Download clean data and charts as CSV/PNG
            """)
    with st.container(border=True):
        st.markdown("""
              <div style="color:white;background-color:blue;text-align:center;font-weight:bold;
              font-size:25px;padding-top:5px;border-radius:5px;">
              <p><b>📦 Our Version</b></p>
              </div>
              """, unsafe_allow_html=True)
        im1, im2 = st.columns([3, 7])
        with im1:
            st.image("images/ver.jpg", )
        with im2:
            st.write("""**Version 1.0** -<p style="font-size:20px;line-height:1.6; text-align:justify;"> March was the end game milestone leading up to our 1.0 release. We wanted the product to meet the high expectations of a 1.0 release and we focused on fundamentals like quality, accessibility, global reach and performance. 
                It transforms raw sales data into clear visuals, trends, and insights in just a few clicks.</p>""",unsafe_allow_html=True)

cf.print_footer()