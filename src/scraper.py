from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:

    def __init__(self, state):
        self.PATH = '..\\dep\\chromedriver.exe'
        self.url = f'https://ecos.fws.gov/ecp/report/species-listings-by-state?stateAbbrev={state}&statusCategory=Listed&s8fid=112761032792&s8fid=112762573902'
        self.options = Options()
        self.options.headless = True
        self.state = state.lower()
        self.driver = webdriver.Chrome(executable_path=self.PATH, options=self.options)
        self.driver.get(self.url)

    def set_table(self):
        check_box = self.driver.find_element_by_xpath('//*[@id="species-listings-by-state"]/div/div/div/div[1]/label/input')
        check_box.click()
        table_button = self.driver.find_element_by_xpath('//*[@id="species-listings-by-state-report"]/thead/tr/th[5]')
        table_button.click()
        print('table ready!')

    def get_table_list(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        table = soup.find_all('table')
        return table
    
    def get_col(self, col):
        dfs = pd.read_html(str(self.get_table_list()))
        df = pd.DataFrame(dfs[0])
        if col.lower() == 'common':
            return list(df['Common Name'])
        elif col.lower() == 'scientific':
            return list(df['Scientific Name'])
        else:
            return list(df['ESA Listing Status'])


        

