---
description: Cursor Rules Location
globs: 
alwaysApply: false
---
---
description: Cursor Rules Location
globs: *.mdc
---
# Cursor Rules Location

Rules for placing and organizing Cursor rule files in the repository.

<rule>
name: cursor_rules_location
description: Standards for placing Cursor rule files in the correct directory
filters:
  - type: file_extension
    pattern: "\\.mdc$"
  - type: content
    pattern: "(?s)<rule>.*?</rule>"
  - type: event
    pattern: "file_create"
actions:
  - type: reject
    conditions:
      - pattern: "^(?!\\.\\/\\.cursor\\/rules\\/.*\\.mdc$)"
        message: "Cursor rule files (.mdc) must be placed in the .cursor/rules directory"
  - type: suggest
    message: |
      When creating Cursor rules:
      
      1. Always place rule files in PROJECT_ROOT/.cursor/rules/:
         ```
         .cursor/rules/
         ├── your-rule-name.mdc
         ├── another-rule.mdc
         └── ...
         ```
      2. Follow the naming convention:
         - Use kebab-case for filenames
         - Always use .mdc extension
         - Make names descriptive of the rule's purpose
         - **Use atomic naming** that describes the element being modified (e.g., `inline-comment.md`) 
         - **Avoid positional naming** that describes how the element is modified (e.g., avoid `inline-comment-beginning.md`)
         - If a rule for an element already exists, update that rule instead of creating a new file
      3. Directory structure:
         ```
         PROJECT_ROOT/
         ├── .cursor/
         │   └── rules/
         │       ├── your-rule-name.mdc
         │       └── ...
         └── ...
         ```
      4. Never place rule files:
         - In the project root
         - In subdirectories outside .cursor/rules
         - In any other location
examples:
  - input: |
      # Bad: Rule file in wrong location
      rules/my-rule.mdc
      my-rule.mdc
      .rules/my-rule.mdc
      
      # Bad: Positional naming
      .cursor/rules/inline-comment-beginning.mdc
      .cursor/rules/variable-naming-pascal-case.mdc
      
      # Good: Rule file in correct location with atomic naming
      .cursor/rules/my-rule.mdc
      .cursor/rules/inline-comment.mdc
      .cursor/rules/variable-naming.mdc
    output: "Correctly placed and named Cursor rule file"
metadata:
  priority: high
  version: 1.0
  keywords: "cursor, rules, location, placement, directory, .cursor/rules, organization, file_create, atomic, naming"
</rule>
