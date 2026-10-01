import streamlit as st
import pandas as pd
import numpy as np
import utils.Common_header as Ch
import utils.Common_footer as cf
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
Ch.print_header()
st.divider()
st.markdown("""<p style='text-align:center;background-color:blue;color:white;font:weight:bold;font-size:35px'><u>View Dataset</u>""",unsafe_allow_html=True)

st.subheader("Showing Information of Dataset:-")
dataset_file_name="Data_set/Dataset(1).csv"
df_dataset=pd.read_csv(dataset_file_name)
col1,col2=st.columns([7,3])
with col1:
        c1,c2=st.columns([3,7])
        with c1:
            with st.container(border=True):
                st.markdown("##### Completed Steps #####")
                st.markdown(" ☑️First 5 Records")
                st.markdown("☑️️Last5 Records")
                st.markdown("☑️Completed dataset")


        with c2:
             st.markdown("<center style='color:blue;background-color:#F8FAFC;margin-bottom:20px;font-size:28px;font-weight:bold;'>Pre-loaded Dataset information</center> ",unsafe_allow_html=True)
             st.success(f"Current Dataset:{dataset_file_name}")
             #st.success(f"Current Dataset: {dataset_file_name}")
             b1,b2=st.columns([2,2])
             with b1:
                with st.container(border=False):
                  if st.button("**Analyze dataset &go to Data_Cleaning**",type="secondary"):
                     st.switch_page("pages/Data_Cleaning.py")
             with b2:
                  if st.button("Analyze dataset & go to dashboard",type="primary"):
                    st.switch_page("Dashboard.py")

        st.markdown("<center style='color:white;background-color:blue;font-size:28px;font-weight:bold'>Choose Any one Data for View</center>",
                    unsafe_allow_html=True)
        first_5_tab, last_5_tab, all_tabs = st.tabs(["First 5 Rows", "Last 5 Rows", "All Rows"])
        with first_5_tab:
            st.dataframe(df_dataset.head())
        with last_5_tab:
            st.dataframe(df_dataset.tail())
        with all_tabs:
            st.dataframe(df_dataset)
x = df_dataset.shape[0]
y = df_dataset.shape[1]
z = df_dataset.notnull().sum().sum()
A = len(df_dataset)
k = len(df_dataset.select_dtypes(include=["int", "float"]).columns)
r = len(df_dataset.select_dtypes(include="str").columns)
with col2:
    st.markdown("##### Dataset Overview #####")
    st.error("Dataset Information")
    with st.container(border=True):
        colx, coly = st.columns([8, 2])
        with colx:
            st.markdown("**Total Observations**")
            st.markdown("*Records:*")
        with coly:
            st.markdown(f"***{x}***")
            st.markdown(f"""*{z}*""")
    with st.container(border=True):
        coll, colr = st.columns([8, 2])
        with coll:
            st.markdown("**Total Features:**")
            st.markdown("*Total Numeric Features:*")
            st.markdown("*Total String Features:*")
        with colr:
            st.markdown(f"***{y}***")
            st.markdown(f"""*{k}*""")
            st.markdown(f"""*{r}*""")

    with st.container(border=True):
        st.markdown("***Features Types***")
        st.scatter_chart(df_dataset.set_index("Region")["City"],height=200)
cf.print_footer()

