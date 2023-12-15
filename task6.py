import heapq


def generate_sorted_sums(A, B):
    n = len(A)

    # Sort arrays A and B
    A.sort()
    B.sort()

    # Create a min heap to store tuples (sum, i, j)
    heap = [(A[0] + B[0], 0, 0)]

    # Set to keep track of visited pairs (i, j)
    visited = set((0, 0))

    for _ in range(n * n):
        current_sum, i, j = heapq.heappop(heap)
        yield current_sum

        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(heap, (A[i + 1] + B[j], i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(heap, (A[i] + B[j + 1], i, j + 1))
            visited.add((i, j + 1))


# Example usage:
A = [1, 4, 2, 3]
B = [5, 2, 6, 8]

result = list(generate_sorted_sums(A, B))
print(result)
