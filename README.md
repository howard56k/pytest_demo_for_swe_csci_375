# Python Unit Tests Demo for GitHub Actions

This is a demonstration project showing how to set up unit tests for Python projects with GitHub Actions CI/CD.

## Project Structure

```
.
├── calculator.py          # Simple calculator module
├── test_calculator.py     # Unit tests using pytest
├── requirements.txt       # Python dependencies
├── .github/
│   └── workflows/
│       └── python-tests.yml  # GitHub Actions workflow
└── README.md
```

## Features

- **Calculator Module**: Simple mathematical operations (add, subtract, multiply, divide, power)
- **Comprehensive Unit Tests**: Test cases covering various scenarios including edge cases
- **GitHub Actions CI/CD**: Automated testing on multiple Python versions
- **Test Coverage**: Coverage reporting with pytest-cov

## Setup

### Local Development

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd pytest_demo_for_swe
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**:
   ```bash
   pytest test_calculator.py -v
   ```

5. **Run tests with coverage**:
   ```bash
   pytest test_calculator.py --cov=calculator --cov-report=term
   ```

## GitHub Actions Workflow

The workflow (`.github/workflows/python-tests.yml`) is configured to:

- **Trigger on**:
  - Push to `main`, `master`, or `develop` branches
  - Pull requests to these branches
  - Manual workflow dispatch

- **Test on multiple Python versions**: 3.9, 3.10, 3.11, and 3.12

- **Steps**:
  1. Checkout code
  2. Set up Python with caching
  3. Install dependencies
  4. Run tests with pytest
  5. Generate coverage reports
  6. (Optional) Upload coverage to Codecov

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with verbose output:
```bash
pytest -v
```

### Run specific test class:
```bash
pytest test_calculator.py::TestAdd -v
```

### Run specific test:
```bash
pytest test_calculator.py::TestAdd::test_add_positive_numbers -v
```

### Run with coverage:
```bash
pytest --cov=calculator --cov-report=html
```

## Example Usage

```python
from calculator import add, subtract, multiply, divide, power

# Addition
result = add(5, 3)  # Returns 8

# Subtraction
result = subtract(10, 4)  # Returns 6

# Multiplication
result = multiply(3, 4)  # Returns 12

# Division
result = divide(15, 3)  # Returns 5.0

# Power
result = power(2, 8)  # Returns 256
```

## License

This is a demo project for educational purposes.
