from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random
driver = webdriver.Chrome()
url = input('\nEnter the form url : ')
driver.get(url)
def handleform():
    try:
        searchval = input('\nEnter the form question to search : ')
        inputval = input('\nEnter the value to put into the text field : ')
        text = driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(searchval))
        for txt in text:
            try:
                txt.click()
            except:
                continue
        msg_box = driver.find_element_by_class_name('quantumWizTextinputPaperinputInput')
        msg_box.send_keys(inputval)
        submit = driver.find_element_by_class_name('quantumWizButtonPaperbuttonLabel')
        submit.click()
        driver.get(url)
        # driver.close()
    except Exception as e:
        print (e)
count = 0
while True:
    handleform()
    print("dumped"+str(count+8)+"times")
    count += 1
    time.sleep(1)
