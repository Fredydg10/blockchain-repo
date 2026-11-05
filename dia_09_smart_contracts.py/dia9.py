# Importaciones de la librería hashlib para generar hashes de claves privadas y direcciones, y de la librería time para medir el tiempo de ejecución de los smart contracts.
import hashlib
import time

class SmartContract:
    def __init__(self, creador, codigo):
        self.creador = creador
        self.codigo = codigo
        self.direccion = hashlib.sha256(f"{creador}{codigo}{time.time()}".encode()).hexdigest()[:42]
        self.balance_eth = 0
        self.es_inmutable = True
        self.estado = "Desplegado"
        print(f"📜 Smart Contract desplegado:")
        print(f"   Dirección: 0x{self.direccion}")
        print(f"   Creador: {creador}")
        print(f"   Código: {codigo[:50]}...")
        print(f"   ⚠️  INMUTABLE: No se puede modificar\n")

class ContratoVenta(SmartContract):
    """Simula una venta automática: si pagas X, recibes Y"""
    
    def __init__(self, creador, precio_eth, item):
        codigo = f"if msg.value >= {precio_eth}: transfer(item, msg.sender)"
        super().__init__(creador, codigo)
        self.precio_eth = precio_eth
        self.item = item
        self.ventas_realizadas = 0
        print(f"   Precio: {precio_eth} ETH")
        print(f"   Item: {item}\n")
    
    def comprar(self, comprador, pago_eth):
        """Simula una compra"""
        print(f"🛒 {comprador} intenta comprar '{self.item}' por {pago_eth} ETH...")
        
        # CODE IS LAW: el código decide, no hay apelación
        if pago_eth >= self.precio_eth:
            self.balance_eth += self.precio_eth
            self.ventas_realizadas += 1
            print(f"   ✅ Venta exitosa!")
            print(f"   {comprador} recibió: {self.item}")
            print(f"   Balance del contrato: {self.balance_eth} ETH\n")
            return True
        else:
            print(f"   ❌ Fondos insuficientes. Se requieren {self.precio_eth} ETH")
            print(f"   El código rechaza la transacción automáticamente.\n")
            return False

class ContratoSubasta(SmartContract):
    """Simula una subasta: el mayor postor gana"""
    
    def __init__(self, creador, item, duracion_segundos=10):
        codigo = f"highest_bidder wins '{item}' after {duracion_segundos}s"
        super().__init__(creador, codigo)
        self.item = item
        self.mayor_postor = None
        self.mayor_oferta = 0
        self.postores = []
        self.activa = True
        print(f"   Item en subasta: {item}")
        print(f"   Duración: {duracion_segundos} segundos\n")
    
    def postular(self, postor, oferta_eth):
        """Recibe una oferta"""
        if not self.activa:
            print(f"   ❌ Subasta finalizada")
            return False
        
        if oferta_eth > self.mayor_oferta:
            # Devolver dinero al postor anterior (si existe)
            if self.mayor_postor:
                print(f"   💰 {self.mayor_postor} fue superado. Su oferta de {self.mayor_oferta} ETH será devuelta.")
            
            self.mayor_postor = postor
            self.mayor_oferta = oferta_eth
            self.postores.append({'nombre': postor, 'oferta': oferta_eth})
            print(f"   📈 Nueva oferta: {postor} ofrece {oferta_eth} ETH")
            return True
        else:
            print(f"   ❌ Oferta de {postor} ({oferta_eth} ETH) es menor que {self.mayor_oferta} ETH")
            return False
    
    def finalizar_subasta(self):
        """Finaliza la subasta y declara ganador"""
        self.activa = False
        print(f"\n🏆 Subasta finalizada!")
        print(f"   Ganador: {self.mayor_postor}")
        print(f"   Precio final: {self.mayor_oferta} ETH")
        print(f"   Item '{self.item}' transferido a {self.mayor_postor}")
        print(f"   Total de postores: {len(self.postores)}\n")

# --- Simulación ---
print("=== Simulación de Smart Contracts ===\n")

print("--- Contrato de Venta Automática ---")
contrato_venta = ContratoVenta(
    creador="Alice",
    precio_eth=0.5,
    item="NFT #1234"
)

contrato_venta.comprar("Bob", 0.5)
contrato_venta.comprar("Charlie", 0.3)  # Debería fallar
contrato_venta.comprar("David", 1.0)    # Debería funcionar

print("\n--- Contrato de Subasta ---")
subasta = ContratoSubasta(
    creador="Alice",
    item="CryptoPunk #7804",
    duracion_segundos=10
)

subasta.postular("Bob", 10)
subasta.postular("Charlie", 15)
subasta.postular("David", 12)  # Debería fallar
subasta.postular("Eve", 20)

subasta.finalizar_subasta()

print("\n" + "="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. Code is Law: El código se ejecuta sin excepciones")
print("2. Inmutabilidad: Una vez desplegado, no se puede cambiar")
print("3. Transparencia: Todos pueden ver el código")
print("4. Automatización: No necesita intermediarios")
print("5. Riesgo: Bugs en el código = pérdidas irreversibles")