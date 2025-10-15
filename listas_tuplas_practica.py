# SIMULACIÓN DE ENTRENAMIENTO DE IA

# Tupla FIJAS de configuración
CONFIG = (0.01, 100, 32)  # lr, epochs, batch

# Lista DINÁMICA de métricas
metricas_loss = []
metricas_precision = []

# Simular entrenamiento
for epoch in range(5):
    # Valores que cambian cada epoch
    loss = 1.0 / (epoch + 1)
    precision = 0.8 + (epoch * 0.05)
    
    metricas_loss.append(loss)
    metricas_precision.append(precision)

print("Configuración fija:", CONFIG)
print("Loss en evolución:", metricas_loss)
print("Precisión mejorando:", metricas_precision)

# ¿Qué pasa si intentamos modificar la tupla?
# CONFIG[0] = 0.02  # ¡ERROR! Las tuplas son inmutables

# Pero las listas sí podemos modificarlas
metricas_loss[0] = 0.95  # ✅ Correcto