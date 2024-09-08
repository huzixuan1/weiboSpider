import base64
import hashlib

decodeMacAddress = ""

def decodeMac(encodedMacAddress: str) -> str:
    global decodeMacAddress
    try:
        decodeBytes = base64.b64decode(encodedMacAddress)
        decodeMacAddress = decodeBytes.decode('utf-8')
        print("Decoded MAC Address:", decodeMacAddress)
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        print(f"Error decoding the data: {e}")
        return None
    return encrypt()

def encrypt(length: int = 12) -> str:
    global decodeMacAddress
    address = decodeMacAddress.replace(":", "").replace("-", "")
    hashObj = hashlib.sha256(address.encode())
    hashHex = hashObj.hexdigest()
    encrypted = hashHex[:length]
    return encrypted

if __name__ == "__main__":
    # encoded_mac = "QjA6MzU6OUY6QTg6OTE6NzU=" 
    encoded_mac = "QjA6MzU6OUY6QTg6OTE6NzU="
    encrypted_result = decodeMac(encoded_mac)
    if encrypted_result:
        print("Encrypted Result:", encrypted_result)
