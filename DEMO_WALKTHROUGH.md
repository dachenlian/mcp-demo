# MCP Demo: Exploring Linguistic Olympiad Research with AI

## Overview

This demo shows how to use MCP (Model Context Protocol) servers in VS Code to:

1. Query a custom linguistic analysis server
2. Search and download academic papers from arXiv
3. Perform deep analysis of research papers

**Time:** ~15-20 minutes

---

## Prerequisites

### 1. Configure MCP Servers in VS Code

Add the following to `.vscode/mcp.json` in your project root:

```json
{
    "servers": {
        "linguistHelper": {
            "type": "stdio",
            "command": "uv",
            "args": [
                "run",
                "fastmcp",
                "run",
                "server.py"
            ]
        },
        "arxiv-mcp-server": {
            "type": "stdio",
            "command": "uvx",
            "args": [
                "arxiv-mcp-server",
                "--storage-path",
                "./data/arxiv_storage"
            ]
        }
    },
    "inputs": []
}
```

### 3. Restart VS Code

After adding the configuration, restart VS Code or reload the window for the MCP servers to activate.

---

## Demo Script: Conversation Flow

### Part 1: Exploring the Custom Linguistic Server

**Objective:** Understand what capabilities your custom MCP server provides.

#### Prompt 1: Discover Available Data

```text
what texts does my db have?
```

**What happens:**

- Copilot queries the `linguistHelper` MCP server (it should, might just read the `server.py` file)
- Server returns list of available corpus texts
- Shows: 3 sample texts (2 English, 1 Chinese)

**Key learning:** MCP servers expose data through "resources" that AI can discover automatically.

---

#### Prompt 2: Discover Available Tools

```text
what tools do I have?
```

**What happens:**

- Copilot lists the tools exposed by the `linguistHelper` server (it should, might just read the `server.py` file)
- Shows: `calculate_ttr`, `count_words`, `find_longest_word`

**Key learning:** Tools are functions the AI can call to perform computations.

---

#### Prompt 3: Use a Tool

```text
please calculate the ttr of en sample 1
```

**What happens:**

- Copilot calls the `calculate_ttr` tool with the text from en_sample_01
- Returns Type-Token Ratio (TTR) of 0.889
- Explains what this means (high lexical diversity)

**Key learning:** AI can chain operations: retrieve data → call tool → interpret results.

---

### Part 2: Academic Research with arXiv MCP Server

**Objective:** Search for research papers and perform analysis using `arxiv-mcp-server`.

GitHub repo: <https://github.com/blazickjp/arxiv-mcp-server>

#### Prompt 4: Search for Papers

```text
help me find papers related to llms solving linguistic olympiad problems
```

**What happens:**

- Copilot uses the `arxiv-mcp-server` to search arXiv
- Applies smart query construction with categories `["cs.CL", "cs.AI"]`
- Returns 15 relevant papers with abstracts
- Highlights the most relevant ones

**Key learning:** MCP servers can wrap external APIs (arXiv) and make them accessible to AI.

---

#### Prompt 5: Download a Paper

```
please download the first one
```

**What happens:**

- Copilot downloads paper 2509.21820v1
- Converts PDF to markdown format for analysis
- Confirms successful download

**Key learning:** MCP tools can perform complex operations (download + convert) as single actions.

---

#### Prompt 6: Deep Analysis

```
please do a deep analysis of it
```

**What happens:**

- Copilot reads the full paper content using MCP resource
- Performs comprehensive analysis covering:
  - Core research questions
  - Key findings (solving vs generating puzzles)
  - Theoretical foundations
  - Dataset details
  - Critical insights
  - Limitations
  - Broader implications

**Key learning:** AI can process long-form content from MCP resources and synthesize complex information.

---

#### Prompt 7: Save Analysis

```
please save this to a markdown file
```

**What happens:**

- Copilot creates `paper_analysis.md` with structured analysis
- File is ready for sharing or further editing

**Key learning:** AI can combine MCP data with file operations to produce artifacts.

---

