from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import report

url="http://www.stage-qa.cloud.wwe.com/inside/polls/which-superstar-do-you-most-enjoy-get-an-rko-outta-nowhere"
htmlFolderPath="c:\\temp\\"

driver = webdriver.Firefox()
webElements = driver.find_element_by_xpath("//*[@id='questions']/div/div/div[1]/a")
webElements.click()

driver.delete_all_cookies()

webElements = driver.find_element_by_xpath("//*[@id='submit']")
webElements.click()
time.sleep(5)

driver = webdriver.Firefox()

#driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(30)
driver.maximize_window()

report.CaptureSnapshot(driver,"Voting.png")