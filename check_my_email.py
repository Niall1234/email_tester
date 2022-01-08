from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import sys

if len(sys.argv) < 2:
	print("Usage: type an email address")
	sys.exit()
	
opts = Options()

opts.headless = True
assert opts.headless

browser = Firefox(executable_path="/root/.local/bin", options=opts)
browser.get("http://ismyemailworking.com")
input_elem = browser.find_element_by_id("verify_email")
input_elem.send_keys(sys.argv[1])
input_button = browser.find_element_by_id("content_cob_check")
input_button.click()
print("checking %s" % sys.argv[1])


browser.close()
print("browser closed")
print("Check your inbox. You should have an email with the subject 'Email Test'")
