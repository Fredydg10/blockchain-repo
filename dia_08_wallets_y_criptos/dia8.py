# Importaciones de la librería hashlib para generar hashes de claves privadas y direcciones, y de la librería secrets para generar números aleatorios.
import hashlib
import secrets
from datetime import datetime

class Wallet:
    def __init__(self, tipo="Hot"):
        self.tipo = tipo  # Hot o Cold
        self.balance = {}  # { 'BTC': 0.5, 'ETH': 10 }
        self.direccion = None
        self.seed_phrase = None
        self.clave_privada = None
        self.crear_wallet()
    
    def crear_wallet(self):
        """Genera una wallet con seed phrase y dirección"""
        # Generar seed phrase (simulado - en realidad son 12/24 palabras de una lista)
        palabras_ejemplo = ['abandon', 'ability', 'able', 'about', 'above', 'absent', 
                           'absorb', 'abstract', 'absurd', 'abuse', 'access', 'accident']
        self.seed_phrase = ' '.join(palabras_ejemplo[:12])
        
        # Generar clave privada desde seed
        self.clave_privada = hashlib.sha256(self.seed_phrase.encode()).hexdigest()
        
        # Generar dirección pública (simplificado)
        self.direccion = hashlib.sha256(self.clave_privada.encode()).hexdigest()[:42]
        self.direccion = '0x' + self.direccion
        
        print(f"🔑 Wallet {self.tipo} creada:")
        print(f"   Dirección: {self.direccion}")
        print(f"   Seed Phrase: {self.seed_phrase}")
        print(f"   ⚠️  GUARDA TU SEED PHRASE EN PAPEL, NUNCA DIGITAL\n")
    
    def recibir_fondos(self, criptomoneda, cantidad):
        """Simula recibir criptomonedas"""
        if criptomoneda not in self.balance:
            self.balance[criptomoneda] = 0
        self.balance[criptomoneda] += cantidad
        print(f"✅ Recibido: {cantidad} {criptomoneda}")
        print(f"   Balance actual: {self.balance}\n")
    
    def enviar_fondos(self, destino, criptomoneda, cantidad):
        """Simula enviar criptomonedas"""
        if criptomoneda not in self.balance or self.balance[criptomoneda] < cantidad:
            print(f"❌ Fondos insuficientes de {criptomoneda}")
            return False
        
        self.balance[criptomoneda] -= cantidad
        print(f"✅ Enviado: {cantidad} {criptomoneda} a {destino[:10]}...")
        print(f"   Balance actual: {self.balance}\n")
        return True
    
    def verificar_seguridad(self):
        """Verifica el nivel de seguridad de la wallet"""
        print(f"\n🔒 Análisis de seguridad:")
        print(f"   Tipo: {self.tipo}")
        if self.tipo == "Hot":
            print(f"   ⚠️  Riesgo: Conectada a internet (vulnerable a hacks)")
            print(f"   Recomendación: Solo para cantidades pequeñas")
        else:
            print(f"   ✅ Seguridad: Alta (sin conexión a internet)")
            print(f"   Recomendación: Para ahorros a largo plazo")

class Exchange:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = {}  # { 'usuario': { 'BTC': 0.5 } }
        print(f"🏦 Exchange {self.nombre} iniciado\n")
    
    def depositar(self, usuario, criptomoneda, cantidad):
        """Usuario deposita cripto al exchange"""
        if usuario not in self.usuarios:
            self.usuarios[usuario] = {}
        if criptomoneda not in self.usuarios[usuario]:
            self.usuarios[usuario][criptomoneda] = 0
        self.usuarios[usuario][criptomoneda] += cantidad
        print(f"📥 {usuario} depositó {cantidad} {criptomoneda} en {self.nombre}")
        print(f"   Balance en exchange: {self.usuarios[usuario]}\n")
    
    def retirar(self, usuario, criptomoneda, cantidad, direccion_wallet):
        """Usuario retira cripto del exchange a su wallet"""
        if usuario not in self.usuarios or self.usuarios[usuario].get(criptomoneda, 0) < cantidad:
            print(f"❌ Fondos insuficientes")
            return
        
        self.usuarios[usuario][criptomoneda] -= cantidad
        print(f"📤 {usuario} retiró {cantidad} {criptomoneda}")
        print(f"   Enviado a: {direccion_wallet[:20]}...")
        print(f"   ⚠️  Ahora SÍ tienes control total de tus fondos\n")

# --- Simulación ---
print("=== WALLETS Y CRIPTOMONEDAS ===\n")

# Crear wallets
print("--- Creando Wallets ---")
wallet_hot = Wallet(tipo="Hot")
wallet_cold = Wallet(tipo="Cold")

# Simular recibir fondos
print("--- Recibiendo Fondos ---")
wallet_hot.recibir_fondos("BTC", 0.5)
wallet_hot.recibir_fondos("ETH", 10)

# Simular exchange
print("--- Usando Exchange (NO recomendado para grandes cantidades) ---")
exchange = Exchange("Binance")
exchange.depositar("Alice", "BTC", 1.0)
exchange.depositar("Alice", "ETH", 20)

# Retirar a wallet personal (mejor práctica)
print("--- Retirando a Wallet Personal (Mejor Práctica) ---")
exchange.retirar("Alice", "BTC", 1.0, wallet_cold.direccion)

# Verificar seguridad
wallet_hot.verificar_seguridad()
wallet_cold.verificar_seguridad()

print("\n" + "="*50)
print("🎓 REGLAS DE ORO PARA GANAR DINERO CON CRIPTO:")
print("1. Nunca inviertas más de lo que puedas perder")
print("2. Usa cold wallets para ahorros a largo plazo")
print("3. Guarda tu seed phrase en papel, nunca digital")
print("4. Investiga antes de comprar (DYOR - Do Your Own Research)")
print("5. Cuidado con estafas y promesas de ganancias rápidas")
print("6. Diversifica: no pongas todo en una sola cripto")
print("7. Aprende sobre DeFi, staking y yield farming (más adelante)")