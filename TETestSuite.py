#Using Behaviour-driven development |Given-When-Then (GWT) technique
#Given that user should be able to submit the vote
#When user is loggedIn in Application
#Then Vote should be increased.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import report
import TEImageCaptureScript
htmlFolderPath="c:\\wwe\\"
url = "https://toughenough-2015-phase2-qa.jenkins.wwe.com/"
firefoxImageData = TEImageCaptureScript.firefoxInstance(url)
ieImageData = TEImageCaptureScript.internetExplorerInstance(url)


AllTestCasedata=firefoxImageData+ieImageData

#AllTestCasedata=AllTestCasedata+Search_Data

report.addTestCaseData("C:\\wwe\\dummy.txt",25,AllTestCasedata,htmlFolderPath)


