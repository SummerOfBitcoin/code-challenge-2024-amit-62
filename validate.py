def validate_txn(txn):
    value_in=0
    value_out=0

    for vin in txn["vin"]:
        value_in+=vin["prevout"]["value"]

    for vout in txn["vout"]:
        value_out+=vout["value"]

    if(value_out>value_in):
        return False
    
    for vin in txn["vin"]:
        scriptpubkey_type = vin["prevout"]["scriptpubkey_type"]
        scriptpubkey_address = vin["prevout"]["scriptpubkey_address"]
        if scriptpubkey_type not in ['v0_p2wpkh', 'v1_p2tr']: 
            return False
        if not scriptpubkey_address.startswith('bc1'): 
            return False

    for vout in txn["vout"]:
        scriptpubkey_type = vout["scriptpubkey_type"]
        scriptpubkey_address = vout.get('scriptpubkey_address', '')           
        if scriptpubkey_type not in ['v0_p2wpkh', 'v1_p2tr']: 
            return False
        if not scriptpubkey_address.startswith('bc1'): 
            return False
   
    return True

