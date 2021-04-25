d=input("Enter diameter of shell in cm or mm  ")
temp1=''
temp2=''
for i in d:
    if i.isdigit():
        temp1+=i
    else:
        temp2+=i
if temp2=='' or temp2.lower()=='mm':
    diameter=float(temp1)
elif temp2.lower()=='cm':
    diameter=float(temp1)*10
else:
    temp2='mm'
    diameter=float(temp1)
p=float(input("Enter internal presssure N/mm^2 "))
perm=float(input("Enter Permessible tensile stress in N/mm^2 "))
t=((p*diameter)/perm)/4

print('*'*50)
print(f'Diamter given is : {diameter} {temp2.lower()}')
print(f'Interpressure given is : {p} N/mm^2')
print(f'Permessible tensile stress given is : {perm} N/mm^2')
print(f"Thickness of given shell whose  : {t} mm")
print('*'*50)
