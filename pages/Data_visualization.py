import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import streamlit as st
from streamlit import selectbox, title

import utils.Common_header as ch
import utils.Common_footer as cf

st.set_page_config(page_title="Welcome to Sales Analytics",page_icon="images/saleslg.jpg",layout="wide")
ch.print_header()
st.divider()
if "type" not in st.session_state:
    st.session_state.type="All"
dataset_file_name="Data_set/Dataset(1).csv"
df_dataset=pd.read_csv(dataset_file_name)
st.markdown("""<p style='text-align:center;background-color:blue;color:white;font:weight:bold;font-size:30px'><u>Data Visualoization</u>""",unsafe_allow_html=True)

col_main,col_right=st.columns([8,2])
with col_main:
      with st.container(border=True):
            lst = [ "All", "Category", "Sales", "Region", "Customer_Type"]
            c_type = st.selectbox("Choose a Filter", lst, key="a")
            t1, t2, = st.columns([8.5,1.5])
            with t2:
                lst = ["All", "Category", "Sales", "Region", "CustomerType"]
                if st.session_state.type ==["Category","Sales", "Region", "CustomerType"]:
                    if st.button("Apply", type="primary"):
                        st.session_state.type = c_type
                        st.rerun()
                if st.button("Apply", type="primary"):
                    st.session_state.type = c_type
                    st.rerun()
with (col_main):
        col1,col2=st.columns(2)
        lst = ["All", "Category", "Sales", "Region", "CustomerType"]
        if st.session_state.type == "Category":


            with col1:
                lst = ["All", "Category", "Sales", "Region", "Customer"]
                # st.text("Chart portion")
                # st.dataframe(df_dataset.head())
                fig,ax=plt.subplots(figsize=(8,7))
                sb.lineplot(data=df_dataset,x="Region",y="Sales",hue="Customer_Type")
                plt.xlabel("Region",fontsize=14,color="navy")
                plt.ylabel("Sales",fontsize=14,color="black")
                plt.title("lineplot",fontsize=22,color="red")
                title="Counting Sales and  Customer"
                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)
                plt.savefig(f"graphs/{title}.png")
                plt.savefig(f"graphs/{title}.pdf")
                plt.show()
            with col2:
                lst= ["All", "Category", "Sales", "Region", "Customer_Type"]
                fig,ax = plt.subplots(figsize=(8, 7))
                sb.countplot(data=df_dataset, x="Customer_Name", hue="Customer_Type",ax=ax, palette="Greens")
                # df_res=df_res.remane(columns={"Customer_Type"})
                plt.xlabel("Customer_Name")
                plt.ylabel("Customer_Type")
                title = "Customer Type counting"
                plt.title("countplot", color="green", fontsize=16)
                st.pyplot(fig)
                plt.close(fig)
                plt.savefig(f"graphs/{title}.png")
                plt.savefig(f"graphs/{title}.pdf")
                plt.show()
        cola,colb=st.columns(2)
        lst = ["All", "Category", "Sales", "Region", "Customer_Type"]
        if st.session_state.type == "Sales":
             with cola:
                lst = ["All", "Category", "Sales", "Region", "Customer_Type"]
                fig, ax = plt.subplots(figsize=(8,7))
                sb.histplot(data=df_dataset,x="Category")
                plt.title("Sales and Profit Analytics", fontsize=16, color="red")
                plt.xlabel("Sales", fontsize=14, color="navy")
                plt.ylabel("Sales in thousand", fontsize=14, color="navy")
                plt.tight_layout()
                title="sales of category"
                st.pyplot(fig)
                plt.close(fig)
                plt.savefig(f"graphs/{title}.jpg")
                plt.savefig(f"graphs/{title}.pdf")
                plt.show()
             with colb:
                 lst = ["All", "Category", "Sales", "Region", "Customer_Type"]
                 fig, ax = plt.subplots(figsize=(8,7))
                 sb.countplot(data=df_dataset,x="Category")
                 plt.title("Sales and Profit Analytics", fontsize=22, color="black")
                 plt.xlabel("Sales", fontsize=14, color="navy")
                 plt.ylabel("price in thousand", fontsize=14, color="navy")
                 title="Sales and Profit"
                 plt.tight_layout()
                 st.pyplot(fig)
                 plt.close(fig)
                 plt.savefig(f"graphs/{title}.png")
                 plt.savefig(f"graphs/{title}.pdf")
                 plt.show()
