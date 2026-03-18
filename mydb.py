import json
import os


class Database:

    def __init__(self):
        self.db_file = 'db.json'
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        """Create db.json if it doesn't exist"""
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({}, f)

    def add_data(self, name, email, password):
        """Add new user to database"""
        try:
            with open(self.db_file, 'r') as rf:
                database = json.load(rf)

            if email in database:
                return 0  # Email already exists
            else:
                database[email] = [name, password]
                with open(self.db_file, 'w') as wf:
                    json.dump(database, wf, indent=2)
                return 1  # Success
        except Exception as e:
            print(f"Database error: {e}")
            return 0

    def search(self, email, password):
        """Search for user and validate password"""
        try:
            with open(self.db_file, 'r') as rf:
                database = json.load(rf)

                if email in database:
                    if database[email][1] == password:
                        return database[email][0]  # Return name
                    else:
                        return 0  # Wrong password
                else:
                    return 0  # Email not found
        except Exception as e:
            print(f"Database error: {e}")
            return 0