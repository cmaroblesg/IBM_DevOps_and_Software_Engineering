def area_of_a_triangle(base: float, height: float) -> float:
    """ Calculates area of a triangle given non-negatives numbers"""
    
    # Check if we have the correct parameters types
    if type(base) not in [int, float]:
        raise TypeError("Base must be a number")
    if type(height) not in [int, float]:
        raise TypeError("Height must be a number")
        
    # Check if we have the correct parameter values
    if base < 0:
        raise ValueError("Base must be a positive number")
    if height < 0:
        raise ValueError("Height must be a positive number")
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
