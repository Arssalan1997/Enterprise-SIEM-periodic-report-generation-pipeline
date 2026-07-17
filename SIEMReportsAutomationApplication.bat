@ECHO OFF
call "D:\Data Science\Projects\SIEM Report Automation With Python Project\venv\Scripts\activate.bat"
streamlit run "D:\Data Science\Projects\SIEM Report Automation With Python Project\introduction.py" --server.address 192.168.1.101 --server.port 8501 --browser.gatherUsageStats false REM --server.headless true --global.developmentMode false --server.enableCORS false --server.enableXsrfProtection false
