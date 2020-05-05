# %%

import matplotlib.pyplot as plt

# %%
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.1, 0.2, 0.5, 0.6, 0.8, 0.8, 0.9, 1.2, 1.5, 1.8]
plt.plot(x, y)
plt.savefig('plottest.png')
