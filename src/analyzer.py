import json
import os
from typing import Set

def load_usernames_from_file(file_path: str) -> Set[str]:
    """Loads usernames from the JSON file based on the expected Instagram data structure."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        usernames = set()
        
        # Check if the structure is for the "following" file
        if 'relationships_following' in data: # Revised key based on common exports
             for item in data['relationships_following']:
                if 'string_list_data' in item and item['string_list_data']:
                    usernames.add(item['string_list_data'][0]['value'])
        elif 'following' in data: # Alternative key
             for item in data['following']:
                if 'string_list_data' in item and item['string_list_data']:
                    usernames.add(item['string_list_data'][0]['value'])
        # Check if the structure is for the "followers" file
        elif 'relationships_followers' in data:
            for item in data['relationships_followers']:
                if 'string_list_data' in item and item['string_list_data']:
                    usernames.add(item['string_list_data'][0]['value'])
        elif 'followers' in data: # Alternative key just in case
            for item in data['followers']:
                if 'string_list_data' in item and item['string_list_data']:
                    usernames.add(item['string_list_data'][0]['value'])

        # Fallback/Generic structure check if needed could go here
        
        return usernames

    except json.JSONDecodeError:
        raise ValueError(f"Could not decode JSON from '{file_path}'.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while processing {file_path}: {e}")


def get_non_followers(following_set: Set[str], followers_set: Set[str]) -> Set[str]:
    """Compares the following and followers lists to find the set difference."""
    return following_set.difference(followers_set)
