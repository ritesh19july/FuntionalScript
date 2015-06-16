from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
 


#Global Varibles
url="http://wwe.com/classics/the-men-in-black-photos"
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
status=True
status=True
keywordReportVar=""
AllTestCasedata=""

def ValidateVideo(driver,noindex,url):
	#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
	#driver = webdriver.Remote(
	   #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
	   #desired_capabilities=desired_cap)
	driver = webdriver.Firefox()
	driver.get(url)
	driver.implicitly_wait(30)
	driver.maximize_window()
	keywordReportVar=""
	keywordReportVar2=""
	keywordReportVar3=""
	
	AllTestCasedata=""
	status=""
	status1=""
	print "Executing testCaseName : Video_Comparision.py"
	webElements = driver.find_element_by_xpath("//div[@id='video_playlist_55738']/div/div/div[4]/div[3]/a[2]")
	webElements.click()

	time.sleep(2)
	strLink = report.CaptureSnapshot(driver,"Video.png")
	keywordReportVar+=report.keywordReportMethod(True,1,"Snapshot before playing the video","Fetching the video text that is visible in playlist",strLink,"Windows")


	FetchedText = driver.find_element_by_xpath("//*[@id='video_playlist_55738']/div/div/div[4]/div[3]/div[2]/div/p").text

	webElements = driver.find_element_by_xpath("//div[@id='video_playlist_55738']/div/div/div[4]/div[3]/div[2]/div/a")
	webElements.click()
	time.sleep(4)

	strLink = report.CaptureSnapshot(driver,"Video2.png")
	keywordReportVar2+=report.keywordReportMethod(True,1,"Snapshot after playing the video","Fetching the video title after playing the video",strLink,"Windows")

	
	FetchedText2 = driver.find_element_by_xpath("//*[@id='page_title_889']/div/div/h1/span").text


	NewFetchedText = FetchedText.lower()
	NewFetchedText2= FetchedText2.lower()

	print NewFetchedText
	print NewFetchedText2

	if NewFetchedText==NewFetchedText2 :
		strMsg = "Video is playing as per the user selection"
		status1=True
		status=True
	else :
		strMsg = "Video is not playing as per the user selection"
		status=False
		status1=False	

		
	path= "/wsx/"+'VideoResult.png'   
	print path
	driver.save_screenshot(htmlFolderPath+path)

	print htmlFolderPath
		
	keywordReportVar3+=report.keywordReportMethod(status1,1,"Video Scenario",strMsg,path,"Windows")    
	#driver.find_element_by_css_selector("a.bgimg.right").click()
	# Wait for 5 seconds
	time.sleep(2)
		
	TestCaseReportVar=report.testcaseMethod(4,"Video",status)
	AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+"</tbody></table></div>"
	return AllTestCasedata
	driver.driver.quit()


