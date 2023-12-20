#TIPOS NUMERICOS
a = 5 + 3j
b = 6 + 9j
print(a + b)

#MAPPING TYPES
joao_dados ={"nome": "joao", "idade": 41}
print(joao_dados["nome"])
print(joao_dados["idade"])


#binnary type
c = b"oi"

d = "oi meu chapa".encode()
print(type(d))

e = bytearray(b"camarada")
print(e)

f = memoryview(c)
print(f)
