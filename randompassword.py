import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

password_len = int(input("how many characters should your password consist of? : "))
password_count = int(input("how many passwords do you want to create? :"))

for x in range(0, password_count):
    password = ""
for x in range(0, password_len):
    password_char = random.choice(Chars)
    password = password + password_char
print("Your Password :", password)
