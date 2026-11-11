# first neural network with keras tutorial :problema di classificazione binaria: dai dati clinici,
# la rete deve prevedere se svilupperà il diabete.
# I dati: pazienti donne di origine Pima, di almeno 21 anni, totale di 768 righe.
# Ogni riga ha 8 variabili di input (le colonne 0-7, cioè X) e un’etichetta (la colonna 8, cioè y).
# 8 variabili: numero di gravidanze, glucosio nel plasma dopo un test di tolleranza orale,
# pressione diastolica, spessore della piega cutanea del tricipite, insulina sierica, indice di massa corporea (BMI),
# funzione di “pedigree” del diabete (un indice di familiarità) ed età.
# L’etichetta y: si tratta di prevedere l’insorgenza del diabete entro 5 anni.
# Il valore 1 indica che la paziente è risultata positiva, 0 che non lo è.
# La rete impara una funzione che trasforma le 8 misure in una probabilità (l’uscita sigmoide, tra 0 e 1).
# L’accuratezza del 76% è la frazione di pazienti per cui la classe prevista, cioè probabilità sopra 0,5, coincide con quella reale.
import os
os.environ["KERAS_BACKEND"] = "torch"    #aggiunto per processori vecchi su cui non va tensorflow
from numpy import loadtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Input
# load the dataset
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Input(shape=(8,)) )
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
y_pred = (model.predict(X) > 0.5).astype(int).ravel()
#pazienti sane riconosciute (TN), sane scambiate per malate (FP),
# malate non riconosciute (FN), malate riconosciute (TP).
TP = np.sum((y_pred == 1) & (y == 1))
TN = np.sum((y_pred == 0) & (y == 0))
FP = np.sum((y_pred == 1) & (y == 0))
FN = np.sum((y_pred == 0) & (y == 1))

print('TN:', int(TN), ' FP:', int(FP))
print('FN:', int(FN), ' TP:', int(TP))
print('Recall: %.2f' % (TP / (TP + FN) * 100))  #frazione di pazienti realmente diabetiche che la rete individua