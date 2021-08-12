from matplotlib import pyplot as plt
import math
x_values=range(1,1001)

y_values=[x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax=plt.subplots()
ax.scatter(x_values,y_values, c='green',s=2)
ax.axis=(0,110,0,1100000)
ax.set_title('PFS',fontsize=20)
ax.set_xlabel('value',fontsize=14)
ax.set_ylabel("vlaue'2",fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=10)
plt.show()