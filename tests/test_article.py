from utilities.BaseClass import BaseClass
from PageObejcts.HomePage import HomePage
from PageObejcts.SingleArticleSide import SingleArticleSide


class TestArticle(BaseClass):

    def test_article(self):

        homePage = HomePage(self.driver)
        self.clickCookiesButton()
        randomArticle = homePage.getRandomArticleNum()
        articleNameBefore = homePage.getRandomArticleName(randomArticle)
        articleSide = homePage.clickRandomArticle(randomArticle)
        articleNameAfter = articleSide.getArticleHeading()
        assert articleNameBefore in articleNameAfter, "the articleheading are not equal."