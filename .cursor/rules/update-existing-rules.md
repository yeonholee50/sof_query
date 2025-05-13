---
description: Update Existing Rules Task
globs: *.md
task: update-existing-rules
alwaysApply: false
---
# Update Existing Rules

This task performs the following actions:

1. **Comprehensive Rule Checking:**
   - **Examine ALL rules** in the codebase, regardless of keyword matches.
   - Exempt only the following system files from examination:
     - add-new-rule.md
     - update-existing-rules.md
     - update-codebase.md
     - master-router.md
     - main.md
     - overlapping-rule-processor.md
   - For each rule file:
     - Check if the rule file contains any inline comments or sections that need to be updated based on the new rule.
     - Provide explicit confirmation after checking each rule: "[Rulename] checked. [Updated/No updates needed]."

2. **Rule Update Process:**
   - For each rule requiring updates:
     - Open the rule file and examine all examples and documentation sections.
     - Apply any new rule requirements to the examples and documentation:
       - For example, if the new rule enforces that inline comments must end with a specific word, update all inline comment examples in the rule to reflect this requirement.
       - If the rule has multiple requirements (e.g., inline horse at beginning AND inline donkey at end), ensure ALL requirements are applied.
     - Update any relevant syntax, formatting, or coding examples to comply with the new rule.
   
3. **Example Updates:**
   - Every rule update MUST include updates to its examples section.
   - Ensure examples demonstrate compliance with the new requirements.
   - For rules with code snippets, modify all applicable code snippets to follow the new rule.

4. **Content Preservation:**
   - When updating rules, preserve all existing functionality.
   - Add to the rule's requirements without removing or changing existing ones.
   - Ensure the rule remains clear and consistent after updates.

5. **Registration Check:**
   - Confirm that all rules in the system are properly registered in the master router.
   - Verify that keyword lists are up-to-date and complete.

6. **Completion Confirmation:**
   - After completing ALL rule checks and updates, explicitly state:
     - "Update-existing-rules task completed. [X] rules checked, [Y] rules updated."
     - "Ready to proceed to update-codebase task."
   - Do not proceed to the next step until this confirmation is acknowledged.
