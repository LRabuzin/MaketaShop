from maketashop.models import Maketa

class WebShopDTO():
    def __init__(self):
        self.makete=Maketa.objects.all().select_related()
    def getMakete(self):
        return self.makete