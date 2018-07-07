# Phish Food

Attack phishing scams with this simple form bot! 

#### All you need is a URL!

## Installation

Requires Python3, requests, bs4

## Configuration

In `config.yaml`, you can define the fields `url` and `method`. 

Alternatively, pass them in as arguments on the command line.

Example: `python3 phishfood.py url method`

- `url`: the URL where the form is located. Phish Food saves you the effort parses the HTML and sends data to the correct URL
- `method`: the way in which usernames and passwords and emails are decided. Either can be `cheese`, which sends crude, rude data to the phisher, or `serious` (default), which scrapes names from census data and creates realistic seeming usernames and email addresses.
