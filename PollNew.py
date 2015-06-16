from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report

#Global Varibles
#all Urls
#Event url="http://www.stage-qa.cloud.wwe.com/node/25064032"
#article url="http://www.stage-qa.cloud.wwe.com/node/26026027"
#Photo Gallery/PG url="http://www.stage-qa.cloud.wwe.com/node/26900979"
#Video url="http://www.stage-qa.cloud.wwe.com/node/26040423"
#Playlist url="http://www.stage-qa.cloud.wwe.com/node/26040287"
url="http://www.stage-qa.cloud.wwe.com/inside/polls/which-superstar-do-you-most-enjoy-get-an-rko-outta-nowhere"
htmlFolderPath="c:\\wwe\\"

#desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
#driver = webdriver.Remote(
 #command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
  # desired_capabilities=desired_cap)

driver = webdriver.Firefox()

#driver = webdriver.Chrome()
print "Executing test case name :: PollNew.py"
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
keywordReportVar+=report.keywordReportMethod(True,1,"Click on Polling Link","Link has been clicked successfully",strLink,"Windows")

webElements = driver.find_element_by_xpath("//*[@id='questions']/div/div/div[1]/a")
webElements.click()

driver.delete_all_cookies()

webElements = driver.find_element_by_xpath("//*[@id='submit']")
webElements.click()
time.sleep(5)


FetchedVotes = driver.find_element_by_xpath("//*[@id='tv']").text
NewFetchedVotes = FetchedVotes.split(": ")
print NewFetchedVotes
beforePollCount= int(NewFetchedVotes[1])


strVote = report.CaptureSnapshot(driver,"Voting.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Snapshot before submitting the poll","Reading the number of votes are :"+NewFetchedVotes[1],strVote,"Windows")



driver.refresh()
time.sleep(2)
#driver.reload()
print beforePollCount

driver.delete_all_cookies()

webElements = driver.find_element_by_xpath("//*[@id='questions']/div/div/div[1]/a")
webElements.click()
webElements = driver.find_element_by_xpath("//*[@id='submit']")
webElements.click()
time.sleep(2)


FetchedVotes2 = driver.find_element_by_xpath("//*[@id='tv']").text
NewFetchedVotes2 = FetchedVotes2.split(": ")
afterPollCount= int(NewFetchedVotes2[1])
print afterPollCount

strVote = report.CaptureSnapshot(driver,"Voting2.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Snapshot after submitting the poll","Option has been selected successfully and the number of votes are :"+NewFetchedVotes2[1],strVote,"Windows")


FetchedText = driver.find_element_by_xpath("//*[@id='results']/div/div[1]/span").text
print FetchedText



time.sleep(2)
if FetchedText=="THANK YOU FOR VOTING!" and afterPollCount>beforePollCount:
		strMsg = "Voting has been done successfully"
		status1=True
else:
		strMsg = "Vote count has not increased."
		status=False
		status1=False
			
path= "/wsx/"+'Pollscreen.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath

keywordReportVar4+=report.keywordReportMethod(status1,4,"Poll Scenario",strMsg,path,"Windows")  

time.sleep(2)
    
TestCaseReportVar=report.testcaseMethod(1,"Poll",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+"</tbody></table></div>"

driver.quit()


report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)
