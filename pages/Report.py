import reportlab.platypus as rp
import  reportlab.lib.styles as rs
import reportlab.lib.colors as colors
import  streamlit as st
import numpy as np
import utils.Common_header as ch
import utils.Common_footer as cf
import pandas as pd
import math

st.set_page_config(page_title="Welcome to Project Name",
                   page_icon="images/saleslg.png",
                   layout="wide")
ch.print_header()
st.divider()
st.markdown("<center style='color:white;font-size:35px;background-color:blue;padding-top:non;"
                      "font-weight:bold'>Report Page</center>",
                      unsafe_allow_html=True)
report_file_name="Data_Sales_report.pdf"
dataset_filename="Data_set/Dataset(1).csv"
df_dataset=pd.read_csv(dataset_filename)
#opening and empty document file for writing content
my_pdf=rp.SimpleDocTemplate(report_file_name)
#Calling method to set style of content during writing
#using program module
style=rs.getSampleStyleSheet()
#Creating an empty Python list to append all concept for pdf
content_list=[]
img=rp.Image("images/company.jpg",width=130,height=70)
content_list.append(img)

para=rp.Paragraph("Data Sales Report",style=style["Title"])
content_list.append(para)
pr=rp.Paragraph("Data Sales : Moderate",style=style["Normal"])
content_list.append(pr)
#start :Table
with st.container(border=True):
    numeric_cols = (df_dataset.select_dtypes(include=["int", "float"]).columns)
    selected_num_col = st.selectbox("Select a numeric columns", numeric_cols)
    max_data = math.ceil(df_dataset[selected_num_col].max())
    min_data = math.ceil(df_dataset[selected_num_col].min())
    avg_data = math.ceil(df_dataset[selected_num_col].mean())
    total_data = math.ceil(df_dataset[selected_num_col].sum())
    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric(f"**Sales Performance**", value=max_data)
        with c2:
            st.metric(f"**Product Sales**", value=min_data)
        with c3:
            st.metric(f"**Region-wise Sales**", value=avg_data)
        with c4:
            st.metric(f"**Total Sales**", value=total_data)


with st.container():
    n1,n2=st.columns(2)
    with n1:
        st.success("Ten Highest sells data")
        prod_high_sell10 = df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Quantity", ascending=False).head(10)
        st.table(prod_high_sell10.set_index(np.arange(1, 11))[["Product_Name", "Quantity"]])
    with n2:
        st.success("Ten Lowest sells data")
        prod_low_sell10 = df_dataset.drop_duplicates(subset=["Product_Name"]).sort_values(by="Quantity", ascending=True).head(10)
        st.table(prod_low_sell10.set_index(np.arange(1, 11))[["Product_Name", "Quantity"]])
df1= prod_high_sell10[["Product_Name","Quantity"]]
df2= prod_low_sell10[["Product_Name","Quantity"]]
tab_data1=[df2.columns.tolist()]+df1.values.tolist()
tab_data2=[df1.columns.tolist()]+df1.values.tolist()
tbl=rp.Table(tab_data1,colWidths=70,rowHeights=20)
tbl=rp.Table(tab_data2,colWidths=70,rowHeights=20)
tbl_border_style=rp.TableStyle([('GRID',(0,0),(-1,-1),1,colors.maroon)]) #full grid lin
tbl_bg_style=rp.TableStyle([('BACKGROUND',(0,0),(-1,0),colors.pink)])
tbl.setStyle(tbl_bg_style)
content_list.append(tbl)
#end: table
#Burning (writing ) list data into document file
my_pdf.build(content_list)
#opening file to download from buffer memory
with open(report_file_name,"rb") as file:
    st.info("Click on the (Download button) For Download Report")
    st.download_button("Download Report",data=file,file_name=("report/Report.pdf"),type="primary")

cf.print_footer()
