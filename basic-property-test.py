import pytest
from hypothesis import given, strategies as st

def string_to_binary(text: str) -> str:
    """Converts a string to its binary representation (space-separated)."""
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_string(binary: str) -> str:
    """Converts a binary string (space-separated) back to text."""
    return ''.join(chr(int(b, 2)) for b in binary.split())

@given(st.text())  # Generate random text strings
def test_binary_conversion(text):
    """Property-based test: Converting to binary and back should return the original text."""
    binary = string_to_binary(text)
    recovered_text = binary_to_string(binary)
    assert recovered_text == text

if __name__ == "__main__":
    pytest.main([__file__])