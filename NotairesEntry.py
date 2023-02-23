class NotairesEntry:
    def __init__(self,name,address,link, phone, mail, language, cabinetname):
        
        self.name = name
        self.address= address
        self.link = link
        self.phone = phone
        self.mail = mail
        self.language = language
        self.cabinetname= cabinetname


    def getDictEntry(self):
        return {
            "name":self.name,
            "address":self.address,
            "link":self.link,
            "phone":self.phone,
            "mail":self.mail,
            "language":self.language,
            "cabinetname":self.cabinetname
        }