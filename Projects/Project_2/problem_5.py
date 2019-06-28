"""
TODO: Add test cases
TODO: Clarify
"""

from hashlib import sha256
from time import gmtime, strftime


class Block:
    def __init__(self, data, prev_hash=None, prev_block=None):
        self.timestamp = strftime("%a, %d %b %Y %I:%M:%S %p %Z", gmtime())
        self.data = data
        self.prev_hash = prev_hash
        self.prev_block = prev_block
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_blockchain(self):
        node = self.head
        while node:
            print('Timestamp: \t', node.timestamp)
            print('Data: \t\t', node.data)
            print('SHA256 Hash: \t', node.hash)
            print('Prev Hash: \t', node.prev_hash, '\n')
            node = node.prev_block

    def add_block(self, data):      # Creates a new Block and adds it to the chain
        self.size += 1              # Increase number of blocks

        if self.head is None:       # Adds genesis block if blockchain is empty
            self.head = Block(data, None)
            return

        new_block = Block(data, self.head.hash)
        new_block.prev_hash = self.head.hash
        new_block.prev_block = self.head
        self.head = new_block


data_1 = 'Genesis block test'
data_2 = '2nd block'
data_3 = '3rd block'

blockchain = BlockChain()

blockchain.add_block(data_1)
blockchain.add_block(data_2)
blockchain.add_block(data_3)

blockchain.print_blockchain()
