
import scraping


s = scraping.Scrapping()
try:
	r = s.scrap("Ideias Bring Solutions Lda")
	#r = s.scrap("HEMOVIDA Lda", 506036944)
	print (r)
except Exception as e:
	print (e)


