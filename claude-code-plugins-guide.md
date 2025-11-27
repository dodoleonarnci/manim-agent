# Complete Guide to Implementing Subagents and Skills Plugins in Claude Code

## Table of Contents
1. [Understanding the Architecture](#understanding-the-architecture)
2. [Creating Custom Subagents](#creating-custom-subagents)
3. [Creating Custom Skills](#creating-custom-skills)
4. [Building a Complete Plugin](#building-a-complete-plugin)
5. [Plugin Hooks Integration](#plugin-hooks-integration)
6. [Custom Slash Commands](#custom-slash-commands)
7. [Installation and Registration](#installation-and-registration)
8. [Team Workflow Configuration](#team-workflow-configuration)
9. [Best Practices](#best-practices)

---

## Understanding the Architecture

Claude Code's plugin system consists of several core components that work together to extend functionality:

### Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (required)
├── commands/                # Custom slash commands
├── agents/                  # Custom subagent definitions
├── skills/                  # Agent skills
├── hooks/
│   └── hooks.json          # Event handlers
└── scripts/                # Supporting utilities
```

### Key Concepts

- **Subagents**: Pre-configured AI personalities that Claude Code can delegate tasks to, each with their own context window
- **Skills**: Modular capabilities that Claude autonomously uses based on context (unlike slash commands which are user-invoked)
- **Plugins**: Bundles that package subagents, skills, commands, and hooks together for distribution

---

## Creating Custom Subagents

### What Are Subagents?

Subagents are specialized AI assistants with focused responsibilities. They maintain separate context windows from the main conversation and are automatically invoked when relevant.

### Storage Locations

- **Project-level**: `.claude/agents/` (team-shared via git)
- **User-level**: `~/.claude/agents/` (personal preferences)
- **Plugin-level**: Inside plugin's `agents/` directory

### Step-by-Step: Creating a Subagent

#### Step 1: Create the Agent File

Create a Markdown file in `.claude/agents/` directory:

**Example: `.claude/agents/code-reviewer.md`**

```markdown
---
name: code-reviewer
description: Specialized agent for comprehensive code reviews focusing on security, performance, and maintainability
model: claude-sonnet-4-5
tools: [read, execute, grep, write]
---

# Code Reviewer Subagent

You are an expert code reviewer specializing in security audits and performance optimization.

## Responsibilities
- Review code for security vulnerabilities (SQL injection, XSS, CSRF, etc.)
- Identify performance bottlenecks and optimization opportunities
- Suggest architectural improvements
- Verify test coverage and edge case handling

## Instructions
- Always check for injection vulnerabilities in user input handling
- Look for resource leaks (unclosed files, connections, etc.)
- Verify error handling is comprehensive and informative
- Check for proper input validation and sanitization
- Assess code complexity and suggest refactoring when appropriate

## Review Checklist
1. Security: Validate all user inputs, check for common vulnerabilities
2. Performance: Identify inefficient algorithms, unnecessary database queries
3. Maintainability: Check code organization, naming conventions, documentation
4. Testing: Verify test coverage, edge cases, error scenarios
```

#### Step 2: Configure Agent Metadata

The frontmatter (YAML section between `---`) defines the agent's configuration:

- **`name`**: Unique identifier (lowercase with hyphens, e.g., `code-reviewer`)
- **`description`**: Clear purpose statement - critical for Claude to know when to invoke the agent
- **`model`**: Optional model specification (defaults to parent model if not specified)
- **`tools`**: Array of allowed tools to restrict access for security

#### Step 3: Write the System Prompt

The Markdown content after the frontmatter becomes the agent's system prompt. Include:
- Role definition
- Specific responsibilities
- Step-by-step instructions
- Examples and checklists

#### Step 4: Access and Test

Use the CLI to manage agents:

```bash
/agents           # Opens agent management interface
```

Claude Code will automatically invoke your custom subagent when the task matches the agent's description.

### Subagent Examples

#### Example 1: Architecture Analyst

```markdown
---
name: architecture-analyst
description: Analyzes software architecture and system design patterns
model: opus
tools: [read, grep, glob]
---

# Architecture Analyst

Analyze software architecture focusing on:
- Design patterns and their appropriateness
- System boundaries and coupling
- Scalability considerations
- Technology stack alignment

Provide architectural recommendations with trade-offs clearly explained.
```

#### Example 2: Test Generator

```markdown
---
name: test-generator
description: Generates comprehensive test cases for code coverage
tools: [read, write, execute]
---

# Test Generator

Generate comprehensive test suites including:
- Unit tests for individual functions
- Integration tests for component interactions
- Edge cases and error scenarios
- Mock data and fixtures

Follow the testing patterns already established in the codebase.
```

---

## Creating Custom Skills

### What Are Skills?

Skills are modular capabilities that extend Claude's functionality. Claude autonomously decides to use skills based on context matching, making them more intelligent than manual commands.

### Storage Locations

- **Personal**: `~/.claude/skills/`
- **Project**: `.claude/skills/`
- **Plugin**: `my-plugin/skills/`

### Step-by-Step: Creating a Skill

#### Step 1: Create the Skill Directory

```bash
mkdir -p .claude/skills/pdf-extraction
```

#### Step 2: Create SKILL.md (Required)

**Example: `.claude/skills/pdf-extraction/SKILL.md`**

```yaml
---
name: pdf-extraction
description: Extract text, tables, and images from PDF files. Use when working with PDF documents, analyzing reports, or converting PDFs to structured data.
allowed-tools: [read, execute, grep]
---

# PDF Extraction Skill

This skill enables Claude to intelligently extract and process content from PDF files.

## Capabilities

- Extract text with formatting preservation
- Parse tables into structured formats (CSV, JSON)
- Identify and extract embedded images
- Handle multi-page documents efficiently
- Preserve document structure and hierarchy

## Usage Triggers

Claude will automatically use this skill when you:
- Ask to read or analyze a PDF file
- Request data extraction from documents
- Want to convert PDF content to other formats
- Need to parse tables from PDF reports

## Implementation Details

The skill uses the following approach:

1. **Validate PDF Access**: Check file exists and is readable
2. **Analyze Content Type**: Determine if PDF contains text, images, or scanned content
3. **Apply Extraction Method**:
   - Text-based PDFs: Direct text extraction with pdfplumber
   - Scanned PDFs: OCR with Tesseract
   - Mixed content: Hybrid approach
4. **Structure Output**: Format extracted data for further processing

## Dependencies

- `pdfplumber`: For text and table extraction
- `Pillow`: For image processing
- `pytesseract`: For OCR (optional)

## Example Usage

```bash
# The skill provides a Python script that Claude can execute
python ${CLAUDE_SKILL_ROOT}/extract_pdf.py --input report.pdf --output data.json
```
```

#### Step 3: Add Supporting Scripts (Optional)

**Example: `.claude/skills/pdf-extraction/extract_pdf.py`**

```python
#!/usr/bin/env python3
"""
PDF Extraction Script
Extracts text, tables, and images from PDF files
"""

import sys
import json
import argparse
import pdfplumber
from pathlib import Path

def extract_pdf(filepath, output_format='json'):
    """Extract content from PDF file"""
    results = {
        'text': [],
        'tables': [],
        'metadata': {},
        'page_count': 0
    }

    with pdfplumber.open(filepath) as pdf:
        results['metadata'] = pdf.metadata
        results['page_count'] = len(pdf.pages)

        for i, page in enumerate(pdf.pages, 1):
            # Extract text
            text = page.extract_text()
            if text:
                results['text'].append({
                    'page': i,
                    'content': text
                })

            # Extract tables
            tables = page.extract_tables()
            for j, table in enumerate(tables, 1):
                results['tables'].append({
                    'page': i,
                    'table_number': j,
                    'data': table
                })

    return results

def main():
    parser = argparse.ArgumentParser(description='Extract content from PDF files')
    parser.add_argument('--input', required=True, help='Input PDF file')
    parser.add_argument('--output', required=True, help='Output file')
    parser.add_argument('--format', default='json', choices=['json', 'txt'])

    args = parser.parse_args()

    # Extract PDF content
    data = extract_pdf(args.input)

    # Write output
    with open(args.output, 'w', encoding='utf-8') as f:
        if args.format == 'json':
            json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            for item in data['text']:
                f.write(f"Page {item['page']}:\n{item['content']}\n\n")

    print(f"Extracted {len(data['text'])} pages, {len(data['tables'])} tables")

if __name__ == '__main__':
    main()
```

#### Step 4: Configure Metadata

The frontmatter in `SKILL.md` defines critical settings:

- **`name`**: Lowercase with hyphens (e.g., `pdf-extraction`)
- **`description`**: Max 1024 characters. Must include:
  - What the skill does
  - **When to use it** (specific triggers)
- **`allowed-tools`**: Array of tools Claude can use (restricts access for security)

### Good vs Bad Skill Descriptions

**Good Description** (specific triggers):
```
Extract text and tables from PDFs using pdfplumber. Use when working with PDF files, analyzing reports, converting documents to structured data, or parsing PDF tables.
```

**Poor Description** (too vague):
```
Helps with documents
```

### Skill Examples

#### Example 1: Code Analysis Skill

```yaml
---
name: code-analysis
description: Perform static code analysis and complexity metrics. Use when analyzing code quality, identifying refactoring opportunities, or measuring technical debt.
allowed-tools: [read, execute, grep, glob]
---

# Code Analysis Skill

Provides comprehensive static code analysis including:
- Cyclomatic complexity measurement
- Code duplication detection
- Dependency analysis
- Security vulnerability scanning

Uses tools like `radon`, `pylint`, `eslint` depending on language.
```

#### Example 2: Database Query Optimizer

```yaml
---
name: sql-optimizer
description: Analyze and optimize SQL queries for performance. Use when working with database queries, investigating slow queries, or optimizing database access patterns.
allowed-tools: [read, execute]
---

# SQL Query Optimizer

Analyzes SQL queries and provides:
- Query execution plan analysis
- Index recommendations
- Query rewriting suggestions
- Performance impact estimates

Supports PostgreSQL, MySQL, SQLite query analysis.
```

---

## Building a Complete Plugin

### Step 1: Create Plugin Directory Structure

```bash
mkdir -p my-advanced-tools/.claude-plugin
mkdir -p my-advanced-tools/{agents,skills,commands,hooks,scripts}
```

### Step 2: Create Plugin Manifest

**File: `my-advanced-tools/.claude-plugin/plugin.json`**

```json
{
  "name": "advanced-code-tools",
  "version": "1.0.0",
  "displayName": "Advanced Code Tools",
  "description": "Collection of specialized agents and skills for code analysis, review, and optimization",
  "author": "Your Organization <team@example.com>",
  "license": "MIT",

  "main": "index.js",
  "commands": "commands/",
  "agents": "agents/",
  "skills": "skills/",
  "hooks": "hooks/hooks.json",

  "keywords": ["code-review", "analysis", "optimization", "security"],
  "homepage": "https://github.com/yourorg/advanced-code-tools",
  "repository": {
    "type": "git",
    "url": "https://github.com/yourorg/advanced-code-tools.git"
  },

  "engines": {
    "claude-code": ">=1.0.0"
  },

  "dependencies": {
    "pdfplumber": "^0.10.0",
    "radon": "^6.0.0"
  }
}
```

### Step 3: Add Plugin Components

Add your subagents to `agents/`, skills to `skills/`, and commands to `commands/` following the structures described above.

### Step 4: Add README

**File: `my-advanced-tools/README.md`**

```markdown
# Advanced Code Tools Plugin

Comprehensive toolkit for code review, analysis, and optimization in Claude Code.

## Features

- **Code Reviewer Agent**: Automated security and performance reviews
- **PDF Extraction Skill**: Extract data from PDF documents
- **Code Analysis Skill**: Static analysis and metrics

## Installation

```bash
/plugin install advanced-code-tools@your-marketplace
```

## Usage

The plugin's agents and skills are automatically available after installation.

### Example: Code Review

Claude will automatically invoke the code-reviewer agent when you ask for code reviews.

### Example: PDF Extraction

Simply reference a PDF file and Claude will use the extraction skill when appropriate.

## Configuration

No additional configuration required. The plugin works out of the box.

## License

MIT
```

---

## Plugin Hooks Integration

Hooks allow plugins to automatically execute commands when certain events occur.

### Step 1: Create Hooks Configuration

**File: `my-advanced-tools/hooks/hooks.json`**

```json
{
  "description": "Automatic code formatting and quality checks",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh",
            "timeout": 30,
            "description": "Auto-format modified files"
          }
        ]
      }
    ],
    "PreCommit": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/lint.sh",
            "timeout": 60,
            "description": "Run linting before commit"
          }
        ]
      }
    ]
  }
}
```

### Step 2: Create Hook Scripts

**File: `my-advanced-tools/scripts/format.sh`**

```bash
#!/bin/bash
# Auto-format code files

