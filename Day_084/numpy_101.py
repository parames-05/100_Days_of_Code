import numpy as np
import matplotlib.pyplot as plt

print("========== Challenge 1 ==========")
# Create array using arange
a = np.arange(10, 30)
print("Array a:")
print(a)


print("\n========== Challenge 2 ==========")
# Slicing operations

print("Last 3 values:")
print(a[-3:])

print("Interval between index 3 and 6:")
print(a[3:6])

print("All values except first 12:")
print(a[12:])

print("Every second value:")
print(a[::2])


print("\n========== Challenge 3 ==========")
# Reverse array

print("Reversed using flip():")
print(np.flip(a))

print("Reversed using slicing:")
print(a[::-1])


print("\n========== Challenge 4 ==========")
# Non-zero elements

b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)

print("Array b:")
print(b)

print("Indices of non-zero elements:")
print(nz_indices)

print("Non-zero values:")
print(b[nz_indices])


print("\n========== Challenge 5 ==========")
# Random 3D array

z = np.random.random((3,3,3))
print("Random 3x3x3 array:")
print(z)

print("Shape of z:")
print(z.shape)


print("\n========== Challenge 6 ==========")
# Linspace example

x = np.linspace(0, 100, num=9)
print("Linspace from 0 to 100 with 9 points:")
print(x)

print("Shape of x:")
print(x.shape)


print("\n========== Challenge 7 ==========")
# Plotting using linspace

y = np.linspace(start=-3, stop=3, num=9)

plt.figure()
plt.plot(x, y)
plt.title("Simple Line Plot using linspace")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()


print("\n========== Challenge 8 ==========")
# Random RGB image (noise)

noise = np.random.random((128,128,3))
print("Noise array shape:")
print(noise.shape)

plt.figure()
plt.imshow(noise)
plt.title("Random RGB Noise Image")
plt.axis('off')
plt.show()