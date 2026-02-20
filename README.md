````markdown
# 📊 GitHub Tracker (Bulk Students)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Excel](https://img.shields.io/badge/Output-Excel-green)

**GitHub Tracker** is a Python tool that fetches **GitHub user and repository data** for multiple students from an **Excel input file** and generates a **comprehensive Excel report** with activity metrics, stars, forks, and ranking. It is ideal for educators, mentors, or team leads who want to **track student contributions in bulk** efficiently.

---

## 🚀 Features

* Read multiple student records from an **Excel sheet**
* Fetch GitHub user data via the **GitHub API**
* Generate a **detailed Excel report** with columns:

  * Rank
  * Student Name
  * College Email
  * GitHub Username
  * Followers
  * Public Repositories
  * Total Stars
  * Total Forks
  * Last Activity Date
  * Status (Success / Invalid Username)

* Automatically **rank students** based on GitHub stars
* Gracefully handles missing or invalid usernames
* Includes **bulk processing** of many students at once
* Minimal setup; only requires **Python 3.10+** and `requests`, `openpyxl`

---

## 🖼 Sample Report

![Sample Excel](https://via.placeholder.com/600x400?text=Sample+Excel+Report)

> Replace with a screenshot of your generated Excel report.

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/Sathvika-g-29/Github_Tracker.git
cd Github_Tracker
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> Ensure you have **Python 3.10+** installed.

---

## 🔑 Setup

1. Create an **input Excel file** named `students_input.xlsx` with headers:

| Student Name | College Email | GitHub Username |
| ------------ | ------------- | --------------- |

2. Fill student data **starting from row 2**.
3. Ensure the file is **saved and closed** before running the script.
4. Optionally, store a **GitHub personal access token** as an environment variable `GITHUB_TOKEN` for higher API rate limits.

---

## ▶ How to Use

Run the main script:

```bash
python student_tracker.py
```

* The script will:

  1. Read all student GitHub usernames from the Excel file
  2. Fetch profile data and repository stats from GitHub
  3. Rank students based on total stars
  4. Generate `students_report.xlsx` with all metrics

> ⚠️ Make sure the input Excel file is **not open** in another program to avoid `PermissionError`.

---

## 🧪 Testing with Bulk Student Data

To quickly test the script, you can **generate fake student entries** in Excel with placeholder GitHub usernames like:

| Student Name   | College Email                                 | GitHub Username |
| -------------- | --------------------------------------------- | --------------- |
| Test Student 1 | [test1@college.edu](mailto:test1@college.edu) | octocat         |
| Test Student 2 | [test2@college.edu](mailto:test2@college.edu) | torvalds        |

> Replace with real GitHub usernames for actual reports.

---

## 👥 Contribution Guidelines

Contributions are welcome! You can help by:

* Reporting bugs or issues
* Suggesting new features
* Adding support for additional GitHub metrics
* Improving code readability or performance

**Workflow:** Fork the repo → Create a feature branch → Make changes → Open a Pull Request

**Please ensure:**

* Code is **PEP8 compliant**
* Add comments for new features
* Test functionality thoroughly

---

## 🧑‍💻 Maintainers

* **Sathvika G** – [GitHub Profile](https://github.com/Sathvika-g-29)

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

```
Do you want me to add that?
```
