"""Tests for file_utils module."""

import pytest
from pathlib import Path
from job_agent.utils import load_prompt_file


def test_load_prompt_file_basic(tmp_path):
    """Test basic file loading."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello World")
    
    result = load_prompt_file(test_file)
    assert result == "Hello World"


def test_load_prompt_file_with_comments(tmp_path):
    """Test file loading with comment filtering."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("# This is a comment\nActual content\n# Another comment\nMore content")
    
    result = load_prompt_file(test_file, ignore_comments=True)
    assert "# This is a comment" not in result
    assert "Actual content" in result
    assert "More content" in result


def test_load_prompt_file_without_comment_filtering(tmp_path):
    """Test file loading without comment filtering."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("# This is a comment\nContent")
    
    result = load_prompt_file(test_file, ignore_comments=False)
    assert "# This is a comment" in result


def test_load_prompt_file_not_found():
    """Test behavior when file doesn't exist."""
    result = load_prompt_file("nonexistent_file.txt")
    assert result is None


def test_load_prompt_file_empty(tmp_path):
    """Test behavior with empty file."""
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    result = load_prompt_file(test_file)
    assert result is None

