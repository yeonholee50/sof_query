---
description: Update Codebase Task
globs: *.md
task: update-codebase
alwaysApply: false
---
# Update Codebase

This task performs a global update across the codebase to integrate changes introduced by new or updated rules. The AI MUST edit actual files in the codebase directly rather than simulating the process:

1. **Prerequisite Check:**
   - Confirm that both the add-new-rule and update-existing-rules tasks have been completed.
   - Do not proceed with this task if either of the previous steps was skipped.

2. **File Iteration Required Tools:**
   - Use `list_dir` tool to recursively traverse the entire codebase to locate all source files in supported languages.
   - Use `read_file` tool to examine each file's contents.
   - Use `edit_file` tool to modify files that need changes.
   - Using only echo commands or simulating changes is NOT acceptable - actual file edits MUST be performed.

3. **Exempt Files:**
   - The following system files should NEVER be modified, even if they match rule patterns:
     - .cursor/rules/master-router.md
     - .cursor/rules/add-new-rule.md
     - .cursor/rules/update-existing-rules.md
     - .cursor/rules/update-codebase.md
     - .cursor/rules/main.md
     - .cursor/rules/overlapping-rule-processor.md
   - Skip these files entirely during the update process.

4. **Rule Application Process:**
   - For each file with extensions matching those in the rules:
     - Read the file's content using `read_file`
     - Analyze the content for sections that don't comply with rules
     - Use `edit_file` to modify the file to bring it into compliance
     - For example, if a rule requires inline comments to end with "donkey", use `edit_file` to add that word to all comments
   - Document which files were examined and which were modified

5. **Logging and Reporting:**
   - Log every file that is visited and document any modifications made.
   - For each modification, list the specific file path and changes applied.
   - Include files that were checked but required no changes.

6. **Completion Confirmation:**
   - After applying actual edits to files across the codebase, explicitly state: 
     - "Update-codebase task completed. [X] files processed, [Y] files modified."
     - Detail which files were changed and how they were changed.

## Example Implementation

Here's an example of how the task should be implemented for a rule requiring inline comments to end with "donkey":

```
1. Use list_dir to find all directories
2. For each directory, find files with extensions matching the rule
3. For each matching file:
   - Use read_file to check for inline comments
   - If inline comments exist and don't end with "donkey", use edit_file to update them
   - Document the file examined and whether changes were made
4. Provide a summary of all files processed and modified
```

This approach ensures that every applicable file in the codebase is visited and that the rules are executed and enforced by making actual edits to the files.





