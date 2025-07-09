# Cura-Test-Automation (QA Project)

![CI](https://github.com/shahabas07/Cura-Test-Automation/actions/workflows/ci.yml/badge.svg)

---

## 🔍 About  
This project is built to test the CURA Hospital Appointment web application using both manual and automated testing techniques, following QA best practices. The automated framework uses Selenium WebDriver in Python, built with the Page Object Model (POM) design pattern and integrated into CI/CD using GitHub Actions.

---

## 🌐 App Under Test  
🔗 [CURA Healthcare Service](https://katalon-demo-cura.herokuapp.com/)

---

## 🧾 Manual Testing Artifacts

### 📋 Test Cases Sheet  
Detailed manual test cases for login, appointment booking, logout, and negative scenarios.

🔗 [View Test Cases - Google Sheet](https://docs.google.com/spreadsheets/d/1u1D_edGypI42bUBoMOv3sp4Lmf7ZF5Sa8tDEczFrPkQ/edit?usp=sharing)

---

### 🐞 Bug Report Sheet  
Bugs identified during manual exploratory testing, including reproducible steps and severity level.

🔗 [View Bug Reports - Google Sheet](https://docs.google.com/spreadsheets/d/12hu5az49L_z8AIFxuuY135ZW3dB7unPwVQInc3dOGAk/edit?usp=sharing)

---

## 🧪 Testing Types
- ✅ Manual Functional Testing
- ✅ Automated UI Testing using Selenium
- ✅ Negative Testing (invalid and missing inputs)
- ✅ Regression Testing via PyTest
- ✅ CI-based Smoke Testing

---

## 🔧 Tools & Technologies

| Category       | Tools Used                            |
|----------------|-------------------------------------|
| Language       | Python                              |
| Automation     | Selenium WebDriver, PyTest          |
| Design Pattern | Page Object Model (POM)             |
| Reporting      | pytest-html, allure-pytest          |
| CI/CD          | GitHub Actions                     |
| Test Runner    | PyTest                             |
| Browser        | Chrome (Headless in CI)             |
| Environment    | VS Code on Linux                    |

---

## 📦 Installation & Running Tests

```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all tests with HTML report
pytest tests/ --html=report.html
```

---

## 🚀 CI/CD and Browser Versions

This project is integrated with GitHub Actions for continuous integration, running automated tests on every push and pull request to the main branch.

### Installed Browser & Driver versions in CI:

| Component    | Version       |
|--------------|---------------|
| Chrome       | 114.0.5675.0  |
| ChromeDriver | 114.0.5735.90 |

Logs and screenshots from test runs are automatically saved and uploaded as artifacts for easy debugging.
