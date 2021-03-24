import numpy as np

# ------------------ AUX -----------------------

def Expected(matrix, ket):
    first = np.matmul(matrix,ket)
    return np.dot(np.conjugate(first),ket)

def mean(matrix, expected):
    size = len(matrix)
    identity = np.identity(size)
    first = expected * identity
    return first

def HermitianOperator(matrix,expected):
    first = mean(matrix, expected)
    return matrix - first

def Nomalized(state):
    new = []
    long = np.linalg.norm(state)
    for i in range(len(state)):
        new.append(state[i]/long)
    return new

# ------------------ end AUX --------------------

# ----------------------------------- SIMULACION SISTEMA CUANTICO 4.1 -------------------------------------------------

#El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea.
# El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

# 1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
def Probabilities(vector, position):
    first = (vector[position])**2
    second = (np.linalg.norm(vector))**2
    return np.abs(np.real(first/second))

# 2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
def VecToVec(v1,v2):
    newv = np.conjugate(v2)
    return np.dot(newv,v1)

# --------------------------------- END SIMULACION SISTEMA CUANTICO 4.1 -----------------------------------------------

# --------------------------------- RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4 ----------------------------------------------

# 2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana,
# y si lo es, calcula la media y la varianza del observable en el estado dado.
def MatrixKet(matrix, ket):
    matrix1 = np.conjugate(np.transpose(matrix))
    a = Expected(matrix, ket)
    b = HermitianOperator(matrix, a)
    media = mean(matrix,a)
    c = np.matmul(b,b)
    d = np.matmul(np.conjugate(ket), c)
    variance = np.dot(d,ket)
    return variance, media

# 3.  El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de
# los vectores propios después de la observación.

def EigenvectorsProbability(matrix, state):
    probabilities = []
    values, vectors = np.linalg.eig(matrix)
    for i in range(len(vectors)):
        p = (np.dot(state, vectors[i]))**2
        probabilities.append(p)
    return values, probabilities

# 4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a
# partir de un estado inicial.

def FinalState(state, matrix):
    final = np.matmul(matrix,state)
    return list(final)

# --------------------------------------------- FUNCIONES ADICIONALES ------------------------------------------------

def ValueDistribution(matrix,state):
    values,probabilities = EigenvectorsProbability(matrix,state)
    a = values[0]*probabilities[0]
    b = values[1]*probabilities[1]
    return a + b

def VerifyUnitary(matrix):
    new = np.conjugate(np.transpose(matrix))
    a = np.matmul(new,matrix)
    b = np.matmul(matrix,new)
    size = len(matrix)
    identity = np.identity(size)
    if (a-b).all:
        if (a-identity).all:
            return True
    else:
        return False

# ---------------------------------------- END FUNCIONES ADICIONALES ---------------------------------------------------

def main():
    matrix = np.array([[0, 1 / 2 ** (1 / 2), 1 / 2 ** (1 / 2), 0],
                       [1j / 2 ** (1 / 2), 0, 0, 1 / 2 ** (1 / 2)],
                       [1 / 2 ** (1 / 2), 0, 0, 1j / 2 ** (1 / 2)],
                       [0, 1 / 2 ** (1 / 2), -(1 / 2 ** (1 / 2)), 0]])
    state = [1, 0, 0, 0]
    print(FinalState(state, matrix))


main()