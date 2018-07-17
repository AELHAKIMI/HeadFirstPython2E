vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
word = input('Entrer un mot: ')
found=[]
for ch in word:
    if ch in vowels:
        if ch not in found:
            found.append(ch)
for ch in found:
    print(ch)       
print("nombre de voyelle est: ", len(found))