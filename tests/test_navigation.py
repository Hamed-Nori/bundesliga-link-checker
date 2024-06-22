from utilities.BaseClass import BaseClass
from PageObejcts.NavigationPage import NavigationPage
from PageObejcts.FooterPage import FooterPage

class TestNavigation(BaseClass):

    def test_navigationHomePage(self):
        self.clickCookiesButton()
        navigationPage = NavigationPage(self.driver)
        navigationPage.checkNavigationsLink()
        footerPage = FooterPage(self.driver)
        footerPage.checkFooterLinks()


