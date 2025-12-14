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

1.  **Extract the ZIP file:** Unzip the downloaded file. This will create a folder (often named after your username).
2.  **Locate the Files:** Navigate inside the extracted folder. The files you need are typically located in a sub-folder structure like:
    ```
    /your_username_date/
        /connections/
            followers_and_following.json  # (Or two separate files: followers.json and following.json)
    ```
3.  **Rename & Place:** Find the JSON files containing the followers and following data and place them in the **same directory** as the Python script (`analyzer.py` - see Stage 3). For simplicity, you may need to check the file names inside your downloaded folder and update the script below if they differ.

---

## 🐍 Stage 3: Script Execution

### Requirements

* Python 3.x installed.

### `analyzer.py` (The Script)

Save the following code as `analyzer.py` in the same directory as your extracted JSON data files:

```python
import json

# --- CONFIGURATION (Adjust File Names if necessary) ---
FOLLOWING_FILE = 'following.json' # Name of the file containing users you follow
FOLLOWERS_FILE = 'followers.json' # Name of the file containing users who follow you
# ----------------------------------------------------

def load_usernames(file_path):
    """Loads usernames from the JSON file based on the expected Instagram data structure."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Instagram's structure for these files often involves a list under a 'relationships_followers' 
        # or 'following' key, where each item has a 'string_list_data' key.
        
        usernames = set()
        
        # Check if the structure is for the "following" file
        if 'following' in data:
            for item in data['following']:
                # The username is usually nested deeply
                if item['string_list_data']:
                    usernames.add(item['string_list_data'][0]['value'])
                    
        # Check if the structure is for the "followers" file
        elif 'relationships_followers' in data:
            for item in data['relationships_followers']:
                if item['string_list_data']:
                    usernames.add(item['string_list_data'][0]['value'])

        # Fallback for simpler file structures (if the above doesn't match)
        else:
             print(f"Warning: Could not interpret data structure for {file_path}. Returning empty set.")
             return set()
             
        return usernames

    except FileNotFoundError:
        print(f"ERROR: The file '{file_path}' was not found.")
        print("Please ensure the file is in the same directory as the script.")
        exit()
    except json.JSONDecodeError:
        print(f"ERROR: Could not decode JSON from '{file_path}'.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred while processing {file_path}: {e}")
        exit()


def find_non_followers():
    """Compares the following and followers lists to find the set difference."""
    
    # 1. Load Data
    following_set = load_usernames(FOLLOWING_FILE)
    followers_set = load_usernames(FOLLOWERS_FILE)
    
    if not following_set or not followers_set:
        print("\nProcess stopped due to data loading errors.")
        return

    # 2. Perform Set Difference
    # Set of people I follow MINUS Set of people who follow me
    non_followers = following_set.difference(followers_set)
    
    # 3. Output Results
    print("--------------------------------------------------")
    print(f"✅ Analysis Complete")
    print(f"Total users I follow:        {len(following_set)}")
    print(f"Total users following me:    {len(followers_set)}")
    print(f"\nTotal Non-Followers Found: {len(non_followers)}")
    print("--------------------------------------------------")
    
    if non_followers:
        print("\nUsers I follow who DO NOT follow me back:")
        # Display the list in alphabetical order for readability
        for username in sorted(list(non_followers)):
            print(f"- {username}")
    else:
        print("🎉 Congratulations! You have no non-followers (based on the data provided).")

if __name__ == "__main__":
    find_non_followers()