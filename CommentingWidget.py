

#def ValidateCommenting(driver,noindex,url):
	
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report

from selenium.webdriver.support.ui import Select

htmlFolderPath="c:\\wwe"
url="http://www.stage-qa.cloud.wwe.com/node/26026027"
#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#driver = webdriver.Remote(
 #  command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
  # desired_capabilities=desired_cap)
driver = webdriver.Firefox()
driver.delete_all_cookies()
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

driver.delete_all_cookies()
print "Executing testCaseName : CommentingWidget.py"
webElements = driver.find_element_by_xpath("//div[@id='comments-loginCanvas']/div/a")
webElements.click()

time.sleep(2)

strLink = report.CaptureSnapshot(driver,"LoginButton.png")
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on Login button to comment","Login button clicked successfully",strLink,"Windows")

webElements = driver.find_element_by_xpath("//div[@id='primary_content_container']/section/div/div/div[2]/div/div/form/div[2]/input").send_keys("ankit.gupta@crestechglobal.com")
webElements = driver.find_element_by_xpath("//div[@id='primary_content_container']/section/div/div/div[2]/div/div/form/div[3]/input").send_keys("crestech123")
time.sleep(5)

strLink = report.CaptureSnapshot(driver,"LoginForm.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Snapshot of Login Page","Filling the Login details",strLink,"Windows")



webElements = driver.find_element_by_xpath("//div[@id='primary_content_container']/section/div/div/div[2]/div/div/form/div[4]/button")
webElements.click()
time.sleep(4)
#	driver.implicitly_wait(30)
webElements = driver.find_element_by_xpath("//div[@id='comments-commentBox']/table/tbody/tr/td/div[3]/div/div/textarea").send_keys("U Rock!!")
time.sleep(2)

strLink = report.CaptureSnapshot(driver,"comment.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Entering the text in comment section","Text U Rock has been typed",strLink,"Windows")

webElements = driver.find_element_by_xpath("//div[@id='comments-postButton']/a")
webElements.click()
time.sleep(2)
print "Post button"
strLink = report.CaptureSnapshot(driver,"comment2.png")
keywordReportVar4+=report.keywordReportMethod(True,4,"Verifying the posted comment","Comment has been posted",strLink,"Windows")


FetchedText = driver.find_element_by_xpath("//*[@id='comments_8df4093dd14345cab62ceb74a6acb8b5']/div[1]/div/table/tbody/tr/td[2]/div[1]/div[1]/span[1]").text
FetchedText2 = driver.find_element_by_xpath("//*[@id='comments_8df4093dd14345cab62ceb74a6acb8b5']/div[1]/div/table/tbody/tr/td[2]/div[3]").text

print "FetchedText "+FetchedText
print "FetchedText2 "+FetchedText2

if FetchedText.find("Ritesh", 0) > -1 and FetchedText2.find("Rock", 0) > -1 :
	strMsg = "User is able to comment"
	status1=True
	status=True
else :
	strMsg = "User is not able to comment"
	status=False
	status1=False	

	
path= "/wsx/"+'CommentResult.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
	
keywordReportVar5+=report.keywordReportMethod(status1,5,"Comment Scenario",strMsg,path,"Windows")    
#driver.find_element_by_css_selector("a.bgimg.right").click()
# Wait for 5 seconds
time.sleep(2)

TestCaseReportVar=report.testcaseMethod(8,"CommentingWidget",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+"</tbody></table></div>"
time.sleep(2)	
driver.quit()
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)

	


	
	
	





