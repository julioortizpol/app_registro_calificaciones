class Calculo:

  def __init__(self, notas):
    self._pr_practicas=self.c_promedio([notas.get_ppractica(), notas.get_spractica()])
    self._pr_foros=self.c_promedio([notas.get_pforo(), notas.get_sforo()])
    self._pr_parciales=self.c_promedio([notas.get_pparcial(), notas.get_sparcial()])
    self._pr_final=self.c_promediof([self.get_pr_parciales(), self.get_pr_practicas(),self.get_pr_foros(), notas.get_final()])
  #end ctr

  def c_promedio(self, notas):
    return (notas[0]+notas[1])/2 if (len(notas)==2) else (notas[0]+notas[1]+notas[2])/3
  #end method

  def c_promediof(self, notas):
    return (notas[0]+notas[1]+notas[2]+notas[3])/4
  #end method

  def get_pr_practicas(self):
    return self._pr_practicas
  #end method

  def get_pr_foros(self):
    return self._pr_foros
  #end method

  def get_pr_parciales(self):
    return self._pr_parciales
  #end method

  def get_pr_final(self):
    return self._pr_final
  #end method

  def get_literal(self):
    literal="F"
    if self._pr_final>60 and self._pr_final<70:
      literal="D"
    elif self._pr_final>70 and self._pr_final<80:
      literal= "C"
    elif self._pr_final>80 and self._pr_final<90:
      literal= "B"
    elif self._pr_final>90 and self._pr_final<=100:
      literal= "A"
    #end condition
    return literal
  #end method

  def _is_approved(self):
    return False if(self._pr_final<70) else True
  #end method
  
#end class