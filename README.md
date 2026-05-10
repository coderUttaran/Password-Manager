# 🔐 Password Manager (Python CLI)

A simple and beginner-friendly **Command Line Password Manager** built using Python.
This project allows users to manage passwords for different websites through a terminal interface.

---

## 📌 Overview

This application helps users:

* Store passwords for multiple websites
* Update existing credentials
* Retrieve saved passwords
* Delete stored data

It is designed to demonstrate core Python concepts like:

* Functions
* Dictionaries
* Conditional statements
* Loops
* User input handling

---

## 🚀 Features

✅ Add new website and password
✅ Update existing password
✅ Delete stored website credentials
✅ Search for a specific password
✅ Display all saved passwords

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Interface:** Command Line (CLI)

---

## 📂 Project Structure

```
password-manager/
│── main.py       # Main application file
│── README.md     # Project documentation
```

---

## ⚙️ How It Works

* The program uses a **Python dictionary** to store data:
  ```
  website → password
  ```
* Users interact with the program using menu-based input.
* Operations are performed based on user choice.

⚠️ **Important:**
Data is stored only in memory and will be lost after closing the program.

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```

### 2. Navigate to the Project Folder

```bash
cd your-repo-name
```

### 3. Run the Program

```bash
python main.py
```

---

## 🖥️ Usage

When you run the program, you will see:

```
----Welcome Password manager----

Choose operation:
1 - Add Password
2 - Delete Website
3 - Show Passwords
4 - Search for password
```

### Example Flow:

* Choose `1` → Add password
* Choose `2` → Delete a stored website
* Choose `3` → View all stored passwords
* Choose `4` → Search for a specific website password

---

## ⚠️ Limitations

* ❌ No data persistence (data is lost after exit)
* ❌ Passwords stored in plain text (not secure)
* ❌ No user authentication system
* ❌ Not suitable for real-world sensitive data

---

## 🔮 Future Improvements

* 🔐 Add password encryption
* 💾 Store data using JSON or a database
* 🔑 Implement user authentication system
* 🖥️ Build a GUI (Tkinter or Web App)
* ☁️ Cloud storage integration

---

## 🎯 Learning Outcomes

Through this project, you will understand:

* How to structure a Python program
* How to manage data using dictionaries
* How to build interactive CLI applications

---

## 👨‍💻 Author

**Uttaran**
Aspiring Developer | Python Enthusiast

---

## ⭐ Support

If you found this project helpful, consider:

* Giving a ⭐ on GitHub
* Sharing feedback
* Suggesting improvements

---

## 📜 License

This project is open-source and free to use for learning purposes.
