---
description: Add New Rule Task
globs: *.md
alwaysApply: false
---
---
description: Add New Rule Task
globs: *.md
task: add-new-rule
keywords: "reflect, our, company, coding, convention, appends, word, end, inline, comment"
reference: main.md
---
# Add New Rule

This task performs the following steps:

1. **Process Keywords:**
   - Extract and normalize the prompt keywords (convert to lowercase, trim spaces).
   - Store these keywords in memory for comparison with existing rules.

2. **Check Overlapping Rules:**
   - For each rule in the `existing_rules` list in master-router.md:
     - Normalize each rule's keyword string by converting to lowercase, splitting on commas, and trimming spaces.
     - Compare each prompt keyword against the rule's keywords.
     - Count the number of matching keywords between the prompt and each rule.
     - Identify the rule with the highest number of keyword matches, if any.

3. **Create New Rule or Update Existing Rule:**
   - **If no matching keywords are found or matching count is zero:**
     - Create a new rule using the template found in main.md.
     - Structure the new rule and place it in the `.cursor/rules/` directory.
     - **Name the file atomically based on the element it pertains to, not its positional attributes:**
       - Use the format `element-name.md` (e.g., `inline-comment.md` instead of `inline-comment-beginning.md` or `inline-comment-ending.md`)
       - Make names reflect what the rule modifies, not how it modifies it
       - If an element rule already exists, use the overlapping-rule-processor to merge requirements instead of creating position-specific files
     - Register the new rule in the `existing_rules` list in master-router.md with its filename and all keywords.

   - **If an existing rule has matching keywords:**
     - Identify the rule with the most keyword matches (most overlapping).
     - Update that rule by:
       - Adding any non-overlapping keywords from the prompt to its keyword list.
       - Modifying the rule's content to incorporate the prompt's requirements.
       - Do not create a new rule, instead enhance the existing one to handle multiple related requirements.
       - **IMPORTANT: PRESERVE ALL EXISTING FUNCTIONALITY and ADD the new requirements. Never replace existing requirements.**
       - Ensure the file remains atomically named based on the element it pertains to.

4. **Completion Confirmation:**
   - After creating a new rule or updating an existing rule, explicitly state:
     - "Add-new-rule task completed. Rule [created/updated]: [filename]."
     - "Ready to proceed to update-existing-rules task."
   - Do not proceed to the next step until this confirmation is acknowledged.

5. **Prepare for Next Steps:**
   - Once the rule is created or updated and registered, the **update-existing-rules** task must be completed before moving to the **update-codebase** task.
