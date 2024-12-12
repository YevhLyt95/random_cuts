import numpy as np
import matplotlib.pyplot as plt
#generate random hyperplane
def generate_random_hyperplane(dimensions):
    #generate random normal vector
    normal_vector = np.random.normal(size = dimensions)
    normal_vector /= np.linalg.norm(normal_vector) #normalisation
    #generate random shift
    offset = np.random.uniform(-1, 1)
    return normal_vector, offset

#example for 2D space
normal, offset = generate_random_hyperplane(2)
print(f"normal: {normal}, shift: {offset}")

#split data

def split_data(points, normal, offset):
    #calculate scalar product for every point
    distances = np.dot(points, normal) - offset
    #split data by distance sign
    left = points[distances < 0]
    right = points[distances >= 0]
    return left, right

# generate random data
data = np.random.uniform(-5, 5,(100, 2))
left, right = split_data(data, normal, offset)
#visualization
plt.scatter(left[:,0], left[:, 1], c = 'blue', label = 'Left')
plt.scatter(right[:, 0], right[:, 1], c = 'red', label = 'Right')
plt.axhline((0, offset), slope = -normal[0]/normal[1], color = 'green', label = 'Hyperplane')
plt.legend()
plt.show()