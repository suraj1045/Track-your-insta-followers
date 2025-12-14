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

Before running the script, you must get the correct files into the correct location.

1.  **Extract the ZIP file:** Unzip the downloaded file.
2.  **Locate the Files:** Find the `followers_and_following.json` (or separate `followers.json` and `following.json`) inside the extracted folders.
3.  **Place in Data Directory:** Move these files into the `data/` folder of this project. Ensure they are named `followers.json` and `following.json`.

---

## 🐍 Stage 3: Script Execution

### Requirements

* Python 3.x installed.

### Running the Script

Open your terminal or command prompt, navigate to the project directory, and run:

```bash
python3 main.py
```

The script will analyze the files in the `data/` directory and print a list of users who do not follow you back.