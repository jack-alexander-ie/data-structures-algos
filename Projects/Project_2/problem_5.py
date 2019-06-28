from hashlib import sha256
from time import gmtime, strftime


class Block:

    def __init__(self, data, previous_hash=None):
        self.timestamp = strftime("%a, %d %b %Y %I:%M:%S %p %Z", gmtime())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def __str__(self):

        node = self.head

        while node:
            print('Timestamp: \t', node.timestamp)
            print('Data: \t', node.data)
            print('SHA256 Hash: \t', node.hash)
            print('Prev Hash: \t', node.hash, '\n')

    def add_block(self, data):      # Creates a new Block and adds it to the chain
        if self.head is None:       # Adds genesis block if blockchain is empty
            self.head = Block(data)

        new_block = Block(data, self.head.hash)
        self.head = new_block


data_1 = 'Genesis block test'
data_2 = '2nd block'
data_3 = '3rd block'

blockchain = BlockChain()

blockchain.add_block(data_1)
blockchain.add_block(data_2)
blockchain.add_block(data_3)