FILE_PATH="$1"

case "$FILE_PATH" in
  *.py)
    black "$FILE_PATH"
    ;;
  *.js|*.ts)
    prettier --write "$FILE_PATH"
    ;;
  *.go)
    gofmt -w "$FILE_PATH"
    ;;
esac
```

### Available Hook Types

- **`PostToolUse`**: After Claude uses a tool (Write, Edit, Execute, etc.)
- **`PreCommit`**: Before git commits
- **`PostCommit`**: After git commits
- **`PrePush`**: Before git push

### Environment Variables

Hooks have access to:
- `${CLAUDE_PLUGIN_ROOT}`: Absolute path to plugin directory
- `${CLAUDE_PROJECT_DIR}`: Project root directory
- `${FILE_PATH}`: File being operated on (context-dependent)

---

## Custom Slash Commands

Add custom slash commands to your plugin for user-invoked functionality.

### Step 1: Create Command File

**File: `my-advanced-tools/commands/analyze-code.md`**

```markdown
---
name: analyze-code
description: Run comprehensive code analysis
arguments:
  - name: file
    description: File path to analyze
    required: true
  - name: depth
    description: Analysis depth (basic|detailed|comprehensive)
    required: false
    default: detailed
---

# Code Analysis Command

Analyze the specified file with comprehensive metrics.

