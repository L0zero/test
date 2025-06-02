if __name__ == "__main__":  
    n = int(input('fib: '))  
    if a <= 2:
        print(1)
        return
 
    l, r = 1, 1
    for i in range(a-2):
        l, r = r, l + r
    print(r)