
#Break
for i in range(1,10):
    print(i, end=' ')
    if(i==5):
        break
print("\n--------")

#Pass
for i in range(0,10,1):
    if i == 6:
        print(i)
    else:
        pass

print("\n--------")
for i in range(0,100):
    if i%5==0:
        print(i, end=" ")
    else:
        pass

#Continue
print("\n--------")
for number in range(10):
    if number%2==0:
        continue
    else:
        print(number, end =" ")

#Same continue program with pass keyword gives same output
print("\n--------")
for number in range(10):
    if number%2==0:
        pass
    else:
        print(number, end =" ")