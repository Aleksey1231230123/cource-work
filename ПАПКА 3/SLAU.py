import numpy as np
for i in range(1,6):
    file = "SLAU" + str(i) + ".csv"
    m = np.genfromtxt(file, delimiter=';')
    A = np.genfromtxt(file, delimiter=';', usecols=(range(len(m-1))))
    B = np.genfromtxt(file, delimiter=';', usecols=(len(m)))
    slau = np.linalg.solve(A, B)
    print("ответ к задаче " + str(i), slau)