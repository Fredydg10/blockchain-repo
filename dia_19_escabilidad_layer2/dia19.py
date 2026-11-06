import hashlib
import time

class Layer1:
    """Blockchain principal (Ethereum)"""
    
    def __init__(self, nombre, tps=15):
        self.nombre = nombre
        self.tps = tps  # Transacciones por segundo
        self.bloques = []
        self.gas_price = 30  # Gwei
        print(f"⛓️  Layer 1: {nombre}")
        print(f"   TPS: {tps} | Gas: {self.gas_price} gwei\n")
    
    def procesar_transaccion(self, tx):
        costo = len(tx) * self.gas_price
        self.bloques.append(tx)
        print(f"   ✅ TX procesada en L1: {tx[:30]}... | Costo: ${costo/100:.2f}")
        return costo


class RollupOptimista:
    """Optimism/Arbitrum - Asume validez, permite disputas"""
    
    def __init__(self, nombre, layer1):
        self.nombre = nombre
        self.layer1 = layer1
        self.transacciones = []
        self.periodo_desafio_dias = 7
        print(f"🟠 Rollup Optimista: {nombre}")
        print(f"   Periodo de desafío: {self.periodo_desafio_dias} días\n")
    
    def agregar_transaccion(self, tx):
        self.transacciones.append(tx)
        print(f"   📝 TX agregada (off-chain): {tx[:30]}...")
    
    def publicar_batch(self):
        """Publica lote en L1"""
        print(f"\n📦 Publicando batch de {len(self.transacciones)} TXs en {self.layer1.nombre}...")
        batch = "|".join(self.transacciones)
        costo = self.layer1.procesar_transaccion(batch)
        print(f"   ⏳ Periodo de desafío: {self.periodo_desafio_dias} días")
        print(f"   ✅ Batch publicado. Costo por TX: ${costo/len(self.transacciones)/100:.4f}\n")
        self.transacciones = []


class RollupZK:
    """zkSync/Starknet - Usa ZK-Proofs"""
    
    def __init__(self, nombre, layer1):
        self.nombre = nombre
        self.layer1 = layer1
        self.transacciones = []
        print(f"🔵 Rollup ZK: {nombre}")
        print(f"   Validación: ZK-Proof (instantánea)\n")
    
    def agregar_transaccion(self, tx):
        self.transacciones.append(tx)
        print(f"   📝 TX agregada: {tx[:30]}...")
    
    def generar_zk_proof(self):
        """Genera prueba de conocimiento cero"""
        print(f"\n🔐 Generando ZK-Proof para {len(self.transacciones)} TXs...")
        proof = hashlib.sha256("".join(self.transacciones).encode()).hexdigest()[:16]
        print(f"   Proof generado: 0x{proof}")
        return proof
    
    def publicar_batch(self):
        proof = self.generar_zk_proof()
        batch = f"proof:{proof}|txs:{len(self.transacciones)}"
        print(f"📦 Publicando batch con ZK-Proof en {self.layer1.nombre}...")
        costo = self.layer1.procesar_transaccion(batch)
        print(f"   ✅ Validación instantánea. Costo por TX: ${costo/len(self.transacciones)/100:.4f}\n")
        self.transacciones = []


class Sidechain:
    """Polygon PoS / BSC - Blockchain independiente"""
    
    def __init__(self, nombre, layer1):
        self.nombre = nombre
        self.layer1 = layer1
        self.transacciones = []
        self.tps = 7000
        print(f"🟣 Sidechain: {nombre}")
        print(f"   TPS: {self.tps} | Consenso propio\n")
    
    def agregar_transaccion(self, tx):
        self.transacciones.append(tx)
        print(f"   📝 TX procesada: {tx[:30]}... | Costo: $0.001")
    
    def checkpoint_en_l1(self):
        """Envía checkpoint periódico a L1"""
        print(f"\n📌 Enviando checkpoint a {self.layer1.nombre}...")
        self.layer1.procesar_transaccion(f"checkpoint:{len(self.transacciones)}")
        print(f"   ✅ {len(self.transacciones)} TXs aseguradas en L1\n")
        self.transacciones = []


class CanalPagos:
    """Lightning Network - Canales off-chain"""
    
    def __init__(self, participante_a, participante_b):
        self.a = participante_a
        self.b = participante_b
        self.balance_a = 0
        self.balance_b = 0
        self.abierto = False
        print(f"⚡ Canal de pagos: {participante_a} ↔ {participante_b}\n")
    
    def abrir_canal(self, deposito_a, deposito_b):
        print(f"🔓 Abriendo canal en blockchain...")
        self.balance_a = deposito_a
        self.balance_b = deposito_b
        self.abierto = True
        print(f"   {self.a}: {deposito_a} | {self.b}: {deposito_b}\n")
    
    def enviar(self, de, monto):
        if not self.abierto:
            print("❌ Canal cerrado")
            return
        if de == self.a:
            self.balance_a -= monto
            self.balance_b += monto
            print(f"⚡ {self.a} envía {monto} a {self.b} (off-chain, instantáneo)")
        else:
            self.balance_b -= monto
            self.balance_a += monto
            print(f"⚡ {self.b} envía {monto} a {self.a} (off-chain, instantáneo)")
        print(f"   Balance: {self.a}={self.balance_a} | {self.b}={self.balance_b}\n")
    
    def cerrar_canal(self):
        print(f"🔒 Cerrando canal en blockchain...")
        print(f"   Balance final: {self.a}={self.balance_a} | {self.b}={self.balance_b}")
        print(f"   ✅ Solo 2 transacciones en L1 (apertura + cierre)\n")
        self.abierto = False


# --- Simulación ---
print("=== Escabilidad Layer 2 ===\n")

ethereum = Layer1("Ethereum", tps=15)

print("--- 1. Rollup Optimista (Arbitrum) ---")
arbitrum = RollupOptimista("Arbitrum", ethereum)
for i in range(10):
    arbitrum.agregar_transaccion(f"Alice->Bob:{i*10} ETH")
arbitrum.publicar_batch()

print("\n--- 2. Rollup ZK (zkSync) ---")
zksync = RollupZK("zkSync", ethereum)
for i in range(10):
    zksync.agregar_transaccion(f"Charlie->Dave:{i*5} ETH")
zksync.publicar_batch()

print("\n--- 3. Sidechain (Polygon) ---")
polygon = Sidechain("Polygon PoS", ethereum)
for i in range(20):
    polygon.agregar_transaccion(f"TX{i}: 1 MATIC")
polygon.checkpoint_en_l1()

print("\n--- 4. Canal de Pagos (Lightning) ---")
canal = CanalPagos("Alice", "Bob")
canal.abrir_canal(1000, 1000)
canal.enviar("Alice", 50)
canal.enviar("Alice", 30)
canal.enviar("Bob", 20)
canal.cerrar_canal()

print("="*60)
print("🎓 CONCEPTOS CLAVE:")
print("1. Layer 1 (Ethereum): Seguro pero lento y caro")
print("2. Rollups Optimistas: Rápidos, 7 días de desafío")
print("3. Rollups ZK: Máxima seguridad con ZK-Proofs")
print("4. Sidechains: Independientes, menos seguras")
print("5. Canales de pagos: Instantáneos, 2 TX en L1")
print("6. ZK-Proofs = probar algo sin revelar información")
print("7. El futuro: múltiples L2 conviviendo (multi-chain)")