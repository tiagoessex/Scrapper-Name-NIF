
import scraping


s = scraping.Scrapping()	

try:
	# randomize the order of the services
	r = s.scrap("Dom Digital - Novas Tecnologias De Informação, Lda.")
	# don't randomize the order of the services
	r = s.scrap("Dom Digital - Novas Tecnologias De Informação, Lda.", randomize = True)
	print (r)
except Exception as e:
	print (e)


