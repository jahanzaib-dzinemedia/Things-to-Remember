
# Take full Screen SS
S = lambda X: drv.execute_script('return document.body.parentNode.scroll'+X)
drv.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
drv.find_element(By.TAG_NAME, 'body').screenshot('ss.png')
print("saved")


# Change Selenium User Agent
user_agent = "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
opts = Options()
opts.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(chrome_options=opts)


# --------------------------------------------------------------------
# Good library for GUI
Gradio


## Notes 
#----------------------------------------------------------------------

"""
curl -X POST -F "files=@doc_data.txt" http://127.0.0.1:5000/upload
curl -X POST -F “hash=96e6709c7bc144dca5b9e4a0db200bda” -F “action=officetopdf”  http://127.0.0.1:5000/convert

source /home/emdclouds/virtualenv/public_html/converter/3.9/bin/activate && cd /home/emdclouds/public_html/converter && python app.py

mysql --host=localhost --user=emdclouds_recordsdb_user --password=H@+r=,-RbpCp emdclouds_file_records_db


SELECT * FROM upload_files
WHERE hash='e9fb75a564ceeb0cfecc84c1a9d68743c4b54f250218a117724557472de2dbda';


Stop flask app
fuser -k 5000/tcp



Check the processes
pgrep -u emdclouds chromedriver



ENV VAR
export PATH="/Users/imac/Desktop/Jahanzaib Babar Files/social video downloader/chromedriver":$PATH 
""