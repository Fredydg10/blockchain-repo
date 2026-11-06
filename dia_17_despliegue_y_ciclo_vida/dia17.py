import hashlib
import time
import random

class Contrato:
    """Simula un smart contract"""
    
    def __init__(self, nombre, version="1.0"):
        self.nombre = nombre
        self.version = version
        self.direccion = hashlib.sha256(f"{nombre}{time.time()}".encode()).hexdigest()[:42]
        self.codigo = f"contract {nombre} v{version}"
        self.balance = 0
        self.esta_desplegado = False
        self.red = None
        print(f"📜 Contrato '{nombre}' v{version} creado")
        print(f"   Dirección: 0x{self.direccion}\n")
    
    def desplegar(self, red):
        self.esta_desplegado = True
        self.red = red
        print(f"   ✅ Desplegado en {red}")
        print(f"   Dirección: 0x{self.direccion}\n")


class Testnet:
    """Simula una red de prueba (Sepolia, Mumbai)"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.contratos_desplegados = []
        self.eth_fake = 100  # ETH de prueba
        print(f"🧪 Testnet '{nombre}' inicializada")
        print(f"   ETH disponible: {self.eth_fake}\n")
    
    def obtener_eth_de_faucet(self, cantidad=10):
        """Obtener ETH fake de un faucet"""
        if cantidad <= self.eth_fake:
            self.eth_fake -= cantidad
            print(f"   💰 Faucet: +{cantidad} ETH (fake)")
            return cantidad
        print(f"   ❌ Faucet sin fondos suficientes")
        return 0
    
    def desplegar_contrato(self, contrato):
        """Desplegar contrato en testnet"""
        print(f"🚀 Desplegando '{contrato.nombre}' en {self.nombre}...")
        print(f"   ⛽ Gas estimado: {random.randint(500000, 2000000)} units")
        print(f"   ⛽ Costo: {random.uniform(0.01, 0.1):.4f} ETH")
        
        contrato.desplegar(self.nombre)
        self.contratos_desplegados.append(contrato)
        
        # Simular testing
        print(f"   🧪 Ejecutando tests en testnet...")
        print(f"   ✅ Todos los tests pasaron\n")


class Mainnet:
    """Red principal (dinero real)"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.contratos_desplegados = []
        print(f"🌐 Mainnet '{nombre}' inicializada")
        print(f"   ⚠️  DINERO REAL - Máxima precaución\n")
    
    def desplegar_contrato(self, contrato, auditoria_completada=True):
        """Desplegar en mainnet (requiere auditoría)"""
        print(f"🚀 Desplegando '{contrato.nombre}' en {self.nombre}...")
        
        if not auditoria_completada:
            print(f"   ❌ RECHAZADO: Auditoría de seguridad no completada")
            print(f"   ⚠️  NUNCA despliegues sin auditoría en mainnet\n")
            return False
        
        print(f"   ✅ Auditoría verificada")
        print(f"   ⛽ Gas estimado: {random.randint(500000, 2000000)} units")
        print(f"   ⛽ Costo: {random.uniform(0.1, 1.0):.4f} ETH (REAL)")
        
        contrato.desplegar(self.nombre)
        self.contratos_desplegados.append(contrato)
        return True


class Monitor:
    """Monitoreo post-despliegue"""
    
    def __init__(self, contrato):
        self.contrato = contrato
        self.alertas = []
        self.transacciones_monitoreadas = 0
        print(f"📡 Monitor activado para '{contrato.nombre}'\n")
    
    def verificar_balance(self):
        """Verifica que el balance del contrato sea correcto"""
        balance_esperado = random.randint(100, 1000)
        balance_real = balance_esperado + random.randint(-10, 10)
        
        print(f"💰 Verificando balance...")
        print(f"   Esperado: {balance_esperado} ETH")
        print(f"   Real: {balance_real} ETH")
        
        if abs(balance_real - balance_esperado) > 5:
            alerta = f"⚠️  ALERTA: Diferencia de balance detectada ({balance_real - balance_esperado} ETH)"
            self.alertas.append(alerta)
            print(f"   {alerta}")
        else:
            print(f"   ✅ Balance correcto\n")
        
        return balance_real
    
    def monitorear_eventos(self):
        """Monitorea eventos emitidos por el contrato"""
        self.transacciones_monitoreadas += 1
        eventos = random.randint(1, 10)
        print(f"📡 Transacción #{self.transacciones_monitoreadas}: {eventos} eventos emitidos")
        
        if eventos > 8:
            alerta = "⚠️  ALERTA: Volumen inusual de eventos"
            self.alertas.append(alerta)
            print(f"   {alerta}")
        else:
            print(f"   ✅ Eventos dentro de rango normal\n")
    
    def verificar_gas_usage(self):
        """Verifica consumo de gas"""
        gas_usado = random.randint(21000, 500000)
        limite = 300000
        
        print(f"⛽ Gas usado: {gas_usado:,} units")
        if gas_usado > limite:
            alerta = f"⚠️  ALERTA: Gas excesivo ({gas_usado:,} > {limite:,})"
            self.alertas.append(alerta)
            print(f"   {alerta}")
        else:
            print(f"   ✅ Gas dentro de límites\n")
    
    def reporte(self):
        """Genera reporte de monitoreo"""
        print(f"\n📊 REPORTE DE MONITOREO")
        print(f"   Contrato: {self.contrato.nombre}")
        print(f"   Transacciones monitoreadas: {self.transacciones_monitoreadas}")
        print(f"   Alertas activas: {len(self.alertas)}")
        for alerta in self.alertas:
            print(f"   - {alerta}")
        print()


