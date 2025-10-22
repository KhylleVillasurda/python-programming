#!/usr/bin/env python3
"""
Main script demonstrating different import styles and namespace management.

This script shows:
1. Importing modules with aliases
2. Importing specific functions
3. Namespace collision scenarios
4. How aliases help avoid conflicts
"""

# Style 1: Import entire module with alias
import helpers.string_utils as str_utils
print("✓ Imported helpers.string_utils as str_utils")

# Style 2: Import specific function from module
from helpers.math_utils import area
print("✓ Imported area from helpers.math_utils")

# Style 3: Import entire module (different style)
import helpers.math_utils as math_utils
print("✓ Imported helpers.math_utils as math_utils")

# Style 4: Import multiple functions
from helpers.string_utils import reverse_string
print("✓ Imported reverse_string from helpers.string_utils")


def demonstrate_basic_usage():
    """Demonstrate basic usage of imported modules and functions."""
    print("\n" + "="*60)
    print("BASIC USAGE DEMONSTRATION")
    print("="*60)
    
    # Using aliased module
    result1 = str_utils.shout("hello world")
    print(f"str_utils.shout('hello world') = {result1}")
    
    # Using directly imported function
    result2 = area(10, 5)
    print(f"area(10, 5) = {result2}")
    
    # Using module alias for other functions
    result3 = math_utils.multiply(6, 7)
    print(f"math_utils.multiply(6, 7) = {result3}")
    
    # Using directly imported function
    result4 = reverse_string("python")
    print(f"reverse_string('python') = {result4}")


def demonstrate_namespace_collisions():
    """Demonstrate namespace collisions and how aliases help."""
    print("\n" + "="*60)
    print("NAMESPACE COLLISION DEMONSTRATION")
    print("="*60)
    
    # COLLISION SCENARIO 1: Same function name from different modules
    print("\n1. COLLISION: Same function name from different sources")
    
    # Let's create a local function that conflicts with an imported one
    def area(radius):
        """Local function that conflicts with imported area()"""
        return 3.14 * radius * radius
    
    print(f"Local area(5) [circle] = {area(5)}")
    print(f"Imported area(10, 5) [rectangle] = {math_utils.area(10, 5)}")
    print("✓ Used math_utils.area to avoid conflict with local area")
    
    # COLLISION SCENARIO 2: What if we hadn't used aliases?
    print("\n2. COLLISION AVOIDANCE: Why we use aliases")
    
    # Bad practice that causes confusion
    # avoid importing 'multiply' into this namespace — use math_utils.multiply instead
    # Now we have multiply from math_utils in our namespace
    
    def multiply(a, b, z):
        """Local function that could conflict"""
        return a * b * z
    
    print(f"Local multiply(2, 3, 4) = {multiply(2, 3, 4)}")
    print(f"Math multiply(2, 3) = {math_utils.multiply(2, 3)}")
    print("✓ Used math_utils.multiply to distinguish from local multiply")
    
    # COLLISION SCENARIO 3: Standard library conflicts
    print("\n3. STANDARD LIBRARY CONFLICTS")
    
    # Imagine if a module had a function called 'open' or 'print'
    # Using aliases prevents overriding built-in functions
    import helpers.string_utils as string_tools  # Can use meaningful alias
    
    result = string_tools.shout("no conflict")
    print(f"Used alias 'string_tools' to avoid any potential conflicts: {result}")


def compare_import_styles():
    """Compare different import styles and their trade-offs."""
    print("\n" + "="*60)
    print("IMPORT STYLE COMPARISON")
    print("="*60)
    
    styles = {
        "import module as alias": {
            "pros": ["Clear namespace", "Avoids collisions", "Explicit source"],
            "cons": ["More typing", "Longer code"],
            "use_case": "Production code, large projects"
        },
        "from module import function": {
            "pros": ["Less typing", "Clean syntax", "Direct access"],
            "cons": ["Namespace pollution", "Collision risk", "Unclear source"],
            "use_case": "Small scripts, quick prototypes"
        },
        "import module": {
            "pros": ["Explicit", "No collisions", "Clear organization"],
            "cons": ["Verbose", "Longer attribute access"],
            "use_case": "When module name is short and clear"
        }
    }
    
    for style, info in styles.items():
        print(f"\n{style}:")
        print(f"  Pros: {', '.join(info['pros'])}")
        print(f"  Cons: {', '.join(info['cons'])}")
        print(f"  Best for: {info['use_case']}")


def explain_namespace_concepts():
    """Explain key namespace and import concepts."""
    print("\n" + "="*60)
    print("NAMESPACE CONCEPTS EXPLAINED")
    print("="*60)
    
    concepts = """
WHAT ARE NAMESPACE COLLISIONS?

A namespace collision occurs when two different objects (functions, 
variables, classes) have the same name in the same namespace, causing 
ambiguity about which one should be used.

Example:
    from module_a import calculate
    from module_b import calculate  # Collision! Which calculate()?

HOW ALIASES HELP:

1. Avoid Ambiguity:
   import module_a as mod_a
   import module_b as mod_b
   mod_a.calculate() vs mod_b.calculate()  # Clear which one!

2. Prevent Overwriting:
   import long_module_name as short
   # Prevents accidentally overwriting imported functions

3. Resolve Built-in Conflicts:
   import my_io_module as custom_io
   # Avoids conflict with Python's built-in io module

KEY PYTHON NAMESPACES:

1. Built-in: print(), len(), etc.
2. Global: Your main module's namespace  
3. Local: Inside functions
4. Module: Each .py file has its own namespace

BEST PRACTICES:

1. Use aliases for:
   - Long module names
   - Modules with common names
   - When importing multiple modules with similar functions

2. Use 'from module import' for:
   - Frequently used functions
   - When the source is obvious
   - In small, single-purpose scripts

3. Avoid 'from module import *':
   - Pollutes namespace uncontrollably
   - Makes code hard to understand
   - High collision risk
"""
    print(concepts)


if __name__ == "__main__":
    print("PYTHON MODULES AND PACKAGES DEMONSTRATION")
    print("="*60)
    
    demonstrate_basic_usage()
    demonstrate_namespace_collisions() 
    compare_import_styles()
    explain_namespace_concepts()
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print("""
✓ Created proper package structure with __init__.py
✓ Demonstrated multiple import styles with aliases
✓ Showed real namespace collision scenarios
✓ Explained how aliases prevent conflicts
✓ Compared trade-offs of different import approaches

The key takeaway: Use import aliases to maintain clear, 
collision-free namespaces, especially in larger projects.
""")