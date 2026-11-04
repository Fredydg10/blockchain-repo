# Importaciones de la librería cryptography para generar claves públicas y privadas, y para firmar y verificar mensajes.
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import utils
import hashlib

print("=== Demostración de Firmas Digitales ===\n")

# 1. Generar par de claves (privada y pública)
private_key = ec.generate_private_key(ec.SECP256K1())  # La misma curva que usa Bitcoin
public_key = private_key.public_key()

print("🔑 Clave Privada generada (NO COMPARTIR):")
print(f"   Tipo: {private_key.key_size} bits")
print(f"   Curva: SECP256K1 (usada en Bitcoin)\n")

print("🔓 Clave Pública generada (se puede compartir):")
print(f"   Tipo: {public_key.key_size} bits\n")

# 2. Crear un mensaje (transacción)
mensaje = "Alice envía 1 BTC a Bob - Bloque #12345"
print(f"📝 Mensaje a firmar: '{mensaje}'\n")

# 3. Firmar el mensaje con la clave privada
firma = private_key.sign(
    mensaje.encode('utf-8'),
    ec.ECDSA(hashes.SHA256())
)

print("✍️  Mensaje firmado con clave privada:")
print(f"   Firma (hex): {firma.hex()[:64]}...\n")

# 4. Verificar la firma con la clave pública
try:
    public_key.verify(
        firma,
        mensaje.encode('utf-8'),
        ec.ECDSA(hashes.SHA256())
    )
    print("✅ Firma VÁLIDA - La transacción es auténtica")
except Exception as e:
    print(f"❌ Firma INVÁLIDA: {e}")

# 5. Simular un ataque: alguien modifica el mensaje
mensaje_modificado = "Alice envía 100 BTC a Bob - Bloque #12345"
print(f"\n🚨 Ataque: Alguien modificó el mensaje a: '{mensaje_modificado}'")

try:
    public_key.verify(
        firma,  # Usamos la firma original
        mensaje_modificado.encode('utf-8'),  # Pero con el mensaje modificado
        ec.ECDSA(hashes.SHA256())
    )
    print("✅ Firma VÁLIDA")
except Exception as e:
    print(f"❌ Firma INVÁLIDA - ¡El ataque fue detectado!")