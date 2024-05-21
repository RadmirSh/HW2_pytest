import subprocess

def test_crc32_hash_calculation():
    file_path = "file.txt"
    result = subprocess.run(["crc32", file_path], capture_output=True, text=True)
    assert result.returncode == 0, "Command failed"
    expected_hash = "C8A32C7A"
    assert expected_hash in result.stdout, f"Expected CRC32 hash {expected_hash} not found in output"