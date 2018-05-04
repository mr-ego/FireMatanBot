from ScraperThread import ScraperThread
from Bot import Bot

bot = Bot()
thread = ScraperThread('https://www.lfvbz.it/freiwillige-feuerwehren-im-einsatz.html', bot)
thread.start()
