from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestData import TestData
from selenium.webdriver.common.by import By
import time



class FooterPage:

    def __init__(self, driver):
        self.driver = driver

    locatorList = ["Rechtliche Hinweise", "Datenschutz", "Broadcaster","Jobs","Partner","Liveticker",
                   "Nutzungsbedingungen","Kontakt","Impressum","Spieler","Newsletter"]
    broadcasterLocator = (By.XPATH, "//ol//li//a[text()='Broadcaster']")

    footerCopyrightText = (By.CSS_SELECTOR,".footer-copyright p")
    def checkFooterLinks(self):
        """
        Checks all text links in the footer. Clicks on them and compares the expected URL with the actual URL.
        """

        footerText = self.driver.find_element(*FooterPage.footerCopyrightText).text
        assert "© 2024 DFL Deutsche Fußball Liga GmbH" in footerText

        for links in range(0, len(FooterPage.locatorList)):
            self.scrollDown()
            if links == 2:
                self.driver.find_element(By.CSS_SELECTOR,".footerNavigation ol li:nth-child(5) a").click()

            elif links == 3:

                jobsSide = self.driver.find_element(By.LINK_TEXT, FooterPage.locatorList[links])
                jobsSide.send_keys(Keys.CONTROL + Keys.RETURN)

                handles = self.driver.window_handles
                new_tab = handles[-1]
                self.driver.switch_to.window(new_tab)
                time.sleep(1)
                actualURL = self.driver.current_url
                self.driver.close()
                originalTab = handles[0]
                self.driver.switch_to.window(originalTab)
                assert actualURL == TestData.listURLFooter[links], f"The acutalURL: {actualURL} != expectedURL: {TestData.listURLFooter[links]}"
                continue
            elif links == 7: # The contact page has an iframe
                self.driver.find_element(By.LINK_TEXT, FooterPage.locatorList[links]).click()
                iFrame = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".usabilla_scroller_area iframe")))
                self.driver.switch_to.frame(iFrame)
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, "#contents a:nth-child(1)").click()
                self.driver.switch_to.default_content()


            else:
                self.driver.find_element(By.LINK_TEXT, FooterPage.locatorList[links]).click()
            time.sleep(1)
            actualURL = self.driver.current_url
            expectedurl = TestData.listURLFooter[links]
            assert actualURL == expectedurl, f"{actualURL} != {expectedurl}"



    def scrollDown(self):
        """
        Scrolls from the webpage to the footer area.
        """

        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True

