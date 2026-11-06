class ERC20Token:
    """Simulación de token fungible (como USDT, SHIB)"""
    
    def __init__(self, nombre, simbolo, supply_inicial):
        self.nombre = nombre
        self.simbolo = simbolo
        self.total_supply = supply_inicial
        self.balances = {}
        self.allowances = {}
        
        # Asignar supply inicial al creador
        self.balances['creator'] = supply_inicial
        print(f"🪙 Token ERC-20 creado: {nombre} ({simbolo})")
        print(f"   Total Supply: {supply_inicial:,}")
        print(f"   Balance inicial del creador: {supply_inicial:,}\n")
    
    def balance_of(self, address):
        """balanceOf(address) - Función obligatoria ERC-20"""
        balance = self.balances.get(address, 0)
        print(f"💰 Balance de {address}: {balance} {self.simbolo}")
        return balance
    
    def transfer(self, from_address, to_address, amount):
        """transfer(to, amount) - Función obligatoria ERC-20"""
        print(f"📤 {from_address} envía {amount} {self.simbolo} a {to_address}")
        
        if self.balances.get(from_address, 0) < amount:
            print(f"   ❌ Fondos insuficientes\n")
            return False
        
        self.balances[from_address] -= amount
        self.balances[to_address] = self.balances.get(to_address, 0) + amount
        
        print(f"   ✅ Transferencia exitosa")
        print(f"   Balance {from_address}: {self.balances[from_address]}")
        print(f"   Balance {to_address}: {self.balances[to_address]}\n")
        return True
    
    def approve(self, owner, spender, amount):
        """approve(spender, amount) - Autorizar gasto"""
        self.allowances[(owner, spender)] = amount
        print(f"✅ {owner} autoriza a {spender} a gastar {amount} {self.simbolo}\n")
    
    def transfer_from(self, spender, from_address, to_address, amount):
        """transferFrom - Gastar tokens autorizados"""
        allowance = self.allowances.get((from_address, spender), 0)
        
        print(f"🔄 {spender} usa transferFrom para mover {amount} {self.simbolo}")
        
        if allowance < amount:
            print(f"   ❌ Allowance insuficiente ({allowance} < {amount})\n")
            return False
        
        self.allowances[(from_address, spender)] -= amount
        return self.transfer(from_address, to_address, amount)


class ERC721NFT:
    """Simulación de NFT (token no fungible)"""
    
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo
        self.owners = {}  # {token_id: owner}
        self.token_uris = {}  # {token_id: metadata_url}
        self.next_token_id = 1
        print(f"🎨 Colección NFT ERC-721 creada: {nombre} ({simbolo})\n")
    
    def mint(self, to_address, token_uri):
        """Crear nuevo NFT"""
        token_id = self.next_token_id
        self.owners[token_id] = to_address
        self.token_uris[token_id] = token_uri
        self.next_token_id += 1
        
        print(f"🖼️  NFT #{token_id} minteado para {to_address}")
        print(f"   Metadata: {token_uri}\n")
        return token_id
    
    def owner_of(self, token_id):
        """ownerOf(tokenId) - Función obligatoria ERC-721"""
        owner = self.owners.get(token_id, None)
        if owner:
            print(f"👤 Owner de NFT #{token_id}: {owner}")
        else:
            print(f"❌ NFT #{token_id} no existe")
        return owner
    
    def transfer_from(self, from_address, to_address, token_id):
        """transferFrom(from, to, tokenId)"""
        print(f"🔄 Transfiriendo NFT #{token_id} de {from_address} a {to_address}")
        
        if self.owners.get(token_id) != from_address:
            print(f"   ❌ {from_address} no es el owner del NFT #{token_id}\n")
            return False
        
        self.owners[token_id] = to_address
        print(f"   ✅ NFT #{token_id} transferido exitosamente\n")
        return True
    
    def token_uri(self, token_id):
        """tokenURI(tokenId) - Link a metadatos"""
        uri = self.token_uris.get(token_id, None)
        print(f"🔗 URI de NFT #{token_id}: {uri}")
        return uri


