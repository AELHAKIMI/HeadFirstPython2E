todos = open('todos.txt', 'w')
print('Ayoub EL HAKIMI', file=todos)
print('26', file=todos)
print('Marrakech', file=todos)
print('Morocco', file=todos)
todos.close()

tasks = open('todos.txt')
for chore in tasks:
    print(chore, end='')
todos.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
