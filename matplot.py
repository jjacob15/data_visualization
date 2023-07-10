import matplotlib.pyplot as plt
from collections import Counter
import random
r = range(1,6)
input_values = [i for i in r]
squares = [i**2 for i in r]

fig,ax = plt.subplots(figsize=(10,6),dpi=128)

ax.plot(input_values,squares,  linewidth=3)
ax.scatter(2,15)
# plt.show()
# plt.savefig("plot.jpg",bbox_inches="tight")

r = [random.randint(1,6) for i in range(100)]
print(Counter(r))