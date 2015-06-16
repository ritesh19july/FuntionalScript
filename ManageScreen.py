from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
import LoginCMS

#Global Varibles

url="http://www.stage-qa.cloud.wwe.com/node/26179108/manage"
htmlFolderPath="c:\\wwe\\"
globalDriverSession=""
# For login in CMS
urlLogin = "http://www.stage-qa.cloud.wwe.com/user"
Login_Data = LoginCMS.login_CMS(1,urlLogin)

#For manage screen test case

#driver = webdriver.Firefox()
#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#driver = webdriver.Remote(
 #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
  # desired_capabilities=desired_cap)
#driver = webdriver.Chrome()
print "Executing test case name :: ManageScreen.py"
print globalDriverSession
driver=globalDriverSession
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()
#assert "Python" in driver.title
status=True
#status=True
keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
keywordReportVar4=""

AllTestCasedata=""

driver.delete_all_cookies()

## For Reporting
strLink = report.CaptureSnapshot(driver,"Link.png")
print strLink
keywordReportVar+=report.keywordReportMethod(True,1,"Open Manage screen url","URL has been opened successfully",strLink,"Windows")
driver.find_element_by_css_selector("input.remove").click()
driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()


strMS = report.CaptureSnapshot(driver,"ManageScreen1.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Objects present","User is able to see the manage screen",strMS,"Windows")
revDate = driver.find_element_by_css_selector("td.rev_date").text
print revDate

strMS2 = report.CaptureSnapshot(driver,"ManageScreen2.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Manage screen page status present","User is able to see the status of screen.",strMS2,"Windows")


authorName = driver.find_element_by_css_selector("td.author").text
print authorName



time.sleep(2)
if True==True:
		strMsg = "Revision date has been verified successfully"
		status1=True
else:
		strMsg = "Revision date has not not verified."
		status=False
		status1=False
			
path= "/wsx/"+'ManageScreen.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath

keywordReportVar4+=report.keywordReportMethod(status1,4,"ManageScreen Scenario",strMsg,path,"Windows")  

time.sleep(2)
    
TestCaseReportVar=report.testcaseMethod(2,"ManageScreen",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+"</tbody></table></div>"
AllTestCasedata=Login_Data+AllTestCasedata
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)

print "finishedddddd"
driver.quit()
quit()

