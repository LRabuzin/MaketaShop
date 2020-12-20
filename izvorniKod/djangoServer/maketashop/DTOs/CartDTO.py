from maketashop.models import Maketa

class CartItem():
    def __init__(self, maketaID, materijal, cijena):
        self.maketa=Maketa.objects.select_related.get(maketaid=maketaID)
        self.materijal=materijal
        self.cijena=cijena

    def getMaketa(self):
        return self.maketa

    def getMaterijal(self):
        return self.materijal
    
    def getCijena(self):
        return self.cijena

    def __eq__(self, obj):
        return isinstace(obj, CartItem) and obj.maketa == self.maketa and obj.materijal == self.materijal and obj.cijena == self.cijena


class CartDTO():
    def __init__(self):
        self.inventory={}

    def getCart(self):
        return self.inventory

    def addMaketa(self, maketaID, materijal, cijena, kolicina):
        maketa = CartItem(Maketa.objects.select_related.get(maketaid=maketaID), materijal, cijena)
        if maketa in self.inventory:
            self.inventory[maketa]=self.inventory[maketa]+kolicina
        else:
            self.inventory[maketa]=kolicina

    def removeMaketa(self, maketaID, materijal, cijena, kolicina):
        maketa = CartItem(Maketa.objects.select_related.get(maketaid=maketaID), materijal, cijena)
        if maketa in self.inventory:
            self.inventory[maketa]=self.inventory[maketa]-kolicina
        if self.inventory[maketa]<=0:
            self.inventory.pop(maketa)
