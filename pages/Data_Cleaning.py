import streamlit as st
import pandas as pd
import numpy as np
from pyarrow.interchange import column

import utils.Common_header as ch
import utils.Common_footer as cf
st.set_page_config(page_title="Welcome to Project Name",
                   page_icon="images/saleslg.png",
                   layout="wide")
ch.print_header()
st.write("---") 
#reading dataset in dataframe
dataset_file_name="Data_set/Dataset(1).csv"
df_dataset=pd.read_csv(dataset_file_name)
st.markdown("<center style='font-size:30px;background-color:blue;color:white;"
            "font-weight:bold;'>Data Cleaning & Analysis</center>",
            unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("##### Current Dataset is:- #####")
    st.success(f"Current Dataset is: dataset_file_name")
    col1,col2=st.columns(2)
    with col1:
       st.markdown(f"**📊 Total Rows:** {df_dataset.shape[0]}")
    with col2:
       st.markdown(f"**📋Total Columns:** {df_dataset.shape[1]}")
st.markdown("<center style='color:maroon;font-size:22px;font-weight:bold;background-color:blue;color:white;font-size:25px'>Overview of Data</center>",
            unsafe_allow_html=True)
with st.container(border=True):
     col_name,col_value,col_null=st.columns([3,1,3])
     with col_name:
         st.markdown("""
        - **🕳️total missing values:**
        
        - **🔁 total duplicate Records:**
        
        - **🔢 total numeric Features:**
        
        - **🏷️ total Category types:**
         """)
     with col_value:
         total_dup_count=df_dataset.duplicated(subset=df_dataset.columns.drop("Order_ID"),keep=False).sum()

         st.markdown(f"""
          {df_dataset.isnull().sum().sum()}
          
          {total_dup_count}            
          
          {len(df_dataset.select_dtypes(include="int").columns)}
          
          {df_dataset.groupby("Order_ID")["Order_ID"]
                     .count().count()}
         """)
st.markdown("<center style='color:green;font-size:25px;background-color:blue;color:white;"
            "font-weight:bold'>Cleaning Operation</center>",
            unsafe_allow_html=True)
with st.container(border=True):
      numeric_fill=st.radio("**Fill Missing numeric Values.** Please choose one value to fill-",["Mean","Median","Zero"])
      string_fill = st.radio("**Fill Missing String Values.** Please choose one value to fill-",["Unknown", "Not Applicable"])
      rem_missing=st.checkbox("**Remove record having missing values.**")
      rem_duplicate=False
      if total_dup_count>0:
          rem_duplicate = st.checkbox("**Remove duplicate records.**")
      col1,col2=st.columns(2)
      with col1:
          with st.container(border=True):
              s1,s2=st.columns(2)
              with s1:
                  btn_clean=st.button("Start Data Cleaning",type="primary")
              with s2:
                  btn_show_dupli=False
                  if total_dup_count>0:
                      btn_show_dupli=st.button("Show Duplicate Records")
      if btn_show_dupli:
          st.markdown("<center style='background-color:navy;color:blue;font-size:22px;"
                      "font-weight:bold'>Cleaning Operation</center>",
                      unsafe_allow_html=True)
          df_duplicate_rec=df_dataset[df_dataset.duplicated(df_dataset.columns.drop("Order_ID"),keep=False)]
          df_duplicate_rec["SRNo"]=np.arange(1,total_dup_count+1)
          st.dataframe(df_duplicate_rec)
if btn_clean:
    st.info("Cleaning your data...")
    numeric_cols=df_dataset.select_dtypes(include=["int","float"]).columns
    string_cols=df_dataset.select_dtypes(include="object").columns
    if rem_duplicate==True:
        df_duplicate_rec(df_dataset.columns.drop("Order_ID"),keep=False,inplace=True)
    if rem_missing==True:
        df_dataset.dropna(inplace=True)
    elif numeric_fill=="Mean":
        for col in numeric_cols:
            col_mean=df_dataset[col].mean()
            # st.write("Filling Mean"+str(col_mean))
            df_dataset[col].fillna(col_mean,inplace=True)
    elif numeric_fill=="Median":
        for col in numeric_cols :
            df_dataset[col]=(df_dataset[col].fillna(df_dataset[col].median(),inplace=True))
    elif numeric_fill=="Zero":
        st.write("Filling Zero")
        df_dataset[numeric_cols]=(df_dataset[numeric_cols].fillna(0))
    if string_fill=="Unknown":
        df_dataset[string_cols]=(df_dataset[string_cols].fillna("Unknown"))
    elif string_fill=="Not Applicable":
        df_dataset[string_cols]=df_dataset[string_cols].fillna("Not Applicable")
    #updating CSV file performing data cleaning....
    df_dataset.to_csv(dataset_file_name,index=False)
    st.success("Congratulation!! Data cleaning successfully")
    st.info("Please check below button to proceed for data Analysis")
    st.markdown("""
    <a  href='Sales_Analysis'><div style='background-color:white;text-decoration:none;font-size:20px;'>Proceed to Data Analysis</div></a>
    """,unsafe_allow_html=True)
cf.print_footer()