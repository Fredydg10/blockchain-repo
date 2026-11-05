# Importaciones de la librería random para generar números aleatorios, y de la librería statistics para calcular la mediana de los precios.
import random
import statistics
import time

class OraculoCentralizado:
    """Oráculo simple de una sola fuente (RIESGOSO)"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"🔮 Oráculo centralizado: {self.nombre}")
        print(f"   ⚠️  Punto único de fallo\n")
    
    def obtener_precio_btc(self):
        """Simula obtener precio de BTC (puede fallar o mentir)"""
        # 10% de probabilidad de dar dato incorrecto
        if random.random() < 0.1:
            precio = 50000 + random.randint(-10000, 10000)  # Dato erróneo
            print(f"   ❌ {self.nombre} dio dato incorrecto: ${precio}")
        else:
            precio = 50000
            print(f"   ✅ {self.nombre} dio precio: ${precio}")
        return precio

class NodoChainlink:
    """Un nodo individual de la red Chainlink"""
    
    def __init__(self, nombre, stake_eth=100):
        self.nombre = nombre
        self.stake = stake_eth  # Dinero apostado como garantía
        self.reputacion = 100
        self.es_honesto = random.random() > 0.1  # 90% honestos
    
    def consultar_precio(self):
        """Consulta el precio de BTC"""
        if self.es_honesto:
            # Precio real con pequeña variación
            return 50000 + random.randint(-100, 100)
        else:
            # Precio manipulado
            return random.randint(30000, 70000)
    
    def recibir_recompensa(self, cantidad):
        self.stake += cantidad
        self.reputacion = min(100, self.reputacion + 1)
    
    def ser_cortado(self, cantidad):  # Slashing
        self.stake -= cantidad
        self.reputacion = max(0, self.reputacion - 10)
        print(f"   ⚠️  {self.nombre} fue penalizado (slashing): -{cantidad} ETH")

class RedChainlink:
    """Red descentralizada de oráculos"""
    
    def __init__(self, num_nodos=7):
        self.nodos = [NodoChainlink(f"Node-{i+1}") for i in range(num_nodos)]
        print(f"⛓️  Red Chainlink con {num_nodos} nodos")
        print(f"   Nodos honestos: {sum(1 for n in self.nodos if n.es_honesto)}")
        print(f"   Nodos maliciosos: {sum(1 for n in self.nodos if not n.es_honesto)}\n")
    
    def obtener_precio_consenso(self):
        """Obtiene precio usando consenso de múltiples nodos"""
        print(f"📡 Consultando red Chainlink...")
        
        precios = []
        for nodo in self.nodos:
            precio = nodo.consultar_precio()
            precios.append(precio)
            print(f"   {nodo.nombre}: ${precio}")
        
        # Usar mediana para resistir valores atípicos
        precio_final = statistics.median(precios)
        print(f"\n   📊 Precio final (mediana): ${precio_final:,.2f}")
        
        # Penalizar nodos que se desviaron mucho
        for nodo, precio in zip(self.nodos, precios):
            if abs(precio - precio_final) > 5000:
                nodo.ser_cortado(10)  # Slashing
            else:
                nodo.recibir_recompensa(1)
        
        return precio_final

class SmartContractConOraculo:
    """Smart contract que usa oráculo para ejecutarse"""
    
    def __init__(self, nombre, oraculo):
        self.nombre = nombre
        self.oraculo = oraculo
        self.ejecuciones = 0
        print(f"📜 Contrato '{self.nombre}' usando oráculo\n")
    
    def ejecutar_si_btc_cae(self, umbral):
        """Ejecuta contrato si BTC cae bajo cierto precio"""
        print(f"🔍 Verificando si BTC < ${umbral}...")
        
        precio_actual = self.oraculo.obtener_precio_consenso()
        
        if precio_actual < umbral:
            self.ejecuciones += 1
            print(f"   ✅ Condición cumplida: BTC está en ${precio_actual:,.2f}")
            print(f"   🚨 Contrato ejecutado: Liquidar posiciones\n")
            return True
        else:
            print(f"   ⏸️  Condición no cumplida: BTC está en ${precio_actual:,.2f}")
            print(f"   Contrato en espera...\n")
            return False

# --- Simulación ---
print("=== ORÁCULOS Y CHAINLINK ===\n")

print("--- Problema: Oráculo Centralizado ---")
oraculo_malo = OraculoCentralizado("CoinAPI-Single")
for i in range(5):
    print(f"Consulta #{i+1}:")
    oraculo_malo.obtener_precio_btc()
    print()

print("\n--- Solución: Red Chainlink Descentralizada ---")
red_chainlink = RedChainlink(num_nodos=7)

# Contrato que usa Chainlink
contrato = SmartContractConOraculo(
    nombre="Liquidador de Préstamos",
    oraculo=red_chainlink
)

# Ejecutar contrato varias veces
for i in range(3):
    print(f"\n--- Ejecución #{i+1} ---")
    contrato.ejecutar_si_btc_cae(umbral=45000)

print("\n" + "="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. Los smart contracts NO pueden acceder a internet")
print("2. Los oráculos son el puente blockchain ↔ mundo real")
print("3. Oráculos centralizados = punto único de fallo")
print("4. Chainlink usa múltiples nodos + consenso + slashing")
print("5. La mediana resiste datos manipulados")
print("6. Casos de uso: DeFi, seguros, NFTs dinámicos, gaming")