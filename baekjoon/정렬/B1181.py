N = int(input())
lst = set()
for _ in range(N):
    lst.add(input())
lst = sorted(lst, key=lambda x: [len(x), x])
print("\n".join(lst))