## Analysis Process

1. Run static analysis tools
2. Measure code complexity
3. Check for security issues
4. Generate report

## Execution

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/analyze.sh "$file" --depth "$depth"
```

## Output

Returns analysis including:
- Cyclomatic complexity metrics
- Security vulnerability scan results
- Performance bottleneck identification
- Code style violations
- Suggested improvements
```

### Step 2: Create Supporting Script

**File: `my-advanced-tools/scripts/analyze.sh`**

```bash
#!/bin/bash
# Code analysis script

FILE="$1"
DEPTH="${2:-detailed}"

echo "Analyzing: $FILE (depth: $DEPTH)"

# Run analysis based on file type
case "$FILE" in
  *.py)
    radon cc "$FILE" -a
    pylint "$FILE"
    ;;
  *.js)
    eslint "$FILE"
    ;;
  *.go)
    golint "$FILE"
    go vet "$FILE"
    ;;
esac
```

### Usage

After plugin installation, users can invoke:

```bash
/analyze-code src/main.py --depth comprehensive
```

---

## Installation and Registration

### Installing Plugins

#### From Marketplace

```bash
/plugin install advanced-code-tools@marketplace-name
```

#### Local Development

```bash
# Install from local directory for testing
/plugin install /path/to/my-advanced-tools@local
```

