from utilities.BaseClass import BaseClass
from PageObejcts.HomePage import HomePage


class TestClubs(BaseClass):


    def test_clubs(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        self.clickCookiesButton()
        clubObject = homePage.getClubsSide()
        randomClubNum = clubObject.choiceArandomclub()
        randomClubName, randomclubStadium = clubObject.saveRandomClubInfos(randomClubNum)
        singlePage = clubObject.clickRandomSingleClub(randomClubNum)
        singleClubName,singleClubStadium = singlePage.getSingleClubInfos()

        assert randomclubStadium == singleClubStadium, "The stadium name are not equal"
        assert randomClubName == singleClubName, "Clubname are not equal"
        print(f"{singleClubName}={randomClubName}")
        print(f"{singleClubStadium}=={randomclubStadium}")

