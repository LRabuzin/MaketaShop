from datetime import datetime
from django.templatetags.static import static
def handle_uploaded_text(f, brojac):

   path = 'maketashop/media/'
   path += datetime.utcnow().strftime("%m%d%Y%H%M%S") + str(brojac) + ".txt"


   fajl = open(path, 'w')
   fajl.write(f)
   fajl.close()

   return path