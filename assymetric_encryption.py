import rsa 

public_key, private_key = rsa.newkeys(512)

message = "Jacob Hossain"

encrypted_message = rsa.encrypt(message.encode(), public_key)

print(encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()

print(decrypted_message)