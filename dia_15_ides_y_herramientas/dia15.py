class ContratoSimulado:
    """Simula un smart contract para análisis de seguridad"""
    
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.vulnerabilidades = []
        self.esta_auditado = False
        print(f"📜 Contrato '{nombre}' cargado para análisis")
        print(f"   Código: {len(codigo)} líneas\n")
    
    def agregar_vulnerabilidad(self, tipo, severidad, descripcion):
        self.vulnerabilidades.append({
            'tipo': tipo,
            'severidad': severidad,
            'descripcion': descripcion
        })


class SlitherAnalyzer:
    """Análisis estático de código (como Slither real)"""
    
    def __init__(self):
        self.nombre = "Slither"
        print(f"🔍 Iniciando {self.nombre} (análisis estático)\n")
    
    def analizar(self, contrato):
        print(f"Analizando '{contrato.nombre}'...")
        
        # Simular detección de vulnerabilidades comunes
        if 'require' not in contrato.codigo.lower():
            contrato.agregar_vulnerabilidad(
                "Missing Require",
                "ALTA",
                "Funciones sin validación de permisos"
            )
        
        if 'transfer' in contrato.codigo.lower() and 'reentrancy' not in contrato.codigo.lower():
            contrato.agregar_vulnerabilidad(
                "Reentrancy",
                "CRÍTICA",
                "Posible ataque de reentrada en función de transferencia"
            )
        
        if 'overflow' not in contrato.codigo.lower() and 'safeMath' not in contrato.codigo.lower():
            contrato.agregar_vulnerabilidad(
                "Integer Overflow",
                "MEDIA",
                "Operaciones matemáticas sin protección"
            )
        
        print(f"   Vulnerabilidades encontradas: {len(contrato.vulnerabilidades)}")
        for vuln in contrato.vulnerabilidades:
            print(f"   ⚠️  [{vuln['severidad']}] {vuln['tipo']}: {vuln['descripcion']}")
        print()


class EchidnaFuzzer:
    """Fuzzing: prueba con inputs aleatorios (como Echidna real)"""
    
    def __init__(self):
        self.nombre = "Echidna"
        print(f"🎲 Iniciando {self.nombre} (fuzzing)\n")
    
    def fuzz(self, contrato, num_tests=1000):
        print(f"Ejecutando {num_tests} tests aleatorios en '{contrato.nombre}'...")
        
        import random
        bugs_encontrados = 0
        
        for i in range(num_tests):
            # Simular input aleatorio
            input_aleatorio = random.randint(-1000000, 1000000)
            
            # Simular detección de bug (1% de probabilidad)
            if random.random() < 0.01:
                bugs_encontrados += 1
                contrato.agregar_vulnerabilidad(
                    "Fuzzing Bug",
                    "ALTA",
                    f"Input {input_aleatorio} causa comportamiento inesperado"
                )
        
        print(f"   Tests ejecutados: {num_tests}")
        print(f"   Bugs encontrados: {bugs_encontrados}")
        print(f"   Resultado: {'❌ CONTRATO INSEGURO' if bugs_encontrados > 0 else '✅ PASÓ FUZZING'}\n")


class MythXAnalyzer:
    """Análisis en la nube (como MythX real)"""
    
    def __init__(self):
        self.nombre = "MythX"
        print(f"☁️  Iniciando {self.nombre} (análisis cloud)\n")
    
    def analizar(self, contrato):
        print(f"Enviando '{contrato.nombre}' a análisis cloud...")
        print(f"   ⏳ Esperando resultados...")
        print(f"   ✅ Análisis completado")
        print(f"   Score de seguridad: {random.randint(40, 95)}/100")
        print(f"   Recomendación: {'Auditoría profesional requerida' if random.random() < 0.7 else 'Listo para testnet'}\n")


class OpenZeppelinLibrary:
    """Biblioteca de contratos seguros"""
    
    def __init__(self):
        self.contratos_disponibles = [
            "ERC20.sol (token fungible seguro)",
            "ERC721.sol (NFT seguro)",
            "Ownable.sol (control de ownership)",
            "ReentrancyGuard.sol (protección contra reentrada)",
            "SafeMath.sol (operaciones matemáticas seguras)"
        ]
        print(f"📚 OpenZeppelin Library cargada")
        print(f"   Contratos disponibles: {len(self.contratos_disponibles)}\n")
    
    def mostrar_contratos(self):
        print("Contratos auditados disponibles:")
        for contrato in self.contratos_disponibles:
            print(f"   ✅ {contrato}")
        print()
    
    def recomendacion(self, tipo_proyecto):
        print(f"🎯 Para tu proyecto '{tipo_proyecto}':")
        if "token" in tipo_proyecto.lower():
            print(f"   Usa: ERC20.sol + SafeMath.sol")
        elif "nft" in tipo_proyecto.lower():
            print(f"   Usa: ERC721.sol + Ownable.sol")
        elif "defi" in tipo_proyecto.lower():
            print(f"   Usa: ReentrancyGuard.sol + SafeMath.sol + Ownable.sol")
        print(f"   ⚠️  NUNCA escribas estos contratos desde cero\n")


# --- Simulación ---
print("=== IDEs Y HERRAMIENTAS DE SEGURIDAD ===\n")

print("--- Paso 1: Crear contrato (con bugs intencionales) ---")
contrato_buggy = ContratoSimulado(
    "MiTokenInseguro",
    """
    contract MiToken {
        mapping(address => uint) balances;
        
        function transfer(address to, uint amount) public {
            balances[msg.sender] -= amount;
            balances[to] += amount;
        }
    }
    """
)

print("--- Paso 2: Análisis con Slither ---")
slither = SlitherAnalyzer()
slither.analizar(contrato_buggy)

print("--- Paso 3: Fuzzing con Echidna ---")
echidna = EchidnaFuzzer()
echidna.fuzz(contrato_buggy, num_tests=1000)

print("--- Paso 4: Análisis cloud con MythX ---")
import random
mythx = MythXAnalyzer()
mythx.analizar(contrato_buggy)

print("--- Paso 5: Solución con OpenZeppelin ---")
oz = OpenZeppelinLibrary()
oz.mostrar_contratos()
oz.recomendacion("Token DeFi")

print("--- Paso 6: Contrato corregido con OpenZeppelin ---")
contrato_seguro = ContratoSimulado(
    "MiTokenSeguro",
    """
    import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
    import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
    
    contract MiToken is ERC20, ReentrancyGuard {
        constructor() ERC20("MiToken", "MTK") {}
        
        function safeTransfer(address to, uint amount) 
            external nonReentrant {
            _transfer(msg.sender, to, amount);
        }
    }
    """
)

slither2 = SlitherAnalyzer()
slither2.analizar(contrato_seguro)

print("="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. Remix = aprender y prototipar")
print("2. Hardhat = proyectos profesionales (JavaScript)")
print("3. Foundry = máximo rendimiento (Rust)")
print("4. OpenZeppelin = NUNCA reinventes la rueda")
print("5. Slither = análisis estático rápido")
print("6. Echidna = fuzzing (inputs aleatorios)")
print("7. MythX = análisis cloud completo")
print("8. Flujo: Slither → Echidna → Auditoría → Testnet → Mainnet")
