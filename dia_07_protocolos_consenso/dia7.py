# Importaciones de la librería random para generar números aleatorios, y de la librería time para medir el tiempo de validación de bloques.
import random
import time

class ProtocoloConsenso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bloques_validados = 0
    
    def validar_bloque(self, transacciones):
        raise NotImplementedError

class ProofOfWork(ProtocoloConsenso):
    def __init__(self):
        super().__init__("Proof of Work (Bitcoin)")
    
    def validar_bloque(self, transacciones):
        print(f"⛏️  {self.nombre}: Minando bloque con {len(transacciones)} transacciones...")
        # Simular trabajo computacional
        time.sleep(0.1)  # Simula 10 minutos en realidad
        self.bloques_validados += 1
        print(f"   ✅ Bloque validado (consumió mucha energía)\n")
        return True

class ProofOfStake(ProtocoloConsenso):
    def __init__(self):
        super().__init__("Proof of Stake (Ethereum)")
    
    def validar_bloque(self, transacciones, stake_del_validador=1000):
        print(f"🎰 {self.nombre}: Validando bloque...")
        # Probabilidad basada en stake
        probabilidad = min(stake_del_validador / 10000, 1.0)
        if random.random() < probabilidad:
            self.bloques_validados += 1
            print(f"   ✅ Bloque validado (stake: {stake_del_validador} ETH)\n")
            return True
        else:
            print(f"   ❌ No seleccionado esta vez\n")
            return False

class DelegatedPoS(ProtocoloConsenso):
    def __init__(self):
        super().__init__("Delegated PoS (EOS)")
        self.delegados = [f"Delegado-{i}" for i in range(1, 22)]  # 21 delegados
        self.delegado_actual = 0
    
    def validar_bloque(self, transacciones):
        delegado = self.delegados[self.delegado_actual % len(self.delegados)]
        print(f"🗳️  {self.nombre}: Delegado {delegado} validando bloque...")
        self.bloques_validados += 1
        self.delegado_actual += 1
        print(f"   ✅ Bloque validado (muy rápido)\n")
        return True

class BFT(ProtocoloConsenso):
    def __init__(self, num_nodos=10):
        super().__init__("Byzantine Fault Tolerance")
        self.nodos = [f"Nodo-{i}" for i in range(num_nodos)]
    
    def validar_bloque(self, transacciones):
        print(f"🏛️  {self.nombre}: Iniciando votación BFT...")
        votos_a_favor = 0
        for nodo in self.nodos:
            # 90% de nodos honestos
            if random.random() < 0.9:
                votos_a_favor += 1
        
        umbral = len(self.nodos) * 2 / 3
        if votos_a_favor >= umbral:
            self.bloques_validados += 1
            print(f"   ✅ Consenso alcanzado ({votos_a_favor}/{len(self.nodos)} votos)\n")
            return True
        else:
            print(f"   ❌ No se alcanzó consenso ({votos_a_favor}/{len(self.nodos)} votos)\n")
            return False

# --- Simulación ---
print("=== Comparación de Protocolos de Consenso ===\n")

transacciones_ejemplo = [
    "Alice -> Bob: 1 BTC",
    "Bob -> Charlie: 0.5 BTC",
    "Charlie -> David: 0.2 BTC"
]

# PoW
pow = ProofOfWork()
pow.validar_bloque(transacciones_ejemplo)

# PoS
pos = ProofOfStake()
pos.validar_bloque(transacciones_ejemplo, stake_del_validador=5000)

# DPoS
dpos = DelegatedPoS()
dpos.validar_bloque(transacciones_ejemplo)

# BFT
bft = BFT(num_nodos=10)
bft.validar_bloque(transacciones_ejemplo)

print("\n📊 Resumen de bloques validados:")
print(f"   PoW: {pow.bloques_validados}")
print(f"   PoS: {pos.bloques_validados}")
print(f"   DPoS: {dpos.bloques_validados}")
print(f"   BFT: {bft.bloques_validados}")