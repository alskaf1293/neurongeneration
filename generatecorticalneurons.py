import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, x, y, z, angles):
        self.x = x
        self.y = y
        self.z = z
        self.angles = angles  # Angles in spherical coordinates (theta, phi)
        self.children = []  # List to hold child nodes

def generate_neuron_structure(root, steps=100, bifurcation_prob=0.005, angle_variance=10):
    if steps == 0:
        return
    
    last_node = root
    new_angles = (last_node.angles[0] + random.randint(-angle_variance, angle_variance),
                  last_node.angles[1] + random.randint(-angle_variance, angle_variance))
    
    # Generate a new node
    new_x = last_node.x + np.sin(np.radians(new_angles[1])) * np.cos(np.radians(new_angles[0]))
    new_y = last_node.y + np.sin(np.radians(new_angles[1])) * np.sin(np.radians(new_angles[0]))
    new_z = last_node.z + np.cos(np.radians(new_angles[1]))
    new_node = Node(new_x, new_y, new_z, new_angles)
    last_node.children.append(new_node)
    
    # Recursively generate more structure
    generate_neuron_structure(new_node, steps-1, bifurcation_prob, angle_variance)
    
    # Check for bifurcation
    if random.random() < bifurcation_prob:
        bifurcation_angles = (new_angles[0] + random.randint(-90, 90),
                              new_angles[1] + random.randint(-90, 90))
        bifurcation_x = new_x + np.sin(np.radians(bifurcation_angles[1])) * np.cos(np.radians(bifurcation_angles[0]))
        bifurcation_y = new_y + np.sin(np.radians(bifurcation_angles[1])) * np.sin(np.radians(bifurcation_angles[0]))
        bifurcation_z = new_z + np.cos(np.radians(bifurcation_angles[1]))
        bifurcation_node = Node(bifurcation_x, bifurcation_y, bifurcation_z, bifurcation_angles)
        last_node.children.append(bifurcation_node)
        
        # Recursively generate more structure
        generate_neuron_structure(bifurcation_node, steps-1, bifurcation_prob, angle_variance)

def plot_tree(root, ax):
    if not root.children:
        return
    for child in root.children:
        ax.plot([root.x, child.x], [root.y, child.y], [root.z, child.z], marker='o', color='b')  # 'b' sets the color to blue
        plot_tree(child, ax)

def generate_multiple_roots(num_roots=5):
    roots = []
    for _ in range(num_roots):
        root = Node(0, 0, 0, (random.randint(0, 360), random.randint(0, 180)))
        generate_neuron_structure(root)
        roots.append(root)
    return roots

def plot_multiple_trees(roots, ax):
    for root in roots:
        plot_tree(root, ax)

# Generate multiple initial roots
roots = generate_multiple_roots()

# Plot the neuron structures
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_multiple_trees(roots, ax)
plt.show()




