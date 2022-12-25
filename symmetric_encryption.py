from cryptography.fernet import Fernet

message = "Sanka_Zver"

key = Fernet.generate_key()
print(key)

fernet = Fernet(key)
#print(fernet)

encrypted_message = fernet.encrypt(message.encode())

print(message.encode())
print("orginal string: ", message)
print("encrypted string: ", encrypted_message)
print(type(encrypted_message))

decrypted_message = fernet.decrypt(encrypted_message).decode()
print(decrypted_message)
