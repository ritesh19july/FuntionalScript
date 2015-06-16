# User should be able to comment when user loggedIn

def ValidateCommenting(driver,noindex,url):
	# Importing packages 
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
	import time
	import report

	from selenium.webdriver.support.ui import Select
	# Firefox configuration for BrowserStack
	htmlFolderPath="c:\\wwe\\"
	#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
	#driver = webdriver.Remote(
	  # command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
	   #desired_capabilities=desired_cap)
	# Firefox configuration for local
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
	# Click on login button
	print "Executing testCaseName : Comment.py"
	webElements = driver.find_element_by_xpath("//div[@id='comments-loginCanvas']/div/a")
	webElements.click()

	time.sleep(2)
	# Taking screen-shot and filling the data in login form
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
	# Writing comments in text area
	webElements = driver.find_element_by_xpath("//div[@id='comments-commentBox']/table/tbody/tr/td/div[3]/div/div/textarea").send_keys("U Rock!!")
	time.sleep(2)

	strLink = report.CaptureSnapshot(driver,"comment.png")
	keywordReportVar3+=report.keywordReportMethod(True,3,"Entering the text in comment section","Text U Rock has been typed",strLink,"Windows")
	# Clicking on submit button
	webElements = driver.find_element_by_xpath("//div[@id='comments-postButton']/a")
	webElements.click()
	time.sleep(2)
	# Capture screen-shot
	strLink = report.CaptureSnapshot(driver,"comment2.png")
	keywordReportVar4+=report.keywordReportMethod(True,4,"Verifying the posted comment","Comment has been posted",strLink,"Windows")

	# Fetching data from UI
	FetchedText = driver.find_element_by_xpath("//*[@id='comments_8df4093dd14345cab62ceb74a6acb8b5']/div[1]/div/table/tbody/tr/td[2]/div[1]/div[1]/span[1]").text
	FetchedText2 = driver.find_element_by_xpath("//*[@id='comments_8df4093dd14345cab62ceb74a6acb8b5']/div[1]/div/table/tbody/tr/td[2]/div[3]").text

	print FetchedText
	print FetchedText2
	# Verifying data with UI data
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
	# Capture screen-shot	
	keywordReportVar5+=report.keywordReportMethod(status1,5,"Comment Scenario",strMsg,path,"Windows")    
	#driver.find_element_by_css_selector("a.bgimg.right").click()
	# Wait for 5 seconds
	time.sleep(2)
	# Adding report in html format
	TestCaseReportVar=report.testcaseMethod(2,"Comment",status)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+"</tbody></table></div>"
	time.sleep(2)	
	driver.quit()
	return AllTestCasedata
	


	
	
	





