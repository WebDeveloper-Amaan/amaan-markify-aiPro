import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time
from datetime import datetime
import pandas as pd


from src.database.db import create_attendance

def show_attendance_result(df, logs):
    st.write('Please review attendance before confirming.')
    st.dataframe(df, hide_index=True, width='stretch')

    # Get timestamp from logs
    timestamp = logs[0]['timestamp'] if logs else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_date = datetime.fromisoformat(timestamp.replace('T', ' ').split('.')[0]).strftime("%B %d, %Y at %I:%M %p")
    
    # Prepare CSV data with header
    csv_header = f"Attendance Report\nDate & Time: {formatted_date}\n\n"
    csv_data = df.to_csv(index=False)
    final_csv = csv_header + csv_data
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('Discard', width='stretch'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()
    
    with col2:
        st.download_button(
            label='Download CSV',
            data=final_csv,
            file_name=f'attendance_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
            mime='text/csv',
            type='secondary',
            use_container_width=True
        )

    with col3:
        if st.button('Confirm & Save', width='stretch', type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error('Sync failed!')



@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)

