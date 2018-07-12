def encrypt(k):
	list_str = []
	for i in range(len(text)):
		list_str.append(chr(ord(text[i])+k))
	encrypted = ''.join(list_str)
	print('Encrypt successfully!')
	print(encrypted)
'''
The ord() method returns an integer representing the 
	Unicode code point of the given Unicode character.
The chr() returns a character (a string) whose 
	Unicode code point is the integer i
'''
def decrypt(k):
	list_str = []
	for i in range(len(text)):
		list_str.append(chr(ord(text[i])-k))
	decrypted = ''.join(list_str)
	print('Decrypt successfully!')
	print(decrypted)

print('''
Select pls!
1.Encrypt
2.Decrypt''')
print()
select = int(input('Your select: '))
text = str(input('Input = ').lower())
k = int(input('Key = '))
print()
if select == 1:
	encrypt(k)
elif select == 2:
	decrypt(k)
else:
	print('NULL!')