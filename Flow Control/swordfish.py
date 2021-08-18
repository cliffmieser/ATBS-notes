#swordfish.py

while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("Hello, Joe. What is the password? (Hint: a type of fish.)")
    password = input()
    if password == 'swordfish':
        break
print('Acess granted.')
