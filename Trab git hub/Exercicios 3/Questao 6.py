N = int(input())
P = int(input())
bacterias =1
dias = 0
while (bacterias<=N):
  bacterias *= P
  if bacterias > N:
    break
  dias+=1

print(dias)