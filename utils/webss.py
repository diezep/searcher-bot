import os
from io import BytesIO
from discord import File

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class WebSS():

    def __init__(self, url):
        self.url = url

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('log-level=3')
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-fullscreen")

        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.driver.set_window_size(2048, 1365)

    def ofElement(self, search, xpath):

        self.driver.get(self.url)
        
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(xpath)).perform()
        _image = self.driver.find_element_by_xpath(xpath).screenshot_as_png
        imageBytes = BytesIO(_image)

        file = File(imageBytes, filename=f"{search}.png")
        # element = driver.find_element_by_xpath("//div[@id='hplogo']")
        #
        # location = element.location
        # size = element.size
        #.
        # driver.save_screenshot("/data/image.png")
        #
        # x = location['x']
        # y = location['y']
        # width = location['x'] + size['width']
        # height = location['y'] + size['height']
        #
        # im = Image.open('/data/WorkArea/image.png')
        # im = im.crop((int(x), int(y), int(width), int(height)))
        return file

    def close(self):
        self.driver.close()