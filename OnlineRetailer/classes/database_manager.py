import csv
class DatabaseManager:

    def create_account(self, username, password, salt):
        with open("database/account_data.csv", "a", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, "False", password, salt])
                
    def is_username_taken(self, username):
        with open("database/account_data.csv", "r", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Username"] == username:
                    return row
            return False
            
    def print_user_data(self):
        with open("database/account_data.csv", "r", newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)