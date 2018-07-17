vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
word = input('Entrer un mot: ')
count = 0
for ch in word:
    if ch in vowels:
        print(ch)
        count+=1
print("nombre de voyelle est: ", count)