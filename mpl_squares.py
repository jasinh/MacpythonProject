import matplotlib.pyplot as plt
input_values=[1, 2, 3, 4, 5,6,7,8,9,10]
squares = [1, 4, 9, 16, 25,26,27,18,19,10]
print(plt.style.available)
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(input_values,squares)
ax.set_title("PFS", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value'2", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()
