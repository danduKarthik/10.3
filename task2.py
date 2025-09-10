def find_common(a, b):
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res

# Get input from user
a = list(map(int, input("Enter the first list of numbers (space-separated): ").split()))
b = list(map(int, input("Enter the second list of numbers (space-separated): ").split()))
print(find_common(a, b))
