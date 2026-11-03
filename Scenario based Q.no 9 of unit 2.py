n = int(input("Enter the number of items: "))

weights = []
values = []

print("Enter the weights of items:")
for i in range(n):
    weights.append(int(input()))

print("Enter the values of items:")
for i in range(n):
    values.append(int(input()))

capacity = int(input("Enter the bag capacity: "))

dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum obtainable value:", dp[n][capacity])
