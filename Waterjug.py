from collections import deque


def water_jug(capacity_a, capacity_b, target):
    # Check whether the target is possible
    if target > max(capacity_a, capacity_b):
        print("Target cannot be measured.")
        return

    # State = (amount of water in Jug A, amount in Jug B)
    start = (0, 0)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        # Goal condition
        if a == target or b == target:
            print("\nSolution Found!")
            print("Step 0:", path[0])

            for i, state in enumerate(path[1:], start=1):
                print(f"Step {i}: {state}")

            print(f"\nTotal steps: {len(path) - 1}")
            print("Final state:", path[-1])
            return

        # Generate all possible next states
        next_states = [
            (capacity_a, b),  # Fill Jug A
            (a, capacity_b),  # Fill Jug B
            (0, b),            # Empty Jug A
            (a, 0),            # Empty Jug B
        ]

        # Pour A into B
        pour = min(a, capacity_b - b)
        next_states.append((a - pour, b + pour))

        # Pour B into A
        pour = min(b, capacity_a - a)
        next_states.append((a + pour, b - pour))

        # Add new states to the queue
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution exists.")


# Take input from the user
capacity_a = int(input("Enter capacity of Jug A: "))
capacity_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

water_jug(capacity_a, capacity_b, target)