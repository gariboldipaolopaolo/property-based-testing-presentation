import pytest
from hypothesis import given, strategies as st
import json
import math

def object_to_binary(obj: dict) -> str:
    """Converts a complex dictionary to a binary string representation."""
    json_str = json.dumps(obj, separators=(",", ":"))  # Minify JSON to reduce inconsistencies
    return ' '.join(format(ord(char), '08b') for char in json_str)


def binary_to_object(binary: str) -> dict:
    """Converts a binary string back to a dictionary."""
    json_str = ''.join(chr(int(b, 2)) for b in binary.split())
    return json.loads(json_str)


# Define strategy for complex nested objects
complex_object_strategy = st.fixed_dictionaries({
    "id": st.uuids().map(str),  # Ensure unique identifiers
    "location": st.fixed_dictionaries({
        "lat": st.floats(min_value=-90, max_value=90, allow_nan=False, allow_infinity=False),
        "long": st.floats(min_value=-180, max_value=180, allow_nan=False, allow_infinity=False),
        "altitude": st.floats(min_value=-500, max_value=10000, allow_nan=False, allow_infinity=False)
    }),
    "data_points": st.lists(
        st.fixed_dictionaries({
            "timestamp": st.integers(min_value=1_600_000_000, max_value=1_900_000_000),  # Unix timestamp range
            "value": st.floats(allow_nan=False, allow_infinity=False)
        }),
        min_size=1,
        max_size=10
    ),
    "meta": st.text(min_size=0, max_size=200)
})


@given(complex_object_strategy)
def test_binary_object_conversion(obj):
    """Property-based test: Converting a complex object to binary and back should return the original object."""
    binary = object_to_binary(obj)
    recovered_obj = binary_to_object(binary)

    # Validate exact match for strings and integers
    assert recovered_obj["id"] == obj["id"]
    assert recovered_obj["meta"] == obj["meta"]

    # Validate floats with precision tolerance
    for key in ["lat", "long", "altitude"]:
        assert math.isclose(recovered_obj["location"][key], obj["location"][key], rel_tol=1e-6)

    for original, recovered in zip(obj["data_points"], recovered_obj["data_points"]):
        assert original["timestamp"] == recovered["timestamp"]
        assert math.isclose(original["value"], recovered["value"], rel_tol=1e-6)

if __name__ == "__main__":
    pytest.main([__file__])
