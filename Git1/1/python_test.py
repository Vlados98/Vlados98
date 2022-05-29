a  = [1,8,32,657867,43124,345,12]

N = len(a)

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j]> a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
