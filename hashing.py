import bcrypt
import time

message = "Hello World!".encode()

start = time.time()
salt = bcrypt.gensalt()

hashed_message = bcrypt.hashpw(message, salt)
end = time.time()
print(hashed_message)

print(end - start)
if bcrypt.checkpw(message, hashed_message):
    print("Matched!")
else:
    print("Invalid!")