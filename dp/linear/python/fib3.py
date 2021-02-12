def fib3(n):
    if n < 4:
        return 1
    s1 = 1
    s2 = 1
    s3 = 1
    for _ in range(3, n):
        s4 = s1 + s2 + s3
        s1 = s2
        s2 = s3
        s3 = s4
    return s4

if __name__ == "__main__":
    for i in range(1, 10):
        print(fib3(i))