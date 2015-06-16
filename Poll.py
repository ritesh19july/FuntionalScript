#Using Behaviour-driven development |Given-When-Then (GWT) technique
#Given that user should be able to submit the vote
#When user is loggedIn in Application
#Then Vote should be increased.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
import SSO 
import Search
import Event_Search
import Comment
import Sharing
import Video_Comparision

#Global Varibles
url="http://release.jenkins.wwe.com/inside/polls/who-was-the-most-absurd-wwe-superstar"
htmlFolderPath="c:\\wwe\\"

# Firefox configuration for BrowserStack
#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
 #  desired_capabilities=desired_cap)
# Firefox configuration for local
driver = webdriver.Firefox()
# Chrome configuration for local
#driver = webdriver.Chrome()

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

## Capture screen-shot and select a option for polling
strLink = report.CaptureSnapshot(driver,"Link.png")
print strLink
keywordReportVar+=report.keywordReportMethod(True,1,"Click on Polling Link","Link has been clicked successfully",strLink,"Windows")


webElements = driver.find_element_by_xpath("//*[@id='questions']/div/div/div[1]/a")
webElements.click()

driver.delete_all_cookies()
## Click on submit button
webElements = driver.find_element_by_xpath("//*[@id='submit']")
webElements.click()
time.sleep(10)

# Fetching data from UI
FetchedVotes = driver.find_element_by_xpath("//*[@id='tv']").text
NewFetchedVotes = FetchedVotes.split(": ")
print NewFetchedVotes
a= int(NewFetchedVotes[1])

## Capture screen-shot
strVote = report.CaptureSnapshot(driver,"Voting.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Snapshot before submitting the poll","Reading the number of votes are :"+NewFetchedVotes[1],strVote,"Windows")


##
driver.refresh()
time.sleep(10)
#driver.reload()
print a

driver.delete_all_cookies()

webElements = driver.find_element_by_xpath("//*[@id='questions']/div/div/div[1]/a")
webElements.click()
webElements = driver.find_element_by_xpath("//*[@id='submit']")
webElements.click()
time.sleep(2)


FetchedVotes2 = driver.find_element_by_xpath("//*[@id='tv']").text
print FetchedVotes2
NewFetchedVotes2 = FetchedVotes2.split(": ")
b= int(NewFetchedVotes2[1])
print b

strVote = report.CaptureSnapshot(driver,"Voting2.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Snapshot after submitting the poll","Option has been selected successfully and the number of votes are :"+NewFetchedVotes2[1],strVote,"Windows")


FetchedText = driver.find_element_by_xpath("//*[@id='results']/div/div[1]/span").text
print FetchedText



time.sleep(2)
if FetchedText=="THANK YOU FOR VOTING!" and b>a:
	strMsg = "Voting has been done successfully"
	status1=True
else :
	strMsg = "User is not able to vote"
	status=False
	status1=False
		
path= "/wsx/"+'Pollscreen.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
	


keywordReportVar4+=report.keywordReportMethod(status1,4,"Poll Scenario",strMsg,path,"Windows")  

    
#driver.find_element_by_css_selector("a.bgimg.right").click()
# Wait for 5 seconds
time.sleep(2)
    
TestCaseReportVar=report.testcaseMethod(1,"Poll",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+"</tbody></table></div>"

driver.quit()


url = "http://release.jenkins.wwe.com/node/26026027"
Comment_Data = Comment.ValidateCommenting(driver,2,url)
Sharing_Data = Sharing.ValidateSharing(driver,3,url)

url = "http://release.jenkins.wwe.com/videos/playlists/randy-orton-earth-shattering-rkos-playlist"
Video_Data = Video_Comparision.ValidateVideo(driver,4,url)

url="http://release.jenkins.wwe.com/"
SSO_Data = SSO.ExecuteSSOPart(driver,5,url)
Search_Data = Search.SearchWrestler(driver,6,url)
url = "http://release.jenkins.wwe.com/events"
Event_Search_Data = Event_Search.SearchEvent(driver,7,url)

AllTestCasedata=AllTestCasedata+Comment_Data+Sharing_Data+Video_Data+SSO_Data+Search_Data+Event_Search_Data

#AllTestCasedata=AllTestCasedata+Search_Data

report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)


