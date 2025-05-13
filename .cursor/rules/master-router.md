---
description: This file orchestrates the rule creation and update process in three sequential steps:
globs: 
alwaysApply: false
---
### File: `.cursor/rules/master-router.md`
---
keywords: reflect,our,company,coding,convention,appends,word,end,inline,comment
do_tasks:
  - add-new-rule.md
  - update-existing-rules.md
  - update-codebase.md
execution_instructions: |
  When adding a new rule or updating existing rules, all three tasks must be executed in sequence:
  1. First, run the add-new-rule.md task to create and register the new rule
  2. Next, run the update-existing-rules.md task to ensure all rules are consistent
  3. Finally, run the update-codebase.md task to apply the rule changes across the codebase
  
  To execute these tasks, use the AI to:
  - Implement each task according to its instructions in the corresponding .md file
  - Confirm completion of each task before moving to the next
  - DO NOT SKIP ANY STEPS OR CHANGE THE ORDER
  - Each step must be explicitly acknowledged as completed before proceeding

  The following files are OFF-LIMITS and should NEVER be modified during the update process:
  - master-router.md
  - add-new-rule.md
  - update-existing-rules.md
  - update-codebase.md
  - main.md
  - overlapping-rule-processor.md
  These system files are exempt from rule updates and should remain unchanged.
existing_rules:
  - file: ../function-creation-convention.md
    keywords: "function, creation, convention, Python, naming, documentation, formatting, code style, guidelines"
  - file: ../type-safety-enforcement.md
    keywords: "type safety, annotations, Python, parameters, return type, type consistency, typing, enforcement"
  - file: ../variable-naming-convention.md
    keywords: "variable, naming, camelCase, snake_case, kebab-case, code style, consistency, formatting"
  - file: ../docstring-convention.md
    keywords: "docstring, Python, documentation, convention, function, Args, Returns, formatting, guidelines"
---

# Master Router

This file orchestrates the rule creation and update process in three sequential steps:

1. **Add New Rule or Update Existing Rule:** See @add-new-rule.md  
   - Process prompt keywords to determine whether to create a new rule or update an existing one.
   - Use the overlapping-rule-processor to check all existing rules for keyword matches.
   - If significant overlap exists with an existing rule, update that rule with new requirements **while preserving ALL existing requirements. Never remove or replace existing functionality.**
   - If no significant overlap exists, create a new rule and register it.
   - For any rule created or updated, its reference (filename) and keywords are maintained in the `existing_rules` list.
   - **WAIT** for confirmation that this step is completed before proceeding.

2. **Update Existing Rules:** See @update-existing-rules.md  
   - This task examines ALL rules in the codebase (excluding system files).
   - Each rule is checked regardless of keyword matches to ensure comprehensive coverage.
   - Rules are updated to reflect any new requirements in their examples and documentation.
   - Confirmation is provided after each rule is examined and potentially updated.
   - **WAIT** for confirmation that this step is completed before proceeding.

3. **Update Codebase:** See @update-codebase.md  
   - This task performs a global update across the entire codebase.
   - Every applicable file is examined and updated according to all relevant rules.
   - Detailed logging tracks which files were processed and what changes were made.
   - After completion, any temporary keywords or rule information are cleared from memory.
   - Only execute this step after steps 1 and 2 are fully completed.




