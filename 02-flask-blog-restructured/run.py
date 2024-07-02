from flaskblog import app

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    #     print("Database created!")
    app.run(debug=True)
