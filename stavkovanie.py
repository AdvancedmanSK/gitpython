N, K, P = list(map(float,input().split()))
medzisucet = int()
if P < 0.5:
    print(int(N))
else:
    for i in range(int(K)):
        bank = (N + medzisucet)*2*P
        medzisucet = bank - N
    print(int(bank))
