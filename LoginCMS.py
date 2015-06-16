

def login_CMS(noindex,url):
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
	import time
	import report
	import ManageScreen
	
	desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
	driver = webdriver.Remote(
	   command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
	   desired_capabilities=desired_cap)
	#driver = webdriver.Firefox()
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
	ManageScreen.globalDriverSession=driver
	print ManageScreen.globalDriverSession
	print "Executing testCaseName : LoginCMS.py"
	
	strLink = report.CaptureSnapshot(driver,"Login.png")
	keywordReportVar+=report.keywordReportMethod(True,1,"Login page opened","Login paged open successfully",strLink,"Windows")
	driver.find_element_by_id("edit-name").clear()
	driver.find_element_by_id("edit-name").send_keys("QA US")
	driver.find_element_by_id("edit-pass").clear()
	driver.find_element_by_id("edit-pass").send_keys("just4test")
	driver.find_element_by_id("edit-submit").click()

	strLink = report.CaptureSnapshot(driver,"LoginSuccessfully.png")
	keywordReportVar2+=report.keywordReportMethod(True,1,"Clicked on submit button","Submit button has been clicked",strLink,"Windows")
	
	
	strText=driver.find_element_by_xpath("//div[@id='branding']/h1").text
	time.sleep(2)

	if strText.find("QA US", 0) > -1:
		strMsg = "User is able to login"
		status1=True
		status=True
	else :
		strMsg = "User is not able to login"
		status=False
		status1=False	

		
	path= "/wsx/"+'Login.png'   
	print path
	driver.save_screenshot(ManageScreen.htmlFolderPath+path)

	print ManageScreen.htmlFolderPath
		
	keywordReportVar3+=report.keywordReportMethod(status1,1,"Login Scenario",strMsg,path,"Windows")    
	#driver.find_element_by_css_selector("a.bgimg.right").click()
	# Wait for 5 seconds
	time.sleep(2)
		
	TestCaseReportVar=report.testcaseMethod(1,"Login",status)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+"</tbody></table></div>"
	#driver.quit()
	return AllTestCasedata