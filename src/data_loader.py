import os
import zipfile
import shutil
import glob

def find_latest_zip(base_path: str) -> str:
    """Finds the most recently modified zip file in the base path."""
    zip_files = glob.glob(os.path.join(base_path, "*.zip"))
    if not zip_files:
        return None
    return max(zip_files, key=os.path.getctime)

def extract_json_files(zip_path: str, target_dir: str) -> bool:
    """
    Extracts 'following.json' and 'followers_1.json' (or 'followers.json') 
    from the zip file to the target directory.
    """
    temp_dir = os.path.join(target_dir, "temp_extraction")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    found_following = False
    found_followers = False

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Walk through the extracted files to find what we need
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file == "following.json":
                    shutil.move(os.path.join(root, file), os.path.join(target_dir, "following.json"))
                    found_following = True
                elif file in ["followers_1.json", "followers.json"]:
                    # Rename to standard followers.json if needed
                    shutil.move(os.path.join(root, file), os.path.join(target_dir, "followers.json"))
                    found_followers = True

        return found_following and found_followers

    except zipfile.BadZipFile:
        print(f"❌ Error: The file '{zip_path}' is not a valid zip file.")
        return False
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        return False
    finally:
        # Cleanup temp directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def setup_instagram_data(base_path: str = ".", data_dir: str = "data") -> bool:
    """
    Orchestrates the finding and extraction of Instagram data.
    """
    print("🔍 Searching for Instagram data zip file...")
    zip_path = find_latest_zip(base_path)
    
    if not zip_path:
        print("❌ No zip file found in the project root.")
        return False
    
    print(f"📦 Found zip file: {os.path.basename(zip_path)}")
    
    # Ensure data directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    print("eparing to extract data...")
    success = extract_json_files(zip_path, data_dir)
    
    if success:
        print("✅ Data successfully extracted to 'data/' directory.")
        return True
    else:
        print("❌ Could not find specific 'following.json' or 'followers.json' inside the zip.")
        return False
