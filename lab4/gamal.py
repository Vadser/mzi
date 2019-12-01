from random import randint as r
def text_to_int(text, encoding='Windows-1251', errors='surrogatepass'):
	b = int.from_bytes(text.encode(encoding, errors), 'big')
	return b


def text_from_int(n, encoding='Windows-1251', errors='surrogatepass'):
	return n.to_bytes(
	    (n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

class Encryptor:
	def __init__(self):
		self.p = r(0, 70000)
		self.phi = self.p-1 #Функция Эйлера от p
		self.g = r(2, self.phi)#gcd(p,phi) #обратный элемент g^phi == 1 mod p
		self.x = r(1,self.p-1) #Случайный 1<x<p-1
		self.y = pow(self.g,self.x,self.p) #y=g^{x} mod p
		self.open_key = [self.p,self.g,self.y]
		self.k = r(1,self.p-1) #Случайное к 1 < k < p-1
		self.a = pow(self.g,self.k,self.p) #a=g^k mod p

	def encrypt(self, text):
		crypt = [self.a] #структура шифрограммы: [a, b1,b2,...,bn] b=y^kM mod p
		for M in text:
			crypt += [(pow(self.y,self.k)*text_to_int(M))%self.p]
		return crypt
	
	def decrypt(self, crypt):
		encrypt = ""
		for b in crypt[1::]:
			encrypt+=text_from_int((b*pow(crypt[0],self.p-1-self.x,self.p))%self.p)
		return encrypt

encryptor = Encryptor()
text = input('Введите ваш текст:')
crypt = encryptor.encrypt(text)

print("Публичный ключ:",encryptor.open_key)
print("Зашифрованный текст:",crypt)
for i in crypt[1::]: 
  print(text_from_int(i),end='')
  
print('\n')
encrypt = encryptor.decrypt(crypt)

print("Закрытый ключ:", encryptor.x)
print("Расшифрованный текст:", encrypt)
