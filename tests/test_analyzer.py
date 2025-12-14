import unittest
import json
import os
from src.analyzer import load_usernames_from_file, get_non_followers

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        # Create dummy data files
        self.test_data_dir = 'tests/test_data'
        os.makedirs(self.test_data_dir, exist_ok=True)
        
        self.following_file = os.path.join(self.test_data_dir, 'following.json')
        self.followers_file = os.path.join(self.test_data_dir, 'followers.json')
        
        # Mock Data Structure (Relationships Following)
        with open(self.following_file, 'w') as f:
            json.dump({
                "relationships_following": [
                    {"string_list_data": [{"value": "user1"}]},
                    {"string_list_data": [{"value": "user2"}]},
                    {"string_list_data": [{"value": "user3"}]}
                ]
            }, f)

        # Mock Data Structure (Relationships Followers)
        with open(self.followers_file, 'w') as f:
            json.dump({
                "relationships_followers": [
                    {"string_list_data": [{"value": "user1"}]},
                    {"string_list_data": [{"value": "user3"}]}
                ]
            }, f)

    def tearDown(self):
        # Clean up files
        if os.path.exists(self.following_file):
            os.remove(self.following_file)
        if os.path.exists(self.followers_file):
            os.remove(self.followers_file)
        os.rmdir(self.test_data_dir)

    def test_load_usernames_following(self):
        usernames = load_usernames_from_file(self.following_file)
        self.assertEqual(usernames, {'user1', 'user2', 'user3'})

    def test_load_usernames_followers(self):
        usernames = load_usernames_from_file(self.followers_file)
        self.assertEqual(usernames, {'user1', 'user3'})

    def test_get_non_followers(self):
        following = {'user1', 'user2', 'user3'}
        followers = {'user1', 'user3'}
        non_followers = get_non_followers(following, followers)
        self.assertEqual(non_followers, {'user2'})

if __name__ == '__main__':
    unittest.main()
