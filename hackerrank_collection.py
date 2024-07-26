


N = int(input())
columns = input().split()
marks_idx = columns.index("MARKS")
print(f"{sum(int(input().split()[marks_idx]) for _ in range(N)) / N:.2f}")
