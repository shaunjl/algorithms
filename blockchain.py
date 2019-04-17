import hashlib

class Block:
	def __init__(self, previous_hash, transactions):
		self.previous_hash = previous_hash
		self.transactions = transactions

		m = hashlib.sha256()
		m.update(str([previous_hash, transactions]).encode())

		self.hash = m.hexdigest()

	def __str__(self):
		return str({'transactions': self.transactions, 'hash': self.hash, 'previous_hash': self.previous_hash})


class BlockChain:
	def __init__(self, genesis_transactions=None):
		self.chain = []
		gen_trans = genesis_transactions or []
		genesis_block = Block(0, gen_trans)

		self.chain = [genesis_block]

	def add_transactions(self, trans_list):
		last_hash = self.chain[-1].hash
		self.chain.append(Block(last_hash, trans_list))

	def print_chain(self):
		for block in self.chain:
			print(block)

chain = BlockChain(['shaun sent 10 bitcoins to ivan', 'ivan sent 2 bitcoins to joe'])

chain.add_transactions(['joe sent 3 bitcoins to shaun', 'ivan sent 4 bitcoins to shaun', 'joe sent 4 bitcoins to ivan'])

chain.print_chain()
