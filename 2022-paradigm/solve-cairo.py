import asyncio

from starknet_py.net.gateway_client import GatewayClient
from starknet_py.contract import Contract
from starknet_py.net import AccountClient, KeyPair
from starknet_py.net.models import StarknetChainId

url = "http://1e5f0f9a-fd5c-4a8f-b638-8efd5029b384@35.193.19.12:5050"
contract_addr = "0x26864d42bb56aeb716d1dc733ef7bc4df03963fa504ebccac54d53dd272a78f"
key = int("0xdcb639fa81d1d8c8d384f4aea4a3b034", 16)

key_pair = KeyPair.from_private_key(key=key)
cli = GatewayClient(url)


async def call():
    client = await AccountClient.create_account(client=cli, private_key=key, chain=StarknetChainId.TESTNET)

    contract = await Contract.from_address(contract_addr, client)
    invoc = await contract.functions['solve'].invoke("man", max_fee=int(0))
    await invoc.wait_for_acceptance()
    print(invoc)
    sol = await contract.functions["solution"].call()
    print(sol)

loop = asyncio.get_event_loop()
loop.run_until_complete(call())
