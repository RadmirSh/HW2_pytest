import pytest
import subprocess

def test_list_files_command():
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    assert result.returncode == 0, "Command failed"
    assert "file.txt" in result.stdout, "File not found in the output"

def test_extract_with_paths_command():
    result = subprocess.run(["tar", "xf", "archive.tar"], capture_output=True, text=True)
    assert result.returncode == 0, "Command failed"
    assert "extracted_file.txt" in subprocess.run(["ls"], capture_output=True, text=True).stdout, "Extracted file not found"