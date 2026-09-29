#PRIMA PARTE

import numpy as np

class Vector2d:
  #definizione della classe vettore 2d , il blueprint dei nuovi oggetti
    def __init__(self,x,y): #parametri self,x,y ,self è un parametro che vienen
                            # riempito automaticamente dentro al metodo che sto creando
        self.x=float(x)  #membri
        self.y=float(y)
  #classe di vettori che sono il quadrato di un altro vettore
    def norm(self):
      return np.sqrt(self.x**2.+self.y**2)

    # classe di vettori
    def __str__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"

    #funzione prodotto due vettori: classe di vettori che sono il prodotto di altri due.
    def dot(self,other:"Vector2d"):  # other sta dicendo che other è una altro oggetto del tipo vector2d , ci serve.
        return self.x * other.x + self.y * other.y


# IO voglio poter testare mentre scirvo il codice che stampi bene il vettore che sto definnendo.
# ma poi mentre lo uso effettivamento non voglio che stampi nulla. Sfrutto il fatto che python cambia il nome
# del modulo creato verso main , questo si chiamerebbe
 #Vector2d , lui lo richiama <__main__nome."numero casuale">
if __name__ == "__main__":   #v è l'instant
        n1=Vector2d(1.,0.)   #questa linea chiama il constructor , cioe lo script dove è definita la classe.
        print(n1)
        n2 = Vector2d(0., 1.)
        print(n2)
        print(n1.x,n1.y)
        print(n1.norm())
        print(n1.dot(n2))