# BunzCoin

import hashlib

class BunzCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()  # calculate the hash


t1 = "Wes sends 2.9 BC to Jar"
t2 = "Bob sends 2.6 BC to Jar"
t3 = "Daniel sends 5.6 BC to Jar"
t4 = "Jar sends 3.2 BC to Wes"
t5 = "Mike sends 9.1 BC to James"
t6 = "James sends 5.5 BC to Will"


initial_block = BunzCoinBlock("Initial String", [t1, t2])


print(initial_block.block_data)
print(initial_block.block_hash)

second_block = BunzCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = BunzCoinBlock(initial_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)