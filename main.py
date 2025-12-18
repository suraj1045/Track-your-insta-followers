import os
import sys
from src.analyzer import load_usernames_from_file, get_non_followers
from src.data_loader import setup_instagram_data

# Configuration
DATA_DIR = 'data'
FOLLOWING_FILE = 'following.json'
FOLLOWERS_FILE = 'followers.json'

def main():
    print("📊 Instagram Non-Follower Analyzer")
    print("-----------------------------------")

    following_path = os.path.join(DATA_DIR, FOLLOWING_FILE)
    followers_path = os.path.join(DATA_DIR, FOLLOWERS_FILE)

    # Check if data files exist, if not try to setup from zip
    if not (os.path.exists(following_path) and os.path.exists(followers_path)):
        print("⚠️  Data files not found. Attempting to auto-load from zip...")
        if not setup_instagram_data(base_path=".", data_dir=DATA_DIR):
            print("   Please download your Instagram data as JSON, zip it, and place it in this folder.")
            return

    try:
        print(f"Loading data from {DATA_DIR}...")
        following_set = load_usernames_from_file(following_path)
        followers_set = load_usernames_from_file(followers_path)
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return

    if not following_set:
        print(f"⚠️  Warning: No users found in {FOLLOWING_FILE}. Check the file format.")
    if not followers_set:
        print(f"⚠️  Warning: No users found in {FOLLOWERS_FILE}. Check the file format.")

    non_followers = get_non_followers(following_set, followers_set)

    print("--------------------------------------------------")
    print(f"✅ Analysis Complete")
    print(f"Total users I follow:        {len(following_set)}")
    print(f"Total users following me:    {len(followers_set)}")
    print(f"\nTotal Non-Followers Found: {len(non_followers)}")
    print("--------------------------------------------------")
    
    if non_followers:
        print("\nUsers I follow who DO NOT follow me back:")
        for username in sorted(list(non_followers)):
            print(f"- {username}")
    else:
        print("🎉 Congratulations! You have no non-followers.")

if __name__ == "__main__":
    main()
