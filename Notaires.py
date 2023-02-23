from Toolkit import Toolkit
from NotairesEntry import NotairesEntry

class Notaires:
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = ["name","address","link", "phone", "mail", "language", "cabinetname"]

    def setPageMax(self, pageMax):
        self.nbPage = pageMax + 1
        return self
    
    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls

    def setEndpoints(self, soup):
        divs = soup.findAll('div', { "class": "text-end"})
        links = []
        for div in divs:
            a = div.find('a')
            try: 
                links.append(a['href'])
            except:
                pass
        self.endpoints = links
        self.endpoints =Toolkit.addBaseUrl(self.baseUrl, self.endpoints)
        return self.endpoints


    def getEndpoints(self):
        return self.endpoints

    def getFinalFieldNames(self):
        return self.finalFileNameFields
    def getInfoByPage(self, soup):

        fiches = []
        contacts = soup.findAll("div",{"class": "card"})
        contact1 = contacts[0]
        if contact1 is not None : 
            link = Toolkit.tryToCleanOrReturnBlank(contact1.find("div", {"class": "field--link"}))
            phone = Toolkit.tryToCleanOrReturnBlank(contact1.find("div", {"class": "field--telephone"}))
            language = Toolkit.tryToCleanOrReturnBlank(contact1.find("div", {"class": "field-spoken-languages"}))
            try :
                maildiv = contact1.find("div", {"class": "field--email"})
                mail = maildiv.find("a")["href"].replace("mailto:", "")
            except : 
                mail = ""
        contact2 = contacts[1]
        if contact2 is not None :
            cabinet = contact2.find("div", {"class": "office-sheet__address-wrap"})
            cabinetname = Toolkit.tryToCleanOrReturnBlank(cabinet.find("p"))
            address = Toolkit.tryToCleanOrReturnBlank(cabinet.find("div")).replace("\n", " ")
        name = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"class": "breadcrumb__current"}))
        fiche = NotairesEntry(name, address, link, phone, mail, language, cabinetname)
        fiches.append(fiche)
        self.result.extend(fiches)
        return fiches
    def getResult(self):
        return self.result

    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result