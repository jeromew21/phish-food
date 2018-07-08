# Phish Food

Attack phishing scams with this simple form bot.

#### All you need is a URL!

## Installation
 
Requires python3, requests, bs4, click

## Configuration

Pass thr `URL` and the `method` in as arguments on the command line.

```
Usage: phishfood.py [OPTIONS]

Options:
  --url TEXT     URL of page with phishing form
  --method TEXT  Method of filling form [serious/cheese]
  --help         Show this message and exit.
```

Example: `python3 phishfood.py --url=http://badguysite.com --method=serious`

- `url`: the URL where the form is located. Phish Food saves you the effort parses the HTML and sends data to the correct URL
- `method`: the way in which usernames and passwords and emails are decided. Either can be `cheese`, which sends crude, rude data to the phisher, or `serious` (default), which scrapes names from census data and creates realistic enough looking usernames and passwords.

## Example!

I found a known phishing site on phishtank.com. And here's the output of Phish Food

```
python phishfood.py https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/
Looping requests. Press ^C to stop.
Making request (1) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'RebeckaAiken967@yahoo.com', 'login_password': '^pA0IxK'}
Making request (2) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'SocorroKeyes611@yahoo.com', 'login_password': 'Q7zVkfU'}
Making request (3) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'DonahueCarole588@hotmail.com', 'login_password': '72d6ZN7Y8'}
Making request (4) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'KiserMohammad689@hotmail.com', 'login_password': 'hqHmL7'}
Making request (5) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'LoraleeDietz680@gmail.com', 'login_password': 'T^$LhMe'}
Making request (6) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'TamarStringer384@yahoo.com', 'login_password': 'PdJpNzEqG'}
Making request (7) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'LeighannBarnes541@gmail.com', 'login_password': 'fI%_URDvrs'}
Making request (8) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'PaulRosen822@gmail.com', 'login_password': 'YgUvs4ooX'}
Making request (9) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'GoodrichFleta674@hotmail.com', 'login_password': 'BWfy##8P&G'}
Making request (10) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'LatashaThayer281@gmail.com', 'login_password': 'yci#4#'}
Making request (11) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'BeamJami863@yahoo.com', 'login_password': 'IRw_zi'}
Making request (12) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'GaskinsJeanene433@gmail.com', 'login_password': '__vyRU3dad'}
Making request (13) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'LydiaDay289@hotmail.com', 'login_password': 'VCuXtZ'}
Making request (14) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'TomlinsonAmerica211@hotmail.com', 'login_password': 'HerpaD'}
Making request (15) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'BernettaVelasco86@hotmail.com', 'login_password': 'USShcz*Z'}
Making request (16) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'ChantelDuffy367@hotmail.com', 'login_password': '5vGc!$XE&l'}
Making request (17) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'WellmanVince273@yahoo.com', 'login_password': '^B2&m0QkVvW'}
Making request (18) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'ShaunaKimble662@yahoo.com', 'login_password': 'akaGk5'}
Making request (19) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'KesslerLan893@yahoo.com', 'login_password': 'kIWz^iB'}
Making request (20) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'ConchitaAltman904@gmail.com', 'login_password': 'mSS5&k*3*O'}
Making request (21) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'MercedesMerchant657@hotmail.com', 'login_password': 'UbAzXrp%lyy'}
Making request (22) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'ChatmanWendi159@hotmail.com', 'login_password': 's9#$m@Du9Y'}
Making request (23) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'MirthaSawyer835@hotmail.com', 'login_password': 's7ePx9LvZAvb'}
Making request (24) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'MeaghanEngel631@hotmail.com', 'login_password': '2lB1v45'}
Making request (25) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'StarksKasi489@hotmail.com', 'login_password': 'LcJRPXw@#'}
Making request (26) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'BernardRochel871@yahoo.com', 'login_password': 'q2jiUx'}
Making request (27) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'VenusBates340@yahoo.com', 'login_password': 'VpstopZ'}
Making request (28) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'TuyetBurgess668@yahoo.com', 'login_password': 'T6#bClnYt'}
Making request (29) to https://serviceinformationaccount.anouarwhms.com/wp-log/Sec/Bin/customer_center/customer-IDPP00C124/myaccount/signin/ with data {'login_email': 'TempleReid390@hotmail.com', 'login_password': 'gZEiAdyEkG'}
```

### To dos

- Credit card fields
