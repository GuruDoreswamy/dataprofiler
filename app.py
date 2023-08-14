import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os


st.set_page_config("Data Profiler",layout = 'wide')

# sidebar

with st.sidebar:
    upload_file = st.file_uploader("upload .csv, .xlsx files not exceeding 10MB")

    if upload_file is not None:
        st.write("modes of operation")
        minimal = st.checkbox('need minimal report?')
        display_mode = st.radio('display mode:', options=('primary','dark','orange'))

        if display_mode =='dark':
            dark_mode = True
            orange_mode = False
        elif display_mode == 'orange':
            dark_mode= False
            orange_mode = True
        else:
            dark_mode=False
            orange_mode=False
            


if upload_file is not None:
    df = pd.read_csv(upload_file)

    #st.dataframe(df.head())

    #Generating data profile report
    with st.spinner("generating report"):
        pr = ProfileReport(df,minimal = minimal,
                      dark_mode = dark_mode,
                      orange_mode = orange_mode)

    st_profile_report(pr)