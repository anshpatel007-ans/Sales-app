import streamlit as st
import utils.Common_header as Ch
import utils.Common_footer as Cf
import pandas as pd
st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
#header section
Ch.print_header()
st.divider()
st.markdown("""<p style='text-align:center;background-color:blue;color:white;font:weight:bold;font-size:30px'><u>Data Uploade</u>""",unsafe_allow_html=True)
st.subheader("Upload Dataset for Analysis")
st.markdown("**Step-1: Understand Required Format & Sample Data** ")
with st.container(border=True):
    st.markdown("**Suggest Required Columns**")
    col_name,col_desc,col_2=st.columns([3,4,3])
    with col_name:
         st.markdown("""
        - **Order_Id**
        
        - **Order_date**
        
        - **Customer_Name**
        
        - **Product_Name**
        
        - **Category**
        
        - **Region**
        
        - **Quantity**
        
        - **Sales**
        
        - **Profit**
        
        - **Payment_Mode**       
        """)
    with col_desc:
        st.markdown("""
        Unique Order ID
        
        Date of Order
        
        Name of Customer
        
        Name of Producct
        
        Product category
        
        Sales Region
        
        Quantity Sold
        
        Total Sales Amount
        
        Profit Earned 
        
        Payment Method(Cash, Card, UPI, etc.) 
        """)
with st.container(border=True):
    col_icon,col_down=st.columns([1,6])
    with col_icon:
        st.image("images/csv_icon.png")
    with col_down:
        st.markdown ("**Download Sample Dataset**")
        st.text("Get a template to understand format of Dataset. ")
        with open("Data_set/Dataset(1).csv","rb") as samp_file:
            st.download_button("Download Sample CSV",data=samp_file,file_name="sample_Sales_dataset.csv")
# Validating uploaded dataset
st.markdown("#### Step 2:- Upload Sales Dataset CSV File: ####")
btn_clear=False
if"uploader_key" not in st.session_state:
    st.session_state.uploader_key=1
with st.container(border=True):
    up_file=st.file_uploader("**Choose or Drop and Dragon your dataset file**",type=["csv"],key=f"upload{st.session_state.uploader_key}")
    if up_file is not None:
       if up_file.name.endswith(".csv") or up_file.name.endswith(".CSV"):
           df_dataset=pd.read_csv(up_file)
           # showing preview...
           st.markdown("**Showing Preview of Uploaded Dataset:-**")
           st.dataframe(df_dataset.head())
           # Validate columns of dataset...
           # Write names of columns from your dataset in below list
           allowed_cols_lst=["Order_ID","Order_Date",	"Customer_Name",	"Customer_Type",	"Product_Name",	"Category",	"Region",	"City",	"State",	"Purchage_Value",	"Quantity",	"Sales",	"Discount",	"Profit",	"Payment_mode",	"Order_Status"];
           missing_cols_lst=[]
           for allowed_cols in allowed_cols_lst:
               if allowed_cols not in df_dataset.columns:
                   missing_cols_lst.append(allowed_cols)
           if len(missing_cols_lst)>0:
               st.error("Below columns are missing from your dataset-")
               st.write(missing_cols_lst)
               st.warning("Warning: Please update your dataset to solve above errors and try again to upload.")
           else:
               st.warning("Your dataset is validated successfully.")
               col1,col2=st.columns([4,6])
               with col1:
                   if  st.button("Save dataset & Proceed"):
                       df_dataset.to_csv("Data_set/Dataset(1).csv",index=False)
                       st.switch_page("pages/View_Dataset.py")
               with col2:
                   if st.button("Clear Dataset",type="primary"):
                       st.session_state.uploader_key+=1
                       st.rerun()
       else:
           st.error("Invalid file format for Dataset. Only .csv format is allowed.")
Cf.print_footer()