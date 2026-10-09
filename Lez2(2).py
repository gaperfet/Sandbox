#Lezione su uso @property
import math

class Vector2d:
    def __init__(self, r, phi):
        self._rr = float(r)      #aggiungo float per convertire l'input , se non si puo dara errore. per evitare input di stringe a un vettore
        self._phi = float(phi)

    #definizione variabili interne vettore:
         #serve per quando in un programma senza enpasulation fin dall'inizio, voglio aggiungere la protezione variavili dopo..?
                 # l'uso è nelle slides ->capire perche è piu "naturale"
    @property
    def r(self):
        return self._r
    #varia il valore di r dal esterno
    @r.setter
    def set_r(new_r):
       self._r = float(new_r)
    @property
    def x(self):
        return self._r * mathcos(self._phi)
    @property
    def y(self):
        return self._r * mathsin(self._phi)
    #se no provvedo questo @x.setter per l'atributo , da attribute error.. , posso aggiungere il printf (magari con un if )piu sotto
    # per far sapere al user del problema specifico
    @x.setter
    def x(self,x):
        #print('Error x is read only')
        new_r =math.sqrt(self.y**2 + self.x**2)
        new_phi =math.atan2(self.y,x)
        self._r = new_r
        self._phi = new_phi

v=Vector2d(3.,0.5math.phi)
v.x = 5
print(v.x)
