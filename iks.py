def generate_meru_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


def display_triangle(triangle):
    """Display the triangle in a formatted manner."""
    if not triangle:
        print("No triangle to display.")
        return

    width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        text = " ".join(map(str, row))
        print(text.center(width))


print("MERU TRIANGLE USING DYNAMIC PROGRAMMING")
print()

try:
    n = int(input("Enter number of rows: "))

    if n <= 0:
        print("Please enter a positive integer.")
    else:
        triangle = generate_meru_triangle(n)

        print("\nGenerated Meru Triangle:\n")
        display_triangle(triangle)

except ValueError:
    print("Invalid input. Please enter an integer.")
