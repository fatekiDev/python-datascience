import numpy as np # <-- libreria especializada en operaciones matemáticas, incluso en operaciones de vectores y matrices. | Su estructura de datos especializada se llama ndarray (array/arreglos).

array1 = np.array([1, 2, 3]) # <-- esto sería un array a partir de una lista.

# ahora lo haremos con una matriz de tipo ndarray
matriz = np.array([[1, 2, 3],
                  [4 ,5 ,6 ]]) # matriz de 2x3

# consultando su dimension
print(f"Dimension de la matriz: {matriz.shape}")

print(f"Total de filas: {len(matriz)}")

# accediendo a los datos de la primera fila
print(f"Datos de primera fila {matriz[0]}")

# Ahora de manera más exacta
print(f"Tercer elemento de la segunda fila {matriz[1][2]}") # OJO con el orden de los index

#Uso del Slicing
print(matriz[:, 1]) # Acá estamos en la segunda columna de la matriz y el ":" (Toma todas las filas)

matriz2 = ([[7,8,9],
            [10, 11, 12]])

print(f"Suma convencional de matrices \n {matriz + matriz2} \n")

# Operaciones que podemos hacer con numpy

matrices_concatenadas = np.concatenate([matriz, matriz2])
print(matrices_concatenadas)

array10 = np.arange(11)
print(array10)

# Funciones aritmeticas sobre los arrays
print(f"Array hasta el 10 elevado a 2: {array10**2}")
print(f"Promedio de la matriz: {np.mean(matriz)}")
print(f"Mediana: {np.median(matriz)}")
print(f"Valor máximo de la matriz: {np.max(matriz)}")
print(f"Valor mínimo de la matriz: {np.min(matriz)}")

#matriz trasoyesta
print(f"matriz traspuesta: \n {matriz.T}")

array10 = np.arange(1,11)
boolean_list = [True] * len(array10) # acá estamos haciendo un enmascaramiento

# eliminando especificamente valores del array
boolean_list[9] = False # elimino el valor con el index de posicion 9 (osea el 10)

print(array10[boolean_list]) # este tiene el valor 10 eliminado

# Ocupando la técnica del enmascaramiento para tomar los valores pares
print(f"Array principal:\n {array10}")
mascara = array10 % 2 == 0
print(f"Mascara: \n {mascara}")
impares = array10[mascara]
print(f"Números pares: \n {impares}")