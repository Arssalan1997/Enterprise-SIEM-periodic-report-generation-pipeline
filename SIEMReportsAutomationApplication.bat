@ECHO OFF
call "E:\a.bazzaz\SIEM Report Automation With Python Project\venv\Scripts\activate.bat"
streamlit run "E:\a.bazzaz\SIEM Report Automation With Python Project\introduction.py" --server.address 192.168.43.76 --server.port 8501 --browser.gatherUsageStats false REM --server.headless true --global.developmentMode false --server.enableCORS false --server.enableXsrfProtection false
