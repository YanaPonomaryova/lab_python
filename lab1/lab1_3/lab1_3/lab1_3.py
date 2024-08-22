N = int(input("Enter a number N (1<N<9) : "))

for i in range(N, 0, -1):
    for j in range(N, N-i, -1):
        print(j, end=" ")
    print()
