from selenium.webdriver.common.by import By
import keyboard

class TestUtilities:

    def __init__(self, driver):
        self.driver = driver
        self.keyboard = keyboard

    def link_checker(self, link_text):
        page = self.driver.find_element(By.LINK_TEXT, link_text).click()
        pagetitle = self.driver.title
        assert pagetitle == page

    def clear_browser_data(self):
        from time import sleep
        self.driver.get('chrome://settings/clearBrowserData')
        sleep(3)
        self.keyboard.send("Enter")

    @staticmethod
    def logger():
        import logging
        import logging.handlers

        logger = logging.getLogger()
        logger.setLevel(logging.INFO) # set logger level

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") # set logger format

        filehandler = logging.FileHandler("C:/Python/Selenium/UTYourStore//Reports/logfile.log") # set file for logger log
        filehandler.setFormatter(formatter) # add format to filehandler

        stream_handler = logging.StreamHandler() # print log into the console
        stream_handler.setFormatter(formatter) # set log format in the console

        logger.addHandler(filehandler) # add object to logger
        logger.addHandler(stream_handler)

        return logger



