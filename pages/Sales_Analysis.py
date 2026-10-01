import math
import streamlit as st
from matplotlib import container
from openpyxl.styles import borders
from pandas import unique

import utils.Common_header as ch
import utils.Common_footer as cf
import pandas as pd
import numpy as np
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
ch.print_header()
st.divider()
dataset_filename="Data_set/Dataset(1).csv"
df_dataset=pd.read_csv(dataset_filename)
st.markdown("""<p style='text-align:center;background-color:blue;color:white;font:weight:bold;font-size:35px'><u>Sales Analysis</u>""",unsafe_allow_html=True)
st.subheader("Dataset Information:-")
col1, col2,col3,col4,col5=st.columns(5)
with col1:
    with st.container(border=True):
        st.metric(label="Records",value=df_dataset.shape[0])
with col2:
    with st.container(border=True):
        st.metric(label="Columns", value=df_dataset.shape[1])
with col3:
    with st.container(border=True):
        total_numeric=len(df_dataset.select_dtypes(include=["int","float"]))
        st.metric(label="Numeric Featurs",value=total_numeric)
with col4:
    with st.container(border=True):
        total_cat=len(df_dataset.select_dtypes(include="object").columns)
        st.metric(label="Categorial Features",value=total_cat)
with col5:
    with st.container(border=True):
        avg_profit=df_dataset["Profit"].mean()
        avg_profit=math.ceil(avg_profit)
        st.metric(label="Average Data sales ",value=avg_profit)
#static  Data Analysis
st.subheader("Statistical Analysis:-")
with st.container(border=True):
    numeric_cols = (df_dataset.select_dtypes(include=["int", "float"]).columns)
    selected_num_col = st.selectbox("Select a numeric columns", numeric_cols)
    max_data = math.ceil(df_dataset[selected_num_col].max())
    min_data = math.ceil(df_dataset[selected_num_col].min())
    avg_data = math.ceil(df_dataset[selected_num_col].mean())
    median_data = math.ceil(df_dataset[selected_num_col].median())
    total_data = math.ceil(df_dataset[selected_num_col].sum())
    missing_data = math.ceil(df_dataset[selected_num_col].isnull().sum())
    std_dev_data = math.ceil(df_dataset[selected_num_col].std())
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1:
        st.metric(f"**Maximum**", value=max_data)
    with c2:
        st.metric(f"**Minimum**", value=min_data)
    with c3:
        st.metric(f"**Average**", value=avg_data)
    with c4:
        st.metric(f"**Median**", value=median_data)
    with c5:
        st.metric(f"**Total**", value=total_data)
    with c6:
        st.metric(f"**Missing**", value=missing_data)
    with c7:
        st.metric(f"**Standard Dev**", value=std_dev_data)

st.subheader("Searching & Sorting:-")
with (st.container(border=True)):
    c1,c2,c3=st.columns(3)
with c1:
    selected_num_col=st.selectbox("Select a column to Sort :",numeric_cols)
with c2:
    sort_order=st.radio("Sort Order:",["Ascending","Descending"],horizontal=True)
with c3:
    st.write("")
    st.write("")
    btn_sort=st.button("Sort Values",type="primary")
if btn_sort:
    if sort_order=="Ascending":
        df_sorted=df_dataset.sort_values(by=selected_num_col,ascending=True)
    else:
        df_sorted= df_dataset.sort_values(by=selected_num_col,ascending=False)
    st.success("Items sorted successfully based on Selected")
    st.dataframe(df_sorted,use_container_width=True)
#Serching
st.subheader("Searching Properties:-")
with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        search_value= st.text_input("Enter a value to search:")
    with col2:
        st.write("")
        st.write("")
        btn_search=st.button("Search Records",type="primary")
if btn_search:
    df_search_result=df_dataset[df_dataset.astype(str).apply(lambda row :row.str.contains(search_value,case=False,na=False).any(),axis=1)]
    st.dataframe(df_search_result)
