from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import time

class Scraper:

    def __init__(self, state):
        self.PATH = '..\\dep\\chromedriver.exe'
        self.options = Options()
        self.options.headless = True

        self.driver = webdriver.Chrome(executable_path=self.PATH, options=self.options)
        self.driver.get(f'https://ecos.fws.gov/ecp/report/species-listings-by-state?stateAbbrev={state}&statusCategory=Listed&s8fid=112761032792&s8fid=112762573902')

    

        

