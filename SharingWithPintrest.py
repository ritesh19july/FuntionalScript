from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
 


#Global Varibles
url="http://www.stage-qa.cloud.wwe.com/node/26026027"
htmlFolderPath="c:\\wwe\\"

keywordReportVar=""
AllTestCasedata=""
status=True
#url="http://www.stage-qa.cloud.wwe.com/node/25064032" for event



desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
driver = webdriver.Remote(
   command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
   desired_capabilities=desired_cap)
#driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()
driver.delete_all_cookies()

keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
AllTestCasedata=""
status=""
status1=""
print "Executing testCaseName : SharingPinterest."

strLink = report.CaptureSnapshot(driver,"Pinterest.png")
print strLink
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on login button for sign in","Login page has been opened",strLink,"Windows")

webElements = driver.find_element_by_xpath("//div[@id='standard_list_5443']/div/div/div[3]/div/div[5]/a")
webElements.click()

time.sleep(5)

strLink = report.CaptureSnapshot(driver,"Pinterest.png")
print strLink
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on login button for sign in","Login page has been opened",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(6)

driver.find_element_by_id("userEmail").clear()
driver.find_element_by_id("userEmail").send_keys("ritesh19july1@gmail.com")
driver.find_element_by_id("userPassword").clear()
driver.find_element_by_id("userPassword").send_keys("crestech")
driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

strLink = report.CaptureSnapshot(driver,"Pinterest1.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Verifying whether user is able to logged in","user is able to login successfully",strLink,"Windows")

#driver.find_element_by_xpath("//li[2]/div/button").click()
#driver.find_element_by_xpath("//button[@type='submit']")
time.sleep(10)
for handle in driver.window_handles:
	driver.switch_to.window(handle)


path= "/wsx/"+'Pinterest3.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
status=False
keywordReportVar3+=report.keywordReportMethod(False,3,"Sharing Pinterest Scenario","User is unable to share(Pin) over Pinterest",path,"Windows")    

# Wait for 5 seconds
time.sleep(2)
TestCaseReportVar=report.testcaseMethod(1,"Pinterest",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+"</tbody></table></div>"
driver.quit()
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)
	
	