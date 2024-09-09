def access_protected_file(user_token, file_id):
    if verify_token(user_token):
        return decrypt_file(file_id)
    else:
        raise Exception("Access Denied: Invalid Security Token")

def verify_token(token):
    # Verify the token is valid and belongs to the authorized user
    return token in valid_tokens_database

def decrypt_file(file_id):
    # Decrypt the file if the token is valid
    encrypted_file = get_encrypted_file(file_id)
    return decrypt(encrypted_file)
