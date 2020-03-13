import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create a genesis Block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of the Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transaction
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the index Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
