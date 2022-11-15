
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