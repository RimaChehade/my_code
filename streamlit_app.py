import streamlit as st
#pip install psycopg2
import psycopg2
import pandas as pd


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from reporting.hibob_export limit 20")

data=pd.DataFrame(rows)
data.columns=['display_name','first_name','last_name','department','operations_department','operations_manager','manager_id','manager_name','skip_manager_name','skip_skip_manager_name','job_title','email','personal_email','github_username','greenhouse_candidate_id','creation_date','employment_effective_date','country','city','city_longitude','city_latitude','gender','level_of_education','site','is_offboarded','termination_date','reason_for_termination','accumulated_tenure_years_','hibob_id','team','salary','bonus','tier','days_off_in_current_cycle','days_off_in_previous_cycle']
st.table(data)
