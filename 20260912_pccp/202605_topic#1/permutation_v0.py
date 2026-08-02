def generate_permutations(nums, path, result):
    if len(path) == len(nums):
        result.append(path.copy())
        return

    for num in nums:
        if num in path:
            continue

        path.append(num)
        generate_permutations(nums, path, result)
        path.pop()

def main():
    while True:
        try:
            n = int(input("Enter N (1 <= N <= 10): ").strip())
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if 1 <= n <= 10:
            break

        print("N must be between 1 and 10.")

    nums = list(range(1, n + 1))
    result = []
    generate_permutations(nums, [], result)

    print(f"All permutations of 1 to {n}:")
    for perm in result:
        print(" ".join(map(str, perm)))

if __name__ == "__main__":
    main()
