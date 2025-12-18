# 📊 Instagram Non-Follower Analyzer

A Python script designed to safely and compliantly determine which users you are **following** who are **not** following you back on Instagram.

This method avoids scraping the live website, which is a violation of Instagram's Terms of Service (ToS), by instead processing the official data package you download directly from the platform.

---

## 🚀 The Safe and Compliant Course of Action

The entire process is broken down into three stages:

1.  **Request & Download:** Requesting your data archive from Instagram.
2.  **Preparation:** Locating and extracting the necessary JSON files.
3.  **Execution:** Running the Python script to compare the lists.

---

## 💻 Stage 1: Request & Download Data

This stage must be performed through the Instagram platform itself.

### Steps:

1.  **Go to Instagram's Settings:**
    * **On Mobile:** Go to your **Profile** $\rightarrow$ **Menu** (three lines) $\rightarrow$ **Your Activity** $\rightarrow$ **Download Your Information**.
    * **On Desktop:** Go to **Settings** $\rightarrow$ **Privacy and Security** $\rightarrow$ Under "Data Download," click **Request Download**.
2.  **Select Data Types:**
    * Choose the **"Select types of information"** option.
3.  **Select Connections:**
    * Locate and select the checkbox for **Connections** or **Followers and Following**.
4.  **Choose Format:**
    * Select **JSON** as the format. This is critical for easy processing by the Python script.
5.  **Submit Request:** Enter your password to confirm.

**Wait:** Instagram will send an email with a link to download a ZIP file (this can take from a few hours up to 48 hours). Download and save this ZIP file.

---

## 🛠️ Stage 2: Data Preparation

1.  **Download your data** from Instagram (as described in Stage 1).
2.  **Do NOT unzip it.**
3.  **Place the ZIP file** (e.g., `instagram-data-download.zip`) into the `data/` folder of this project.

---

## 🐍 Stage 3: Script Execution

### Requirements

* Python 3.x installed.

### Running the Script

Open your terminal or command prompt, navigate to the project directory, and run:

```bash
python3 main.py
```

The script will automatically:
1.  Find your zip file.
2.  Extract the necessary data.
3.  Analyze your followers.
4.  Print a list of users who do not follow you back.

The script will analyze the files in the `data/` directory and print a list of users who do not follow you back.

---

## 📂 Project Structure

```
.
├── data/
├── src/
│   ├── __init__.py
│   └── analyzer.py
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
├── main.py
└── readme.md
```