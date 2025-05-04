# 📚 OOP Assignment - Week 5

### By [William Oneka](https://github.com/OneWilly)

This project demonstrates core Object-Oriented Programming (OOP) concepts in Python. It includes class design with inheritance, encapsulation, and polymorphism, along with a real-world inspired example of polymorphism using vehicles.

---

## 🏗️ Assignment 1: Book & EBook Classes

### 📁 File: `book_classes.py`

#### ✅ Features Implemented:
- **Class:** `Book`
- **Subclass:** `EBook` (inherits from `Book`)
- **Encapsulation:** `_pages` is a protected attribute
- **Polymorphism:** Overridden `describe()` method in `EBook`
- **Methods:** `describe()`, `read()`, `download()`
- **Constructors:** Used to initialize each object with unique values

#### 🔍 Example Output:
'1984' by George Orwell, 328 pages.
You start reading '1984'.
'Sapiens' (eBook) by Yuval Noah Harari, 443 pages, 5MB.
Downloading 'Sapiens'...

perl
Copy
Edit

---

## 🎭 Activity 2: Vehicle Polymorphism

### 📁 File: `vehicle_polymorphism.py`

Demonstrates polymorphism through a shared `move()` method implemented differently in each subclass.

#### ✅ Classes:
- `Vehicle` (base class)
- `Car` → `move()` returns `"Driving 🚗"`
- `Plane` → `move()` returns `"Flying ✈️"`
- `Boat` → `move()` returns `"Sailing 🚤"`

#### 🔍 Example Output:
Driving 🚗
Flying ✈️
Sailing 🚤

yaml
Copy
Edit

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/OneWilly/<your-repo-name>.git
   cd <your-repo-name>
Run the main script:

bash
Copy
Edit
python main.py
This script imports classes from book_classes.py and vehicle_polymorphism.py and demonstrates their functionality.

📂 Project Structure
css
Copy
Edit
oop-week5-assignment/
├── book_classes.py
├── vehicle_polymorphism.py
├── main.py
└── README.md
📄 License
This project is created for educational purposes and class submissions.

📬 Contact
Connect on GitHub for questions or feedback.
