# Importaciones de la librería hashlib para generar hashes de transacciones, y de la librería time para medir el tiempo de minería.
import hashlib
import time
from datetime import datetime

class Minero:
    def __init__(self, nombre, costo_electricidad_kwh=0.10, potencia_watts=1000):
        self.nombre = nombre
        self.balance_btc = 0.0
        self.bloques_minados = 0
        self.costo_electricidad = costo_electricidad_kwh  # USD por kWh
        self.potencia = potencia_watts  # Watts
        self.recompensa_bloque = 3.125  # BTC actuales (post-2024 halving)
        print(f"⛏️  Minero {self.nombre} iniciado")
        print(f"   Costo electricidad: ${self.costo_electricidad}/kWh")
        print(f"   Potencia: {self.potencia}W\n")
    
    def minar_bloque(self, transacciones, dificultad=3):
        """Simula la minería de un bloque"""
        print(f"🔨 {self.nombre} comenzando a minar bloque...")
        
        # Datos del bloque
        datos_bloque = f"bloque{self.bloques_minados + 1}"
        for tx in transacciones:
            datos_bloque += f"{tx['origen']}{tx['destino']}{tx['monto']}{tx['comision']}"
        
        # Buscar nonce (Proof of Work)
        nonce = 0
        prefijo_objetivo = "0" * dificultad
        inicio = time.time()
        
        while True:
            texto = f"{datos_bloque}{nonce}"
            hash_resultante = hashlib.sha256(texto.encode()).hexdigest()
            
            if hash_resultante.startswith(prefijo_objetivo):
                fin = time.time()
                tiempo_segundos = fin - inicio
                
                # Calcular costos
                horas = tiempo_segundos / 3600
                kwh_consumidos = (self.potencia * horas) / 1000
                costo_electricidad = kwh_consumidos * self.costo_electricidad
                
                # Calcular comisiones totales
                comisiones_totales = sum(tx['comision'] for tx in transacciones)
                
                # Recompensa total
                recompensa_total = self.recompensa_bloque + comisiones_totales
                
                # Actualizar balance
                self.balance_btc += recompensa_total
                self.bloques_minados += 1
                
                print(f"✅ ¡Bloque minado!")
                print(f"   Nonce: {nonce}")
                print(f"   Hash: {hash_resultante[:32]}...")
                print(f"   Tiempo: {tiempo_segundos:.4f} segundos")
                print(f"   Transacciones incluidas: {len(transacciones)}")
                print(f"   Recompensa bloque: {self.recompensa_bloque} BTC")
                print(f"   Comisiones: {comisiones_totales} BTC")
                print(f"   Total ganado: {recompensa_total} BTC")
                print(f"   Costo electricidad: ${costo_electricidad:.6f} USD")
                print(f"   Balance total: {self.balance_btc} BTC")
                print(f"   Bloques minados: {self.bloques_minados}\n")
                
                return True
            
            nonce += 1
            
            # Simular tiempo de minería real (acelerado para demostración)
            if nonce % 100000 == 0:
                print(f"   ... probando nonce {nonce}")
    
    def calcular_rentabilidad(self, precio_btc_usd=50000):
        """Calcula si es rentable minar"""
        print(f"\n📊 Análisis de rentabilidad para {self.nombre}:")
        print(f"   Precio BTC: ${precio_btc_usd} USD")
        print(f"   Balance: {self.balance_btc} BTC = ${self.balance_btc * precio_btc_usd:,.2f} USD")
        
        # Costo por bloque (estimado)
        # Asumimos 10 minutos por bloque en promedio
        horas_por_bloque = 10 / 60
        kwh_por_bloque = (self.potencia * horas_por_bloque) / 1000
        costo_por_bloque = kwh_por_bloque * self.costo_electricidad
        
        # Ingreso por bloque
        ingreso_por_bloque = self.recompensa_bloque * precio_btc_usd
        
        # Ganancia neta
        ganancia_neta = ingreso_por_bloque - costo_por_bloque
        
        print(f"   Ingreso por bloque: ${ingreso_por_bloque:,.2f} USD")
        print(f"   Costo electricidad por bloque: ${costo_por_bloque:.4f} USD")
        print(f"   Ganancia neta por bloque: ${ganancia_neta:,.2f} USD")
        
        if ganancia_neta > 0:
            print(f"   ✅ Rentable - El minero gana dinero")
        else:
            print(f"   ❌ No rentable - El minero pierde dinero")
        
        return ganancia_neta

# --- Simulación ---
print("=== Simulación de Minería e Incentivos ===\n")

# Crear mineros con diferentes costos de electricidad
minero1 = Minero("Minero-Profesional", costo_electricidad_kwh=0.05, potencia_watts=3000)
minero2 = Minero("Minero-Casero", costo_electricidad_kwh=0.15, potencia_watts=500)

# Simular transacciones con comisiones
transacciones = [
    {'origen': 'Alice', 'destino': 'Bob', 'monto': 1.0, 'comision': 0.0001},
    {'origen': 'Bob', 'destino': 'Charlie', 'monto': 0.5, 'comision': 0.0002},
    {'origen': 'Charlie', 'destino': 'David', 'monto': 0.2, 'comision': 0.00015}
]

print(f"Transacciones en mempool: {len(transacciones)}")
print(f"Comisiones totales: {sum(tx['comision'] for tx in transacciones)} BTC\n")

# Minero 1 mina un bloque
minero1.minar_bloque(transacciones, dificultad=3)

# Minero 2 mina otro bloque
transacciones2 = [
    {'origen': 'Eve', 'destino': 'Frank', 'monto': 2.0, 'comision': 0.0003},
    {'origen': 'Frank', 'destino': 'Grace', 'monto': 1.5, 'comision': 0.00025}
]
minero2.minar_bloque(transacciones2, dificultad=3)

# Análisis de rentabilidad
print("\n" + "="*50)
minero1.calcular_rentabilidad(precio_btc_usd=50000)
minero2.calcular_rentabilidad(precio_btc_usd=50000)

# Simular halving
print("\n" + "="*50)
print("📉 Simulación de Halving (reducción de recompensa)")
print(f"Recompensa actual: {minero1.recompensa_bloque} BTC")
minero1.recompensa_bloque = minero1.recompensa_bloque / 2
print(f"Recompensa post-halving: {minero1.recompensa_bloque} BTC")
print("Los mineros menos eficientes dejarán de operar.\n")