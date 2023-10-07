#loop controler break, continue, pass
#executing break statement
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i = i + 1
#for continue put condition of increment decrement above then put continue condition
i = 10
while i > 0:
    i = i - 1
    if i == 2:
        continue
    print(i)
#pass mean nothing 
i = 10
while i > 0:
    i = i - 1
    if i == 2:
        pass
    print(i)