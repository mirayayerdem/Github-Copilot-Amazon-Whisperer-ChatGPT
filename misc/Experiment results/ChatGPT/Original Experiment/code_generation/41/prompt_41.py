def car_race_collision(n: int):
    left_cars = [(i, 0) for i in range(n)]  # Initialize left-moving cars at position 0
    right_cars = [(i, n) for i in range(n)]  # Initialize right-moving cars at position n
    collisions = 0  # Initialize collisions to 0
    for t in range(n):  # Repeat for n time steps
        # Move left-moving cars one unit to the right
        left_cars = [(i, p + 1) for i, p in left_cars]
        # Move right-moving cars one unit to the left
        right_cars = [(i, p - 1) for i, p in right_cars]
        # Check for collisions
        for i, p in left_cars:
            for j, q in right_cars:
                if p == q:  # Check if p and q are equal
                    collisions += 1  # Increment collisions
    return collisions
