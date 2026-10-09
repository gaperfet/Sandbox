#Lezione su come fare l'encapsulation , per evitare la modifica di data della definizione classe
import math

class Vector2d:
    def __init__(self, r, phi):
        self._rr = float(r)      #aggiungo float per convertire l'input , se non si puo dara errore. per evitare input di stringe a un vettore
        self._phi = float(phi)
    #definizione variabili interne vettore:
    def r(self):
        return self._r
    def phi(self):
        return self._phi
    def x(self):
        return self._r * math.cos(self._phi)
    #varia il valore di r dal esterno
    def set_r(self,new_r):
       new_r = float(new_r)
       if new_r < 0:
           print('The radius cannot be negative')
       else:
           self._r = new_r
    #def abs(self):
     #   return math.sqrt(self.x**2 + self.y**2)

    def rotate_counter_Clock(theta):
        self.phi += theta

v=Vector2d(3.,1.)

print(v.v())
print(v._r,v._phi)
v.rotate_counter_Clock(0.5*math.pi)
print(v.r)
#print(v.abs())