class ProxyContract:
    """Contrato proxy para upgradeability"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.direccion = hashlib.sha256(f"proxy_{nombre}".encode()).hexdigest()[:42]
        self.implementacion_actual = None
        self.admin = 'creator'
        self.estado = {}  # Datos del contrato (balances, etc.)
        print(f"🔀 Proxy Contract '{nombre}' creado")
        print(f"   Dirección: 0x{self.direccion}")
        print(f"   Admin: {self.admin}\n")
    
    def set_implementation(self, nueva_implementacion, caller):
        """Actualiza la implementación (solo admin)"""
        print(f"🔄 Intentando actualizar implementación...")
        
        if caller != self.admin:
            print(f"   ❌ RECHAZADO: Solo el admin puede actualizar")
            print(f"   Caller: {caller}")
            print(f"   Admin: {self.admin}\n")
            return False
        
        version_anterior = self.implementacion_actual
        self.implementacion_actual = nueva_implementacion
        
        print(f"   ✅ Implementación actualizada")
        print(f"   Versión anterior: {version_anterior}")
        print(f"   Versión nueva: {nueva_implementacion}")
        print(f"   Estado preservado: {len(self.estado)} registros\n")
        return True
    
    def delegar_llamada(self, funcion, caller):
        """Delega la llamada a la implementación actual"""
        if not self.implementacion_actual:
            print(f"   ❌ No hay implementación asignada")
            return None
        
        print(f"📞 {caller} llama a '{funcion}'")
        print(f"   Proxy delega a: {self.implementacion_actual}")
        print(f"   ✅ Función ejecutada con estado preservado\n")
        return f"Resultado de {funcion}"


# --- Simulación del ciclo de vida completo ---
print("=== DESPLIEGUE Y CICLO DE VIDA ===\n")

print("--- Paso 1: Desarrollo Local ---")
contrato = Contrato("MiTokenDeFi", version="1.0")
print(f"   💻 Desarrollo en Hardhat/Foundry local")
print(f"   🧪 Tests unitarios: 15/15 pasaron")
print(f"   🧪 Tests de integración: 8/8 pasaron")
print(f"   📊 Coverage: 98%\n")

print("--- Paso 2: Despliegue en Testnet ---")
testnet = Testnet("Sepolia")
testnet.obtener_eth_de_faucet(10)
testnet.desplegar_contrato(contrato)
print(f"   🧪 Testing en testnet por 2 semanas")
print(f"   🐛 3 bugs encontrados y corregidos\n")

print("--- Paso 3: Auditoría de Seguridad ---")
print(f"   🔍 Auditoría con CertiK")
print(f"   📝 Reporte: 2 issues medios encontrados")
print(f"   ✅ Issues corregidos y re-auditados\n")

print("--- Paso 4: Despliegue en Mainnet ---")
mainnet = Mainnet("Ethereum")
mainnet.desplegar_contrato(contrato, auditoria_completada=True)

print("--- Paso 5: Monitoreo Post-Despliegue ---")
monitor = Monitor(contrato)
monitor.verificar_balance()
monitor.monitorear_eventos()
monitor.monitorear_eventos()
monitor.verificar_gas_usage()
monitor.reporte()

print("\n--- Bonus: Upgradeability con Proxy ---")
proxy = ProxyContract("MiTokenDeFi_Proxy")
proxy.set_implementation("MiTokenDeFi_v1.0", 'creator')
proxy.delegar_llamada("transfer", 'Alice')

# Intento de upgrade por no-admin
proxy.set_implementation("MiTokenDeFi_v2.0", 'hacker')  # Debe fallar

# Upgrade legítimo
proxy.set_implementation("MiTokenDeFi_v2.0", 'creator')
proxy.delegar_llamada("transfer", 'Bob')

print("="*60)
print("🎓 CONCEPTOS CLAVE:")
print("1. Flujo: Local → Testnet → Auditoría → Mainnet")
print("2. NUNCA despliegues en mainnet sin auditoría")
print("3. Testnets: Sepolia, Mumbai, Goerli (dinero fake)")
print("4. Monitoreo: balance, eventos, gas usage")
print("5. Herramientas: Tenderly, OpenZeppelin Defender, Etherscan")
print("6. Upgradeability: Proxy pattern permite 'actualizar' contratos")
print("7. Tipos de proxy: Transparent, UUPS, Diamond")
print("8. El estado se preserva, solo cambia la lógica")
print("9. Riesgo: si el admin del proxy es malicioso, puede romper todo")