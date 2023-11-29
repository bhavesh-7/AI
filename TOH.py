def hanoi(n, P1, P2, P3):
    """ Move n discs from pole P1 to pole P3. """
    if n == 0:
        
        return

    global count
    count += 1

    
    hanoi(n-1, P1, P3, P2)

    if P1:
        
        P3.append(P1.pop())
        print(A, B, C)

    
    hanoi(n-1, P2, P1, P3)


n = 5
A = list(range(n, 0, -1))
B, C = [], []

print(A, B, C)

count = 0
hanoi(n, A, B, C)
print(count)
