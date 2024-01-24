import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

# create virtual environment for interpreter and install modules there 
#1. create a virtual environment -py for PCs, for macs python3. (EX: python3 -m venv myvenv)
# make sure youre in the virtual root environment
#2. activate your virtual environment -> source myvenv/bin/activate
#3. install 3rd party library or module -> pip3 install matplotlib