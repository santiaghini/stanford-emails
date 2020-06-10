# Stanford Emails Scraping

As a strategy for reaching out to every single student in the Class of 2023 at Stanford, I coded this small project to generate a csv with the emails or eveyone.

First, I extract text from my lookbook (with the names of everyone) via the Google Vision API.
Then, I have a script that parses the data and generates a clean csv file with names.
Finally, I make a request to the Stanford profiles API to get an email for every name.