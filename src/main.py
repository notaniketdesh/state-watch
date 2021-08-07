from gui import Window
from scraper import Scraper

submit_page = Window(700, 400, "Endangered Species")
submit_page.create_submit_page()
submit_page.display()

scraper = Scraper(submit_page.state_name)
scraper.set_table()

info_page = Window(900, 350, f'Information for {submit_page.state_name.upper()}')
info_page.create_info_page(scraper)
info_page.display()


