def primo(numero):
  for i in range(2,numero):
   if not numero%i:
    return False
  else:
   print(str(numero) + ' eh primo')
   return True

print(primo(10))
print(primo(13))

for numero in range(1,101):
   primo(numero)
