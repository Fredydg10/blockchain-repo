import random

class TokenContract:
    """Contrato simulado con bugs intencionales para testing"""
    
    def __init__(self, nombre, simbolo, supply):
        self.nombre = nombre
        self.simbolo = simbolo
        self.total_supply = supply
        self.balances = {'creator': supply}
        self.allowances = {}
        self.paused = False
    
    def transfer(self, from_addr, to_addr, amount):
        """Transferir tokens - CON BUG INTENCIONAL"""
        # BUG: No verifica si from_addr tiene fondos suficientes
        if self.paused:
            return False, "Contrato pausado"
        
        self.balances[from_addr] = self.balances.get(from_addr, 0) - amount
        self.balances[to_addr] = self.balances.get(to_addr, 0) + amount
        return True, "Transferencia exitosa"
    
    def balance_of(self, address):
        return self.balances.get(address, 0)
    
    def pause(self, admin):
        if admin == 'creator':
            self.paused = True
            return True
        return False


class TestRunner:
    """Simula un framework de testing como Foundry/Hardhat"""
    
    def __init__(self):
        self.tests_pasados = 0
        self.tests_fallidos = 0
        self.tests_totales = 0
        self.cobertura_lineas = set()
        self.total_lineas = 0
    
    def run_test(self, nombre_test, funcion_test):
        """Ejecuta un test individual"""
        self.tests_totales += 1
        print(f"🧪 Ejecutando: {nombre_test}")
        
        try:
            resultado = funcion_test()
            if resultado:
                self.tests_pasados += 1
                print(f"   ✅ PASÓ\n")
            else:
                self.tests_fallidos += 1
                print(f"   ❌ FALLÓ\n")
        except Exception as e:
            self.tests_fallidos += 1
            print(f"   ❌ FALLÓ con excepción: {e}\n")
    
    def calcular_cobertura(self):
        """Calcula % de código cubierto por tests"""
        if self.total_lineas == 0:
            return 0
        cobertura = (len(self.cobertura_lineas) / self.total_lineas) * 100
        return min(cobertura, 100)
    
    def reporte_final(self):
        """Genera reporte estilo Foundry/Hardhat"""
        print("\n" + "="*60)
        print("📊 REPORTE DE TESTS")
        print("="*60)
        print(f"Total de tests:    {self.tests_totales}")
        print(f"Pasados:           {self.tests_pasados} ✅")
        print(f"Fallidos:          {self.tests_fallidos} ❌")
        print(f"Cobertura:         {self.calcular_cobertura():.1f}%")
        print(f"Estado:            {'✅ TODOS PASARON' if self.tests_fallidos == 0 else '❌ HAY TESTS FALLIDOS'}")
        print("="*60)


# --- Tests Unitarios ---
print("=== Pruebas de Contratos ===\n")

print("--- Unit Tests para TokenContract ---\n")

test_runner = TestRunner()
test_runner.total_lineas = 10  # Simulado

# Test 1: Transferencia básica
def test_transferencia_basica():
    token = TokenContract("Test", "TST", 1000)
    exito, msg = token.transfer('creator', 'Alice', 100)
    test_runner.cobertura_lineas.update([1, 2, 3])
    return exito and token.balance_of('Alice') == 100

test_runner.run_test("test_transferencia_basica", test_transferencia_basica)

# Test 2: Transferencia con fondos insuficientes (DEBERÍA FALLAR - bug)
def test_fondos_insuficientes():
    token = TokenContract("Test", "TST", 100)
    exito, msg = token.transfer('creator', 'Alice', 200)
    test_runner.cobertura_lineas.update([1, 2])
    # El bug: no valida fondos, así que pasa aunque no deba
    return token.balance_of('creator') >= 0  # Debería ser False pero el bug lo hace True

test_runner.run_test("test_fondos_insuficientes (detecta bug)", test_fondos_insuficientes)

# Test 3: Contrato pausado
def test_contrato_pausado():
    token = TokenContract("Test", "TST", 1000)
    token.pause('creator')
    exito, msg = token.transfer('creator', 'Alice', 100)
    test_runner.cobertura_lineas.update([1, 2, 3, 4])
    return not exito  # Debe fallar porque está pausado

test_runner.run_test("test_contrato_pausado", test_contrato_pausado)

# Test 4: Balance inicial correcto
def test_balance_inicial():
    token = TokenContract("Test", "TST", 5000)
    test_runner.cobertura_lineas.update([1])
    return token.balance_of('creator') == 5000

test_runner.run_test("test_balance_inicial", test_balance_inicial)

# Test 5: Transferencia a sí mismo
def test_transferencia_a_si_mismo():
    token = TokenContract("Test", "TST", 1000)
    exito, msg = token.transfer('creator', 'creator', 100)
    test_runner.cobertura_lineas.update([1, 2, 3])
    return token.balance_of('creator') == 1000  # Debe mantenerse igual

test_runner.run_test("test_transferencia_a_si_mismo", test_transferencia_a_si_mismo)


# --- Integration Tests ---
print("\n--- Integration Tests ---\n")

def test_interaccion_multiple_contratos():
    """Simula interacción entre Token + Exchange"""
    token = TokenContract("Test", "TST", 10000)
    
    # Usuario aprueba al exchange
    token.allowances[('Alice', 'Exchange')] = 500
    
    # Exchange transfiere tokens aprobados
    exito, msg = token.transfer('Alice', 'Exchange', 500)
    test_runner.cobertura_lineas.update([1, 2, 3, 5])
    
    return exito and token.balance_of('Exchange') == 500

test_runner.run_test("integration_test_token_exchange", test_interaccion_multiple_contratos)


# --- Fuzz Tests (como Echidna) ---
print("\n--- Fuzz Tests (inputs aleatorios) ---\n")

def test_fuzz_transferencia():
    """Prueba con 100 inputs aleatorios"""
    token = TokenContract("Test", "TST", 10000)
    bugs_encontrados = 0
    
    for i in range(100):
        amount = random.randint(1, 20000)  # Algunos montos > balance
        exito, msg = token.transfer('creator', 'Alice', amount)
        
        # Si pasó con monto mayor al balance, hay bug
        if exito and amount > 10000:
            bugs_encontrados += 1
    
    test_runner.cobertura_lineas.update([1, 2, 3])
    return bugs_encontrados == 0  # Debe ser 0 si no hay bugs

test_runner.run_test("fuzz_test_transferencia (100 iteraciones)", test_fuzz_transferencia)


# Reporte final
test_runner.reporte_final()

print("\n" + "="*60)
print("🎓 CONCEPTOS CLAVE:")
print("1. Unit tests: prueban funciones individuales")
print("2. Integration tests: prueban interacción entre contratos")
print("3. Fuzz tests: inputs aleatorios para encontrar edge cases")
print("4. Coverage: % de código ejecutado por tests (meta: 100%)")
print("5. Foundry/Hardhat: frameworks profesionales de testing")
print("6. NUNCA despliegues sin tests - el dinero es real")
print("7. Un bug en blockchain = pérdida irreversible")