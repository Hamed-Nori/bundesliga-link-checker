from selenium.webdriver.common.by import By
import time

class SingleClubPage:
    def __init__(self,driver):
        self.driver = driver

    clubName = (By.CSS_SELECTOR,"header h1")
    stadiumName = (By.CSS_SELECTOR,"span.stadiumName")

    def getSingleClubInfos(self):
        """
        Stores the name of the team and the name of their stadium.
        """

        time.sleep(0.5)
        clubname = self.driver.find_element(*SingleClubPage.clubName).text
        stadiumName = self.driver.find_element(*SingleClubPage.stadiumName).text
        return clubname,stadiumName



