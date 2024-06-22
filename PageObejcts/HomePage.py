import time
from selenium.webdriver.common.by import By
import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObejcts.MatchSide import MatchSide
from PageObejcts.SingleArticleSide import SingleArticleSide
from PageObejcts.ClubsPage import Clubpage
from TestData import TestData


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    sliderMatchBarRight = (By.CSS_SELECTOR, ".matchbar-tournament  .sliderNaviRight")
    matchFixture = (By.CSS_SELECTOR, ".swiper-slide match-fixture")
    TeamNames = (By.CSS_SELECTOR, ".swiper-slide match-fixture span")
    matchLinks = (By.CSS_SELECTOR, "a.tile__match")
    contactPageIFrameexitButton = (By.CSS_SELECTOR, "matchbar-tournaments .sliderNaviRight")
    mostSharedArticles = (By.CSS_SELECTOR,".mostshared dfl-top-list")
    headingMostSharedArticles = (By.CSS_SELECTOR, "span")
    navLinkClubs = (By.LINK_TEXT,"Clubs")

    def getClubsSide(self):
        """
        Navigate from the homepage to the club page via the navigation in the header.
         An object of ClubPage is returned as the return value.
        """

        self.driver.find_element(*HomePage.navLinkClubs).click()
        clubObject = Clubpage(self.driver)
        return clubObject



    def getMatchFixture(self):
        """
        Saves all elements of the Euro 2024 match bar into a list and returns it.
        """

        try:
            slider_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".matchbar-tournament .sliderNaviRight"))
            )


            while True:
                try:

                    if not slider_element.is_displayed():
                        break

                    slider_element.click()
                    time.sleep(0.5)
                except Exception as e:

                    print(f"Error during interaction: {e}")
                    break

            print("The slider element is no longer visible or an error has occurred..")

        except Exception as e:
            print(f"Error finding the slider element: {e}")

        allNames = self.driver.find_elements(*HomePage.matchFixture)
        return allNames

    def choiceAMatch(self):
        """
        Selects a random number from the match bar list and returns it as the return value.
        """

        allMatches = self.getMatchFixture()
        if allMatches:
            match = random.randint(0, len(allMatches) - 1)
            return match

        else:
            raise Exception("No matches found")

    def getHomeTeamName(self,match):
        """
        From a randomly selected match, retrieves and stores the name of the host team as text.
        """

        list = self.getMatchFixture()
        HomeTeam = list[match].find_elements(*HomePage.TeamNames)
        assert len(HomeTeam) == 2, "The Team number is greater than two"
        return HomeTeam[0].get_attribute("textContent")

    def getGuestTeamName(self,match):
        """
        From a randomly selected match, retrieves and stores the name of the guest team as text.
        """

        list = self.getMatchFixture()
        guestTeam = list[match].find_elements(*HomePage.TeamNames)
        assert len(guestTeam) == 2, "The Team number is greater than two"
        return guestTeam[1].get_attribute("textContent")

    def clickMatchLink(self,match):
        """
        Clicks on the randomly selected Euro 2024 match.
        """

        list = self.driver.find_elements(*HomePage.matchLinks)
        list[match].click()
        time.sleep(0.5)
        matchSide = MatchSide(self.driver)
        return matchSide


    def getRandomArticleNum(self):
        """
        Identifies the most read articles on the homepage and selects one randomly from a list.
        """

        articleNum = self.driver.find_elements(*HomePage.mostSharedArticles)
        return random.randint(0, len(articleNum) - 1)

    def getRandomArticleName(self,articlenum):
        """
        From a randomly selected article, retrieves the headline of the article on the homepage and returns it as text.
        """

        list = self.driver.find_elements(*HomePage.mostSharedArticles)
        heading = list[articlenum].find_element(*HomePage.headingMostSharedArticles).text
        return heading

    def clickRandomArticle(self, articleNum):
        """
        Clicks on a randomly selected article and lands on the article page. Creates an object of the class mArticleSide.
        """

        articles = self.driver.find_elements(*HomePage.mostSharedArticles)
        articles[articleNum].click()
        #time.sleep(3)
        articleSide = SingleArticleSide(self.driver)
        return articleSide










