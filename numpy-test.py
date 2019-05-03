import numpy as np
my_list = [1,2,3,4,5,6,7,8,9,10]

my_array = np.array(my_list)


my_matrix_1= [[1,2,3],[4,5,6],[7,8,9]]
my_2d_array = np.array(my_matrix_1)

my_matrix_2 = np.arange(0,10)
my_matrix_3 = np.arange(0,10,2)

my_matrix_4= np.zeros( (5,5) )

my_linspace = np.linspace(0,5,10)

my_identity_matrix = np.eye(4)

print(my_identity_matrix)
