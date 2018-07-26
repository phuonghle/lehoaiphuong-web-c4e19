# At /user/<username> route, return a page showing respective user profile (name, gender, age, hobbies, ...) 
# if the requested username doesn’t exist return “User not found” message

from flask import Flask
app = Flask(__name__)
from users import users


@app.route('/user/<string:username>')
def user_profile(username):
    users_total = users()

    if username in users_total:
        return "Name: {0}, Age: {1}, Gender: {2}, Hobbies: {3}".format(users_total[username]["name"], users_total[username]["age"], users_total[username]["gender"], users_total[username]["Hobbies"])
    else:
        return "User not found"                                                                  

if __name__ == '__main__':
  app.run(debug=True)