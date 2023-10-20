import numpy as np

# Define data
noise = np.random.normal(loc=0.0, scale=0.02, size=101)
x = np.linspace(0, 20, 101) / 20
y = - x ** 3 + 2 * x ** 2 - x + 1 + noise

# Global config option
gconfig = {
    'toImageButtonOptions': {
        'format': 'png',
        'scale': 5
    }
}