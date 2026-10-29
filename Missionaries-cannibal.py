from collections import deque


def missionaries_cannibals():
    # State = (missionaries_left, cannibals_left, boat_position)
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Possible boat movements: (missionaries, cannibals)
    moves = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1)   # One missionary and one cannibal
    ]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("\nSolution Found!")

            for step, (m, c, boat) in enumerate(path):
                side = "Left" if boat == 0 else "Right"

                print(
                    f"Step {step}: "
                    f"Missionaries left = {m}, "
                    f"Cannibals left = {c}, "
                    f"Boat = {side}"
                )

            print("\nTotal crossings:", len(path) - 1)
            return

        m, c, boat = state

        for move_m, move_c in moves:

            # Calculate the next state
            if boat == 0:
                new_state = (
                    m - move_m,
                    c - move_c,
                    1
                )
            else:
                new_state = (
                    m + move_m,
                    c + move_c,
                    0
                )

            new_m, new_c, _ = new_state

            # Check population limits
            if not (0 <= new_m <= 3 and 0 <= new_c <= 3):
                continue

            # Calculate people on the right bank
            right_m = 3 - new_m
            right_c = 3 - new_c

            # Check safety on both banks
            if new_m > 0 and new_c > new_m:
                continue

            if right_m > 0 and right_c > right_m:
                continue

            # Avoid repeated states
            if new_state not in visited:
                visited.add(new_state)
                queue.append(
                    (new_state, path + [new_state])
                )

    print("No solution exists.")


missionaries_cannibals()