### Managing Plugins

```bash
/plugin              # Interactive plugin menu
/plugin list         # Show all installed plugins
/plugin info advanced-code-tools   # Show plugin details
/plugin disable advanced-code-tools  # Disable without uninstalling
/plugin enable advanced-code-tools   # Re-enable
/plugin uninstall advanced-code-tools  # Remove plugin
```

### Development Workflow

1. **Create plugin structure** (see above)
2. **Test locally**: Install with `/plugin install` using local path
3. **Iterate**: Make changes and reinstall to reload
4. **Publish**: Push to marketplace when ready

---

## Team Workflow Configuration

### Repository-level Configuration

Share plugin configuration with your team by adding to `.claude/settings.json`:

**File: `.claude/settings.json`**

```json
{
  "plugins": [
    {
      "name": "advanced-code-tools",
      "version": "1.0.0",
      "marketplace": "company-internal",
      "enabled": true
    },
    {
      "name": "team-conventions",
      "version": "2.1.0",
      "marketplace": "npm",
      "enabled": true
    }
  ],
  "agents": [
    "code-reviewer",
    "architecture-analyst"
  ],
  "skills": [
    "pdf-extraction",
    "code-analysis",
    "sql-optimizer"
  ],
  "defaultAgent": "code-reviewer"
}
```

### Benefits

- All team members get consistent tooling
- Agents and skills are automatically available
- Shared configuration through version control
- Easier onboarding for new team members

