from maketashop.models import Maketa

class CartDTO():
    def __init__(self):
        self.inventory={}

    def getCart(self):
        return self.inventory

    def addMaketa(self, maketaID, kolicina):
        maketa = Maketa.objects.select_related.get(maketaid=maketaID)
        if maketa in self.inventory:
            self.inventory[maketa]=self.inventory[maketa]+kolicina
        else:
            self.inventory[maketa]=kolicina

    def removeMaketa(self, maketaID, kolicina):
        maketa = Maketa.objects.select_related.get(maketaid=maketaID)
        if maketa in self.inventory:
            self.inventory[maketa]=self.inventory[maketa]-kolicina
        if self.inventory[maketa]<=0:
            self.inventory.pop(maketa)
