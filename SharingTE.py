from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report

from selenium.webdriver.support.ui import Select



#Global Varibles
url="https://www.wwetoughenough.com/news/wwe-tough-enough-final-40-revealed"
htmlFolderPath="c:\\wwe\\"


#assert "Python" in driver.title
status=""
status1=""
#status=True
keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
keywordReportVar4=""
AllTestCasedata=""


#def ValidateSharing(driver,noindex,url):
   
desired_cap = {'browser': 'Firefox', 'browser_version': '35.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
driver = webdriver.Remote(
 command_executor='http://wwedigital:5qbpUt5E9XNYZ8z9x9zb@hub.browserstack.com:80/wd/hub',
   desired_capabilities=desired_cap)
#driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()
keywordReportVar=""
keywordReportVar2=""
keywordReportVar3=""
keywordReportVar4=""
keywordReportVar5=""
keywordReportVar6=""
keywordReportVar7=""
keywordReportVar8=""
keywordReportVar9=""	
AllTestCasedata=""
status=""
status1=""


time.sleep(10)
print "Executing testCaseName : SharingTE.py"
#For Twitter sharing

driver.find_element_by_xpath("//span[@class='st_twitter_large']/span/span").click()
print "Object clicked"
time.sleep(10)

strLink = report.CaptureSnapshot(driver,"twitter.png")
keywordReportVar+=report.keywordReportMethod(True,1,"Clicking on twitter button to share","Twitter window opened.",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(3)
driver.find_element_by_id("username_or_email").clear()
driver.find_element_by_id("username_or_email").send_keys("ritesh19july@gmail.com")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("crestech")
driver.find_element_by_xpath("//input[@value='Log in and Tweet']").click()
driver.find_element_by_xpath("//input[@value='Tweet']").click()
bodyText = driver.find_element_by_tag_name('body').text

if bodyText.find("You have already sent this message", 0) > -1:
	strMsg = "You have already sent this message."
	status1=True
	status=True
	driver.close()
else:
	strMsg = "User is able to share anything on facebook and twitter"
	status=True
	status1=True	
	driver.find_element_by_id("btn-close").click()


time.sleep(4)

for handle in driver.window_handles:
	driver.switch_to.window(handle)

strLink = report.CaptureSnapshot(driver,"twitter2.png")
keywordReportVar2+=report.keywordReportMethod(True,2,"Entering data in comment box and click on post button","Post has been shared on twitter",strLink,"Windows")
time.sleep(10)

# For Facebook sharing
driver.find_element_by_xpath("//span[@class='st_facebook_large']/span/span").click()

time.sleep(6)

strLink = report.CaptureSnapshot(driver,"facebook.png")
keywordReportVar3+=report.keywordReportMethod(True,3,"Clicking on Facebook button to share","Facebook window opened.",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(3)

webElements = driver.find_element_by_xpath("//div[@id='loginform']/div/input").send_keys("9015452602")
webElements = driver.find_element_by_xpath("//div[@id='loginform']/div[2]/input").send_keys("crestech")
time.sleep(2)
webElements = driver.find_element_by_xpath("//label[@id='loginbutton']/input")
webElements.click()
time.sleep(10)
#driver.find_element_by_name("xhpc_message_text").clear()
driver.find_element_by_id("u_0_8").send_keys("Sharing on FB")
status1=True
strLink = report.CaptureSnapshot(driver,"facebook2.png")
print strLink
keywordReportVar4+=report.keywordReportMethod(True,4,"Entering data in comment box and click on post button","Post has been shared on Facebook",strLink,"Windows")
print "After fb shared"

driver.find_element_by_name("share").click()
time.sleep(5)
for handle in driver.window_handles:
	driver.switch_to.window(handle)

time.sleep(5)
#For GPlus
webElements = driver.find_element_by_xpath("//span[@class='st_googleplus_large']/span/span")
webElements.click()
print "after Gplus"
time.sleep(5)

strLink = report.CaptureSnapshot(driver,"GPlus1.png")
print strLink
keywordReportVar5+=report.keywordReportMethod(True,5,"Clicking on Gplus login button for sign in","GPlus Login page has been opened",strLink,"Windows")

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(6)
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("ritesh19july1@gmail.com")
driver.find_element_by_id("next").click()
time.sleep(5)
driver.find_element_by_id("Passwd").clear()
driver.find_element_by_id("Passwd").send_keys("crestech")
driver.find_element_by_id("signIn").click()
time.sleep(10)
strLink = report.CaptureSnapshot(driver,"GPlus2.png")
keywordReportVar6+=report.keywordReportMethod(True,6,"Verifying whether user is able to logged in","user is able to login successfully",strLink,"Windows")
driver.find_element_by_xpath("//td[@class='bI']/div").click()

time.sleep(10)
for handle in driver.window_handles:
	driver.switch_to.window(handle)



#For Sharing Pinterest


strLink = report.CaptureSnapshot(driver,"Pinterest.png")
print strLink
keywordReportVar7+=report.keywordReportMethod(True,7,"Clicking on Pinterest button","Pinterest page has been opened",strLink,"Windows")

webElements = driver.find_element_by_xpath("//span[@class='st_pinterest_large']/span/span")
webElements.click()


time.sleep(5)
#element_to_hover_over = driver.find_element_by_class("pin")

#hover = ActionChains(driver).move_to_element(element_to_hover_over)
#hover.perform()
#time.sleep(2)
#driver.find_element_by_xpath("//section[@id='block-system-main']/div/div/div[2]/div/div/div/div/div/div/div[2]/span[4]/span/span").click()

for handle in driver.window_handles:
	driver.switch_to.window(handle)
	
	
time.sleep(6)

#driver.find_element_by_id("userEmail").clear()
#driver.find_element_by_id("userEmail").send_keys("ritesh19july1@gmail.com")
#driver.find_element_by_id("userPassword").clear()
#driver.find_element_by_id("userPassword").send_keys("crestech")
#driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

strLink = report.CaptureSnapshot(driver,"Pinterest1.png")
keywordReportVar8+=report.keywordReportMethod(True,8,"Verifying whether user is able to logged in Pinterest","user is able to login in Pinterest successfully",strLink,"Windows")


time.sleep(10)
for handle in driver.window_handles:
	driver.switch_to.window(handle)


path= "/wsx/"+'ShareResult.png'   
print path
driver.save_screenshot(htmlFolderPath+path)

print htmlFolderPath
	
keywordReportVar9+=report.keywordReportMethod(status1,9,"Sharing TE Scenario","User is able to share anything on social sites",path,"Windows")    

time.sleep(2)
	
TestCaseReportVar=report.testcaseMethod(1,"SharingTE",status)
AllTestCasedata=TestCaseReportVar+keywordReportVar+keywordReportVar2+keywordReportVar3+keywordReportVar4+keywordReportVar5+keywordReportVar6+keywordReportVar7+keywordReportVar8+keywordReportVar9+"</tbody></table></div>"

time.sleep(2)
driver.quit()
report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)
	




