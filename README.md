# 🛒 Amazon UI Automation Framework

A robust and scalable **UI Automation Testing Framework** developed using **Python, Selenium WebDriver, PyTest, and the Page Object Model (POM)**. The framework automates an end-to-end Amazon shopping workflow while following industry best practices for maintainability, reusability, and reliability.

> **Note:** This project is created for learning and portfolio purposes. It demonstrates automation framework design and should be used only in accordance with Amazon's Terms of Service.

---

# 📌 Project Overview

This framework automates the following user journey on Amazon:

* Launch the browser
* Navigate to Amazon
* Login using valid credentials
* Validate successful login
* Search for a product
* Select a product from the search results
* Add the product to the cart
* Handle the optional "Add to Your Order" popup
* Navigate to the shopping cart
* Proceed to checkout

The framework has been designed with modularity and scalability in mind, making it easy to extend for additional test scenarios.

---

# 🚀 Technologies Used

| Technology              | Purpose              |
| ----------------------- | -------------------- |
| Python 3.x              | Programming Language |
| Selenium WebDriver      | Browser Automation   |
| PyTest                  | Test Framework       |
| pytest-html             | HTML Report Generation |
| ChromeDriver            | Browser Driver       |
| webdriver-manager       | ChromeDriver Management |
| Page Object Model (POM) | Design Pattern       |
| Logging                 | Execution Logging    |
| Explicit Waits          | Synchronization      |
| Git & GitHub            | Version Control      |

---

# 🏗️ Framework Architecture

The project follows the **Page Object Model (POM)** design pattern.

```text
AmazonAutomationFramework/
│
├── base/
│   ├── __init__.py
│   └── base_page.py
│
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── search_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   └── test_login.py
│
├── Reports/
│   ├── report.html          (Generated HTML test report)
│   └── screenshots/         (Auto-captured failure screenshots)
│
├── config.py                (Configuration - uses environment variables)
├── conftest.py              (pytest fixtures & screenshot hooks)
├── pytest.ini               (pytest configuration & test markers)
├── requirements.txt         (Python dependencies)
├── run_tests.bat           (Windows test runner script)
├── run_tests.sh            (Linux/Mac test runner script)
├── .gitignore              (Excludes Reports and cache from git)
└── README.md
```

Each web page is represented by its own class, keeping locators and page-specific actions separate from test logic.

---

# 📂 Framework Design

```text
Home Page
      │
      ▼
Login Page
      │
      ▼
Dashboard Page
      │
      ▼
Search Page
      │
      ▼
Product Page
      │
      ▼
Cart Page
```

This architecture improves:

* Code Reusability
* Readability
* Scalability
* Easy Maintenance
* Separation of Concerns

---

# ✨ Key Features

## ✅ Page Object Model (POM)

Each page has its own class containing:

* Locators
* Actions
* Page validations

This minimizes duplicate code and makes maintenance easier.

---

## ✅ Reusable BasePage

The framework contains a centralized `BasePage` class that provides reusable utility methods shared across all pages.

### Implemented Utilities

* Wait for Visibility
* Wait for Clickable
* Scroll to Element
* Safe Click
* Retry Mechanism
* Page Validation

---

## ✅ Explicit Wait Strategy

The framework avoids `time.sleep()` for synchronization wherever possible by using Selenium Explicit Waits.

```python
wait_for_visibility(locator)

wait_for_clickable(locator)
```

Benefits:

* Faster execution
* Stable tests
* Reduced flaky failures

---

## ✅ HTML Report Generation & Auto Screenshots

The framework now automatically generates professional HTML reports and captures screenshots on test failures.

### Features

* **Self-contained HTML Report** - Single file includes all test results, logs, and execution times
* **Auto Screenshot Capture** - Timestamped screenshots on every test failure for quick failure diagnosis
* **Organized Storage** - Reports and screenshots stored in `Reports/` directory, excluded from version control via `.gitignore`
* **pytest Hooks** - `pytest_runtest_makereport` hook handles screenshot capture without manual intervention

### Usage

Screenshots are **automatically captured** on any test failure. No manual action needed.

Generated artifacts:
* `Reports/report.html` - Complete test execution report
* `Reports/screenshots/` - Failure screenshots with timestamps (e.g., `test_invalid_login_20260831_174200.png`)

---

## ✅ Environment Variable Support

Credentials are now sourced from environment variables for better security.

### Configuration

In `config.py`, credentials use `os.environ.get()` with safe fallbacks:

```python
email_id = os.environ.get('AMAZON_EMAIL', 'lmpravee+usca2@amazon.com')
password_id = os.environ.get('AMAZON_PASSWORD', 'testing')
```

### Setting Environment Variables

**Linux/Mac:**
```bash
export AMAZON_EMAIL="your-email@amazon.com"
export AMAZON_PASSWORD="your-password"
```

**Windows (PowerShell):**
```powershell
$env:AMAZON_EMAIL = "your-email@amazon.com"
$env:AMAZON_PASSWORD = "your-password"
```

**Windows (Command Prompt):**
```cmd
set AMAZON_EMAIL=your-email@amazon.com
set AMAZON_PASSWORD=your-password
```

---

## ✅ Test Configuration (pytest.ini)

The `pytest.ini` file defines test markers and logging configuration.

### Test Markers

Organize tests by category:

```bash
pytest -m login           # Run only login tests
pytest -m smoke           # Run smoke tests
pytest -m integration     # Run integration tests
```

Available markers: `smoke`, `regression`, `login`, `search`, `cart`, `integration`

---

## ✅ Logging

