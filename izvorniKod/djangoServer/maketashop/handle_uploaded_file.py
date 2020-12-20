from datetime import datetime

def handle_uploaded_file(f, nastavak, brojac):

   path = 'maketashop/media/'
   path += datetime.utcnow().strftime("%m%d%Y%H%M%S") + str(brojac) + "." + nastavak

   with open(path, 'wb+') as destination:
      for chunk in f.chunks():
         destination.write(chunk)

   return path