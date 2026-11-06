class StackBlockchain:
    """Representa el stack completo de un desarrollador blockchain"""
    
    def __init__(self):
        self.capas = {
            'Frontend': {'lenguaje': 'JavaScript/TypeScript', 'herramientas': ['React', 'Next.js', 'Vue']},
            'Conexión Blockchain': {'lenguaje': 'JavaScript', 'herramientas': ['ethers.js', 'web3.js', 'wagmi']},
            'Smart Contracts': {'lenguaje': 'Solidity/Rust', 'herramientas': ['Hardhat', 'Foundry', 'Remix']},
            'Backend/API': {'lenguaje': 'Python/Node.js', 'herramientas': ['FastAPI', 'Express', 'GraphQL']},
            'Data/Analytics': {'lenguaje': 'Python', 'herramientas': ['pandas', 'Dune Analytics', 'The Graph']},
            'Infraestructura': {'lenguaje': 'Go', 'herramientas': ['Docker', 'Kubernetes', 'geth']},
            'Testing': {'lenguaje': 'Solidity/JS', 'herramientas': ['Foundry', 'Hardhat', 'Echidna']}
        }
        print("🏗️  Stack Completo de Desarrollador Blockchain\n")
    
    def mostrar_stack(self):
        for i, (capa, info) in enumerate(self.capas.items(), 1):
            print(f"{i}. {capa}")
            print(f"   Lenguaje: {info['lenguaje']}")
            print(f"   Herramientas: {', '.join(info['herramientas'])}\n")
    
    def ruta_aprendizaje(self, perfil):
        print(f"🎯 Ruta recomendada para perfil: {perfil}\n")
        
        rutas = {
            'Frontend dApps': ['JavaScript', 'React', 'ethers.js', 'Next.js'],
            'Smart Contract Dev': ['Solidity', 'Hardhat/Foundry', 'OpenZeppelin', 'Testing'],
            'Backend Blockchain': ['Python', 'Node.js', 'Web3.py', 'APIs'],
            'Data Analyst': ['Python', 'pandas', 'SQL', 'Dune Analytics'],
            'Full Stack Web3': ['JavaScript', 'Solidity', 'Python', 'ethers.js', 'React'],
            'Blockchain Core': ['Rust', 'Go', 'Criptografía', 'Consenso']
        }
        
        if perfil in rutas:
            print(f"   Aprende en este orden:")
            for i, tech in enumerate(rutas[perfil], 1):
                print(f"   {i}. {tech}")
        else:
            print(f"   Perfil no encontrado")
        print()


class ProyectoFullStack:
    """Simula un proyecto blockchain full stack"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"🚀 Proyecto: {nombre}\n")
    
    def desarrollar_frontend(self):
        print(f"📱 Frontend (JavaScript/React):")
        print(f"   - UI para conectar wallet")
        print(f"   - Mostrar balances y transacciones")
        print(f"   - Formularios para interactuar con contratos\n")
    
    def desarrollar_contrato(self):
        print(f"📜 Smart Contract (Solidity):")
        print(f"   - Lógica de negocio en blockchain")
        print(f"   - Tests con Foundry")
        print(f"   - Auditoría de seguridad\n")
    
    def desarrollar_backend(self):
        print(f"⚙️  Backend (Python/Node.js):")
        print(f"   - API para indexar datos on-chain")
        print(f"   - Webhooks para eventos")
        print(f"   - Caché con Redis\n")
    
    def analizar_datos(self):
        print(f"📊 Análisis (Python):")
        print(f"   - Dashboard de métricas")
        print(f"   - Detección de patrones")
        print(f"   - Reportes automáticos\n")
    
    def desplegar(self):
        print(f"🌐 Despliegue (Go/DevOps):")
        print(f"   - Contrato en Ethereum mainnet")
        print(f"   - Frontend en Vercel/IPFS")
        print(f"   - Backend en AWS/Docker\n")


# --- Simulación ---
print("=== Lenguajes de Apoyo - Stack Completo ===\n")

stack = StackBlockchain()
stack.mostrar_stack()

print("\n--- Rutas de Aprendizaje ---")
stack.ruta_aprendizaje("Full Stack Web3")
stack.ruta_aprendizaje("Smart Contract Dev")
stack.ruta_aprendizaje("Data Analyst")

print("\n--- Proyecto Full Stack: DEX Descentralizado ---")
proyecto = ProyectoFullStack("MiDEX")
proyecto.desarrollar_frontend()
proyecto.desarrollar_contrato()
proyecto.desarrollar_backend()
proyecto.analizar_datos()
proyecto.desplegar()

print("="*60)
print("🎓 CONCEPTOS CLAVE:")
print("1. JavaScript/TS: 95% de frontends de dApps")
print("2. Python: Análisis, bots, backend, data science")
print("3. Go: Infraestructura y blockchains custom")
print("4. Rust: Máximo rendimiento (Solana, contratos críticos)")
print("5. Solidity: Estándar para Ethereum/EVM")
print("6. No necesitas saber TODOS, elige según tu perfil")
print("7. Full Stack Web3 = JS + Solidity + Python (mínimo)")
print("8. El mercado paga $80K-$200K por estos skills")