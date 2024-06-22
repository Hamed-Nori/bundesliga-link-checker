from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from TestData import TestData
from selenium.webdriver.common.by import By
import time

class NavigationPage:

    def __init__(self,driver):
        self.driver = driver



    locatorListURLs = ["Spielplan","Tabelle", "Clubs","Liveticker","60 Jahre Bundesliga",
                   "Videos","Tickets","Statistiken","Tabellenrechner","Awards","Spieler","FAQ", "Broadcaster"]
    loginButton = (By.CSS_SELECTOR,".account li")
    bl1Link = (By.CSS_SELECTOR,".competitions a.bl1")
    bl2Link = (By.CSS_SELECTOR,".competitions a.bl2")
    euroLink = (By.CSS_SELECTOR,"a.competition.euro")
    externLinkTextList = ["Bundesliga App", "Fantasy Manager", "#BundesligaWIRKT", "DFL"]
    vblLinLocator = (By.CSS_SELECTOR, "a.vbl")

    def checkNavigationsLink(self):

        for links in range(0, len(NavigationPage.externLinkTextList)):
            side = self.driver.find_element(By.LINK_TEXT, NavigationPage.externLinkTextList[links])
            side.send_keys(Keys.CONTROL + Keys.RETURN)


            handles = self.driver.window_handles
            new_tab = handles[-1]
            self.driver.switch_to.window(new_tab)
            time.sleep(1)
            actualURL = self.driver.current_url
            self.driver.close()
            originalTab = handles[0]
            self.driver.switch_to.window(originalTab)
            assert actualURL == TestData.externURL[
                links], f"The acutalURL: {actualURL} != expectedURL: {TestData.externURL[links]}"

        side = self.driver.find_element(*NavigationPage.vblLinLocator)
        side.send_keys(Keys.CONTROL + Keys.RETURN)
        handles = self.driver.window_handles
        new_tab = handles[-1]
        self.driver.switch_to.window(new_tab)
        time.sleep(1)
        actualURL = self.driver.current_url
        self.driver.close()
        originalTab = handles[0]
        self.driver.switch_to.window(originalTab)
        assert actualURL == TestData.vlbExternLink, f"The acutalURL: {actualURL} != expectedURL: {TestData.vlbExternLink}"


        for pages in range(0, len(NavigationPage.locatorListURLs)):

            self.driver.find_element(By.LINK_TEXT,NavigationPage.locatorListURLs[pages]).click()
            time.sleep(1.5)
            url = self.driver.current_url

            exceptedURL = TestData.ListURLNavigationPage[pages]
            assert exceptedURL == url, f"{url} != {exceptedURL}"

        self.driver.find_element(*NavigationPage.loginButton).click()
        time.sleep(2)
        url = self.driver.current_url
        time.sleep(1)
        assert url == TestData.LoginPageURL, f"{url} != {TestData.LoginPageURL}"
        self.driver.find_element(*NavigationPage.bl1Link).click()
        time.sleep(1)
        url = self.driver.current_url
        assert url == TestData.bl1PageURL, "The Bundesliga 1 URl is not equal"
        self.driver.find_element(*NavigationPage.bl2Link).click()
        time.sleep(1)
        url = self.driver.current_url
        assert url == TestData.bl2PageURL, "The Bzndesliga 2 URl is not equal"
        self.driver.find_element(*NavigationPage.euroLink).click()
        time.sleep(2)
        url = self.driver.current_url
        assert url == TestData.euroPageURL, f"{url} =! {TestData.euroPageURL}"
        self.driver.back()
        self.driver.back()

        return print("Test passed")
