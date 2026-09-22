import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
# параметры распределения
mu, sigma = 50, 15
data = np.random.normal(mu, sigma, 10000)
# визуализация гистограммы и теоретической плотности
sns.histplot(data, bins=50, stat="density", kde=False, color="skyblue")
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
plt.plot(x, norm.pdf(x, mu, sigma), 'r', linewidth=2, label="Теоретическая плотность")
plt.title("Нормальное распределение")
plt.xlabel("Значения")
plt.ylabel("Плотность")
plt.legend()
plt.show()