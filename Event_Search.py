# User should be able to search any event on this page.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
import SSO 

from selenium.webdriver.support.ui import Select



#Global Varibles
url="http://wwe.com/events"
htmlFolderPath="c:\\wwe\\"

status=""
status1=""
#status=True
keywordReportVar=""
AllTestCasedata=""


def SearchEvent(driver,noindex,url):
	
	# Firefox configuration for BrowserStack
	#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
	#driver = webdriver.Remote(
	   #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
	   #desired_capabilities=desired_cap)
	# Firefox configuration for local
	driver = webdriver.Firefox()
	driver.delete_all_cookies()
	driver.get(url)
	keywordReportVar=""
	keywordReportVar2=""
	keywordReportVar3=""	
	AllTestCasedata=""
	status=""
	status1=""
	# Press Key 'ESCAPE'
	webElements = driver.find_element_by_xpath("//div[@id='live_events_1153']/div/div/div/div[2]/div/div/div/select").send_keys(Keys.ESCAPE)
	print "Escape"
	# Select event in drop-down
	webElements = Select(driver.find_element_by_xpath("//div[@id='live_events_1153']/div/div/div/div[2]/div/div/div/select"))
	webElements.select_by_visible_text('Raw')
	# Capture screen-shot
	strLink = report.CaptureSnapshot(driver,"Event.png")
	keywordReportVar+=report.keywordReportMethod(True,1,"Selecting the RAW event","Event has been selected",strLink,"Windows")


	time.sleep(2)

	webElements = driver.find_element_by_xpath("//div[@id='live_events_1153']/div/div/div/div[2]/div[3]/div[4]/a")
	webElements.click()
	# Capture screen-shot and fetching data from UI
	strLink = report.CaptureSnapshot(driver,"SearchEvent.png")
	keywordReportVar2+=report.keywordReportMethod(True,1,"Click on search event","Event has been selected",strLink,"Windows")
	
	
	time.sleep(5)
	
	FetchedText = driver.find_element_by_xpath("//*[@id='live_events_1153']/div/div/div/div[3]/span[1]/a").get_attribute("title")
	FetchedText2 = driver.find_element_by_xpath("//*[@id='live_events_1153']/div/div/div/div[4]/span[1]/a").get_attribute("title")
#	FetchedText3 = driver.find_element_by_xpath("//*[@id='live_events_1153']/div/div/div/div[5]/span[1]/a").get_attribute("title")
		
	print FetchedText
	print FetchedText2
#	print FetchedText3

	time.sleep(2)
	# Verifying data from UI
	if FetchedText.find("Raw", 0) > -1 and FetchedText2.find("Raw", 0) > -1 :
		strMsg = "User is able to search any event"
		status1=True
		status=True
	else :
		strMsg = "User is not able to search the event"
		status=False
		status1=False	

		
	path= "/wsx/"+'EventSearchResult.png'   
	print path
	driver.save_screenshot(htmlFolderPath+path)

	print htmlFolderPath
		
	keywordReportVar3+=report.keywordReportMethod(status1,1,"Event Search Scenario",strMsg,path,"Windows")    
	#driver.find_element_by_css_selector("a.bgimg.right").click()
	# Wait for 5 seconds
	time.sleep(2)
	# Adding report in html formate
	TestCaseReportVar=report.testcaseMethod(7,"Event Search",status)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+"</tbody></table></div>"
	return AllTestCasedata
	driver.quit()






