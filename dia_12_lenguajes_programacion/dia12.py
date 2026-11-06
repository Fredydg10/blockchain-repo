class LenguajeBlockchain:
    def __init__(self, nombre, blockchain, dificultad, casos_uso):
        self.nombre = nombre
        self.blockchain = blockchain
        self.dificultad = dificultad  # 1-5
        self.casos_uso = casos_uso
        self.desarrolladores = 0
    
    def mostrar_info(self):
        print(f"📝 {self.nombre}")
        print(f"   Blockchain: {self.blockchain}")
        print(f"   Dificultad: {'⭐' * self.dificultad}")
        print(f"   Casos de uso: {', '.join(self.casos_uso)}")
        print(f"   Desarrolladores activos: {self.desarrolladores:,}\n")

class Proyecto:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # Token, NFT, DeFi, Blockchain completa
        self.lenguaje_recomendado = None
    
    def seleccionar_lenguaje(self, lenguajes_disponibles):
        """Selecciona el mejor lenguaje según el tipo de proyecto"""
        print(f"🎯 Proyecto: {self.nombre} ({self.tipo})")
        
        if self.tipo == "Token ERC-20":
            self.lenguaje_recomendado = "Solidity"
        elif self.tipo == "NFT Collection":
            self.lenguaje_recomendado = "Solidity"
        elif self.tipo == "DeFi Protocol":
            self.lenguaje_recomendado = "Solidity"
        elif self.tipo == "High-Frequency Trading":
            self.lenguaje_recomendado = "Rust"
        elif self.tipo == "Blockchain Custom":
            self.lenguaje_recomendado = "Go"
        elif self.tipo == "Secure Vault":
            self.lenguaje_recomendado = "Vyper"
        
        print(f"   ✅ Lenguaje recomendado: {self.lenguaje_recomendado}\n")
        return self.lenguaje_recomendado

# --- Simulación ---
print("=== Lenguajes de Programacion para Blockchain ===\n")

# Crear lenguajes
solidity = LenguajeBlockchain(
    "Solidity", 
    "Ethereum, BSC, Polygon", 
    3, 
    ["Tokens ERC-20", "NFTs", "DeFi", "DAOs"]
)
solidity.desarrolladores = 250000

vyper = LenguajeBlockchain(
    "Vyper", 
    "Ethereum", 
    2, 
    ["Contratos seguros", "Vaults", "Protocolos DeFi simples"]
)
vyper.desarrolladores = 15000

rust = LenguajeBlockchain(
    "Rust", 
    "Solana, NEAR, Polkadot", 
    5, 
    ["Alto rendimiento", "Gaming", "DEX rápidos"]
)
rust.desarrolladores = 80000

go = LenguajeBlockchain(
    "Go", 
    "Cosmos, Hyperledger", 
    3, 
    ["Blockchains custom", "Infraestructura", "Nodos"]
)
go.desarrolladores = 120000

# Mostrar info de cada lenguaje
print("--- Lenguajes Disponibles ---\n")
solidity.mostrar_info()
vyper.mostrar_info()
rust.mostrar_info()
go.mostrar_info()

# Simular selección de lenguaje para diferentes proyectos
print("--- Selección de Lenguaje para Proyectos ---\n")

proyectos = [
    Proyecto("Mi Token Meme", "Token ERC-20"),
    Proyecto("Colección NFT de Arte", "NFT Collection"),
    Proyecto("Protocolo de Préstamos", "DeFi Protocol"),
    Proyecto("Exchange de Alta Frecuencia", "High-Frequency Trading"),
    Proyecto("Mi Propia Blockchain", "Blockchain Custom"),
    Proyecto("Bóveda de Fondos Segura", "Secure Vault")
]

for proyecto in proyectos:
    proyecto.seleccionar_lenguaje([solidity, vyper, rust, go])

print("="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. Solidity = estándar de la industria (80% del mercado)")
print("2. Vyper = seguridad sobre flexibilidad")
print("3. Rust = máximo rendimiento (Solana)")
print("4. Go = para construir blockchains completas (Cosmos)")
print("5. Elige según tu proyecto, no según moda")