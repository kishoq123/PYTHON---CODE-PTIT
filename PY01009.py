n = input()
l=0
u=0
for i in range(len(n)):
    if n[i] == n[i].upper():
        u+=1
    else:
        l+=1
if l >= u:
    print(n.lower())
else:
    print(n.upper())