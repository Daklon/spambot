from splinter import Browser

class Caller:
    
    def call_genesis(self,number):
        with Browser() as browser:
            url = "https://te-llamamos.genesis.es/user-details"
            browser.visit(url)
            browser.find_by_id('onetrust-accept-btn-handler').first.click()
            browser.find_by_id('primaryPhoneInput').first.fill(str(number))
            browser.find_by_id('continueButton').first.click()

