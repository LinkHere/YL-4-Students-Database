# streamlit_app.py

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

from streamlit_option_menu import option_menu
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]

with st.sidebar:
    selected = option_menu("Main Menu", ["Block 1-A", "Block 1-B", "Block 2-A", "Block 2-B", "Block 3-A", "Block 3-B", "Block 4-A", "Block 4-B", "Block 5-A", "Block 5-B"], menu_icon="house", default_index=0)


# Print results.
#df = pd.DataFrame(rows)

#st.dataframe(df, 900, 800)

# for row in rows:
#     st.write(row)

if selected == "Block 1-A":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="1-A"')
                           
if selected == "Block 1-B":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="1-B"')
    
if selected == "Block 2-A":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="2-A"')

if selected == "Block 2-B":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="2-B"')

if selected == "Block 3-A":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="3-A"')

if selected == "Block 3-B":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="3-B"')
    
if selected == "Block 4-A":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="4-A"')

if selected == "Block 4-B":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="4-B"')
    
if selected == "Block 5-A":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="5-A"')
    
if selected == "Block 5-B":
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE Block="5-B"')

st.markdown(f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
""", unsafe_allow_html=True)

for row in rows:
    mobile = row.Mobile_No
    mobile_no = int(mobile)
    
    if mobile_no is not None:
        mobile_no = mobile_no
    
    if row.Vaccine_Id is not None:
        btn_state = ""
    else:
        btn_state = "disabled"
    
    st.markdown(f"""
        <div class="card" style="margin-bottom: 2rem; color: #777;">
          <div class="card-header">
            <span style="font-size: 25px;"><strong>Name:</strong> {row.Last_Name}, {row.First_Name} {row.Middle_Initial}</span>
          </div>
          <div class="card-body">
            <strong>Permanent Address:</strong> {row.Permanent_Address}<br>
            <strong>Current Address:</strong> {row.Current_Address}<br
            <span><strong>Leaving With:</strong></span> {row.Leaving_With}<br>
            <strong>Mother/Mobile No.:</strong> {row.Mother_and_Mobile}<br>
            <strong>Father/Mobile:</strong> {row.Father_and_Mobile}<br>
            <strong>Emergency Contact Person:</strong> {row.Emergency_Contact_Person}<br>
            <strong>Email:</strong> {row.CEU_Mail}<br>
            <strong>Mobile No.:</strong> {mobile_no}<br>
            <strong>PhilHealth:</strong> {row.PhilHealth}<br>
            <strong>PhilHealth Category:</strong> {row.PhilHealth_Category}<br>
            <strong>Medical Insurance:</strong> {row.Medical_Insurance}<br>
            <strong>List of Medical Insurance:</strong> {row.List_of_Medical_Insurance}<br>
            <strong>Covid-19 Vaccine:</strong> {row.Covid19_Vaccine}<br>
            <a href="{row.Vaccine_Id}" class="btn btn-outline-dark {btn_state}">Vaccination ID/Certificate</a>
          </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
