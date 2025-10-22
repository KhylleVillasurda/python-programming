"""
String utility functions for the helpers package.
"""

def shout(s: str) -> str:
    """
    Convert a string to uppercase with excitement!
    
    Args:
        s: Input string to convert
        
    Returns:
        Uppercase version of the string with exclamation mark
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")
    
    return s.upper() + "!"


def reverse_string(s: str) -> str:
    """
    Reverse a string.
    
    Args:
        s: Input string to reverse
        
    Returns:
        Reversed string
    """
    return s[::-1]


# Module-level demonstration
if __name__ == "__main__":
    # Test the functions when run directly
    print("Testing string_utils:")
    print(f"shout('hello') = {shout('hello')}")
    print(f"reverse_string('python') = {reverse_string('python')}")