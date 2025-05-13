---
description: Python Docstring Convention
globs: 
alwaysApply: false
---
---
description: Python Docstring Convention
globs: *.py
---
# Python Docstring Convention

Standards for writing consistent and descriptive docstrings in Python.

<rule>
name: docstring_convention
description: Ensures Python functions follow the project's docstring format
filters:
  - type: file_extension
    pattern: "\\.py$"
  - type: content
    pattern: "def\\s+([a-zA-Z0-9_]+)\\s*\\("
actions:
  - type: reject
    conditions:
      - pattern: "def\\s+([a-zA-Z0-9_]+)\\s*\\([^)]*\\)\\s*:\\s*(?![\"\'])"
        message: "Function missing a docstring"
  - type: suggest
    message: |
      **Python Docstring Convention**
      
      Every function must include a docstring formatted as follows:
      
      ```python
      def function_name(arg1, arg2):
          """
          Short description.
          
          Args:
              arg1 (type): Description.
              arg2 (type): Description.
          
          Returns:
              type: Description.
          """
      ```
metadata:
  priority: high
  version: 1.0
  keywords: "docstring, Python, documentation, convention, function, Args, Returns, formatting, guidelines"
</rule>

## Example

```python
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.
    
    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    # Multiply width by height
    return width * height
```



