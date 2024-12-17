
import hashlib
import time
import json

# Blok sınıfı
class Block:
    def __init__(self, index, timestamp, maintenance_data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.maintenance_data = maintenance_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Blok hash'ini hesapla
    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + json.dumps(self.maintenance_data, sort_keys=True) + self.previous_hash
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

# Blockchain sınıfı
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Genesis bloğunu oluştur (ilk blok)
    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    # Sonraki bloğu oluştur
    def add_block(self, maintenance_data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), maintenance_data, last_block.hash)
        self.chain.append(new_block)

    # Blockchain'i görüntüle
    def display_chain(self):
        for block in self.chain:
            print(f"Block #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Maintenance Data: {block.maintenance_data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-----------")

# Araç bakım kaydı ekleme fonksiyonu
def add_maintenance_record(blockchain, vehicle_id, service_provider, maintenance_description):
    maintenance_data = {
        'vehicle_id': vehicle_id,
        'service_provider': service_provider,
        'maintenance_description': maintenance_description
    }
    blockchain.add_block(maintenance_data)

# Blockchain oluşturma ve bakım kaydının eklenmesi
vehicle_blockchain = Blockchain()

# Araç bakım kayıtlarını ekleyelim
add_maintenance_record(vehicle_blockchain, "ABC123", "Servis A", "Yağ Değişimi")
add_maintenance_record(vehicle_blockchain, "ABC123", "Servis B", "Fren Bakımı")
add_maintenance_record(vehicle_blockchain, "XYZ789", "Servis C", "Motor Bakımı")

# Blockchain'in görüntülenmesi
vehicle_blockchain.display_chain()


