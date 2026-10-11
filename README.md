# 🎓 Smart Academic Advisor

A smart web application that predicts a student's **final grade** and determines whether they are **academically safe or at risk** — using a Linear Regression model built entirely from scratch with NumPy (no sklearn).

---

## 🚀 Live Demo

🌐 **Live Web App:** [https://smart-academic-advisor-one.vercel.app](https://smart-academic-advisor-one.vercel.app)

---

## 🖥️ Screenshots

> Enter your academic data → Get instant prediction → Know your status!

| Input Form | Prediction Result |
|------------|------------------|
| Fill 6 academic features | See predicted grade & SAFE / AT RISK status |

---

## ⚙️ How It Works

1. **Loads** 5000 student records from `students_5000_logical.csv`
2. **Normalizes** features using mean & standard deviation
3. **Trains** a Linear Regression model via Gradient Descent (3000 epochs, lr=0.01)
4. **Predicts** the final grade from user inputs
5. **Classifies**:
   - ✅ **SAFE** → predicted grade ≥ 50
   - ⚠️ **AT RISK** → predicted grade < 50

---

## 📊 Features Used

| Feature | Description |
|---------|-------------|
| `attendance` | Attendance percentage |
| `study_hours` | Weekly study hours |
| `assignments` | Assignment scores |
| `quizzes` | Quiz scores |
| `difficulty` | Course difficulty level |
| `gpa` | Cumulative GPA |

---

## 🧪 Example

| Input | Value |
|-------|-------|
| Attendance | 85% |
| Study Hours | 6 hrs |
| Assignments | 90% |
| Quizzes | 78% |
| Difficulty | 3/5 |
| GPA | 3.5 |

**Result:** 🎯 Predicted Final Grade: **75.53%** → ✅ **SAFE**

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML:** NumPy (Linear Regression from scratch)
- **Data:** Pandas
- **Frontend:** HTML, CSS (Dark Mode)

---

## 📦 Installation

```bash
pip install flask numpy pandas
python app.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```
📦 Smart Academic Advisor
├── app.py                      # Flask app + ML model
├── students_5000_logical.csv   # Dataset (5000 students)
├── templates/
│   └── index.html              # Frontend UI
└── README.md
```

---

## 👨‍💻 Author

Built with ❤️ using Python & Flask
