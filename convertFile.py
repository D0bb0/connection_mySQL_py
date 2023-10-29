class ConvertFile:
  def __init__(self,nVersion,oVersion,descripcion,habilitado):
    self.nVersion = nVersion
    self.oVersion = oVersion
    self.descripcion = descripcion
    self.habilitado = habilitado

  def getFile(self):
    with open('C:/Users/jvaldez/Documents/python/consultas.txt', 'r') as archivo :
      reemplazo = archivo.read()

    rp = {'{NEW_VERSION}':self.nVersion,'{OLD_VERSION}':self.oVersion,'{DESC_VERSION}':self.descripcion,'(HABILITADO)':self.habilitado}
    for x,i in rp.items():
      reemplazo = reemplazo.replace(x, i)

    return reemplazo