---

## Best Practices

### For Subagents

1. **Single Responsibility**: Design agents with focused, well-defined purposes
   - Good: `code-reviewer` - reviews code for issues
   - Bad: `general-helper` - does everything

2. **Clear System Prompts**: Include comprehensive instructions
   - Define the agent's role and expertise
   - List specific responsibilities
   - Provide step-by-step guidelines
   - Include checklists and examples

3. **Tool Restrictions**: Limit tools to what the agent needs
   - Read-only agents: `[read, grep, glob]`
   - Analysis agents: `[read, execute, grep]`
   - Full-capability agents: `[read, write, execute, edit]`

4. **Descriptive Names**: Use clear, searchable names
   - Use lowercase with hyphens
   - Be specific: `security-auditor` vs `auditor`

5. **Documentation**: Document expected behavior and limitations

### For Skills

1. **Trigger-Rich Descriptions**: Include specific usage scenarios
   ```yaml
   description: Extract PDF content. Use when working with PDF files, analyzing reports, or parsing document tables.
   ```

2. **Security Through Restrictions**: Use `allowed-tools` to limit access
   ```yaml
   allowed-tools: [read, execute]  # No write access
   ```

3. **Logical Organization**: Structure supporting files clearly
   ```
   skill-name/
   ├── SKILL.md
   ├── extractor.py
   ├── templates/
   └── docs/
   ```

4. **Test Contextual Activation**: Verify Claude invokes the skill appropriately

5. **Version with Project**: Track skills in version control alongside code

### For Plugins

1. **Comprehensive README**: Include installation, usage examples, and troubleshooting

2. **Semantic Versioning**: Use semver for version management
   - `1.0.0` - Initial release
   - `1.1.0` - New features, backward compatible
   - `2.0.0` - Breaking changes

3. **Document Everything**: Agents, skills, commands, and hooks
   - What they do
   - When to use them
   - Configuration options

4. **Test Hooks Thoroughly**: Ensure hooks don't interfere with workflow

5. **Provide Marketplace Metadata**: Help users discover your plugin
   - Clear description
   - Relevant keywords
   - Screenshots/examples

6. **Handle Dependencies**: List all required tools and libraries

### General Guidelines

- **Start Simple**: Begin with one agent or skill, expand later
- **Test in Isolation**: Verify each component works independently
- **Get Feedback**: Test with team members before wide deployment
- **Iterate**: Improve based on actual usage patterns
- **Document Gotchas**: Note any limitations or edge cases

---

## References

This guide is based on official Claude Code documentation:

- **Plugins Overview**: https://code.claude.com/docs/en/plugins.md
- **Subagents Guide**: https://code.claude.com/docs/en/sub-agents.md
- **Skills Documentation**: https://code.claude.com/docs/en/skills.md
- **Hooks Integration**: https://code.claude.com/docs/en/hooks.md
- **Slash Commands**: https://code.claude.com/docs/en/slash-commands.md

---

## Quick Reference

### File Locations

```
Project Level (.claude/)
├── agents/          # Team-shared subagents
├── skills/          # Project-specific skills
├── commands/        # Custom slash commands
└── settings.json    # Team configuration

User Level (~/.claude/)
├── agents/          # Personal subagents
├── skills/          # Personal skills
└── settings.json    # User preferences

Plugin (my-plugin/)
├── .claude-plugin/
│   └── plugin.json  # Manifest
├── agents/          # Plugin subagents
├── skills/          # Plugin skills
├── commands/        # Plugin commands
├── hooks/           # Event handlers
└── scripts/         # Supporting utilities
```

### Essential Commands

```bash
# Plugin Management
/plugin                         # Interactive menu
/plugin list                    # List installed
/plugin install <name>          # Install plugin
/plugin uninstall <name>        # Remove plugin

# Agent Management
/agents                         # Agent interface
/agent <name>                   # Use specific agent

# Help
/help                           # General help
/help plugins                   # Plugin help
```

---

## Conclusion

Claude Code's plugin system provides a powerful way to extend functionality through subagents, skills, and custom commands. By following this guide, you can create specialized tools that integrate seamlessly into your development workflow and share them with your team.

Start small, test thoroughly, and iterate based on feedback to build plugins that truly enhance productivity.
