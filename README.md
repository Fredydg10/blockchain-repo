# 🚀 Aprendiendo Blockchain en 28 Días

> Un viaje completo desde los fundamentos hasta el desarrollo profesional de blockchain, con simulaciones prácticas en Python y código real en Solidity.

![Estado](https://img.shields.io/badge/Estado-22%2F22%20completados-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Solidity](https://img.shields.io/badge/Solidity-0.8.x-purple)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black)

---

## 📖 Sobre este proyecto

Este repositorio documenta mi reto personal de aprender **blockchain desde cero**. Cada día incluye:

- 📚 **Teoría clara y directa** sobre un concepto específico
- 💻 **Simulación práctica en Python** que demuestra el concepto
- 🎯 **Ejercicios reales** (Remix IDE, MetaMask, testnets)
- 📝 **Commits diarios** mostrando mi progreso

**Objetivo:** Entender blockchain a fondo para luego aplicar ese conocimiento en el mundo real (DeFi, NFTs, dApps, inversiones informadas).

---

## 📋 Índice de Contenidos

### 🏗️ Módulo 1: Fundamentos (Días 1-4)

- [x] **Día 1** - ¿Qué es Blockchain? [📁](./dia_01_hash_simple/)
  - Libro mayor distribuido, Bitcoin, eliminar intermediarios
- [x] **Día 2** - Estructura de Blockchain [📁](./dia_02_simulacion_pow/)
  - Bloques, hash, cadena, árbol de Merkle, Proof of Work simulado
- [x] **Día 3** - Criptografía [📁](./dia_03_firmas_digitales/)
  - Hashing SHA-256, firmas digitales, claves pública/privada
- [x] **Día 4** - Descentralización [📁](./dia_04_red_descentralizada/)
  - Descentralización vs confianza, almacenamiento distribuido

### ⚙️ Módulo 2: Operaciones y Consenso (Días 5-8)

- [x] **Día 5** - Operaciones básicas [📁](./dia_05_ciclo_vida_transaccion/)
  - Ciclo de vida de una transacción, nodos, mempool
- [x] **Día 6** - Minería e incentivos [📁](./dia_06_mineria_e_incentivos/)
  - Proof of Work, recompensas, comisiones, halving
- [x] **Día 7** - Protocolos de consenso [📁](./dia_07_protocolos_consenso/)
  - PoW vs PoS, BFT, DPoS, cuándo usar cada uno
- [x] **Día 8** - Criptomonedas y wallets [📁](./dia_08_wallets_y_criptos/)
  - Bitcoin vs altcoins, hot/cold wallets, "not your keys, not your coins"

### 🔀 Módulo 3: Ecosistema Avanzado (Días 9-11)

- [x] **Día 9** - Smart Contracts [📄](./dia_09_smart_contracts.py)
  - Qué son, inmutabilidad, "code is law", contratos híbridos
- [x] **Día 10** - Oráculos y Chainlink [📁](./dia_10_oraculos_chainlink/)
  - Problema del dato fuera de cadena, redes de oráculos
- [x] **Día 11** - Forks e interoperabilidad [📁](./dia_11_forks_e_interoperabilidad/)
  - Hard/soft forks, bridges, wrapped tokens

### 👨‍💻 Módulo 4: Desarrollo (Días 12-15)

- [x] **Día 12** - Lenguajes de programación [📁](./dia_12_lenguajes_programacion/)
  - Solidity, Vyper, Rust, Go - para qué sirve cada uno
- [x] **Día 13** - Solidity básico [📁](./dia_13_solidity_basico_simulacion/)
  - Hola Mundo, variables, funciones, modifiers, eventos
- [x] **Día 14** - Tokens ERC [📁](./dia_14_tokens_erc/)
  - ERC-20, ERC-721 (NFTs), ERC-1155
- [x] **Día 15** - IDEs y herramientas [📁](./dia_15_ides_y_herramientas/)
  - Remix, Hardhat, Foundry, OpenZeppelin, MythX, Slither, Echidna

### 🧪 Módulo 5: Producción (Días 16-17)

- [x] **Día 16** - Pruebas de contratos [📁](./dia_16_pruebas_contratos/)
  - Unit tests, integration tests, fuzzing, coverage
- [x] **Día 17** - Despliegue y ciclo de vida [📁](./dia_17_despliegue_y_ciclo_vida/)
  - Testnet, mainnet, monitoreo, upgradeability (proxies)

### 🌐 Módulo 6: Ecosistema Completo (Días 18-22)

- [x] **Día 18** - dApps y librerías cliente [📁](./dia_18_dapps_y_librerias/)
  - ethers.js, web3.js, Moralis, ABI
- [x] **Día 19** - Escalabilidad Layer 2 [📁](./dia_19_escabilidad_layer2/)
  - Rollups optimistas, ZK-rollups, sidechains, Lightning Network
- [x] **Día 20** - Ethereum 2.0 y escalado [📁](./dia_20_ethereum2_sharding/)
  - The Merge, sharding, Danksharding, EIP-4844
- [x] **Día 21** - Servicios y casos de uso [📁](./dia_21_servicios_y_casos_uso/)
  - Alchemy, Infura, NFTs, DAOs, DeFi, IPFS
- [x] **Día 22** - Stack completo [📁](./dia_22_stack_completo/)
  - Stack completo: JS, Python, Go, Rust, Solidity

### 🎯 Módulo 7: Integración (Pendiente)

- [ ] **Día 23** - Proyecto final: Mini-dApp *(Pendiente - requiere TypeScript)*
  - Diseñar mini-dApp: contrato + frontend + wallet + testnet

---

## 🎓 Aprendizajes Clave

### 🔐 Seguridad
- Los smart contracts manejan dinero real - **un bug = pérdida irreversible**
- NUNCA desplegar sin auditoría (Slither → Echidna → MythX → auditoría profesional)
- "Not your keys, not your coins" - usa cold wallets para ahorros

### 🏗️ Arquitectura
- Blockchain es inmutable por diseño - los forks son la única "actualización"
- Layer 2 (rollups) es el futuro de la escalabilidad
- Los oráculos conectan blockchain con el mundo real

### 💼 Desarrollo Profesional
- OpenZeppelin = NUNCA reinventes la rueda
- Foundry > Hardhat para testing (100x más rápido)
- El stack completo: JS (frontend) + Solidity (contratos) + Python (backend/data)

### 💡 Inversión Informada
- Entender la tecnología = no caer en estafas
- DYOR (Do Your Own Research) antes de invertir
- Diversificar y nunca invertir más de lo que puedas perder

---

## 🛠️ Tecnologías Usadas

| Categoría | Herramientas |
|-----------|--------------|
| **Lenguajes** | Python 3.10+, Solidity 0.8.x |
| **Simulación** | Scripts Python con clases y OOP |
| **IDEs** | Remix IDE, VS Code |
| **Blockchains** | Ethereum (conceptual), Bitcoin (conceptual) |
| **Herramientas** | Git, GitHub, MetaMask (conceptual) |
| **Librerías** | `hashlib`, `cryptography`, `secrets` |

---

## 🚀 Cómo usar este repositorio

### Para aprender blockchain:
```bash
# Clona el repositorio
git clone https://github.com/TU_USUARIO/blockchain-repo.git
cd blockchain-repo

# Ejecuta cualquier día
python dia_01_hash_simple/nombre_del_script.py
python dia_06_mineria_e_incentivos/nombre_del_script.py
