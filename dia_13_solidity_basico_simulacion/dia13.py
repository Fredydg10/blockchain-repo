class HolaMundoContrato:
    """Simulación de un contrato Solidity en Python"""
    
    def __init__(self, deployer_address):
        # Variables de estado (como en Solidity)
        self.mensaje = "¡Hola Mundo desde Blockchain!"
        self.owner = deployer_address
        self.contador_saludos = 0
        self.eventos = []
        
        print(f"📜 Contrato HolaMundo desplegado")
        print(f"   Owner: {self.owner}")
        print(f"   Mensaje inicial: '{self.mensaje}'")
        print(f"   Contador: {self.contador_saludos}\n")
    
    def cambiar_mensaje(self, caller_address, nuevo_mensaje):
        """Simula: function cambiarMensaje(string memory _nuevoMensaje) public"""
        print(f"📝 {caller_address} llama a cambiarMensaje('{nuevo_mensaje}')")
        
        # Actualizar estado
        self.mensaje = nuevo_mensaje
        self.contador_saludos += 1
        
        # Emitir evento (como en Solidity: emit SaludoEnviado(...))
        evento = {
            'nombre': 'SaludoEnviado',
            'de': caller_address,
            'mensaje': nuevo_mensaje
        }
        self.eventos.append(evento)
        
        print(f"   ✅ Mensaje actualizado a: '{self.mensaje}'")
        print(f"   ✅ Contador: {self.contador_saludos}")
        print(f"   📡 Evento emitido: {evento}\n")
    
    def leer_mensaje(self):
        """Simula: function leerMensaje() public view returns (string memory)"""
        # view = solo lectura, no modifica estado, no gasta gas
        print(f"👀 Leyendo mensaje: '{self.mensaje}'")
        return self.mensaje
    
    def obtener_contador(self):
        """Simula: function obtenerContador() public view returns (uint256)"""
        print(f"🔢 Contador de saludos: {self.contador_saludos}")
        return self.contador_saludos
    
    def transferir_ownership(self, caller_address, nuevo_owner):
        """Simula: function transferirOwnership(address _nuevoOwner) public soloOwner"""
        print(f"🔄 {caller_address} intenta transferir ownership a {nuevo_owner}")
        
        # Modifier: soloOwner (require)
        if caller_address != self.owner:
            print(f"   ❌ Revertido: Solo el owner puede hacer esto")
            print(f"   Caller: {caller_address}")
            print(f"   Owner actual: {self.owner}\n")
            return False
        
        # Transferir ownership
        self.owner = nuevo_owner
        print(f"   ✅ Ownership transferido a {nuevo_owner}\n")
        return True

# --- Simulación ---
print("=== Solidity Basico - Simulacion ===\n")

# Desplegar contrato
deployer = "0x1234...abcd"
contrato = HolaMundoContrato(deployer)

# Leer datos (funciones view)
contrato.leer_mensaje()
contrato.obtener_contador()
print()

# Cambiar mensaje (función que modifica estado)
contrato.cambiar_mensaje("0x5678...efgh", "¡Hola Ethereum!")
contrato.cambiar_mensaje("0x9abc...ijkl", "¡Hola Solidity!")

# Intentar transferir ownership desde cuenta incorrecta
contrato.transferir_ownership("0x5678...efgh", "0x9abc...ijkl")  # Debería fallar

# Transferir ownership desde el owner correcto
contrato.transferir_ownership(deployer, "0x9abc...ijkl")  # Debería funcionar

# Verificar que el nuevo owner puede cambiar el mensaje
contrato.cambiar_mensaje("0x9abc...ijkl", "¡Ahora soy el nuevo owner!")

# Mostrar todos los eventos emitidos
print("\n--- Historial de Eventos ---")
for i, evento in enumerate(contrato.eventos, 1):
    print(f"{i}. {evento['nombre']}: {evento['de']} -> '{evento['mensaje']}'")

print("\n" + "="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. Variables de estado se guardan en blockchain (cuestan gas)")
print("2. Funciones view/read-only no modifican estado (gratis)")
print("3. Constructor se ejecuta una vez al desplegar")
print("4. Modifiers protegen funciones (ej: soloOwner)")
print("5. Events permiten escuchar cambios desde frontend")
print("6. msg.sender = dirección de quien llama la función")
print("7. require() revierte la transacción si falla la condición")