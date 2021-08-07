from gui import Window
from scraper import Scraper

window = Window(700, 400, "Endangered Species")
window.create_submit_page()
window.display()

test = Scraper('NJ')

