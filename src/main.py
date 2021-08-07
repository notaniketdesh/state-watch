from gui import Window
from scraper import Scraper

submit_page = Window(700, 400, "Endangered Species")
submit_page.create_submit_page()
submit_page.display()

scraper = Scraper(submit_page.state_name)
scraper.set_table()
scraper.get_table_list()

info_page = Window(1000, 500, f'Information for {submit_page.state_name.upper()}')
info_page.create_info_page()
info_page.display()


