import streamlit as st
import pandas as pd
import math
import utils.Common_header as Ch
import utils.Common_footer as Cf
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
#Header section
Ch.print_header()
st.divider()
#welcome section

dataset_filename="Data_set/Dataset(1).csv"
df_dataset=pd.read_csv(dataset_filename)
with st.container(border=True):
    st.markdown("""
    ### Welcome 👋

    **Sales Analytics Dashboard** is a data-driven application designed to analyze and visualize sales performance in an interactive and user-friendly way.

    **Key Features:**  
    This dashboard helps organizations transform raw sales data into actionable insights for better business decisions. 
    By uploading a sales dataset in CSV format, users can quickly explore key metrics such as:
    - **Total Sales**
    - **Total Profit** 
    - **Monthly Sales Trends**
    - **Top Products**
    - **Region-wise Sales**
    """)
p1,p2=st.columns(2)
with  p1:
    with st.container(border=True):
        st.image("images/ds.png",)
with  p2:
    with st.container(border=True):
        st.image("images/dss.jpg")

st.divider()
col_feat,col_aim,col_visual=st.columns(3,gap="medium")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='background-color:#E3F2FD; padding:15px; border-radius:10px'>
    <h4>✨ Key Features</h4>
    <ul>
        <li>Upload and analyze sales data directly from CSV files</li>
        <li>Track <b>Total Sales, Profit, and Key Metrics</b> in real-time</li>
        <li>Break down performance by <b>Region, Category, and Product</b></li>
        
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background-color:#E8F5E9; padding:15px; border-radius:10px'>
    <h4>🎯 Our Aim</h4>
    <ul>
        <li>Automate sales reporting and save valuable time</li>
        <li>Provide clear visibility into overall sales and profit trends</li>
        <li>Identify <b>Top Products and Customers</b> driving revenue</li>
       
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background-color:#FFF8E1; padding:15px; border-radius:10px;'>
    <h4>📊 Visual Analytics</h4>
    <ul>
        <li><b>Monthly Sales Trends</b> - Line Chart</li>
        <li><b>Top 10 Products</b> - Bar Chart</li>
        <li><b>Region-wise Sales</b> - Pie Chart</li>
        <li><b>Category Performance</b> - Bar Chart</li>
      
        
    </ul>
    </div>
    """, unsafe_allow_html=True)
st.divider()
total_sell=math.ceil(df_dataset["Sales"].sum())
total_profit=math.ceil(df_dataset["Profit"].sum())
prod_high_sell10 = df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Quantity", ascending=False).head(10)
top_po=prod_high_sell10["Product_Name"].iloc[0]
total_cus=math.ceil(df_dataset["Customer_Name"].nunique())

#facts
with st.container(border=True):
    st.subheader("Dashboard Cards")
    c1,c2,c3,c4,c5=st.columns(5)
    c1.metric("Total Sales",f"{total_sell}")
    c2.metric("Total Profit",f"{total_profit}")
    c3.metric("Monthly Sales","50,000","+80%")
    c4.metric("Top Products",f"{top_po}")
    c5.metric("Top Customers",f"{total_cus}")

#project flow
st.markdown("## Project Flow")
with st.container(border=True):
    c1,c2,c3,c4,c5,c6,c7=st.columns([1,1,1,1,1,1,1])
    with c1:
        if st.button("**Sales Dataset**", key="btn1", use_container_width=True,type="primary"):
            st.switch_page("pages/Data_Upload.py")
    c2.markdown("<div style='font-size:18px;padding-top:10px;padding-left:50px;'>➡️</div>", unsafe_allow_html=True)
    with c3:
        if st.button("**Sales Analytic**", key="bt2", use_container_width=True,type="primary"):
            st.switch_page("pages/Data_Cleaning.py")
    c4.markdown("<div style='font-size:18px;padding-top:10px;padding-left:50px;'>➡️</div>", unsafe_allow_html=True)
    with c5:
        if st.button("**Analyze Sales**", key="bt3", use_container_width=True,type="primary"):
            st.switch_page("pages/Sales_Analysis.py")
    c6.markdown("<div style='font-size:18px;padding-top:10px;padding-left:50px;'>➡️</div>", unsafe_allow_html=True)
    with c7:
        if st.button(("**Reports/Charts**"), use_container_width=True, type="primary"):
            st.switch_page("pages/Report.py", )
#footer
Cf.print_footer()