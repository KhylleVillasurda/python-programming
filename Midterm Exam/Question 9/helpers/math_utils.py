"""
Math utility functions for the helpers package.
"""

def area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: Length of the rectangle
        width: Width of the rectangle
        
    Returns:
        Area (length × width)
        
    Raises:
        ValueError: If length or width are negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


# Module-level demonstration  
if __name__ == "__main__":
    # Test the functions when run directly
    print("Testing math_utils:")
    print(f"area(5, 3) = {area(5, 3)}")
    print(f"multiply(4, 7) = {multiply(4, 7)}")