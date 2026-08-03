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
| ChromeDriver            | Browser Driver       |
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
│   └── base_page.py
│
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── search_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   └── test_amazon.py
│
├── config.py
├── conftest.py
├── requirements.txt
├── README.md
└── Reports/
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

## ✅ Safe Click Implementation

The `safe_click()` method improves click reliability by performing multiple validation steps.

Workflow:

1. Wait until the element is clickable
2. Scroll the element into view
3. Perform a normal Selenium click
4. Retry if the click fails due to dynamic page behavior
5. Perform JavaScript Click as a final fallback

This approach handles most common Selenium click issues.

---

## ✅ Retry Mechanism

The framework includes a reusable retry mechanism that automatically retries failed actions.

Handled Exceptions:

* `StaleElementReferenceException`
* `ElementClickInterceptedException`

This significantly improves test stability on dynamic web applications.

---

## ✅ Intelligent Login Validation

Instead of checking only for successful login, the framework intelligently detects multiple outcomes.

Possible login states:

* Successful Login
* Invalid Credentials
* CAPTCHA Challenge

If CAPTCHA is detected, the framework stops execution and reports the issue, preventing false-positive test results.

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

Run all tests

```bash
pytest -v
```

Generate an HTML report

```bash
pytest -v --html=Reports/report.html
```

Run a specific test

```bash
pytest tests/test_amazon.py -v
```

---

# 📊 Reports

The framework supports HTML reporting using **pytest-html**.

Example command:

```bash
pytest -v --html=Reports/report.html --self-contained-html
```

The generated report contains:

* Test Results
* Pass / Fail Status
* Execution Time
* Detailed Logs

---

# 🔮 Future Enhancements

The framework is designed to be easily extendable.

Planned improvements include:

* Jenkins CI/CD Integration
* GitHub Actions Workflow
* Cross-Browser Testing
* Parallel Execution using `pytest-xdist`
* Allure Reporting
* Screenshot Capture on Test Failure
* Data-Driven Testing
* Docker Support
* Headless Browser Execution
* Browser Compatibility Matrix

---

# 💡 Automation Concepts Implemented

* Page Object Model (POM)
* Explicit Waits
* Retry Mechanism
* JavaScript Executor
* Exception Handling
* Reusable Base Class
* Object-Oriented Programming (OOP)
* Logging
* Environment Variables
* Modular Framework Design

---

# 📸 Suggested Repository Screenshots

To make the repository more attractive, consider adding screenshots of:

* Project Folder Structure
* Test Execution in Terminal
* HTML Report
* Jenkins Job (if integrated)
* GitHub Actions Workflow (future enhancement)

Create a folder named `screenshots/` and reference them like:

```markdown
![Framework Structure](screenshots/framework.png)

![HTML Report](screenshots/report.png)

![Jenkins](screenshots/jenkins.png)
```

---

# 📦 Required Packages

Example `requirements.txt`

```text
selenium
pytest
pytest-html
webdriver-manager
```

Install with:

```bash
pip install -r requirements.txt
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
