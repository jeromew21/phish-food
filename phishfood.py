import requests, yaml, time, sys
import urllib.parse
import click
from bs4 import BeautifulSoup
from random import choice, randint

PASSWORD_CHARS = "1234567890!@#$%^&*zxcvbnma" + \
    "sdfghjklqwertyuiopQWERTYUIOPASDFGHJKLZXCVBNM_"

def make_password():
    return ''.join([choice(PASSWORD_CHARS) for i in range(randint(6, 12))])

GARBAGE_PILE = ('Big balls', '669696969', 'L33T HACKER XD')

with open('firstnames.txt') as f:
    FIRST_NAMES = [n.strip().capitalize() for n in f.readlines()]

with open('lastnames.txt') as f:
    LAST_NAMES = [n.strip().capitalize() for n in f.readlines()]
 
class Phish:
    def __init__(self, url, method):
        self.request_count = 0
        self.url = url
        self.method = method
        self.action = self.url
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        forms = soup.find_all('form')
        index = 0
        if len(forms) > 1:
            pass #do stuff and find index of wanted form
        form = forms[index]
        if form['action'] and form['action'] not in ('', '#', '.'):
            self.action = urllib.parse.urljoin(self.url, form['action'])
        self.fields = [item['name'] for item in form.find_all('input')]
    def make_input(self, field):
        if self.method in ('cheese', 'silly'):
            return choice(GARBAGE_PILE)
        field = field.lower()
        if field.endswith('word'): #password field
            return make_password()            
        elif field == 'name': #full name field
            return choice(FIRST_NAMES) + " " + choice(LAST_NAMES)
        elif field.endswith('name'):
            if randint(1, 3) == 2: #'username' field
                res = choice(LAST_NAMES) + choice(FIRST_NAMES)
            else:
                res = choice(FIRST_NAMES) + choice(LAST_NAMES)
            return res + str(randint(0, 1000))
        elif field.endswith('mail'): #email field
            if randint(1, 3) == 2:
                addr = choice(LAST_NAMES) + choice(FIRST_NAMES)
            else:
                addr = choice(FIRST_NAMES) + choice(LAST_NAMES)
            addr += str(randint(0, 1000))
            addr += choice(('@gmail.com', '@gmail.com', '@gmail.com', '@yahoo.com',  '@yahoo.com', '@hotmail.com'))
            return addr
        return make_password()
    def make_request(self):
        data = {}
        for item in self.fields:
            data[item] = self.make_input(item)
        newcount = self.request_count + 1
        print("Making {} request ({}) to {} with data {}".format(
            self.method,
            newcount, 
            self.action, 
            str(data))
        )
        r = requests.post(self.action, data)
        self.request_count = newcount
    def loop(self):
        print('Looping {} requests. Press ^C to stop.'.format(self.method))
        while True:
            self.make_request()
            time.sleep(1.5)

@click.command()
@click.option('--url', prompt='URL', help='URL of page with phishing form')
@click.option('--method', default='serious', help='Method of filling form [serious/cheese]')
def phish(url, method):
    p = Phish(url, method)
    p.loop()

if __name__ == '__main__':
    phish()
