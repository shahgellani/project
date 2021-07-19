**Banking System**
An OOP based project to store and retrive information of a user's transcations using file system.

**Installing Python**
For MACOS:
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
$ export PATH=/usr/local/bin:/usr/local/sbin:$PATH
$ brew install python

For Windows:
Visit this link for proper guide 
_https://realpython.com/installing-python/_

Clone the project by typing this command in your terminal

_$ clone https://github.com/shahrukhPhaedrian/project.git_

Run main.py by using  this command
_python3 main.py_

ID -> admin.
Pass -> admin.

login using given id and pincode to start using the program and create account for a user to test the user side.

Libraries
Pickle
To serialize and deserialize the data, to store the data from object to file and retrieve it from file to object.
Datatime
To get the current data for the transaction done by the user and store it in the file.

Classes
User Class
Class to store all the attributes for the user and contains all the functions required to perform user's actions.
Admin Class
Class to handle the task related to user creation , report generation and user account deletion tasks
Main Class
