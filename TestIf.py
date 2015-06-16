from selenium import webdriver
from selenium.selenium import selenium as SeleniumOne
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url="http://www.stage-qa.cloud.wwe.com/node/26026027"
driver = webdriver.Remote(desired_capabilities = DesiredCapabilities.FIREFOX)
sel = Selenium(host, port, '*webdriver', url)
sel.start(driver = driver)
