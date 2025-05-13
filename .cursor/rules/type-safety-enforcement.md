---
description: Type Safety Enforcement
globs: 
alwaysApply: false
---
---
description: Type Safety Enforcement
globs: *.py
---
# Type Safety Enforcement

Standards for enforcing type safety in all functions.

<rule>
name: type_safety_enforcement
description: Ensures all Python functions have proper type annotations for both parameters and return values
filters:
  - type: file_extension
    pattern: "\\.py$"
  - type: content
    pattern: "def\\s+([a-zA-Z0-9_]+)\\s*\\("
actions:
  - type: reject
    conditions:
      - pattern: "def\\s+[a-zA-Z0-9_]+\\s*\\((?![^)]*:\\s*[a-zA-Z][a-zA-Z0-9_]*)[^)]*\\)"
        message: "Function parameters missing type annotations"
      - pattern: "def\\s+[a-zA-Z0-9_]+\\s*\\([^)]*\\)\\s*(?!->\\s*[a-zA-Z][a-zA-Z0-9_]*)"
        message: "Function missing return type annotation"
  - type: suggest
    message: |
      **Type Safety Enforcement**
      
      Ensure all functions have proper type annotations. For example:
      
      ```python
      def example_function(param1: str, param2: int) -> bool:
          """
          Description.
          
          Args:
              param1 (str): Description.
              param2 (int): Description.
          
          Returns:
              bool: Description.
          """
          # This is properly typed
      ```
metadata:
  priority: high
  version: 1.0
  keywords: "type safety, annotations, Python, parameters, return type, type consistency, typing, enforcement"
</rule>




