from selenium.webdriver.common.by import By
import random



class MatchSide:
    def __init__(self,driver):
        self.driver = driver

    HomeTeamName = (By.CSS_SELECTOR, ".clubHome .d-lg-block")
    GuestTeamName = (By.CSS_SELECTOR, ".clubAway .d-lg-block")


    def getHomeTeamName(self):
        h2= self.driver.find_element(*MatchSide.HomeTeamName)
        return h2.find_element(By.TAG_NAME,"a").get_attribute("textContent")


    def getGuestTeamName(self):
        h2= self.driver.find_element(*MatchSide.GuestTeamName)
        return h2.find_element(By.TAG_NAME, "a").get_attribute("textContent")




