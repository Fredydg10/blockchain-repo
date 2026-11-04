import hashlib
import random

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.blockchain = []  # Cada nodo tiene su copia
        self.conectado = True
    
    def agregar_bloque(self, bloque):
        """Agrega un bloque a su copia local"""
        self.blockchain.append(bloque)
        print(f"   📦 {self.nombre} agregó bloque #{len(self.blockchain)}")
    
    def verificar_integridad(self):
        """Verifica que su copia no haya sido modificada"""
        for i in range(1, len(self.blockchain)):
            bloque_actual = self.blockchain[i]
            bloque_anterior = self.blockchain[i-1]
            
            # Verificar que el hash anterior coincide
            if bloque_actual['hash_previo'] != bloque_anterior['hash']:
                print(f"   ❌ {self.nombre}: ¡Cadena corrupta en bloque #{i}!")
                return False
        
        print(f"   ✅ {self.nombre}: Cadena válida ({len(self.blockchain)} bloques)")
        return True

class RedDescentralizada:
    def __init__(self, num_nodos=5):
        self.nodos = [Nodo(f"Nodo-{i+1}") for i in range(num_nodos)]
        print(f"🌐 Red creada con {num_nodos} nodos\n")
    
    def crear_bloque(self, datos, hash_previo):
        """Crea un nuevo bloque"""
        bloque = {
            'datos': datos,
            'hash_previo': hash_previo,
            'hash': hashlib.sha256(f"{datos}{hash_previo}".encode()).hexdigest()
        }
        return bloque
    
    def propagar_bloque(self, bloque):
        """Envía el bloque a todos los nodos"""
        print(f"📡 Propagando bloque: '{bloque['datos']}'")
        for nodo in self.nodos:
            if nodo.conectado:
                nodo.agregar_bloque(bloque)
        print()
    
    def simular_ataque(self, nodo_idx, bloque_idx, nuevos_datos):
        """Simula que un nodo malicioso modifica un bloque"""
        print(f"🚨 ATACANTE: Modificando bloque #{bloque_idx} en {self.nodos[nodo_idx].nombre}")
        self.nodos[nodo_idx].blockchain[bloque_idx]['datos'] = nuevos_datos
        print(f"   Datos cambiados a: '{nuevos_datos}'\n")
    
    def detectar_y_corregir(self):
        """Los nodos honestos detectan y rechazan la copia corrupta"""
        print("🔍 Verificando integridad de todos los nodos...\n")
        
        nodos_validos = []
        nodos_invalidos = []
        
        for nodo in self.nodos:
            if nodo.verificar_integridad():
                nodos_validos.append(nodo)
            else:
                nodos_invalidos.append(nodo)
        
        print(f"\n📊 Resultado:")
        print(f"   Nodos válidos: {len(nodos_validos)}")
        print(f"   Nodos corruptos: {len(nodos_invalidos)}")
        
        if len(nodos_invalidos) > 0:
            print(f"\n⚠️  La red rechaza la copia de: {[n.nombre for n in nodos_invalidos]}")
            print("   Los nodos honestos mantienen la versión correcta.")

# --- Simulación ---
print("=== Simulación de Red Descentralizada ===\n")

red = RedDescentralizada(num_nodos=5)

# Crear bloque génesis (primer bloque)
bloque_genesis = {
    'datos': 'Bloque Génesis',
    'hash_previo': '0000000000000000000000000000000000000000000000000000000000000000',
    'hash': hashlib.sha256('Bloque Génesis'.encode()).hexdigest()
}

# Agregar bloque génesis a todos los nodos
for nodo in red.nodos:
    nodo.agregar_bloque(bloque_genesis)

print()

# Agregar más bloques
bloque1 = red.crear_bloque("Alice envía 1 BTC a Bob", bloque_genesis['hash'])
red.propagar_bloque(bloque1)

bloque2 = red.crear_bloque("Bob envía 0.5 BTC a Charlie", bloque1['hash'])
red.propagar_bloque(bloque2)

# Simular ataque
red.simular_ataque(nodo_idx=2, bloque_idx=1, nuevos_datos="Alice envía 100 BTC a Bob")

# Detectar y corregir
red.detectar_y_corregir()