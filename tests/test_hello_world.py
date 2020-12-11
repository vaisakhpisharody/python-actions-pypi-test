"""
Tests for the Hello World Module
"""
from src.hello_world import get_hello_world_string

def test_get_hello_world():
    """
    This function tests the get_hello_world function
    """
    assert "Hello World" == get_hello_world_string()