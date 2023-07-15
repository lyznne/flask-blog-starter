Flask Blog Starter
This is a simple Flask blog starter template. It provides a basic structure and starting point for building a blog application using Flask, SQLAlchemy.

Features
Simple Sqlite database setup.
Structured for big Flask Apps.


Installation
Clone the repository:

git clone https://github.com/lyznne/flask-blog-starter.git
Change into the project directory:

cd flask-blog-starter
Create a virtual environment(optional):

python3 -m venv venv
Activate the virtual environment:

#Linux / mac
    #Bash shell
    source env/bin/activate

    #Fish shell
    source env/bin/activate.fish 

    #csh / tsch
    source env/bin/activate.csh

#windows
    #Bash shell
    source env\bin\activate


Install the required packages:
e
pip install -r requirements.txt



Usage
To run the application, use the following command:

python run.py

The development server will start, and you can access the application in your browser at http://localhost:5000/.

Configuration
The application uses a configuration file config.py to manage settings. You can modify the configuration options to suit your needs.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. Feel free to use and modify the code according to your needs.

Acknowledgements
This project was inspired by the Flask Mega-Tutorial .

Resources
Flask documentation: https://flask.palletsprojects.com/
SQLAlchemy documentation: https://docs.sqlalchemy.org/