class ERC1155MultiToken:
    """Simulación de token multi-tipo (fungible + NFT)"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.balances = {}  # {(address, token_id): balance}
        print(f"🎮 Multi-Token ERC-1155 creado: {nombre}")
        print(f"   Soporta tokens fungibles Y no fungibles en un solo contrato\n")
    
    def mint_fungible(self, address, token_id, amount):
        """Mintear tokens fungibles (ej: 1000 monedas de oro)"""
        key = (address, token_id)
        self.balances[key] = self.balances.get(key, 0) + amount
        print(f"🪙 {address} recibió {amount} tokens fungibles ID #{token_id}")
        print(f"   Balance: {self.balances[key]}\n")
    
    def mint_nft(self, address, token_id):
        """Mintear NFT único"""
        key = (address, token_id)
        self.balances[key] = 1  # Solo 1 unidad = único
        print(f"🎨 {address} recibió NFT único ID #{token_id}\n")
    
    def balance_of(self, address, token_id):
        """Ver balance de cualquier token"""
        balance = self.balances.get((address, token_id), 0)
        tipo = "NFT" if balance == 1 else "Fungible"
        print(f"📊 {address} tiene {balance} {tipo} (ID #{token_id})")
        return balance
    
    def batch_transfer(self, from_address, to_address, token_ids, amounts):
        """Transferir múltiples tokens en una sola transacción"""
        print(f"📦 Batch transfer de {from_address} a {to_address}:")
        
        for token_id, amount in zip(token_ids, amounts):
            key_from = (from_address, token_id)
            key_to = (to_address, token_id)
            
            if self.balances.get(key_from, 0) < amount:
                print(f"   ❌ Fondos insuficientes para token #{token_id}")
                continue
            
            self.balances[key_from] -= amount
            self.balances[key_to] = self.balances.get(key_to, 0) + amount
            print(f"   ✅ {amount} unidades del token #{token_id} transferidas")
        
        print()


# --- Simulación ---
print("=== Tokens ERC ===\n")

print("--- ERC-20: Token Fungible (USDT) ---")
usdt = ERC20Token("Tether USD", "USDT", 1_000_000)
usdt.balance_of('creator')
usdt.transfer('creator', 'Alice', 1000)
usdt.transfer('Alice', 'Bob', 250)
usdt.approve('Alice', 'Exchange', 500)
usdt.transfer_from('Exchange', 'Alice', 'Charlie', 300)

print("\n--- ERC-721: NFT (Colección de Arte) ---")
nft_collection = ERC721NFT("CryptoArt", "CART")
token1 = nft_collection.mint("Alice", "https://ipfs.io/Qm123")
token2 = nft_collection.mint("Bob", "https://ipfs.io/Qm456")
nft_collection.owner_of(token1)
nft_collection.transfer_from("Alice", "Charlie", token1)
nft_collection.owner_of(token1)  # Ahora es de Charlie

print("\n--- ERC-1155: Multi-Token (Juego) ---")
game = ERC1155MultiToken("MiJuegoBlockchain")
game.mint_fungible("Alice", 1, 1000)  # 1000 monedas de oro
game.mint_nft("Alice", 100)  # Espada legendaria única
game.balance_of("Alice", 1)
game.balance_of("Alice", 100)
game.batch_transfer("Alice", "Bob", [1, 100], [500, 1])

print("="*50)
print("🎓 CONCEPTOS CLAVE:")
print("1. ERC-20 = tokens intercambiables (monedas)")
print("2. ERC-721 = NFTs únicos (arte, coleccionables)")
print("3. ERC-1155 = híbrido (gaming, marketplaces)")
print("4. Los estándares permiten compatibilidad universal")
print("5. Sin ERC, cada wallet/exchange necesitaría integración custom")