# Importaciones de la librería hashlib para generar hashes de transacciones, y de la librería datetime para obtener la fecha y hora actual.
import hashlib
import time
from datetime import datetime

class Transaccion:
    def __init__(self, origen, destino, monto, clave_privada_simulada):
        self.origen = origen
        self.destino = destino
        self.monto = monto
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.hash = None
        self.firma = None
        self.estado = "Creada"
        
        # Simular firma (en realidad usaría criptografía real como en Día 3)
        datos_a_firmar = f"{origen}{destino}{monto}{self.timestamp}"
        self.firma = hashlib.sha256(f"{datos_a_firmar}{clave_privada_simulada}".encode()).hexdigest()
        self.hash = hashlib.sha256(datos_a_firmar.encode()).hexdigest()
    
    def __str__(self):
        return f"TX: {self.origen} -> {self.destino} | {self.monto} BTC | Estado: {self.estado}"

class Mempool:
    def __init__(self):
        self.transacciones_pendientes = []
        print("📦 Mempool inicializado (sala de espera de transacciones)\n")
    
    def agregar_transaccion(self, transaccion):
        """Agrega una transacción al mempool"""
        # Validar transacción
        if self.validar_transaccion(transaccion):
            transaccion.estado = "En Mempool"
            self.transacciones_pendientes.append(transaccion)
            print(f"✅ Transacción agregada al mempool: {transaccion}")
        else:
            print(f"❌ Transacción rechazada: {transaccion}")
    
    def validar_transaccion(self, transaccion):
        """Valida que la transacción sea correcta"""
        # Simulación: verificar que la firma sea válida
        if transaccion.firma and len(transaccion.firma) == 64:
            return True
        return False
    
    def obtener_transacciones_para_bloque(self, num_transacciones=3):
        """El minero selecciona transacciones del mempool (las que pagan más comisiones)"""
        # En realidad, los mineros eligen por comisión, aquí tomamos las primeras
        seleccionadas = self.transacciones_pendientes[:num_transacciones]
        return seleccionadas
    
    def remover_transacciones(self, transacciones):
        """Remueve transacciones que ya fueron incluidas en un bloque"""
        for tx in transacciones:
            if tx in self.transacciones_pendientes:
                self.transacciones_pendientes.remove(tx)
                tx.estado = "Confirmada en Bloque"

class Nodo:
    def __init__(self, nombre, tipo="Completo"):
        self.nombre = nombre
        self.tipo = tipo
        self.mempool = Mempool()
        self.blockchain = []
        print(f"🖥️  Nodo {nombre} ({tipo}) iniciado\n")
    
    def recibir_transaccion(self, transaccion):
        """Recibe una transacción de un usuario y la valida"""
        print(f"📡 {self.nombre} recibe transacción...")
        self.mempool.agregar_transaccion(transaccion)
        print()

class Red:
    def __init__(self):
        self.nodos = [
            Nodo("Nodo-1", "Completo"),
            Nodo("Nodo-2", "Completo"),
            Nodo("Nodo-3", "Minero")
        ]
    
    def transmitir_transaccion(self, transaccion):
        """Transmite la transacción a todos los nodos"""
        print(f"🌐 Transmitiendo transacción a la red...")
        for nodo in self.nodos:
            nodo.recibir_transaccion(transaccion)
    
    def minar_bloque(self, nodo_minero_idx=2):
        """Un nodo minero crea un bloque con transacciones del mempool"""
        minero = self.nodos[nodo_minero_idx]
        print(f"⛏️  {minero.nombre} está minando un bloque...\n")
        
        # Seleccionar transacciones del mempool
        transacciones = minero.mempool.obtener_transacciones_para_bloque(3)
        
        if not transacciones:
            print("   No hay transacciones en el mempool")
            return
        
        # Crear bloque
        bloque = {
            'numero': len(self.nodos[0].blockchain) + 1,
            'transacciones': transacciones,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'hash': hashlib.sha256(f"bloque{len(self.nodos[0].blockchain)}".encode()).hexdigest()
        }
        
        # Agregar bloque a todos los nodos
        for nodo in self.nodos:
            nodo.blockchain.append(bloque)
            print(f"   📦 {nodo.nombre} agregó bloque #{bloque['numero']}")
        
        # Remover transacciones del mempool
        minero.mempool.remover_transacciones(transacciones)
        
        print(f"\n✅ Bloque #{bloque['numero']} minado con {len(transacciones)} transacciones")
        print(f"   Hash: {bloque['hash'][:32]}...\n")

# --- Simulación del ciclo de vida ---
print("=== Simulación del ciclo de vida de una transacción ===\n")

# Paso 1: Crear transacción
print("📝 Paso 1: Alice crea una transacción")
tx1 = Transaccion("Alice", "Bob", 1.0, "clave_privada_alice_123")
print(f"   {tx1}\n")

# Paso 2: La transacción ya está firmada (en el constructor)
print("✍️  Paso 2: Transacción firmada con clave privada de Alice")
print(f"   Firma: {tx1.firma[:32]}...\n")

# Paso 3: Transmitir a la red
print("📡 Paso 3: Transmitiendo a la red")
red = Red()
red.transmitir_transaccion(tx1)

# Agregar más transacciones
print("\n--- Agregando más transacciones ---\n")
tx2 = Transaccion("Bob", "Charlie", 0.5, "clave_privada_bob_456")
tx3 = Transaccion("Charlie", "David", 0.2, "clave_privada_charlie_789")

red.transmitir_transaccion(tx2)
red.transmitir_transaccion(tx3)

# Paso 4: Minar bloque
print("\n--- Paso 4: Minero crea un bloque ---\n")
red.minar_bloque(nodo_minero_idx=2)

# Verificar estado
print("\n--- Estado final ---")
print(f"Transacciones en mempool de Nodo-1: {len(red.nodos[0].mempool.transacciones_pendientes)}")
print(f"Bloques en blockchain de Nodo-1: {len(red.nodos[0].blockchain)}")
print(f"Estado de TX1: {tx1.estado}")