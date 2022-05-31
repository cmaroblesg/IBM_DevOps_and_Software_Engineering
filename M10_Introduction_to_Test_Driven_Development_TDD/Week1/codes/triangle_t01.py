def area_of_a_triangle(base, height):
    return (base/2)*height

test_data=[(3.5, 8.5),  # Float
           (2, 5),      # Integer
           (0, 5),      # Zero
           (-2, 5),     # Negative
           (True, 5),   # Boolean
           ("base", 5)] # String

for data in test_data:
    print(f"The area of a triangle {data}"\
          f" is: {area_of_a_triangle(*data)}")
