import pytest
import subprocess

def test_list_files_command():
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    assert result.returncode == 0, "Command failed"
    assert "file.txt" in result.stdout, "File not found in the output"