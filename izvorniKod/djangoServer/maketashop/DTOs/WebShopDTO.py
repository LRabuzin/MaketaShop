from maketashop.models import Maketa
from maketashop.models import Napravljenaod
from maketashop.DTOs.MaketaDTO import MaketaDTO

class WebShopDTO():
    def __init__(self):
        self.makete=Maketa.objects.all().select_related()
        self.sveMakete=[]
        for maketa in self.makete:
            if maketa.vrsta.ime =='webshop':
                self.sveMakete.append(MaketaDTO(maketa.maketaid))
    def getMakete(self):
        return self.sveMakete