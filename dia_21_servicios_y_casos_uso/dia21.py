import hashlib
import time

class NodeService:
    """Node as a Service (Alchemy, Infura, etc.)"""
    
    def __init__(self, nombre, requests_gratis):
        self.nombre = nombre
        self.requests_gratis = requests_gratis
        self.requests_usados = 0
        print(f"🔌 {nombre}")
        print(f"   Plan gratis: {requests_gratis:,} requests/mes\n")
    
    def hacer_request(self, metodo):
        self.requests_usados += 1
        print(f"   📡 {metodo} | Usados: {self.requests_usados:,}/{self.requests_gratis:,}")
        
        if self.requests_usados > self.requests_gratis:
            print(f"   ⚠️  Límite excedido - actualizar plan\n")
            return None
        return {"resultado": "ok"}


class NFT:
    """Non-Fungible Token"""
    
    def __init__(self, nombre, creador, precio_eth):
        self.nombre = nombre
        self.creador = creador
        self.precio_eth = precio_eth
        self.owner = creador
        self.token_id = hashlib.sha256(f"{nombre}{time.time()}".encode()).hexdigest()[:16]
        print(f"🎨 NFT '{nombre}' creado")
        print(f"   Token ID: {self.token_id}")
        print(f"   Creador: {creador} | Precio: {precio_eth} ETH\n")
    
    def vender(self, comprador, precio_eth):
        print(f"💰 Vendiendo '{self.nombre}' a {comprador} por {precio_eth} ETH")
        self.owner = comprador
        print(f"   ✅ Nuevo owner: {comprador}\n")


class DAO:
    """Organización Autónoma Descentralizada"""
    
    def __init__(self, nombre, treasury_eth):
        self.nombre = nombre
        self.treasury = treasury_eth
        self.miembros = {}
        self.propuestas = []
        print(f"🏛️  DAO '{nombre}' creada")
        print(f"   Treasury: {treasury_eth} ETH\n")
    
    def agregar_miembro(self, address, tokens):
        self.miembros[address] = tokens
        print(f"   👤 Miembro {address}: {tokens} tokens de gobernanza")
    
    def crear_propuesta(self, creador, descripcion):
        prop_id = len(self.propuestas) + 1
        self.propuestas.append({
            'id': prop_id,
            'descripcion': descripcion,
            'votos_a_favor': 0,
            'votos_en_contra': 0,
            'estado': 'activa'
        })
        print(f"\n📋 Propuesta #{prop_id}: {descripcion}")
    
    def votar(self, miembro, prop_id, voto):
        tokens = self.miembros.get(miembro, 0)
        prop = self.propuestas[prop_id - 1]
        
        if voto == 'si':
            prop['votos_a_favor'] += tokens
        else:
            prop['votos_en_contra'] += tokens
        
        print(f"   🗳️  {miembro} votó '{voto}' con {tokens} tokens")
    
    def ejecutar_propuesta(self, prop_id):
        prop = self.propuestas[prop_id - 1]
        if prop['votos_a_favor'] > prop['votos_en_contra']:
            prop['estado'] = 'aprobada'
            print(f"\n✅ Propuesta #{prop_id} APROBADA")
            print(f"   A favor: {prop['votos_a_favor']} | En contra: {prop['votos_en_contra']}")
        else:
            prop['estado'] = 'rechazada'
            print(f"\n❌ Propuesta #{prop_id} RECHAZADA")


class DeFiProtocol:
    """Protocolo DeFi (préstamos, exchange)"""
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # lending, dex, yield
        self.liquidez = 0
        print(f"💎 Protocolo DeFi: {nombre} ({tipo})\n")
    
    def depositar_liquidez(self, usuario, monto):
        self.liquidez += monto
        print(f"   💧 {usuario} depositó {monto} ETH")
        print(f"   Liquidez total: {self.liquidez} ETH\n")
    
    def pedir_prestamo(self, usuario, monto, colateral):
        if colateral < monto * 1.5:  # 150% colateralización
            print(f"   ❌ Colateral insuficiente (necesitas {monto*1.5} ETH)\n")
            return False
        print(f"   💸 {usuario} pidió {monto} ETH prestados")
        print(f"   Colateral bloqueado: {colateral} ETH\n")
        return True


class IPFS:
    """InterPlanetary File System - Almacenamiento descentralizado"""
    
    def __init__(self):
        self.archivos = {}
        print(f"🌐 IPFS inicializado")
        print(f"   Almacenamiento descentralizado P2P\n")
    
    def subir_archivo(self, contenido):
        cid = hashlib.sha256(contenido.encode()).hexdigest()[:46]
        self.archivos[cid] = contenido
        print(f"   📤 Archivo subido")
        print(f"   CID: {cid}")
        print(f"   Acceso: ipfs://{cid}\n")
        return cid
    
    def descargar_archivo(self, cid):
        contenido = self.archivos.get(cid, None)
        if contenido:
            print(f"   📥 Descargando {cid}...")
            print(f"   Contenido: {contenido[:50]}...\n")
        else:
            print(f"   ❌ Archivo no encontrado\n")
        return contenido


# --- Simulación ---
print("=== Servicios y Casos de Uso ===\n")

print("--- 1. Node as a Service ---")
alchemy = NodeService("Alchemy", 300_000_000)
alchemy.hacer_request("eth_getBalance")
alchemy.hacer_request("eth_sendTransaction")

print("\n--- 2. NFTs ---")
nft = NFT("CryptoPunk #7804", "LarvaLabs", 4200)
nft.vender("Collector_X", 5000)

print("\n--- 3. DAO ---")
dao = DAO("MiDAO", 1000)
dao.agregar_miembro("0xAlice", 100)
dao.agregar_miembro("0xBob", 150)
dao.agregar_miembro("0xCharlie", 80)
dao.crear_propuesta("0xAlice", "Invertir 200 ETH en protocolo X")
dao.votar("0xAlice", 1, 'si')
dao.votar("0xBob", 1, 'si')
dao.votar("0xCharlie", 1, 'no')
dao.ejecutar_propuesta(1)

print("\n--- 4. DeFi ---")
aave = DeFiProtocol("Aave", "lending")
aave.depositar_liquidez("Alice", 100)
aave.pedir_prestamo("Bob", 50, 80)  # Debería fallar (80 < 75)
aave.pedir_prestamo("Bob", 50, 100)  # Debería pasar

print("\n--- 5. IPFS ---")
ipfs = IPFS()
cid = ipfs.subir_archivo("Metadatos de mi NFT: imagen, nombre, descripción")
ipfs.descargar_archivo(cid)

print("="*60)
print("🎓 CONCEPTOS CLAVE:")
print("1. NaaS: Alchemy, Infura, QuickNode (no corras tu propio nodo)")
print("2. NFTs: Arte, gaming, música, tickets")
print("3. DAOs: Gobernanza descentralizada por tokens")
print("4. DeFi: Préstamos, exchanges, yield farming sin bancos")
print("5. IPFS: Almacenamiento descentralizado (CID único)")
print("6. Filecoin/Arweave: Incentivos económicos para almacenar")
print("7. El ecosistema crypto es mucho más que solo Bitcoin")