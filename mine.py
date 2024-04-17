import binascii
import hashlib
from validate import validate_txn

def calculate_block_hash(block_header):
    block_header_bin = binascii.unhexlify(block_header)
    block_hash = hashlib.sha256(hashlib.sha256(block_header_bin).digest()).digest()
    return block_hash[::-1].hex()

def mine_block(transactions, prev_block_hash, difficulty_target):
    nonce = 0
    while True:
        block_header = prev_block_hash + format(nonce, '08x')
        block_hash = calculate_block_hash(block_header)
        
        if block_hash < difficulty_target:
            valid_transactions = []
            for tx in transactions:
                if validate_txn(tx):
                    valid_transactions.append(tx)
            if not valid_transactions:
                raise Exception("No valid transactions to mine.")
                
            coinbase_transaction = valid_transactions[0]
            txid_list = []
            for tx in valid_transactions:
                txid_list.append(tx['vin'][0]['txid'])
            
            return block_header, block_hash, coinbase_transaction, txid_list
        
        nonce += 1  

