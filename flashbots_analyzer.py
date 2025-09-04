import requests

ETH_RPC = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"

def get_latest_block():
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    response = requests.post(ETH_RPC, json=payload).json()
    return int(response['result'], 16)

if __name__ == "__main__":
    block = get_latest_block()
    print(f"Latest Ethereum block: {block}")
