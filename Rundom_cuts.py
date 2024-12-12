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
#blue and red symbolized different parts of data
plt.axhline(y=offset, color='green', label='Hyperplane')
#Hyperplane slope is determined by a random normal vector, and its offset is a random value within given limits.
plt.legend(loc = 'lower left')
plt.show()
# creating random forest of cuts anda data clasterization
class RandomCutTree:
    def __init__(self, depth = 0):
        self.left = None
        self.right = None
        self.normal = None
        self.offset = None
        self.depth = depth
    def fit(self, points):
        if len(points) <= 1 or self.depth > 10: #depth constraints
            return
        #generate random hyperplane
        dimensions = points.shape[1]
        self.normal, self.offset = generate_random_hyperplane(dimensions)
        #splitting the data
        left_points, right_points = split_data(points, self.normal, self.offset)
        #creating recursion tree
        self.left = RandomCutTree(self.depth + 1)
        self.right = RandomCutTree(self.depth + 1)
        self.left.fit(left_points)
        self.right.fit(right_points)
    def predict(self, point):
        if self.left is None and self.right is None:
            return self.depth #depth as "score"
        distance = np.dot(point, self.normal) - self.offset
        if distance < 0:
            return self.left.predict(point)
        else:
            return self.right.predict(point)

#example of work
tree = RandomCutTree()
tree.fit(data)
#points score
scores = [tree.predict(point) for point in data]

#visualization
plt.scatter(data[:, 0], data[:, 1], c = scores, cmap = 'viridis')
plt.colorbar(label = 'Depth Score')
plt.show()
#lighter points are closer to the root - along or anomaly