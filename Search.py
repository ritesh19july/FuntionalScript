from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
 


#Global Varibles
url="http://wwe.com"
htmlFolderPath="c:\\wwe\\"


#desired_cap = {'browser': 'Firefox', 'browser_version': '26.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#driver = webdriver.Remote(
#    command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
#    desired_capabilities=desired_cap)

#driver = webdriver.Firefox()
#driver.get(url)
#driver.implicitly_wait(30)
#driver.maximize_window()
#assert "Python" in driver.title

#status=True
keywordReportVar=""
AllTestCasedata=""
status=True

def SearchWrestler(driver,noindex,url):
	#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
	#driver = webdriver.Remote(
	   #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
	   #desired_capabilities=desired_cap)
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
	print "Executing testCaseName : Search.py"
	webElements = driver.find_element_by_xpath("//div[@id='search_box_202']/div/div/input").send_keys("John Cena")
	webElements = driver.find_element_by_xpath("//div[@id='search_box_202']/div/div/a")
	webElements.click()

	time.sleep(2)

	strLink = report.CaptureSnapshot(driver,"DesiredSearch.png")
	keywordReportVar+=report.keywordReportMethod(True,1,"Typing the John Cena in search field and clicking on search button","John cena stuff has been searched",strLink,"Windows")

	ArrOfData = report.ValidateTheSearchInDiffTabs(driver)


	webElements = driver.find_element_by_xpath("//*[@id='wwe_search_gsa_results1']/div[1]/div/span[5]")
	webElements.click()
	time.sleep(3)
	ArrOfData2 = report.ValidateTheSearchInDiffTabs(driver)


	strLink = report.CaptureSnapshot(driver,"DesiredSearch2.png")
	keywordReportVar2+=report.keywordReportMethod(True,1,"Checking the searched item in video tab","John cena stuff has been found",strLink,"Windows")



	webElements = driver.find_element_by_xpath("//*[@id='wwe_search_gsa_results1']/div[1]/div/span[6]")
	webElements.click()
	time.sleep(3)
	ArrOfData3 = report.ValidateTheSearchInDiffTabs(driver)

	strLink = report.CaptureSnapshot(driver,"DesiredSearch3.png")
	keywordReportVar3+=report.keywordReportMethod(True,1,"Checking the searched item in photos tab","John cena stuff has been found",strLink,"Windows")

	webElements = driver.find_element_by_xpath("//*[@id='wwe_search_gsa_results1']/div[1]/div/span[8]")
	webElements.click()
	time.sleep(3)
	strLink = report.CaptureSnapshot(driver,"DesiredSearch2.png")
	keywordReportVar4+=report.keywordReportMethod(True,1,"Checking the searched item in lists tab","John cena stuff has been found",strLink,"Windows")

	ArrOfData4 = report.ValidateTheSearchInDiffTabs(driver)

	time.sleep(2)

	if ArrOfData[0].find("Cena", 0) > -1 and ArrOfData[1].find("Cena", 0) > -1 and ArrOfData2[0].find("Cena", 0) > -1 and ArrOfData2[1].find("Cena", 0) > -1 and ArrOfData3[0].find("Cena", 0) > -1 and ArrOfData3[1].find("Cena", 0) > -1 and ArrOfData4[0].find("Cena", 0) > -1 and ArrOfData4[1].find("Cena", 0) > -1:
		strMsg = "User is able to search any wrestler"
		status1=True
		status=True
	else :
		strMsg = "User is not able to search"
		status=False
		status1=False	

		
	path= "/wsx/"+'SearchResult.png'   
	print path
	driver.save_screenshot(htmlFolderPath+path)

	print htmlFolderPath
		
	keywordReportVar5+=report.keywordReportMethod(status1,1,"Search Scenario",strMsg,path,"Windows")    
	#driver.find_element_by_css_selector("a.bgimg.right").click()
	# Wait for 5 seconds
	time.sleep(2)
		
	TestCaseReportVar=report.testcaseMethod(6,"Search",status)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+"</tbody></table></div>"
	driver.quit()
	return AllTestCasedata
	