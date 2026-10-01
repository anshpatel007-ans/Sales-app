import streamlit as  st
import utils.Common_header as ch
import utils.Common_footer as cf
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
ch.print_header()
st.divider()
st.markdown("""<p style='text-align:center;background-color:blue;color:white;font:weight:bold;font-size:30px'><u>Home Page</u>""",unsafe_allow_html=True)
st.subheader("Introduction:-")
with st.container(border=True):
    st.markdown("<div style='font-size:16px;padding-left:25px;'>Sales Analytics Dashboard is a data-driven application developed to analyze and visualize sales performance in an interactive and user-friendly manner. Te dashboard helps organizations transform raw sales dataset into meaningful insights that support better business decisions. By uploading a sales, dataset in CSV formate, users can quickly explore key performance indicators such as Total Sales, Total Profit, Monthly Sales Trends, Top Products, Top Products, Top Costumers, Region-wise Sales, and Category-wise Sales.</div>",unsafe_allow_html=True)

st.markdown("### Project Pages Button ###")
with st.container(border=True):
    c1,c2,c3,c4,c5,c6,c7=st.columns([1,1,1,1,1,1,1])
    with c1:
        if st.button("**Sales Dataset**", key="btn1", use_container_width=True,type="primary"):
            st.switch_page("pages/Data_Upload.py")
    c2.markdown("<div style='font-size:20px;padding-top:18x;padding-left:25px;'>➡️</div>", unsafe_allow_html=True)
    with c3:
        if st.button("**Sales Analytic**", key="bt2", use_container_width=True,type="primary"):
            st.switch_page("pages/Data_Cleaning.py")
    c4.markdown("<div style='font-size:20px;padding-top:18px;padding-left:25px;'>➡️</div>", unsafe_allow_html=True)
    with c5:
        if st.button("**Analyze Sales**", key="bt3", use_container_width=True,type="primary"):
            st.switch_page("pages/Sales_Analysis.py")
    c6.markdown("<div style='font-size:20px;padding-top:18px;padding-left:25px;'>➡️</div>", unsafe_allow_html=True)
    with c7:
        if st.button(("**Reports/Charts**"), use_container_width=True, type="primary"):
            st.switch_page("pages/Report.py")
cf.print_footer()