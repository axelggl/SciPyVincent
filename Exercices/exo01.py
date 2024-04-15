# Utilisez scipy.io.loadmat pour lire un fichier MATLAB.mat fictif contenant les variables x et y. (Supposez que le fichier s'appelle data.mat). 

import scipy.io as sio

data = sio.loadmat('data.mat')
x = data['x']
y = data['y']

print("==== Variable x ====")
print(x)
print("==== Variable y ====")
print(y)