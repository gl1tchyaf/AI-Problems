import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Advertising.csv")
y = data['Sales']
x = np.column_stack((data['Radio'], data['TV']))
print(x, y)
type(x)
type(y)
scaler = StandardScaler()
x_scaling = scaler.fit_transform(x)
print(x_scaling)


def gradient_descent(W, x, y):
    y_hat = x.dot(W).flatten()
    error = (y - y_hat)
    mse = (1.0 / len(x)) * np.sum(np.square(error))
    gradient = -(1.0 / len(x)) * error.dot(x)
    return gradient, mse


w = np.array((-40, -40))
alpha = 0.1
threshold = 1e-3

old_w = []
errors = []

iterations = 1
for i in range(200):
    gradient, error = gradient_descent(w, x_scaling, y)
    new_w = w - alpha * gradient

    if iterations % 10 == 0:
        print("Iteration : %d - Error: %.4f" % (iterations, error))
        old_w.append(new_w)
        errors.append(error)

    if np.sum(abs(new_w - w)) < threshold:
        print("Converged")
        break

    iterations += 1
    w = new_w

print("W = ", w)

ws = np.array(old_w)
errors.append(600)
errors.append(500)
errors.append(400)
errors.append(300)
errors.append(325)
errors.append(225)

levels = np.sort(np.array(errors))

w0 = np.linspace(-w[0]*5, w[0]*5, 100)
w1 = np.linspace(-w[1]*5, w[1]*5, 100)
e_vals = np.zeros(shape=(w0.size, w1.size))

for i , val1 in enumerate(w0):
    for j, val2 in enumerate(w1):
        temp = np.array((val1, val2))
        e_vals[i, j] = gradient_descent(temp, x_scaling, y)[1]

plt.contourf(w0, w1, e_vals, levels, alpha=0.7)
plt.axhline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)
plt.axvline(0, color='black', alpha=0.5, dashes=[2, 4], linewidth=1)

for i in range(len(old_w)-1):
    plt.annotate('', xy=ws[i+1, :], xytext=ws[i, :], arrowprops={'arrowstyle': '->', 'color': 'r'}, va='center', ha='center')

CS = plt.contour(w0, w1, e_vals, levels, linewidths=1, color='black')
plt.clabel(CS, inline=1, fontsize=14)
plt.title("Contour Plot of Gradeint Descent")
plt.xlabel("w0")
plt.ylabel("w1")
plt.show()