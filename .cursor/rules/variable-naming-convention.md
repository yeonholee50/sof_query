---
description: Variable Naming Convention Rule
globs: 
alwaysApply: false
---
---
description: Variable Naming Convention Rule
globs: *.js,*.ts,*.jsx,*.tsx,*.py,*.java,*.c,*.cpp,*.cs
---
# Variable Naming Convention

This rule enforces that all variables follow the camelCase convention.

<rule>
name: variable_naming_convention
description: Ensures all variables follow camelCase naming
filters:
  - type: file_extension
    pattern: "\\.(js|ts|jsx|tsx|py|java|c|cpp|cs)$"
  - type: content
    pattern: "(?:var|let|const|int|float|double|string|boolean|char|long|class|function|def)\\s+([a-zA-Z0-9_]+)"
actions:
  - type: reject
    conditions:
      - pattern: "(?:var|let|const|int|float|double|string|boolean|char|long)\\s+([a-z][a-z0-9]*_[a-z0-9_]*)"
        message: "Variable names should use camelCase, not snake_case"
      - pattern: "(?:var|let|const|int|float|double|string|boolean|char|long)\\s+([a-z][a-z0-9]*-[a-z0-9-]*)"
        message: "Variable names should use camelCase, not kebab-case"
      - pattern: "(?:var|let|const|int|float|double|string|boolean|char|long)\\s+([A-Z][a-zA-Z0-9]*)"
        message: "Variable names should use camelCase, not PascalCase"
  - type: suggest
    message: |
      **Variable Naming Convention**
      
      Ensure variables follow camelCase. For example:
      
      ```javascript
      let firstName = "John"; // User's first name
      const maxAttempts = 3; // Maximum number of login attempts
      ```
      
      
examples:
  - input: |
      let first_name = "John"; // User's first name
      const MAX_ATTEMPTS = 3; // Maximum number of login attempts
    output: |
      let firstName = "John"; // User's first name
      const maxAttempts = 3; // Maximum number of login attempts
metadata:
  priority: high
  version: 1.0
  keywords: "variable, naming, camelCase, snake_case, kebab-case, code style, consistency, formatting"
</rule>




