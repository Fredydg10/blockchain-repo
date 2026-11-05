# Tener el hashlib instalado y el time para que funcione el programa
import hashlib
import time

class Blockchain:
    def __init__(self, nombre, regla_tamano_bloque=1):
        self.nombre = nombre
        self.bloques = []
        self.regla_tamano_bloque = regla_tamano_bloque
        self.nodos = 1000
        print(f"⛓️  Blockchain '{self.nombre}' creada")
        print(f"   Regla: Bloques de {regla_tamano_bloque}MB")
        print(f"   Nodos: {self.nodos}\n")
    
    def agregar_bloque(self, transacciones):
        tamano = len(transacciones) * 0.001
        
        if tamano > self.regla_tamano_bloque:
            print(f"   ❌ Bloque rechazado: {tamano:.3f}MB > {self.regla_tamano_bloque}MB")
            return False
        
        bloque = {
            'numero': len(self.bloques) + 1,
            'transacciones': transacciones,
            'hash': hashlib.sha256(f"{len(self.bloques)}{time.time()}".encode()).hexdigest()
        }
        self.bloques.append(bloque)
        print(f"   ✅ Bloque #{bloque['numero']} agregado ({tamano:.3f}MB)")
        return True

class SoftFork:
    def __init__(self, blockchain_original, nueva_regla):
        self.blockchain = blockchain_original
        self.nueva_regla = nueva_regla
        print(f"🔄 Soft Fork en {blockchain_original.nombre}")
        print(f"   Nueva regla: Bloques de {nueva_regla}MB")
        print(f"   Compatible con nodos antiguos: SÍ\n")
    
    def aplicar(self):
        self.blockchain.regla_tamano_bloque = self.nueva_regla
        print(f"✅ Soft Fork aplicado exitosamente")
        print(f"   Todos los nodos pueden seguir operando\n")

class HardFork:
    def __init__(self, blockchain_original, nueva_regla, nombre_nueva):
        self.original = blockchain_original
        self.nueva_regla = nueva_regla
        self.nombre_nueva = nombre_nueva
        print(f"💥 Hard Fork en {blockchain_original.nombre}")
        print(f"   Nueva cadena: {nombre_nueva}")
        print(f"   Nueva regla: Bloques de {nueva_regla}MB")
        print(f"   Compatible con nodos antiguos: NO\n")
    
    def ejecutar(self):
        nueva_chain = Blockchain(self.nombre_nueva, self.nueva_regla)
        nueva_chain.bloques = self.original.bloques.copy()
        
        print(f"✅ Hard Fork completado")
        print(f"   {self.original.nombre}: Mantiene regla de {self.original.regla_tamano_bloque}MB")
        print(f"   {self.nombre_nueva}: Nueva regla de {self.nueva_regla}MB")
        print(f"   Ahora existen DOS blockchains separadas\n")
        
        return nueva_chain

class Token:
    def __init__(self, nombre, blockchain):
        self.nombre = nombre
        self.blockchain = blockchain
        self.balance = 0
        print(f"🪙 Token '{self.nombre}' en {blockchain.nombre}\n")

