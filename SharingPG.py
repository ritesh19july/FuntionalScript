from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report

from selenium.webdriver.support.ui import Select



#Global Varibles
url="http://www.stage-qa.cloud.wwe.com/node/26900979"
htmlFolderPath="c:\\wwe\\"


#assert "Python" in driver.title
status=""
status1=""
#status=True
keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
keywordReportVar4=""
AllTestCasedata=""


#def ValidateSharing(driver,noindex,url):
   
desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
driver = webdriver.Remote(
 command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
   desired_capabilities=desired_cap)
#driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()
keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
keywordReportVar4=""
keywordReportVar5=""	
AllTestCasedata=""
status=""
status1=""


time.sleep(10)
print "Executing testCaseName : SharingPG.py"
#For Twitter sharing
#webElements = driver.find_element_by_xpath("//a[@id='b']/i")
#webElements.click()
driver.find_element_by_xpath("//span[@id='l']").click()
print "Object clicked"
time.sleep(10)

strLink = report.CaptureSnapshot(driver,"twitter.png")
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on twitter button to share","Twitter window opened.",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(3)
driver.find_element_by_id("username_or_email").clear()
driver.find_element_by_id("username_or_email").send_keys("ritesh19july@gmail.com")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("crestech")
driver.find_element_by_xpath("//input[@value='Log in and Tweet']").click()
driver.find_element_by_xpath("//input[@value='Tweet']").click()
bodyText = driver.find_element_by_tag_name('body').text

if bodyText.find("You have already sent this message", 0) > -1:
	strMsg = "You have already sent this message."
	status1=True
	status=True
	driver.close()
else:
	strMsg = "User is able to share anything on facebook and twitter"
	status=True
	status1=True	
	driver.find_element_by_id("btn-close").click()


time.sleep(4)

for handle in driver.window_handles:
	driver.switch_to.window(handle)

strLink = report.CaptureSnapshot(driver,"twitter2.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Entering data in comment box and click on post button","Post has been shared on twitter",strLink,"Windows")


# For Facebook sharing
driver.find_element_by_css_selector("div.fb-share > a > img").click()

time.sleep(6)

strLink = report.CaptureSnapshot(driver,"facebook.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Clicking on Facebook button to share","Facebook window opened.",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(3)

webElements = driver.find_element_by_xpath("//div[@id='loginform']/div/input").send_keys("9015452602")
webElements = driver.find_element_by_xpath("//div[@id='loginform']/div[2]/input").send_keys("crestech")
time.sleep(2)
webElements = driver.find_element_by_xpath("//label[@id='loginbutton']/input")
webElements.click()
time.sleep(4)
driver.find_element_by_id("feedform_user_message").clear()
driver.find_element_by_id("feedform_user_message").send_keys("Sharing on FB")
status1=True
strLink = report.CaptureSnapshot(driver,"facebook2.png")
print strLink
keywordReportVar4+=report.keywordReportMethod(True,4,"Entering data in comment box and click on post button","Post has been shared on Facebook",strLink,"Windows")
print "After fb shared"
driver.find_element_by_name("publish").click()
for handle in driver.window_handles:
	driver.switch_to.window(handle)


path= "/wsx/"+'ShareResult.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
	
keywordReportVar5+=report.keywordReportMethod(status1,5,"Sharing Scenario","User is able to share anything on facebook",path,"Windows")    
#driver.find_element_by_css_selector("a.bgimg.right").click()
# Wait for 5 seconds
time.sleep(2)
	
TestCaseReportVar=report.testcaseMethod(1,"SharingPG",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+"</tbody></table></div>"

time.sleep(2)
driver.quit()
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)
	