## What This Demo Shows

### 1. MCP's Core Value Proposition

**Traditional approach (without MCP):**

- Manually visit arXiv website
- Copy/paste search queries
- Download PDFs manually
- Use separate tools to convert and analyze
- Switch between multiple applications

**With MCP:**

- Natural language instructions
- AI discovers and uses appropriate tools
- Seamless integration across different servers
- All within your development environment

---

### 2. Two Types of MCP Servers in Action

#### Custom Server (`linguistHelper`)

- **Purpose:** Domain-specific linguistic analysis
- **Demonstrates:** How to build specialized tools for your research
- **Key features:**
  - Resources (corpus data)
  - Tools (TTR calculation, word counting)
  - Prompts (analysis workflows)

#### Third-Party Server (`arxiv-mcp-server`)

- **Purpose:** Access external academic databases
- **Demonstrates:** Reusing community-built servers
- **Key features:**
  - Paper search with advanced filtering
  - PDF download and conversion
  - Paper storage and retrieval

---

### 3. AI Orchestration

Notice how Copilot:

1. **Discovers capabilities** automatically (doesn't need to be told what tools exist)
2. **Chains operations** (search → download → read → analyze → save)
3. **Handles complexity** (formats queries, manages async operations, error handling)
4. **Provides context** (explains what it's doing and why)

---

## Extension Ideas for Class

### Beginner Level

1. **Add a new tool** to `server.py`: Calculate Flesch Reading Ease score
2. **Query different categories** on arXiv: Try searching for papers on syntax or morphology
3. **Customize the analysis**: Ask for comparison between multiple papers

### Intermediate Level

1. **Create a new MCP server** for accessing a different corpus (e.g., Universal Dependencies)
2. **Chain multiple tools**: Calculate TTR for all texts in the corpus and find the most diverse one
3. **Export to different formats**: Generate LaTeX or HTML reports from paper analysis

### Advanced Level

1. **Build a research pipeline**: Search → download → extract methodology → compare approaches
2. **Integrate with databases**: Create an MCP server that queries your annotation database
3. **Multi-modal analysis**: Combine text analysis with figure extraction from papers

---

## Troubleshooting

### MCP servers not appearing in Copilot

1. Check `.vscode/mcp.json` is in the project root
2. Verify JSON syntax (no trailing commas)
3. Restart VS Code completely
4. Check the Output panel for MCP-related errors

### Server connection errors

```bash
# Test the linguistic server manually
uv run fastmcp run server.py

# Test the arxiv server manually
uvx arxiv-mcp-server --storage-path ./data/arxiv_storage
```

### Dependencies missing

```bash
# Install project dependencies
uv sync

# Or manually
pip install fastmcp arxiv-mcp-server
```

---

## Key Takeaways

1. **MCP makes tools discoverable**: AI doesn't need pre-programmed knowledge of what tools exist
2. **One protocol, many servers**: Mix custom and community servers seamlessly
3. **Natural language interface**: Complex operations become simple conversations
4. **Local control**: Your data and credentials stay on your machine
5. **Extensible ecosystem**: Easy to add new capabilities as your research evolves

---

## Resources

- **MCP Official Docs**: <https://modelcontextprotocol.io/>
- **fastmcp Library**: <https://github.com/jlowin/fastmcp>
- **arXiv MCP Server**: <https://github.com/blazickjp/arxiv-mcp-server>
- **MCP Server Examples**: <https://github.com/modelcontextprotocol/servers>
- **This Demo Project**: `mcp_short.ipynb` for detailed MCP introduction

### MCP Registries

Find more MCP servers here:

- <https://mcpservers.org/>
- <https://github.com/blazickjp/arxiv-mcp-server>

---

## Questions for Discussion

1. How could MCP improve your current research workflow?
2. What linguistic analysis tools would you want to expose via MCP?
3. What are the security implications of giving AI access to your research data?
4. How does this compare to using Jupyter notebooks for corpus analysis?
5. What research tasks would benefit most from AI orchestration via MCP?
