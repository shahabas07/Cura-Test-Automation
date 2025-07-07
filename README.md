# Cura-Test-Automation (QA Project)

## 🔍 About
This project is built to test the CURA Hospital Appointment web application using both manual and automated testing techniques following QA best practices.

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
- Manual Functional Testing
- Automated UI Testing (with Selenium WebDriver)

---

## 🔧 Tools & Technologies
- **Language:** Python
- **Automation Framework:** Selenium WebDriver + PyTest (with Page Object Model)
- **Reporting:** pytest-html (for HTML test reports)
- **Test Runner:** PyTest
- **Browser:** Chrome (via ChromeDriver)
- **Platform:** Linux (tested in VS Code)

---

## 📦 Installation & Running Tests

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ --html=report.html