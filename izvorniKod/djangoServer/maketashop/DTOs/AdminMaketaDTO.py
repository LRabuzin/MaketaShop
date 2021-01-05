from maketashop.models import Materijal

class AdminMaketaDTO():

      def __init__(self):
         self.materijali = Materijal.objects.select_related().all()
      
      def getMaterijale(self):
         imena = [materijal.ime for materijal in self.materijali]
         return imena 