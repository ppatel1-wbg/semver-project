# Test-Driven GitHub Actions PR Blocking Demo

This project demonstrates how to set up GitHub Actions workflows that automatically block PR merges when tests fail, ensuring code quality and preventing broken code from reaching the main branch.

## 🎯 Project Overview

This repository contains:
- A simple Python calculator module with comprehensive tests
- GitHub Actions workflow that runs on every PR
- Branch protection rules that block merges when tests fail
- Security scanning and code quality checks

## 📁 Project Structure

```
semver-project/
├── .github/
│   ├── workflows/
│   │   ├── test-pr-validation.yml    # Main test workflow
│   │   └── code-review.yml           # AI code review workflow  
│   ├── scripts/
│   │   └── setup-branch-protection.sh # Automated branch protection setup
│   └── docs/
│       └── BRANCH_PROTECTION_SETUP.md # Manual setup instructions
├── src/
│   ├── __init__.py
│   ├── calculator.py                 # Calculator functions
│   └── main.py                       # Main application
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py            # Comprehensive tests
│   └── test_failure_demo.py          # Intentional failure tests for demo
├── requirements-test.txt             # Test dependencies
├── pyproject.toml                    # pytest configuration
└── README.md                         # This file
```

## 🚀 Quick Setup

### 1. Clone and Test Locally

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run tests locally
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing
```

### 2. Set Up Branch Protection (Choose One)

#### Option A: Automated Setup (Recommended)
```bash
# Install GitHub CLI if not already installed
brew install gh  # macOS
# or visit https://cli.github.com/ for other platforms

# Authenticate
gh auth login

# Run the setup script
./.github/scripts/setup-branch-protection.sh
```

#### Option B: Manual Setup
Follow the detailed instructions in [`.github/docs/BRANCH_PROTECTION_SETUP.md`](.github/docs/BRANCH_PROTECTION_SETUP.md)

## 🧪 Testing the PR Blocking Workflow

### Test 1: Create a PR with Passing Tests
```bash
# Create a feature branch
git checkout -b feature/add-documentation
echo "# Additional Documentation" >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "Add changelog file"
git push origin feature/add-documentation
```
Then create a PR on GitHub. You should see:
- ✅ All tests pass
- ✅ Security scans pass  
- ✅ Merge button is enabled

### Test 2: Create a PR with Failing Tests
```bash
# Create a branch with failing tests
git checkout -b feature/failing-tests

# Edit the test file to make it fail
# Uncomment line 17 in tests/test_failure_demo.py:
# assert add(2, 2) == 5, "This is an intentional failure for testing"

git add tests/test_failure_demo.py
git commit -m "Add failing test to demonstrate blocking"
git push origin feature/failing-tests
```
Then create a PR on GitHub. You should see:
- ❌ Tests fail
- 🚫 Merge button is disabled with "Merging is blocked" message

## 🔍 Workflow Details

### The Test Workflow (`test-pr-validation.yml`) includes:

1. **Multi-Python Version Testing**
   - Tests run on Python 3.9, 3.10, and 3.11
   - Ensures compatibility across Python versions

2. **Comprehensive Test Coverage**
   - Runs pytest with coverage reporting
   - Requires minimum 80% code coverage
   - Generates coverage reports for Codecov

3. **Code Quality Checks**
   - Flake8 linting for code style
   - Bandit security scanning for vulnerabilities
   - Safety check for dependency vulnerabilities

4. **PR Validation Gate**
   - Final job that depends on all previous jobs
   - Only passes if all tests and security scans pass
   - This job is what blocks the merge when added to branch protection

### Status Checks Created:
- `Run Tests (3.9)`
- `Run Tests (3.10.0)`
- `Run Tests (3.11)`
- `Security Scan`
- `PR Merge Validation`

## 🔒 Branch Protection Configuration

When properly configured, the branch protection rules ensure:
- ✅ Pull requests are required before merging
- ✅ At least 1 approval is required
- ✅ All status checks must pass
- ✅ Branches must be up to date before merging
- ✅ Conversations must be resolved
- ✅ Force pushes and deletions are prevented

## 🛠️ Development Workflow

1. **Create a feature branch**: `git checkout -b feature/your-feature`
2. **Write code and tests**: Ensure tests cover your changes
3. **Run tests locally**: `pytest tests/ -v`
4. **Push and create PR**: GitHub Actions will automatically run
5. **Review results**: Check the Actions tab for detailed results
6. **Fix issues**: If tests fail, fix them before merge is allowed
7. **Merge**: Once all checks pass, the PR can be merged

## 📊 Code Coverage

The workflow generates code coverage reports and uploads them to Codecov. Coverage requirements:
- Minimum 80% overall coverage (configured in `pyproject.toml`)
- Coverage reports show which lines need test coverage

## 🔧 Customization

### Adding More Test Types
Add new jobs to `.github/workflows/test-pr-validation.yml`:
```yaml
integration-tests:
  name: Integration Tests
  runs-on: ubuntu-latest
  steps:
    # Add your integration test steps
```

### Adjusting Coverage Requirements
Modify `pyproject.toml`:
```toml
[tool.pytest.ini_options]
addopts = [
    "--cov-fail-under=90"  # Require 90% coverage
]
```

### Adding Status Checks
Update the branch protection rules to include new check names from your workflow.

## 🎯 Best Practices Demonstrated

1. **Fail Fast**: Tests run early in the process to catch issues quickly
2. **Multi-Environment Testing**: Tests run on multiple Python versions
3. **Security First**: Security scans are mandatory, not optional
4. **Clear Feedback**: Workflow provides clear success/failure messages
5. **Automation**: Branch protection prevents human error in merge decisions
6. **Documentation**: Clear instructions for setup and usage

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub CLI Documentation](https://cli.github.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for your changes
4. Ensure all tests pass locally
5. Create a pull request
6. Wait for automated checks to complete
7. Address any issues found by the workflow

---

**Note**: This setup ensures that no code reaches the main branch without passing all tests and security checks, maintaining high code quality and preventing regressions.
