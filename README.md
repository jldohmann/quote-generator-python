# Quote Generator: Python
A simple Flask app that generates Stephen Wolfram quotes when the page is refreshed

An extended version of [this Flask project](https://thecodebits.com/flask-project-for-beginners-inspirational-quotes/).

## Environment and Setup
Create a project directory, then change into it:
```
mkdir quote-generator
cd quote-generator
```
Create and activate a virtual environment to install Flask and any needed dependencies:
```
python3 -m venv venv
. venv/bin/activate
```
Install Flask:
```
pip3 install Flask
```
The rest of the project structure follows.

When you come back to the project, remember to reset your environment variables:
```
export FLASK_APP=quote-generator
export FLASK_ENV=development
```

## Data
Initial data is pulled from the [Stephen Wolfram Wikiquote page](https://en.wikiquote.org/wiki/Stephen_Wolfram). The script, `quotes/initial-quotes.py`, performs a GET request to access the page and parses and stores HTML. [XPath](https://www.w3schools.com/xml/xml_xpath.asp) is then used to traverse the tree and target the individual quotes living in the `<li>` elements.

There's additional content living in the `<li>` tags of this page which was removed; data cleaning is ad-hoc because it depends on the structure of the webpage.

Further cleaning is done and the data is exported to `quotes.json`. Additional quotes will be manually added to this file.