with (col_main):
        c1, c2 = st.columns(2)
        lst = ["All", "Category", "Sales", "Region", "Customer_Type"]
        if st.session_state.type == "Region":
            with c1:
                    lst = ["All", "Category", "Sales", "Region ", "Customer_Type"]
                    fig, ax = plt.subplots(figsize=(8, 7))
                    sb.countplot(data=df_dataset, x="State", hue="Customer_Type", ax=ax, palette="BuPu")
                    plt.title("City and State wise Data", fontsize=22, color="red")
                    plt.xlabel("State Name", fontsize=14, color="navy")
                    plt.ylabel("Existing And New Customer", fontsize=14, color="navy")
                    plt.tight_layout()
                    title="Sales Data in "
                    st.pyplot(fig)
                    plt.close(fig)
                    plt.savefig(f"graphs/{title}.png")
                    plt.savefig(f"graphs/{title}.pdf")
                    plt.show()
            with c2:
                    lst = ["All", "Category", "Sales", "Region ", "Customer_Type"]
                    fig, ax = plt.subplots(figsize=(8, 7))
                    sb.histplot(data=df_dataset, x="State", y="City", ax=ax, palette="Reds")
                    plt.title("State And City Name ", fontsize=22, color="red")
                    plt.xlabel("State Name", fontsize=14, color="navy")
                    plt.ylabel("City Name", fontsize=14, color="navy")
                    plt.tight_layout()
                    st.pyplot(fig)
                    plt.close(fig)
                    plt.savefig(f"graphs/{title}.png")
                    plt.savefig(f"graphs/{title}.pdf")
                    plt.show()
        c1, c2 = st.columns(2)
        lst = ["All", "Category", "Sales", "Region", "Customer_Type"]
        if st.session_state.type == "Customer_Type":
            with c1:
                    lst = ["All", "Category", "Sales", "Region ", "Customer_Type"]
                    fig, ax = plt.subplots(figsize=(8, 7))
                    sb.histplot(data=df_dataset, x="City", hue="Customer_Type", ax=ax, palette="BuPu")
                    plt.title("New And Existing Customer", fontsize=22, color="red")
                    plt.xlabel("City", fontsize=14, color="navy")
                    plt.ylabel("Customer Name", fontsize=14, color="navy")
                    plt.tight_layout()
                    title="Customer Name and City "
                    st.pyplot(fig)
                    plt.close(fig)
                    plt.savefig(f"graphs/{title}.png")
                    plt.savefig(f"graphs/{title}.pdf")
                    plt.show()
            with c2:
                    lst= ["All", "Category", "Sales", "Region ", "Customer_Type"]
                    fig,ax = plt.subplots(figsize=(8, 7))
                    sb.histplot(data=df_dataset, x="City", y="Customer_Name", ax=ax, palette="Reds")
                    plt.title("City", fontsize=22, color="red")
                    plt.xlabel("Customer City", fontsize=14, color="navy")
                    plt.ylabel("Customer Name", fontsize=14, color="navy")
                    title="Customer Name And City"
                    plt.tight_layout()
                    st.pyplot(fig)
                    plt.close(fig)
                    plt.savefig(f"graphs/{title}.png")
                    plt.savefig(f"graphs/{title}.pdf")
                    plt.show()

with col_right:
    with st.container(border=True):
        st.markdown("""<p style='text-align:center;color:blue;background-color:;
        font-weight:bold;font-size:20px;'><u>Sales Filters</u></p>""", unsafe_allow_html=True)
    with st.container(border=True):
      df_dataset["Order_Date"]=pd.to_datetime(df_dataset["Order_Date"],errors="coerce")
      start_date=df_dataset["Order_Date"].min()
      end_date=df_dataset["Order_Date"].max()
      date_range=st.sidebar.date_input("Date_Range",[start_date,end_date])
      with st.form("Product_details"):
               ls = ["All", "Category", "Sales", "Region ", "Customer_Type"]

      st.text("Export Option")
      c1,c2,c3=st.columns(3)
      with c1:
        st.write("📑PDF")
      with c2:
        st.write("📊CSV")
      with c3:
        st.write("🖼️Image")




cf.print_footer()