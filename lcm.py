m = int(input("Enter Number: "))
n = int(input("Enter Number: "))
if m > n:
    smallestt_num = m 
else:
    smallestt_num = n 
lcm = False

for i in range(smallestt_num, (m*n+1)):
    if not lcm:
        if(i%m==0) and (i%n==0):
            lcm=True
            lcm=i 
print(lcm)