from fastmcp import FastMCP

# Initialize server (like FastAPI's app = FastAPI())
mcp = FastMCP("LinguistHelper")

# Mock corpus (in reality, this could be a database)
CORPUS = {
    "en_sample_01": "The quick brown fox jumps over the lazy dog.",
    "en_sample_02": "To be, or not to be, that is the question.",
    "zh_sample_01": "學而不思則罔,思而不學則殆。",
}

# ============================================================================
# RESOURCES: Give AI access to data
# ============================================================================


@mcp.resource("corpus://list")
def list_texts() -> str:
    """List all available text IDs in the corpus."""
    return "\n".join(CORPUS.keys())


@mcp.resource("corpus://{text_id}")
def get_text(text_id: str) -> str:
    """Retrieve text content by ID."""
    if text_id not in CORPUS:
        available = ", ".join(CORPUS.keys())
        return f"Error: Text '{text_id}' not found. Available: {available}"
    return CORPUS[text_id]


# ============================================================================
# TOOLS: Give AI computational capabilities
# ============================================================================


@mcp.tool()
def calculate_ttr(text: str) -> float:
    """
    Calculate Type-Token Ratio (TTR) of a text.
    TTR = (Unique Words / Total Words)
    Higher values indicate greater lexical diversity.

    Example: "the cat sat on the mat" -> 5/6 = 0.83
    """
    if not text:
        return 0.0

    tokens = text.lower().split()  # Simple tokenization
    types = set(tokens)  # Unique words

    return len(types) / len(tokens) if tokens else 0.0


@mcp.tool()
def count_words(text: str) -> int:
    """Count total words in text."""
    return len(text.split())


@mcp.tool()
def find_longest_word(text: str) -> str:
    """Find the longest word in the text."""
    words = text.split()
    return max(words, key=len) if words else ""


# ============================================================================
# PROMPTS: Pre-built workflows for common tasks
# ============================================================================


@mcp.prompt()
def analyze_complexity(text_id: str) -> str:
    """Generate a prompt for analyzing text complexity."""
    return f"""
Please analyze the linguistic complexity of corpus://{text_id}.

Steps:
1. First, read the text using the corpus://{text_id} resource
2. Calculate its Type-Token Ratio using the calculate_ttr tool
3. Find the longest word using the find_longest_word tool
4. Provide a brief assessment of lexical complexity

A TTR above 0.7 typically indicates rich vocabulary.
"""


if __name__ == "__main__":
    mcp.run()
