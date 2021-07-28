# REST_API

Documentation

Yi Yan
Drexel University
UnderGraduate Student
07/28/2021

Basic Description:

 - This basic API allows for one user to POST/GET/DELETE their mood on a given date to a database file.

Functionality:

 - POST a json to the database
        - Tested with Postman application and http://localhost/mood
        - Includes a rudimentary login system
                  - Will return an error if username or password does not matach the ones in the database
                  - If no exisiting username and password/ first POST, it will take the username and password from the json structure seen below.
        - Cannot POST more than once a day
        - Returns the id of the POST and current streak of POST
                  - Increments by 1 everytime the user POST and drops to 1 if user misses a day
        - POST json structure must be similar to the following example:
                    {
                      "mood_value": "5",
                      "username": "JohnDoe",
                      "password": "abc123"
                     }
 - GET returns id, mood_value, day, streak, and username of stored data in the database
        - Tested with Postman application and http://localhost/mood or http://localhost/mood/<id>
        - Cannot GET unless you have already POST today
        - Can specific id to get a specific date of info
  
  -DELETE deletes a given id in the database
        -Tested with Postman application and http://localhost/mood/<id>
        -Delete all id stored in the database in order to set up a new username and password
  
API setup:
  
  1. First make sure you in the command line you are in the working directory (e.g. REST_API_mood)
  2. Create a virtual environment (e.g. python3 -m venv .venv)
  2. Activate the virtual environment (e.g. source .venv/bin/activate)
  3. Install the necessary packages "pip3 install flask" "pip3 install flask-sqlalchemy"
  4. Export "export FLASK_APP=[mood.py file location]" "export FLASK_ENV=development"
  5. Run Flask "flask run"
  6. The user should be able to POST, GET, and DELETE now
  7. Other requirements can be seen in the requirements.txt
  
Document what, if anything, you would do differently if this were a production application and not an assessment? 
  
  Most definitely do more user testing. While I am confident that the API does what I described in the functionality, there is always that off chance that something   goes wrong which I didn't catch. I would also create a better front end for the POST/GET/DELETE. A better log in system which can support multiple users at once.
  
What tech would you use? 
  There is something called flask-login which seems perfect for managing the log in system but I was not too familiar with that to implement it. I would also bring   in JavaScript, HTML, and CSS to create the front end for an easier use.
  
How would you handle things differently if it needed to handle more users, more data, etc?
  Something along the lines of a server, preventing abuse (e.g. DDos), better network, better log in system, better storage system then what I have, and better       error handling.
