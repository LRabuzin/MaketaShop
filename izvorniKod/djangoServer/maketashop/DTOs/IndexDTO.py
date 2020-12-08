from maketashop.models import Prica

class IndexDTO():

    def __init__(self):
        self.price=Prica.objects.all().select_related()
    def getPrice(self):
        return self.price
