from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('http://35.193.50.147:8545/dfc3fe5d-db6c-47a1-9365-ab9ac6b3cbd5'))
web3.eth.account.from_key("0x47990eb5a4bc26f20e8732edeb8d2a960f187227966b21b4af5e3888a94ea476")
setup_addr = "0x7969353BDa86E16abF3e41D374b16389B96FB7cB"

'''
with open('fun-reversing/public/compiled/Setup.sol/Setup.json') as f:
    setup_abi = json.load(f)
    setup_abi = setup_abi['abi']
'''


random = web3.eth.get_code(setup_addr)
print(random.hex())



