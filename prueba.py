from werkzeug.security import generate_password_hash

# Reemplaza "admin123" por la contraseña que desees
hash = generate_password_hash("admin123")
print(hash)
