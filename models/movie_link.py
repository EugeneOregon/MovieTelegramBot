import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver


class Movie:
    PATH = r"\movie telegrambot\models\chromedriver.exe"

    def __init__(self):
        self.driver = None

    def get_movie(self, url):
        self.driver = webdriver.Chrome(executable_path=self.PATH)
        self.driver.get(url)
        self.get_film()
        links = []
        for request in self.driver.requests:
            if request.response:
                if '.mp4:hls:manifest.m3u8' in request.url:
                    link = request.url.replace(':hls:manifest.m3u8', '')
                    links.append(link)
        self.driver.close()
        self.driver.quit()
        return links[-1]

    def establish_quality(self):
        self.click_element_by_xpath('//*[@id="oframecdnplayer"]/pjsdiv[15]/pjsdiv[3]')
        self.click_element_by_xpath('//*[@id="oframecdnplayer"]/pjsdiv[22]/pjsdiv[1]/pjsdiv/pjsdiv[1]')
        self.click_element_by_xpath('//*[@id="oframecdnplayer"]/pjsdiv[22]/pjsdiv[1]/pjsdiv/pjsdiv[7]')

    def click_element_by_xpath(self, path_element):
        self.driver.find_element(By.XPATH, path_element).click()
        time.sleep(3)

    def click_element_by_class_name(self, class_name_element):
        voice_acting_list = self.driver.find_elements('class name', class_name_element)
        voice_acting = []
        dubbing = []
        hdrezka = []
        for item in voice_acting_list:
            if item.text == 'Дубляж':
                dubbing.append(item)
            elif item.text == 'HDrezka Studio':
                hdrezka.append(item)
            else:
                voice_acting.append(item)

        if len(hdrezka) > 1:
            hdrezka[1].click()
        if len(hdrezka) < 1 <= len(dubbing):
            dubbing[0].click()
        else:
            voice_acting[0].click()
        time.sleep(3)

    def click_element_by_id(self, id_element):
        self.driver.find_element('id', id_element).click()
        time.sleep(15)

    def voice_acting(self):
        try:
            self.click_element_by_class_name('b-translator__item')
        except IndexError as err:
            print(err)

    def push_player(self):
        self.click_element_by_id('cdnplayer')

    def get_film(self):
        self.establish_quality()
        self.voice_acting()
        self.push_player()
