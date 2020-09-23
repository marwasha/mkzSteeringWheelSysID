import numpy as np
import matplotlib.pyplot as plt
stepI = "tests/StepInput"
stepIF = "tests/StepInputFlip"

response = {}
for i in range(3):
    with open(stepI + str(i) + ".csv", "r") as file:
        response["I" + str(i)] = np.loadtxt(file, delimiter=",", skiprows = 1)
    with open(stepIF + str(i) + ".csv", "r") as file:
        response["IF" + str(i)] = np.loadtxt(file, delimiter=",", skiprows = 1)

fig, axs = plt.subplots(2,3)
axs[0,0].plot(response["I0"][:,1], response["I0"][:,2])
plt.plot(response["I0"][:,1], response["I0"][:,2])
