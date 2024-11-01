from cryptography.fernet import Fernet

# Fungsi untuk menghasilkan kunci
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Fungsi untuk memuat kunci dari file
def load_key():
    return open("secret.key", "rb").read()

# Fungsi untuk mengenkripsi data
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Fungsi untuk mendekripsi data
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Contoh penggunaan
if _name_ == "_main_":
    generate_key()  # Jalankan ini sekali untuk menghasilkan kunci

    message = "Ini adalah pesan rahasia."
    encrypted = encrypt_message(message)
    print(f"Pesan terenkripsi: {encrypted}")

    decrypted = decrypt_message(encrypted)
    print(f"Pesan terdekripsi: {decrypted}")