"""Utility functions for file operations."""

from pathlib import Path
from typing import Optional


def load_prompt_file(file_path: str | Path, ignore_comments: bool = True) -> Optional[str]:
    """
    Load a prompt file and optionally filter out comment lines.
    
    Args:
        file_path: Path to the prompt file
        ignore_comments: Whether to filter out lines starting with '#'
        
    Returns:
        The file contents as a string, or None if file doesn't exist or is empty
    """
    path = Path(file_path)
    
    # Check if file exists
    if not path.is_file():
        print(f"[DEBUG] File not found at path: {path}")
        return None
    
    # Check if file is empty
    if path.stat().st_size == 0:
        print(f"[DEBUG] File exists but is empty: {path}")
        return None
    
    # Read and process the file
    try:
        content = path.read_text(encoding="utf-8")
        
        if ignore_comments:
            # Filter out comment lines
            lines = content.splitlines(keepends=True)
            content = "".join(line for line in lines if not line.strip().startswith("#"))
        
        print(f"[DEBUG] Successfully loaded file. Length: {len(content)} characters")
        return content
        
    except Exception as e:
        print(f"[ERROR] Failed to read file {path}: {e}")
        return None

