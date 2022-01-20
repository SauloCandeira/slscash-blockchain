from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/2de412684b8048b8984e09ec6fc78e6b"
web3 = Web3(Web3.HTTProvider(infura_url))
web3.isConnected()