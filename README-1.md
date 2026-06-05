# 🔐 Password Strength Analyzer

A Python-based cybersecurity tool that evaluates password strength using common security standards such as length, character diversity, and complexity requirements. The application provides users with actionable feedback to help create stronger and more secure passwords.

---

## 📖 Overview

Weak passwords are one of the most common causes of unauthorized access and security breaches. This project analyzes passwords based on several security criteria and classifies them as:

* Weak
* Moderate
* Strong

The analyzer also provides recommendations for improving password security.

---

## ✨ Features

* Password length validation
* Uppercase letter detection
* Lowercase letter detection
* Numeric digit detection
* Special character detection
* Password strength scoring
* Security recommendations
* Simple command-line interface

---

## 🛠 Technologies Used

* Python 3.x
* Regular Expressions (`re` module)

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── password_strength_analyzer.py
├── README.md
│
└── requirements.txt (optional)
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer
```

### Requirements

* Python 3.x installed on your system

No external libraries are required.

---

## ▶️ Usage

Run the program using:

```bash
python password_strength_analyzer.py
```

Enter a password when prompted.

Example:

```text
Enter Password: MySecure@Pass123
```

Output:

```text
Password Strength: Strong

Excellent! Your password is secure.
```

---

## 🔍 Password Evaluation Criteria

The analyzer checks for:

| Criterion          | Requirement                    |
| ------------------ | ------------------------------ |
| Length             | Minimum 8 characters           |
| Uppercase Letters  | At least one uppercase letter  |
| Lowercase Letters  | At least one lowercase letter  |
| Numbers            | At least one digit             |
| Special Characters | At least one special character |

---

## 📊 Strength Levels

| Score Range | Strength |
| ----------- | -------- |
| 0 - 2       | Weak     |
| 3 - 5       | Moderate |
| 6+          | Strong   |

---

## 💡 Example

### Input

```text
hello123
```

### Output

```text
Password Strength: Moderate

Suggestions:
- Add at least one uppercase letter.
- Add at least one special character.
```

---

## 🚀 Future Improvements

* Graphical User Interface (Tkinter)
* Password Strength Meter
* Password Generator
* Common Password Detection
* Password Breach Database Integration
* Password Crack Time Estimation
* Web Application using Flask
* Database Logging and Analytics

---

## 🎯 Learning Outcomes

* Understanding password security principles
* Working with Python Regular Expressions
* Implementing validation and scoring logic
* Developing user-friendly security tools

---

## 📜 License

This project is intended for educational and learning purposes.
