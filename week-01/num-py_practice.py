import numpy as np

a1 = np.array([1, 2, 3, 4, 5])

a2 = np.array([[25,56],[55,34]])

a3 = np.array([[[12,41],[11,21]],[[31,88],[24,45]]])

# print(a1)
# print(a2)
# print(a3) 


### Numpy.fromiterable

my_list = [1, 2, 3, 4, 5]
updated_array = np.fromiter(my_list, dtype=int)
print(updated_array)