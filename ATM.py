n , x = (input().split())
n = int(n)
x = float(x)
if n % 5 == 0:
    if x >= n + 0.50:
        m = (x - n) - 0.50
        print("%.2f"%m)
    else:
        print('%.2f'%x)
else:
    
    print('%.2f'%x)