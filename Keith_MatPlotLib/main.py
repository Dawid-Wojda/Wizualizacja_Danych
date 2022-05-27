import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x = [0, 1, 2, 3, 4]
# y = [0, 2, 4, 6, 8]

# Resize your Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
# plt.figure(figsize=(5, 3), dpi=150)

# Line 1

# Keywordd Argument Notation
# plt.plot(x, y, label='2x', color='red', linewidth='2', linestyle='--', marker='.', markersize='10', markeredgecolor='blue')

# Use shorthand notation
# fmt = '[color][marker][line]'
# plt.plot(x, y, 'b^--', label='2x')

# Line 2

# Select interval we want to points at
# x2 = np.arange(0, 4.5, 0.5)

# Plot part of the graph as line
# plt.plot(x2[:6], x2[:6] ** 2, 'r', label='x^2')

# Plot part remainder of graph as a dot
# plt.plot(x2[5:], x2[5:] ** 2, 'r--')

# Add a title (specify parameters with fontdict)
# plt.title('Our First Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y Labels
# plt.xlabel('X Axis!')
# plt.ylabel('Y Axis!')

# X, Y axis tickmarks (scale of your graph)
# plt.xticks([0, 1, 2, 3, 4])
# plt.yticks([0, 2, 4, 6, 8])

# Add a legend
# plt.legend()

# Save figure (dpi 300 is good when saving so graph has high resolution
# plt.savefig('mygraph.png', dpi=1000)

# Show plot
# plt.show()

### BAR CHART

labels = ['A', 'B', 'C']
values = [1, 4, 2]

bars = plt.bar(labels, values)

bars[0].set_hatch('/')
bars[1].set_hatch('O')
bars[2].set_hatch('*')

plt.figure(figsize=(6, 4))

plt.show()
