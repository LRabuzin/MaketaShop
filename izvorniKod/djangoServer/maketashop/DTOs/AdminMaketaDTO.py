from maketashop.models import Materijal

class AdminMaketaDTO():

      def __init__(self, request):
         self.materijali = Materijal.objects.select_related().all()
      
      def getMaterijale(self):
         return self.materijali