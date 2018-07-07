import requests, yaml, time, sys
import urllib.parse
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
    def __init__(self):
        self.request_count = 0
        attrs = ('url', 'method')
        if len(sys.argv) > 1:
            data = {}
            i = 1
            for a in attrs:
                if i < len(sys.argv):
                    data[a] = sys.argv[i]
                    i += 1
        else:
            with open('config.yaml') as f:
                data = yaml.safe_load(f)
        for a in attrs:
            if a in data:
                val = data[a]
            else:
                val = None
            setattr(self, a, val)
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
            addr += choice(('@gmail.com', '@yahoo.com', '@hotmail.com'))
            return addr
        return make_password()
    def make_request(self):
        data = {}
        for item in self.fields:
            data[item] = self.make_input(item)
        newcount = self.request_count + 1
        print("Making request ({}) to {} with data {}".format(newcount, self.action, str(data)))
        r = requests.post(self.action, data)
        self.request_count = newcount
    def loop(self):
        print('Looping requests. Press ^C to stop.')
        while True:
            self.make_request()
            time.sleep(1.5)

if __name__ == '__main__':
    p = Phish()
    p.loop()
