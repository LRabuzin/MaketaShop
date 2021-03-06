from maketashop.models import Maketa

class CartItem():
    def __init__(self, maketaID, materijal, cijena):
        self.maketa=Maketa.objects.select_related().get(maketaid=maketaID)
        self.materijal=materijal
        self.cijena=cijena

    def getMaketa(self):
        return self.maketa

    def getMaketaId(self):
        return self.maketa.maketaid

    def getMaterijal(self):
        return self.materijal
    
    def getCijena(self):
        return self.cijena

    def getMedia(self):
        return self.maketa.mediaid.putdodatoteke
    
    def getIme(self):
        return self.maketa.ime

    def __eq__(self, obj):
        return isinstance(obj, CartItem) and obj.maketa == self.maketa and obj.materijal == self.materijal and obj.cijena == self.cijena

    def __hash__(self):
        return hash((self.maketa, self.materijal, self.cijena))

class CartDTO():
    def __init__(self):
        self.inventory={}
        self.suma=0
        self.brItema=0

    def getCart(self):
        return self.inventory

    def addMaketa(self, maketaID, materijal, cijena, kolicina):
        maketa = CartItem(maketaID, materijal, cijena)
        self.suma=self.suma + cijena * kolicina
        self.brItema=self.brItema+kolicina
        if maketa in self.inventory:
            self.inventory[maketa]=self.inventory[maketa]+kolicina
        else:
            self.inventory[maketa]=kolicina
        return self

    def removeMaketa(self, maketaID, materijal, cijena, kolicina):
        maketa = CartItem(maketaID, materijal, cijena)
        self.suma=self.suma - cijena * kolicina
        self.brItema-=kolicina
        if maketa in self.inventory:
            self.inventory[maketa]=self.inventory[maketa]-kolicina
        if self.inventory[maketa]<=0:
            self.brItema=self.brItema-self.inventory[maketa]
            self.suma=self.suma - cijena * self.inventory[maketa]
            self.inventory.pop(maketa)

    def removeSveOdMaketa(self, maketaID, materijal, cijena):
        maketa = CartItem(maketaID, materijal, cijena)
        if maketa in self.inventory:
            kolicina = self.inventory[maketa]
            self.suma = self.suma - cijena*kolicina
            self.brItema = self.brItema-kolicina
            self.inventory.pop(maketa)

    def getSuma(self):
        return self.suma

    def getDostava(self):
        return round(self.suma * 0.05,2)

    def getUkupno(self):
        return self.getDostava() + self.getSuma()

    def getBrItema(self):
        return self.brItema