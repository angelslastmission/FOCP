def encrypt_message(message):
    message_without_spaces = message.replace(" ", "")
    
    encrypted_message = message_without_spaces[::-1]
    
    return encrypted_message

original_message = "This is a secret message"
encrypted_message = encrypt_message(original_message)

print("Original message:", original_message)
print("Encrypted message:", encrypted_message)
