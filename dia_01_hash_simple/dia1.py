import hashlib

def generar_hash(texto):
    # Codificamos el texto a bytes y aplicamos SHA-256
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

# Prueba 1: Texto original
texto_original = "Alice envia 1 BTC a Bob"
print(f"Texto: '{texto_original}'")
print(f"Hash:  {generar_hash(texto_original)}\n")

# Prueba 2: Cambiamos un solo carácter (1 por 2)
texto_modificado = "Alice envia 2 BTC a Bob"
print(f"Texto: '{texto_modificado}'")
print(f"Hash:  {generar_hash(texto_modificado)}\n")

# Observa cómo el hash cambia completamente, aunque solo cambió un número.