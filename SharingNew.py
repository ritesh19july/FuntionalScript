from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report

from selenium.webdriver.support.ui import Select



#Global Varibles
url="http://www.stage-qa.cloud.wwe.com/node/26026027"
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
   
#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#driver = webdriver.Remote(
 #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
 #  desired_capabilities=desired_cap)
driver = webdriver.Firefox()
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


time.sleep(6)
print "Executing testCaseName : Sharing.py"
webElements = driver.find_element_by_xpath("//*[@id='comments-checkbox-twitter-image']")
webElements.click()

time.sleep(6)

strLink = report.CaptureSnapshot(driver,"twitter.png")
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on twitter checkbox to share","Twitter window opened.",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(3)
#webElements = driver.switch_to_window("facebook")
webElements = driver.find_element_by_xpath("//*[@id='oauth_form']/fieldset[1]/div[1]/label").send_keys("ritesh19july@gmail.com")
webElements = driver.find_element_by_xpath("//*[@id='password']").send_keys("crestech")
time.sleep(2)
webElements = driver.find_element_by_xpath("//*[@id='allow']")
webElements.click()
time.sleep(4)

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
webElements = driver.find_element_by_xpath("//div[@id='comments-commentBox']/table/tbody/tr/td/div[3]/div/div/textarea").send_keys("Sharing on twitter")

webElements = driver.find_element_by_xpath("//div[@id='comments-postButton']/a")
webElements.click()
time.sleep(2)
FetchedText2 = driver.find_element_by_xpath("//*[@id='comments-loginCanvas']/div").text

strLink = report.CaptureSnapshot(driver,"twitter2.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Entering data in comment box and click on post button","Post has been shared on twitter",strLink,"Windows")


print FetchedText2


webElements = driver.find_element_by_xpath("//div[@id='comments-checkbox-facebook']/div")
webElements.click()

time.sleep(6)

strLink = report.CaptureSnapshot(driver,"facebook.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Clicking on facebook checkbox to share","facebook window opened.",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(3)
#webElements = driver.switch_to_window("facebook")
webElements = driver.find_element_by_xpath("//div[@id='loginform']/div/input").send_keys("ritesh19july@gmail.com")
webElements = driver.find_element_by_xpath("//div[@id='loginform']/div[2]/input").send_keys("crestech")
time.sleep(2)
webElements = driver.find_element_by_xpath("//label[@id='loginbutton']/input")
webElements.click()
time.sleep(4)

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
webElements = driver.find_element_by_xpath("//div[@id='comments-commentBox']/table/tbody/tr/td/div[3]/div/div/textarea").send_keys("Sharing on fb")

webElements = driver.find_element_by_xpath("//div[@id='comments-postButton']/a")
webElements.click()
time.sleep(4)

#driver.get("http://www.facebook.com")
#driver.implicitly_wait(30)
#driver.maximize_window()

FetchedText = driver.find_element_by_xpath("//*[@id='comments-loginCanvas']/div").text

#webElements = driver.find_element_by_xpath("//*[@id='comments-loginCanvas']/div/a")
#webElements.click()

time.sleep(6)

strLink = report.CaptureSnapshot(driver,"facebook2.png")
keywordReportVar4+=report.keywordReportMethod(True,4,"Entering data in comment box and click on post button","Post has been shared on facebook",strLink,"Windows")


	
print FetchedText

if FetchedText.find("ritesh", 0) > -1 and FetchedText.find("Logout", 0) > -1 and FetchedText2.find("ritesh", 0) > -1 and FetchedText2.find("Logout", 0) > -1  :
	strMsg = "User is able to share anything on facebook and twitter"
	status1=True
	status=True
else :
	strMsg = "User is not able to share anything on facebook and twitter"
	status=False
	status1=False	

	
path= "/wsx/"+'ShareResult.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
	
keywordReportVar5+=report.keywordReportMethod(status1,5,"Sharing Scenario",strMsg,path,"Windows")    
#driver.find_element_by_css_selector("a.bgimg.right").click()
# Wait for 5 seconds
time.sleep(2)
	
TestCaseReportVar=report.testcaseMethod(3,"Sharing",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+"</tbody></table></div>"

time.sleep(2)
driver.quit()
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)
	