class Bridge:
    def __init__(self, chain_a, chain_b):
        self.chain_a = chain_a
        self.chain_b = chain_b
        self.tokens_bloqueados = {}
        print(f"🌉 Bridge creado entre {chain_a.nombre} y {chain_b.nombre}\n")
    
    def bloquear_y_acunar(self, token, cantidad):
        """Bloquea tokens en chain A y crea wrapped tokens en chain B"""
        print(f"🔒 Bloqueando {cantidad} {token.nombre} en {self.chain_a.nombre}...")
        
        if token.balance < cantidad:
            print(f"   ❌ Fondos insuficientes")
            return None
        
        token.balance -= cantidad
        if token.nombre not in self.tokens_bloqueados:
            self.tokens_bloqueados[token.nombre] = 0
        self.tokens_bloqueados[token.nombre] += cantidad
        
        wrapped_token = Token(f"Wrapped {token.nombre}", self.chain_b)
        wrapped_token.balance = cantidad
        
        print(f"   ✅ {cantidad} {token.nombre} bloqueados")
        print(f"   ✅ {cantidad} Wrapped {token.nombre} creados en {self.chain_b.nombre}\n")
        
        return wrapped_token
    
    def quemar_y_desbloquear(self, wrapped_token, cantidad):
        """Quema wrapped tokens en chain B y desbloquea originales en chain A"""
        print(f"🔥 Quemando {cantidad} {wrapped_token.nombre} en {self.chain_b.nombre}...")
        
        if wrapped_token.balance < cantidad:
            print(f"   ❌ Fondos insuficientes")
            return False
        
        wrapped_token.balance -= cantidad
        
        token_original_nombre = wrapped_token.nombre.replace("Wrapped ", "")
        if token_original_nombre in self.tokens_bloqueados:
            self.tokens_bloqueados[token_original_nombre] -= cantidad
        
        print(f"   ✅ {cantidad} {wrapped_token.nombre} quemados")
        print(f"   ✅ {cantidad} tokens originales desbloqueados en {self.chain_a.nombre}\n")
        
        return True

# --- Simulación ---
print("=== Forks e Interoperabilidad ===\n")

print("--- Ejemplo 1: Soft Fork (SegWit en Bitcoin) ---")
bitcoin = Blockchain("Bitcoin", regla_tamano_bloque=1)
bitcoin.agregar_bloque(["tx1", "tx2", "tx3"])

soft_fork = SoftFork(bitcoin, nueva_regla=2)
soft_fork.aplicar()
bitcoin.agregar_bloque(["tx4", "tx5", "tx6", "tx7", "tx8"])

print("\n--- Ejemplo 2: Hard Fork (Bitcoin → Bitcoin Cash) ---")
bitcoin_original = Blockchain("Bitcoin", regla_tamano_bloque=1)
bitcoin_original.agregar_bloque(["tx1", "tx2"])

hard_fork = HardFork(bitcoin_original, nueva_regla=8, nombre_nueva="Bitcoin Cash")
bitcoin_cash = hard_fork.ejecutar()

bitcoin_original.agregar_bloque(["tx3", "tx4"])
bitcoin_cash.agregar_bloque(["tx3", "tx4", "tx5", "tx6", "tx7", "tx8", "tx9", "tx10"])

print("\n--- Ejemplo 3: Bridge entre Ethereum y Polygon ---")
ethereum = Blockchain("Ethereum", regla_tamano_bloque=100)
polygon = Blockchain("Polygon", regla_tamano_bloque=100)

eth_token = Token("ETH", ethereum)
eth_token.balance = 10

bridge = Bridge(ethereum, polygon)

wrapped_eth = bridge.bloquear_y_acunar(eth_token, 5)
print(f"Balance ETH en Ethereum: {eth_token.balance}")
print(f"Balance Wrapped ETH en Polygon: {wrapped_eth.balance}")

bridge.quemar_y_desbloquear(wrapped_eth, 3)
print(f"Balance Wrapped ETH en Polygon: {wrapped_eth.balance}")
print(f"Tokens bloqueados en bridge: {bridge.tokens_bloqueados}")

print("\n" + "="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. Soft Fork: Actualización compatible (no divide la red)")
print("2. Hard Fork: Cambio radical (crea nueva blockchain)")
print("3. Ejemplos: Bitcoin/Bitcoin Cash, Ethereum/Ethereum Classic")
print("4. Bridges: Conectan blockchains aisladas")
print("5. Wrapped tokens: Representación de un token en otra cadena")
print("6. Interoperabilidad: Futuro de blockchain (Polkadot, Cosmos)")
print("7. Riesgo: Bridges son puntos de ataque (hackeos millonarios)")