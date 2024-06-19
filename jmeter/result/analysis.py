import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('result.csv')

# Análisis básico
# print(data.describe())  # Resumen estadístico

# Histograma de tiempos de respuesta
data['elapsed'].hist(bins=50)
plt.title('Histograma de Tiempos de Respuesta')
plt.xlabel('Tiempo de Respuesta (ms)')
plt.ylabel('Frecuencia')
plt.savefig("result")
plt.show()

# Análisis de error rate
# error_rate = data[data['responseCode'] == '400'].shape[0] / data.shape[0] * 100
# print(f"Tasa de Errores: {error_rate}%")
