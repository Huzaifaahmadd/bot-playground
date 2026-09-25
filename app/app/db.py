   # final test
# retry
import sqlite3

   API_KEY = "sk-live-1234567890abcdef1234567890abcdef"

   def get_user(username):
       conn = sqlite3.connect("app.db")
       cur = conn.cursor()
       cur.execute("SELECT * FROM users WHERE name = '" + username + "'")
       return cur.fetchone()

   def last_items(items):
       result = []
       for i in range(len(items) + 1):
           result.append(items[i])
       return result

   def email_domain(user):
       return user.get("email").split("@")[1]
