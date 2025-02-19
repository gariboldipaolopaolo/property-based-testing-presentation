import pytest
from hypothesis import given, strategies as st
import json

def object_to_binary(obj: dict) -> str:
    """Converts a dictionary to a binary string representation."""
    json_str = json.dumps(obj)  # Convert object to JSON string
    return ' '.join(format(ord(char), '08b') for char in json_str)  # Convert JSON to binary

def binary_to_object(binary: str) -> dict:
    """Converts a binary string back to a dictionary."""
    json_str = ''.join(chr(int(b, 2)) for b in binary.split())  # Convert binary to JSON string
    return json.loads(json_str)  # Convert JSON string to dictionary

# Define the Hypothesis strategy for generating complex objects
complex_object_strategy = st.fixed_dictionaries({
    "value": st.integers(min_value=-1_000_000, max_value=1_000_000),
    "lat": st.floats(min_value=-90, max_value=90, allow_nan=False, allow_infinity=False),
    "lon": st.floats(min_value=-180, max_value=180, allow_nan=False, allow_infinity=False),
})

@given(complex_object_strategy)
def test_binary_object_conversion(obj):
    """Property-based test: Converting an object to binary and back should return the original object."""
    binary = object_to_binary(obj)
    recovered_obj = binary_to_object(binary)
    assert recovered_obj == obj

if __name__ == "__main__":
    pytest.main([__file__])