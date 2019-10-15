s=str(input())
r,c=list(map(int,s.split('X')))

a='~'
h='#'
j=1

for i in range(r//2):                   #top half of pattern
    print((a*(j)).center(c,'h'))
    j=j+2

print(a*c)                              #middle row

for i in range(r//2):                   #bottom half of pattern
    j=j-2
    print((a*(j)).center(c,'h'))
    
