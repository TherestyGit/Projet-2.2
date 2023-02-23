from Scraper import Scraper
from Notaires import Notaires

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.notaires.fr'
uri =  "/fr/directory/notaries?location=10000%20Troyes&lat=48.292817&lon=4.075149&locality=Troyes&postal_code=10000&search_id=QdYj8JNWzV6f3ixEpIueMaPxKw9jrT8Ic7ZbBfA4nXg&page="

notInst = Notaires(baseUrl, uri, 0)
notInst2 = Notaires(baseUrl, uri, 1)
notInst3 = Notaires(baseUrl, uri, 2)
notInst4 = Notaires(baseUrl, uri, 3)
notInst5 = Notaires(baseUrl, uri, 4)


scraper = Scraper(notInst, "linksList1.csv", "infosp1.csv")
scraper2 = Scraper(notInst2, "linksList2.csv", "infosp2.csv")
scraper3 = Scraper(notInst3, "linksList3.csv", "infosp3.csv")
scraper4 = Scraper(notInst4, "linksList4.csv", "infosp4.csv")
scraper5 = Scraper(notInst5, "linksList5.csv", "infosp5.csv")


scraper.exec()
scraper2.exec()
scraper3.exec()
scraper4.exec()
scraper5.exec()

print("Done")