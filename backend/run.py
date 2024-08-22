#print("Starting to import create_app...")
from app import create_app
#print("create_app imported successfully")

#print("Creating app...")
app = create_app()
#print("App created successfully")

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)