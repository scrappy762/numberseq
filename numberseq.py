# Define a function that checks for patterns in a sequence of numbers
def find_pattern(sequence):
    n = len(sequence)

    # Check that sequence has at least four elements
    if n < 4:
        return None

    # Normalize the sequence by dividing each value by the first value
    normalized_sequence = [x / sequence[0] for x in sequence]

    # Check for constant sequences
    is_constant = all(x == normalized_sequence[0] for x in normalized_sequence)
    if is_constant:
        return [sequence[-1] * normalized_sequence[0]] * 3

    # Check for linear sequences
    differences = [normalized_sequence[i] - normalized_sequence[i-1] for i in range(1, n)]
    is_linear = all(differences[0] == diff for diff in differences)
    if is_linear:
        next_numbers = [sequence[-1] * (normalized_sequence[-1] + differences[0])] * 3
        return next_numbers

    # Check for quadratic sequences
    second_differences = [differences[i] - differences[i-1] for i in range(1, n-1)]
    is_quadratic = all(second_differences[0] == diff for diff in second_differences)
    if is_quadratic:
        a = second_differences[0] / 2
        b = differences[-1] - 3 * a - 2 * differences[0]
        c = normalized_sequence[-1] - a - b
        next_numbers = [sequence[-1] * (a * (n+1)**2 + b * (n+1) + c) for n in range(1, 4)]
        return next_numbers

    # Check for geometric sequences
    ratios = [normalized_sequence[i] / normalized_sequence[i-1] for i in range(1, n)]
    is_geometric = all(ratios[0] == ratio for ratio in ratios)
    if is_geometric:
        next_numbers = [sequence[-1] * (normalized_sequence[-1] * ratios[0]**i) for i in range(1, 4)]
        return next_numbers

    # Check for other patterns
    # ...

    # If no pattern is recognized, return None
    return None


# Main loop of the program
while True:
    numbers_str = input("Enter a sequence of at least four numbers, separated by spaces (or 'quit' to exit): ")
    if numbers_str == 'quit':
        break

    numbers_list = numbers_str.split()
    sequence = [int(x) for x in numbers_list]

    # Check for patterns
    pattern = None
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            a, b = sequence[i], sequence[j]

            # For each pair of numbers, calculate a list of possible next numbers
            possible_sequence = []
            for op in [lambda x, y: x+y, lambda x, y: x-y, lambda x, y: x*y]:
                for p in [op(a, b), op(b, a), a/b,
