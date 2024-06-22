from selenium.webdriver.common.by import By



class SingleArticleSide:
    def __init__(self,driver):
        self.driver = driver

    articleHeading = (By.CSS_SELECTOR, "header h1")

    def getArticleHeading(self):
        """
        Retrieves the headline of the article and returns it as the return value.
        """

        return self.driver.find_element(*SingleArticleSide.articleHeading).text
