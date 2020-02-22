from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.hotstar.com")
driver.find_element_by_xpath("//div[@class='signIn displayElement']").click()   # Click on login icon
driver.find_element_by_xpath("//input[@name='email']").send_keys("xyz@edureka.co") # Entering email address
driver.find_element_by_name("password").send_keys("edureka123")    #Entering the given password
driver.find_element_by_xpath("//button[@type='submit']").click()      #Clicking submit button to login