st.subheader("Apply Filters in Dataset:- ")
with st.container(border=True):
    f1,f2,f3,f4,f5,f6=st.columns(6)
    with f1:
        sorted_Cat=sorted(df_dataset["Category"].dropna().unique())
        prop_types=st.selectbox("Select Category",["All"]+sorted_Cat)
    with f2:
        sorted_Reg = sorted(df_dataset["Region"].dropna().unique())
        prop_Re = st.selectbox("Select Region", ["All"]+sorted_Reg)
    with f3:
        sorted_St = sorted(df_dataset["State"].dropna().unique())
        prop_St = st.selectbox("Select State", ["All"]+sorted_St)
    with f4:
        sorted_PM = sorted(df_dataset["Payment_mode"].dropna().unique())
        prop_PM = st.selectbox("Payment_mode", ["All"]+sorted_PM)
    with f5:
        sorted_OS = sorted(df_dataset["Order_Status"].dropna().unique())
        prop_OS = st.selectbox("Select Order_status", ["All"]+sorted_OS)
    with f6:
        st.write("")

        apply_btn=st.button("Apply Filter",type="primary")
if apply_btn:
    df_filter=df_dataset.copy()
    if prop_types!="All":
        df_filter=df_filter[df_filter["Category"]==prop_types]
    if prop_Re!="All":
        df_filter=df_filter[df_filter["Region"]==prop_Re]
    if prop_St!="All":
        df_filter=df_filter[df_filter["State"]==prop_St]
    if prop_PM!="All":
        df_filter=df_filter[df_filter["Payment_mode"]==prop_PM]
    if prop_OS!="All":
        df_filter=df_filter[df_filter["Order_Status"]==prop_OS]
    rec_count=len(df_filter)
    if rec_count>0:
        st.success(f"Filter applied. Total {rec_count} records found")
        st.dataframe(df_filter,use_container_width=True)
    else:
        st.warning("Any matching record not found.")
#filter top product
st.subheader("Sorting:-")
top_dup,top_cheef=st.columns(2)
with top_dup:
    df_dataset["Unit_Cost"]=df_dataset["Sales"] / df_dataset["Quantity"]
    with top_dup:
        with st.container(border=True):
            btn_dup =st.button("Show top 10 Trending Products",type="primary")
        if btn_dup:
            with st.container(border=True):
                top_10=df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Unit_Cost",ascending=False).head(10)
                st.table(top_10.set_index(np.arange(1,11))[['Product_Name','Unit_Cost']])
with top_cheef:
    with st.container(border=True):
        btn_cheef =st.button("Show 10 cheefest  Products",type="primary")
        if btn_cheef:
            cheef_10=df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Unit_Cost",ascending=True).head(10)
            st.table(cheef_10.set_index(np.arange(1,11))[['Product_Name','Unit_Cost']])
top_sell,low_sell=st.columns(2)
with top_sell:
    with st.container(border=True):
        btn_top =st.button("Show top 10 most Saling Products",type="primary")
        if btn_top:
            prod_most_sell10=df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Quantity",ascending=False).head(10)
            st.table(prod_most_sell10.set_index(np.arange(1,11))[["Product_Name","Quantity"]])
with low_sell:
    with st.container(border=True):
        btn_low=st.button("Show top 10 lowest Saling Products",type="primary")
        if btn_low:
            prod_most_sell10=df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Quantity",ascending=True).head(10)
            st.table(prod_most_sell10.set_index(np.arange(1,11))[["Product_Name","Quantity"]])
cost,profit=st.columns(2)
with cost:
    with st.container(border=True):
        cost =st.button("Show top 10 most Costly Products",type="primary")
        if cost:
            prod_most_sell10=df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Sales",ascending=False).head(10)
            st.table(prod_most_sell10.set_index(np.arange(1,11))[["Product_Name","Sales"]])
with profit:
    with st.container(border=True):
        profit=st.button("Show top 10 Profit Products",type="primary")
        if profit:
            prod_most_sell10=df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Profit",ascending=True).head(10)
            st.table(prod_most_sell10.set_index(np.arange(1,11))[["Product_Name","Profit"]])

cf.print_footer()