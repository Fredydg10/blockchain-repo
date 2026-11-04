# Importaciones de hashlib y time
import hashlib
import time

def simulacion_proof_of_work(datos_bloque, dificultad=3):
    # La dificultad define cuántos ceros debe tener el hash al inicio
    prefijo_objetivo = "0" * dificultad
    nonce = 0
    
    print(f"🔨 Minando bloque... (Buscando hash que empiece con '{prefijo_objetivo}')")
    inicio = time.time()
    
    while True:
        # Combinamos los datos del bloque con el nonce que estamos probando
        texto_a_hashear = f"{datos_bloque}{nonce}"
        hash_resultante = hashlib.sha256(texto_a_hashear.encode('utf-8')).hexdigest()
        
        # Verificamos si cumple la condición
        if hash_resultante.startswith(prefijo_objetivo):
            fin = time.time()
            print(f"✅ ¡BLOQUE MINADO CON ÉXITO!")
            print(f"   Nonce encontrado: {nonce}")
            print(f"   Hash resultante:  {hash_resultante}")
            print(f"   Intentos totales: {nonce + 1}")
            print(f"   Tiempo tardado:   {fin - inicio:.4f} segundos")
            return nonce
        
        # Si no cumple, probamos con el siguiente número
        nonce += 1

# --- Ejecución ---
datos_del_bloque = "Bloque #2: Alice envia 5 BTC a Bob | Hash Anterior: 0000abc..."
print(f"Datos a procesar: '{datos_del_bloque}'\n")

# Puedes cambiar la dificultad a 4 o 5 para ver cómo tarda mucho más (¡cuidado si pones 6!)
simulacion_proof_of_work(datos_del_bloque, dificultad=3)