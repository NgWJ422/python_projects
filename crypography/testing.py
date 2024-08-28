from cryptography.fernet import Fernet

message = str(input("Please write your message here: "))

key = Fernet.generate_key()
print(key)

fernet_obj = Fernet(key)

encrypted_message = fernet_obj.encrypt(message.encode())
print(encrypted_message)

decrypted_message = fernet_obj.decrypt(encrypted_message).decode()
print(decrypted_message)