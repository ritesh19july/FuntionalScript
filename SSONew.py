from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
 


#Global Varibles
url="http://www.stage-qa.cloud.wwe.com/"
htmlFolderPath="c:\\wwe\\"

keywordReportVar=""
AllTestCasedata=""
status=True


#def ExecuteSSOPart(driver,noindex,url):
driver = webdriver.Firefox()
#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#driver = webdriver.Remote(
   #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
   #desired_capabilities=desired_cap)
driver.delete_all_cookies()
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()
keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
AllTestCasedata=""
status=""
status1=""
print "Executing testCaseName : SSONew.py"
webElements = driver.find_element_by_xpath("//div[@id='login_links_200']/div/div/div/div/a[2]")
webElements.click()

time.sleep(2)

strLink = report.CaptureSnapshot(driver,"SSO.png")
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on login button for sign in","Login page has been opened",strLink,"Windows")


webElements = driver.find_element_by_xpath("//div[@id='primary_content_container']/section/div/div/div[2]/div/div/form/div[2]/input").send_keys("ritesh19july@gmail.com")
webElements = driver.find_element_by_xpath("//div[@id='primary_content_container']/section/div/div/div[2]/div/div/form/div[3]/input").send_keys("crestech")
time.sleep(2)
webElements = driver.find_element_by_xpath("//div[@id='primary_content_container']/section/div/div/div[2]/div/div/form/div[4]/button")
webElements.click()
time.sleep(2)
#driver.close()
#driver = webdriver.Firefox()
#driver.get(url)
#driver.implicitly_wait(30)
#driver.maximize_window()
strLink = report.CaptureSnapshot(driver,"SSO.png")
keywordReportVar2+=report.keywordReportMethod(True,1,"Verifying whether user is able to logged in","user is able to login successfully",strLink,"Windows")


FetchedText = driver.find_element_by_xpath("//*[@id='login_links_200']/div/div/div/div[2]/div/div[1]/a").text
print FetchedText
#//div[@id='login_links_200']/div/div/div/div[2]/div/div/a
#.//*[@id='login_links_200']/div/div/div/div[2]/div/div[1]/a


if FetchedText.find("RITESH", 0) > -1 :
	strMsg = "User is able to login successfully"
	status1=True
	status=True
else :
	strMsg = "User is not able to login"
	status=False
	status1=False
		
path= "/wsx/"+'Login.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
	
keywordReportVar3+=report.keywordReportMethod(status1,1,"SSO Scenario",strMsg,path,"Windows")    
#driver.find_element_by_css_selector("a.bgimg.right").click()
# Wait for 5 seconds
time.sleep(2)
TestCaseReportVar=report.testcaseMethod(5,"SSO",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+"</tbody></table></div>"
driver.quit()
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)
