"""
Test runner script for Sepik Fresh
Run all tests with: python run_tests.py
"""
import pytest
import sys

def run_tests():
    """Run all tests and display results"""
    print("=" * 70)
    print("SEPIK FRESH - RUNNING UNIT TESTS")
    print("=" * 70)
    print()
    
    # Run pytest with verbose output
    exit_code = pytest.main([
        'tests/',
        '-v',
        '--tb=short',
        '--color=yes'
    ])
    
    print()
    print("=" * 70)
    if exit_code == 0:
        print("✅ ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED")
    print("=" * 70)
    
    return exit_code

if __name__ == '__main__':
    sys.exit(run_tests())
