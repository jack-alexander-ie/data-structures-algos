from hashlib import sha256
from time import gmtime, strftime
import json


class Block:
    def __init__(self, data, prev_hash=None, prev_block=None):
        self.timestamp = strftime("%a, %d %b %Y %I:%M:%S %p %Z", gmtime())
        self.data = data
        self.prev_hash = prev_hash
        self.prev_block = prev_block
        self.hash = self.calc_hash()

    def calc_hash(self):
        info = {'timestamp': self.timestamp,
                'data': self.data,
                'prev_hash': self.prev_hash}
        r = json.dumps(info)
        hash_str = r.encode('utf-8')
        sha = sha256()
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_blockchain(self):
        if self.size < 1:
            print('Blockchain is empty, nothing to report.')
            return

        node = self.head
        while node:
            print('Timestamp: \t', node.timestamp)
            print('Data: \t\t', node.data)
            print('SHA256 Hash: \t', node.hash)
            print('Prev Hash: \t', node.prev_hash, '\n')
            node = node.prev_block

    def add_block(self, data):                          # Creates a new Block and adds it to the chain
        if data is None:
            print('No data to add, cannot create block.')
            return
        self.size += 1                                  # Increase number of blocks
        if self.head is None:                           # Adds genesis block if blockchain is empty
            self.head = Block(data, None)
            return
        new_block = Block(data, self.head.hash)
        new_block.prev_hash = self.head.hash
        new_block.prev_block = self.head
        self.head = new_block


# Test Case 1 - Expected
blockchain = BlockChain()

data_1 = 'Genesis Block'
data_2 = '2nd Block'
data_3 = '3rd Block'

blockchain.add_block(data_1)
blockchain.add_block(data_2)
blockchain.add_block(data_3)
blockchain.print_blockchain()

"""
Expected Output:

Timestamp: 	 Tue, 02 Jul 2019 07:42:06 PM GMT
Data: 		 3rd Block
SHA256 Hash: 90e42a13bcd851dff8e1234131215ca9c715dd910867642a894eeaa319d243a9
Prev Hash: 	 7bf4566843cf1301ab6481557651511bf65afccbd2cb2bd4c8f68fb046821ee1 

Timestamp: 	 Tue, 02 Jul 2019 07:42:06 PM GMT
Data: 		 2nd Block
SHA256 Hash: 7bf4566843cf1301ab6481557651511bf65afccbd2cb2bd4c8f68fb046821ee1
Prev Hash: 	 d2ad962f7abbabb49a7a4af0707ee3f46ad2207f2e34818566d72ab17d862f15 

Timestamp: 	 Tue, 02 Jul 2019 07:42:06 PM GMT
Data: 		 Genesis Block
SHA256 Hash: d2ad962f7abbabb49a7a4af0707ee3f46ad2207f2e34818566d72ab17d862f15
Prev Hash: 	 None 
"""

# Test Case 2 - Empty Blockchain

# blockchain = BlockChain()
# blockchain.print_blockchain()

"""
Expected Output: Blockchain is empty, nothing to report.

"""

# Test Case 3 - None passed into data field
# blockchain = BlockChain()
# blockchain.add_block(None)
"""
Expected Output: No data to add, cannot create block.
"""

# Test Case 4 - Tampered block
# blockchain = BlockChain()
#
# data_1 = 'Genesis Block'
# data_2 = '2nd Block'
# data_3 = '3rd Block'
#
# blockchain.add_block(data_1)
# blockchain.add_block(data_2)
# blockchain.add_block(data_3)
#
# tampered_block = blockchain.head.prev_block.prev_block
# tampered_block.data = 'altered data, invalidating block'
# comparison_block = blockchain.head.prev_block
#
# print("Expected hash:\t", comparison_block.prev_hash)
# print('Corrupted hash:\t', tampered_block.calc_hash())
