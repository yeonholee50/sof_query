---
description: Function Creation Convention
globs: 
alwaysApply: false
---
---
description: Function Creation Convention
globs: *.py
---
# Function Creation Convention

Standards for creating consistent and well-structured functions in Python.

<rule>
name: function_creation_convention
description: Ensures all Python functions follow the project's formatting, naming, and documentation requirements
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
      **Function Creation Convention**
      
      All functions must:
      
      1. Use snake_case for names.
      2. Include a docstring in the following format:
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
      3. Use camelCase for variables.
      4. Maintain a single responsibility, use 4 spaces for indentation, and have a max line length of 100 characters.
examples:
  - input: |
      def calculate_sum(a, b):
          # Add two numbers
          return a + b
      
      def process_data(data_list):
          result = []
          for item in data_list:
              # Process each item
              result.append(item * 2)
          return result
    output: |
      def calculate_sum(a, b):
          # Add two numbers
          return a + b
      
      def process_data(data_list):
          result = []
          for item in data_list:
              # Process each item
              result.append(item * 2)
          return result
metadata:
  priority: high
  version: 1.0
  keywords: "function, creation, convention, Python, naming, documentation, formatting, code style, guidelines"
</rule>



