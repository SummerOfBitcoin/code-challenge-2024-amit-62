import os
import json 
from mine import mine_block
from validate import validate_txn    

def read_json_files(folder_path):
    data = []

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            # Parse the JSON data from the file
            json_data = json.load(file)
            data.append(json_data)

    return data

def main():
    print("hello")
    folder_path = "./mempool"
    txns = read_json_files(folder_path)
    print(len(txns))
    valid_transactions = []
    for tx in txns:
        if validate_txn(tx):
            valid_transactions.append(tx)
    print(f"Number of valid transactions: {len(valid_transactions)}")

    prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    difficulty_target = "0000ffff00000000000000000000000000000000000000000000000000000000"
    
    block_header, block_hash, coinbase_transaction, txid_list = mine_block(txns, prev_block_hash, difficulty_target)
    
    with open("output.txt", 'w') as output_file:
        output_file.write(block_header + "\n")
        output_file.write(json.dumps(coinbase_transaction) + "\n")  
        for txid in txid_list:
            output_file.write(txid + "\n")
    
    

if __name__ == "__main__":
    main()

    # 37079526