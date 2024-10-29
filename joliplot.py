import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([
    [2, 7, 7, 6, 11, 11, 11, 11],
    [2, 7, 6, 6, 6, 10, 11, 4],
    [2, 7, 7, 6, 10, 10, 10, 4],
    [2, 5, 5, 0, 0, 10, 4, 4],
    [2, 5, 5, 0, 0, 1, 4, 3],
    [8, 12, 5, 1, 1, 1, 9, 3],
    [8, 12, 12, 12, 1, 9, 9, 3],
    [8, 8, 8, 12, 9, 9, 3, 3]
])

plt.imshow(matrix, cmap="Set3")  
plt.xticks([])  0
plt.yticks([])
plt.show()
