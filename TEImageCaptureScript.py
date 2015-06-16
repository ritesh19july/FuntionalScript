

def firefoxInstance(url):
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
	import time
	import report
		
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
	AllTestCasedata=""
	status=""
	status1=""
	print "Executing testCaseName : LoginCMS.py"
	
	strLink = report.CaptureSnapshot(driver,"Firefox.png")
	keywordReportVar+=report.keywordReportMethod(True,1,"Given url page should open.","Given url opened successfully",strLink,"Windows")
		
	TestCaseReportVar=report.testcaseMethod(1,"Firefox",True)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+"</tbody></table></div>"
	driver.quit()
	return AllTestCasedata

def internetExplorerInstance(url):
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
	import time
	import report
		
	#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
	#driver = webdriver.Remote(
	 #  command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
	  # desired_capabilities=desired_cap)
	  
	driver = webdriver.Ie()
	driver.delete_all_cookies()
	driver.get(url)
	driver.get("javascript:document.getElementById('overridelink').click();")
	driver.implicitly_wait(30)
	driver.maximize_window()
	keywordReportVar=""
	AllTestCasedata=""
	
	print "Executing testCaseName : LoginCMS.py"
	
	strLink = report.CaptureSnapshot(driver,"IE.png")
	keywordReportVar+=report.keywordReportMethod(True,1,"Given url page should open.","Given url opened successfully",strLink,"Windows")
		
	TestCaseReportVar=report.testcaseMethod(2,"InternetExplorer",True)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+"</tbody></table></div>"
	driver.quit()
	return AllTestCasedata