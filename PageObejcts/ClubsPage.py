from selenium.webdriver.common.by import By
import random
from PageObejcts.SingleClubPage import SingleClubPage

COUNTALLCLUBS = 18
class Clubpage:
    def __init__(self,driver):
        self.driver = driver

    clubCards = (By.CSS_SELECTOR, ".clubs.grid club-card")
    clubName = (By.CSS_SELECTOR,".club")
    stadiumName = (By.CSS_SELECTOR,".content .stadium")

    def getAllClubCards(self):
        """
        Retrieves all clubs and returns them as a list.
        """

        allClubs = self.driver.find_elements(*Clubpage.clubCards)
        return allClubs

    def choiceArandomclub(self):
        """
        Selects a random club from the list of all clubs and returns it as a number.
        """

        allClubs = self.driver.find_elements(*Clubpage.clubCards)
        if allClubs:
            randomClub = random.randint(0, len(allClubs)-1)
            return randomClub
        else:
            print("The list is empty")


    def saveRandomClubInfos(self,randomClubNum):
        """
        Stores the name of the team and the stadium as text and returns it as a tuple.
        """

        allClubs = self.getAllClubCards()
        clubname = allClubs[randomClubNum].find_element(*Clubpage.clubName).text
        stadiumName = allClubs[randomClubNum].find_element(*Clubpage.stadiumName).text
        return clubname,stadiumName

    def clickRandomSingleClub(self,randomClubNum):
        """
        Clicks on the randomly selected team and creates an object of the class SingleClubPage.
        """

        allClubs = self.getAllClubCards()
        allClubs[int(randomClubNum)].click()
        singlePage = SingleClubPage(self.driver)
        return singlePage








