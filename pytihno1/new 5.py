import numpy as np
import matplotlib.pyplot as plt

# Generate a 100x100 array of random numbers from 0 to 10
array = np.random.randint(0, 11, size=(100, 100))

# Create a color chart using matplotlib
plt.imshow(array, cmap='viridis')
plt.colorbar()

# Add labels and title to the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Color Chart')

# Display the plot
plt.show()
