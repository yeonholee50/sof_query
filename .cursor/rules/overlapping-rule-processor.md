---
description: Overlapping Rule Processor
globs: *.md
alwaysApply: false
---
---
description: Overlapping Rule Processor
globs: *.md
---
# Overlapping Rule Processor

This utility handles the processing of overlapping rules, determining whether to create a new rule or update an existing one.

<rule>
name: overlapping_rule_processor
description: Processes keywords to determine rule overlap and decides whether to create or update rules
filters:
  - type: event
    pattern: "rule_creation"
actions:
  - type: process
    steps:
      - extract_keywords:
          description: "Extract and normalize all keywords from the prompt"
          normalize: true
      - compare_rules:
          description: "Compare keywords against all existing rules to find overlap"
          count_matches: true
          find_best_match: true
      - decide_action:
          description: "Decide whether to create new rule or update existing rule"
          threshold: 1
          action_if_match: "update"
          action_if_no_match: "create"
      - update_rule:
          description: "Update the most overlapping rule with new requirements"
          preserve_existing: true
          merge_keywords: true
        **never_replace_existing_requirements: true**
      - create_rule:
          description: "Create a new rule if no significant overlap exists"
          template: "main.md"
          naming: "atomic"
      - register_rule:
          description: "Register the new or updated rule in master-router.md"
          update_keywords: true
  - type: suggest
    message: |
      **Overlapping Rule Processing**
      
      When processing keywords for rule overlap:
      
      1. Extract all keywords from the prompt
      2. Compare against existing rules to find overlaps
      3. If significant overlap exists with an existing rule:
         - Update the existing rule to include new requirements
         - Merge any non-overlapping keywords
      4. If no significant overlap exists:
         - Create a new rule based on the template
         - Use atomic file naming that reflects the element being modified (e.g., `inline-comment.md`) 
         - Avoid positional naming schemes (e.g., avoid `inline-comment-beginning.md` or `inline-comment-ending.md`)
      5. Register the new or updated rule in master-router.md
      
      Example of handling overlapping requirements:
      
      ```python
      # Before: Rule for inline comments exists in inline-comment.md
      def example():
          x = 5  # donkey this is a comment
          
      # After: Rule updated to include multiple requirements in the same file
      def example():
          x = 5  # donkey this is a comment jaguar
      ```
examples:
  - input: |
      # Processing overlapping keywords
      prompt_keywords = ["inline", "comment", "end", "word"]
      existing_rule_keywords = ["inline", "comment", "start", "style"]
      
      # Significant overlap: 2 matching keywords ("inline", "comment")
      # Decision: Update existing rule
    output: |
      # Rule updated to include both requirements in a single atomic file
      def example():
          x = 5  # required_start_word this is a comment required_end_word
metadata:
  priority: high
  version: 1.0
  keywords: "overlap, rule, processing, keywords, matching, update, create, merge, requirements, atomic, naming"
</rule>