Execution logs are captured using Python's built-in `logging` module.

Example:

```text
INFO - Launching browser
INFO - Logging in
INFO - Product selected
INFO - Product added to cart
INFO - Navigated to Cart
INFO - Closing browser
```

Logging simplifies debugging and helps identify failures quickly.

---

## ✅ Environment Variable Support

Passwords are **not hardcoded** inside the project.

Example:

```python
password = os.environ.get("AMAZON_PASSWORD")
```

This improves security and follows industry best practices.

---

# 🧪 Test Scenario Covered

### End-to-End Shopping Flow

* Open Amazon
* Login
* Validate login
* Search for a product
* Select the first available product
* Add product to cart
* Handle optional warranty popup
* Navigate to cart
* Proceed to checkout

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/AmazonAutomationFramework.git
```

Navigate into the project

```bash
cd AmazonAutomationFramework
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Tests

## Quick Start (Recommended)

Use the provided test runner scripts for easy HTML report generation and automatic screenshot capture.

### Windows
```bash
.\run_tests.bat
```

### Linux/Mac
```bash
./run_tests.sh
```

## Manual Test Execution

Run all tests with HTML report:

```bash
pytest tests/test_login.py -v --html=Reports/report.html --self-contained-html
```

Run a specific test:

```bash
pytest tests/test_login.py::test_valid_login -v
```

Run tests by marker:

```bash
pytest tests/test_login.py -m login -v                # Login tests only
pytest tests/test_login.py -m smoke -v                # Smoke tests only
pytest tests/test_login.py -m integration -v          # Integration tests only
```

---

# 📊 Reports

The framework automatically generates comprehensive HTML reports and captures screenshots on failures.

### HTML Report Features

* **Test Results** - Pass/fail status with color coding
* **Execution Time** - Per-test and total execution duration
* **Console Logs** - Full timestamped logging output
* **Failure Details** - Tracebacks and error messages
* **Self-Contained** - Single HTML file, no external dependencies

### Screenshot Capture

Screenshots are **automatically captured** on test failure:

* **File naming** - `{test_name}_{YYYYMMDD}_{HHMMSS}.png`
* **Storage** - `Reports/screenshots/` directory
* **Logging** - Path logged to console on capture

### Viewing Reports

After running tests:

1. Open `Reports/report.html` in any web browser
2. View failure screenshots in `Reports/screenshots/` directory

### Example Report Command

```bash
pytest tests/test_login.py -v --html=Reports/report.html --self-contained-html --tb=short
```

This generates:
* `Reports/report.html` - Complete test report
* `Reports/screenshots/*.png` - Failure screenshots (auto-captured)

---

# 🔮 Future Enhancements

The framework is designed to be easily extendable.

Planned improvements include:

* Jenkins CI/CD Integration
* GitHub Actions Workflow
* Cross-Browser Testing
* Parallel Execution using `pytest-xdist`
* Allure Reporting (alternative to pytest-html)
* Data-Driven Testing
* Docker Support
* Headless Browser Execution
* Browser Compatibility Matrix
* Email Report Distribution
* Slack Integration for Test Results

---

# 💡 Automation Concepts Implemented

* Page Object Model (POM)
* Explicit Waits (visibility, clickable, presence)
* Retry Mechanism (handles StaleElementReferenceException, ElementClickInterceptedException)
* Safe Click Implementation (wait → scroll → click → retry → JS fallback)
* JavaScript Executor
* Exception Handling
* Reusable Base Class
* Object-Oriented Programming (OOP)
* Logging with timestamps
* Environment Variables for credentials
* Modular Framework Design
* Automatic Screenshot Capture on Failures
* HTML Report Generation
* pytest Hooks for test lifecycle management
* Test Markers for test categorization

---

# 📸 Test Reports & Screenshots

The framework generates professional test reports with automatic screenshot capture on failures.

### Report Artifacts

After running tests, check:

* `Reports/report.html` - Complete test execution report (open in browser)
* `Reports/screenshots/` - Failure screenshots with timestamps

### Example Artifacts

```
Reports/
├── report.html                           (Auto-generated on each test run)
├── screenshots/
│   ├── test_invalid_login_20260831_174200.png
│   ├── test_product_search_20260831_174205.png
│   └── test_add_to_cart_20260831_174210.png
└── .gitkeep                              (Directory tracking)
```

### CI/CD Integration

Reports are perfect for CI/CD pipelines:

* **Jenkins** - Archive `Reports/` as artifacts
* **GitHub Actions** - Upload HTML report and screenshots
* **GitLab CI** - Store reports as job artifacts

Example GitHub Actions:

```yaml
- name: Archive Test Reports
  if: always()
  uses: actions/upload-artifact@v2
  with:
    name: test-reports
    path: Reports/
```

---

# 📦 Required Packages

The framework requires the following packages (all pinned to tested versions):

```text
selenium==4.46.0           # Web browser automation
pytest==9.1.1              # Test framework
pytest-html==4.1.1         # HTML report generation
webdriver-manager==4.0.2   # ChromeDriver management
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Verify Installation

```bash
python -m pip list | grep -E "(selenium|pytest|webdriver)"
```

---

# 👨‍💻 Author

**Praveen M**

**Automation QA Engineer**

### Skills

* Python
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* Manual Testing
* Functional Testing
* Regression Testing
* API Testing (Learning)
* SQL (Learning)
* Jenkins
* Git
* GitHub

---

# ⭐ If You Found This Project Useful

If this project helps you or gives you ideas for your own automation framework, consider giving the repository a ⭐ on GitHub.

Feedback and suggestions are always welcome!
