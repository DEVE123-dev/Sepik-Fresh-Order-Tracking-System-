"""
Generate bcrypt password hash for Pass@2026!
Run this to get the correct hash for the database
"""
import bcrypt

password = "Pass@2026!"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

print("="*60)
print("Password Hash Generator")
print("="*60)
print(f"Password: {password}")
print(f"Hashed:   {hashed}")
print("="*60)
print("\nUse this hash in your database.sql file")
print("="*60)
