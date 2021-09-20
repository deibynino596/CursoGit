class coche():
  def _init_(self):

    self._largochasis=250
    self._anchochasis=120
    self._ruedas=4
    self._enmarcha=False
  
  def arrancar(self,arrancamos):
    self._enmarcha=True
    if(self._enmarcha):
      chequeo=self.chequeo_interno()

    if(self._enmarcha and chequeo):
      return "El coche esta en marcha"
    elif(self._enmarcha and chequeo==False):
      return "problemas en chequeo"
    else:
      return "El coche esta parado"

  def estado(self):
    print("El coche tiene", self._ruedas, "ruedas. Un ancho de ", self._anchochasis, "y un largo de ", self._largochasis)
  
  def chequeo_interno(self):
    print("relizando chequeo interno")
    self.gasolina="ok"
    self.aceite="ok"
    self.puertas="cerradas"

    if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
      return True
    else:
      return False

micoche=coche()
print(micoche.arrancar(True))
micoche.estado()

print("creamos el segundo objeto")
micoche2=coche()
print(micoche2.arrancar(False))
micoche2.estado()
#agregado al repo git pull
