import rsa

message = str(input("Please write a message"))

public_key, private_key = rsa.newkeys(512)

print("The public key is: ", public_key)
print("The private key is: ", private_key)

encrypted_message = rsa.encrypt(message.encode(), public_key)
print("The encrypted message is: ", encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message,private_key).decode()
print("The decrypted message is: ", decrypted_message)