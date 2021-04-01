import mechanize
import os

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0')]

br.open('https://lordsmobile.igg.com/gifts/')
br.select_form(nr=0)

playername = input('Enter your player name:')
giftcode = input('Enter your gift code:')

br.form['charname'] = playername
br.form['cdkey_2'] = giftcode

br.submit()


giftcode1 = 'SaintSeiya'
print(giftcode1)

# GOTTA CONTINUE THIS
