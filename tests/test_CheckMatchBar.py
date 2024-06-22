from utilities.BaseClass import BaseClass
from PageObejcts.HomePage import HomePage
import time


class TestOne(BaseClass):

    def test_first(self):
        """
This test starts on the homepage of the Bundesliga. Under the header, there is a match bar for the Euro 2024.
This test compares match information on the homepage with match information after clicking on the match.
The names of both teams are compared: the guest team and the host team.
"""

        self.clickCookiesButton()
        homePage = HomePage(self.driver)
        match = homePage.choiceAMatch()
        print(match)
        homeTeamName = homePage.getHomeTeamName(match)
        guestTeamName = homePage.getGuestTeamName(match)
        matchSide = homePage.clickMatchLink(match)
        homeTeamNameAfter = matchSide.getHomeTeamName()
        guestTeamNameAfter = matchSide.getGuestTeamName()

        assert homeTeamName == homeTeamNameAfter, "The Home-Team Names are not equal"
        assert guestTeamName == guestTeamNameAfter, "The Guest-Team names are not equal"





