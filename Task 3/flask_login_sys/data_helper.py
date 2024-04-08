from pymongo import MongoClient

def get_database():

   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost:27017"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['DemoDatabase']

def get_user(email, password):

   db = get_database()

   collection_name = db["users"]

   result = [item for item in collection_name.find({"_id":email, "password": password})]

   if len(result) > 0 :

      # authentication successfull!
      return 1

   else:

      # authentication failed!
      return 0

def insert_user(username, password, email):

   db = get_database()

   collection_name = db["users"]

   try:

      user = {
         "_id" :email,
         "username": username,
         "password": password
      }

      collection_name.insert_one(user)

      return 1

   except:

      # Email exist
      
      return 0
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   

   result = get_user(password='admin', email='admin@gmail.com')

   if result == 1:

      print("Login Successfull.")

   else:

      print("Login Failed!")

   result = insert_user(username="admin", password='admin', email='main-admin@gmail.com')

   if result == 1:

      print("Added successfully.")

   else:

      print("Email alredy exist!")