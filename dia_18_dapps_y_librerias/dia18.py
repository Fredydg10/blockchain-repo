import hashlib
import json

class SmartContractSimulado:
    """Simula un smart contract en blockchain"""
    
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.balances = {'0xAlice': 1000, '0xBob': 500}
        self.propietario = '0xAlice'
        print(f"📜 Contrato '{nombre}' en {direccion}\n")
    
    def balance_of(self, address):
        return self.balances.get(address, 0)
    
    def transfer(self, from_addr, to_addr, amount):
        if self.balances.get(from_addr, 0) < amount:
            return False, "Fondos insuficientes"
        self.balances[from_addr] -= amount
        self.balances[to_addr] = self.balances.get(to_addr, 0) + amount
        return True, "Transferencia exitosa"


class ABI:
    """Application Binary Interface - Traductor entre JS y Solidity"""
    
    def __init__(self, contrato):
        self.contrato = contrato
        self.funciones = [
            {"name": "balanceOf", "inputs": ["address"], "outputs": ["uint256"]},
            {"name": "transfer", "inputs": ["address", "uint256"], "outputs": ["bool"]},
            {"name": "owner", "inputs": [], "outputs": ["address"]}
        ]
        print(f"📋 ABI generado para '{contrato.nombre}'")
        print(f"   Funciones disponibles: {len(self.funciones)}\n")
    
    def llamar_funcion(self, nombre_funcion, args):
        """Simula llamada desde frontend"""
        print(f"📞 Frontend llama a: {nombre_funcion}({args})")
        
        if nombre_funcion == "balanceOf":
            resultado = self.contrato.balance_of(args[0])
            print(f"   ✅ Resultado: {resultado}\n")
            return resultado
        elif nombre_funcion == "transfer":
            exito, msg = self.contrato.transfer(args[0], args[1], args[2])
            print(f"   {'✅' if exito else '❌'} {msg}\n")
            return exito


class EthersJS:
    """Simula la librería ethers.js"""
    
    def __init__(self):
        self.provider = None
        self.signer = None
        print("🔌 ethers.js inicializado\n")
    
    def conectar_wallet(self, wallet_address):
        """Simula conexión con MetaMask"""
        self.provider = "Ethereum Mainnet"
        self.signer = wallet_address
        print(f"🦊 MetaMask conectado: {wallet_address}")
        print(f"   Provider: {self.provider}\n")
    
    def crear_contrato(self, direccion, abi):
        """Crea instancia de contrato"""
        print(f"📜 Creando instancia de contrato en {direccion}")
        return abi


class Web3JS:
    """Simula la librería web3.js (alternativa a ethers.js)"""
    
    def __init__(self):
        self.web3 = None
        print("🌐 web3.js inicializado\n")
    
    def conectar(self, provider_url):
        self.web3 = provider_url
        print(f"   Conectado a: {provider_url}\n")
    
    def get_balance(self, address):
        print(f"💰 Balance de {address}: 1.5 ETH\n")
        return 1.5


class Moralis:
    """Simula Moralis (Backend-as-a-Service)"""
    
    def __init__(self):
        self.usuarios = {}
        self.contratos = {}
        print("⚡ Moralis inicializado (BaaS)\n")
    
    def autenticar_usuario(self, wallet_address):
        """Autenticación con wallet (sin passwords)"""
        user_id = hashlib.sha256(wallet_address.encode()).hexdigest()[:16]
        self.usuarios[wallet_address] = user_id
        print(f"🔐 Usuario autenticado: {wallet_address}")
        print(f"   User ID: {user_id}\n")
        return user_id
    
    def guardar_dato(self, tabla, dato):
        """Guardar en base de datos descentralizada"""
        print(f"💾 Guardando en tabla '{tabla}': {dato}\n")
    
    def escuchar_eventos(self, contrato, evento):
        """Websocket para escuchar eventos en tiempo real"""
        print(f"👂 Escuchando evento '{evento}' en {contrato}")
        print(f"   📡 Evento recibido: Transferencia de 100 tokens\n")


# --- Simulación ---
print("=== dApps y Librerias Cliente ===\n")

# Crear contrato
contrato = SmartContractSimulado("MiToken", "0x1234...abcd")
abi = ABI(contrato)

# Simular frontend con ethers.js
print("--- Frontend con ethers.js ---")
ethers = EthersJS()
ethers.conectar_wallet("0xAlice")
instancia = ethers.crear_contrato("0x1234...abcd", abi)
instancia.llamar_funcion("balanceOf", ["0xAlice"])
instancia.llamar_funcion("transfer", ["0xAlice", "0xBob", 100])

# Simular web3.js
print("\n--- Alternativa con web3.js ---")
web3 = Web3JS()
web3.conectar("https://mainnet.infura.io/v3/...")
web3.get_balance("0xAlice")

# Simular Moralis
print("\n--- Backend con Moralis ---")
moralis = Moralis()
moralis.autenticar_usuario("0xAlice")
moralis.guardar_dato("transacciones", {"de": "0xAlice", "a": "0xBob", "monto": 100})
moralis.escuchar_eventos("0x1234...abcd", "Transfer")

print("="*60)
print("🎓 CONCEPTOS CLAVE:")
print("1. dApp = Frontend + Blockchain (sin servidor central)")
print("2. ethers.js = librería moderna y ligera (recomendada)")
print("3. web3.js = librería original (legacy)")
print("4. Moralis = BaaS para blockchain (rápido desarrollo)")
print("5. ABI = traductor entre JavaScript y Solidity")
print("6. Provider = conexión a la red blockchain")
print("7. Signer = wallet que firma transacciones")