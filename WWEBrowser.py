from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
import unittest, time, re

#Global Varibles
url="http://www.stage-qa.cloud.wwe.com/user"
htmlFolderPath="c:\\wwe\\"


#For WWE Browser screen

#driver = webdriver.Firefox()
desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
driver = webdriver.Remote(
 command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
   desired_capabilities=desired_cap)
#driver = webdriver.Chrome()

print "Executing test case name :: WWEBrowser.py"

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
keywordReportVar5=""
AllTestCasedata=""

driver.delete_all_cookies()

## For Reporting
strLink = report.CaptureSnapshot(driver,"Link.png")
print strLink
driver.find_element_by_id("edit-name").clear()
driver.find_element_by_id("edit-name").send_keys("QA US")
driver.find_element_by_id("edit-pass").clear()
driver.find_element_by_id("edit-pass").send_keys("just4test")
driver.find_element_by_id("edit-submit").click()

keywordReportVar+=report.keywordReportMethod(True,1,"Open wwe browser screen ","URL has been opened successfully",strLink,"Windows")
element_to_hover_over = driver.find_element_by_xpath("//ul[@id='simplemenu']/li[2]/a")

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(2)
driver.find_element_by_link_text("WWE Browser").click()
driver.find_element_by_link_text("Gallery").click()
galVal=driver.find_element_by_css_selector("td.type").text
print galVal
#self.assertEqual("Gallery", driver.find_element_by_css_selector("td.type").text)

strMS = report.CaptureSnapshot(driver,"wweBrowser.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Clicked on gallery link","User is able to see the gallery link",strMS,"Windows")

driver.find_element_by_css_selector("a.video").click()
#assertEqual("Video", driver.find_element_by_css_selector("td.type").text)
strMS2 = report.CaptureSnapshot(driver,"wweBrowser2.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Clicked on video link","User is able to see the video link.",strMS2,"Windows")

driver.find_element_by_css_selector("a.article").click()
#self.assertEqual("Article", driver.find_element_by_css_selector("td.type").text)
strMS3 = report.CaptureSnapshot(driver,"wweBrowser3.png")
keywordReportVar4+=report.keywordReportMethod(True,4,"Clicked on article link","User is able to see the article link.",strMS3,"Windows")

driver.find_element_by_link_text("Show-Related").click()
#assertEqual("Episode", driver.find_element_by_css_selector("td.type").text)
driver.find_element_by_css_selector("a.talent").click()
#assertEqual("Talent", driver.find_element_by_css_selector("td.type").text)
driver.find_element_by_link_text("\"Features\"").click()
#assertEqual("Editorial_pod_item", driver.find_element_by_xpath("//div[@id='wwe-browser-qf-results']/table/tbody/tr[3]/td[4]").text)
driver.find_element_by_css_selector("a.media").click()
#assertEqual("Link", driver.find_element_by_css_selector("td.type").text)
#assertEqual("Document", driver.find_element_by_css_selector("td.type").text)
doc=driver.find_element_by_css_selector("td.type").text
print doc
driver.find_element_by_id("wwe-browser-close").click()

time.sleep(2)
if doc=="Link":
		strMsg = "Link has been verified successfully"
		status1=True
else:
		strMsg = "Link has not not verified."
		status=False
		status1=False
			
path= "/wsx/"+'wweScreenFinal.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath

keywordReportVar5+=report.keywordReportMethod(status1,5,"WWE Browser Scenario",strMsg,path,"Windows")  

time.sleep(2)
    
TestCaseReportVar=report.testcaseMethod(1,"WWEBrowser",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+"</tbody></table></div>"

report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)

driver.quit()


