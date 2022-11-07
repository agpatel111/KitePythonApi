from kiteconnect import KiteConnect

api_key = "j279yw6xbxn0b1jv"

api_secret = "er15uqxqszizkq939e52sb7tz1zyhrpr"

kite = KiteConnect(api_key=api_key)
print(kite.login_url())


rq_token = "GOoo1CVwD3iPliTG6w0xAK723aE10MTe"

generate_ssn = kite.generate_session("GOoo1CVwD3iPliTG6w0xAK723aE10MTe",api_secret)
access_token = generate_ssn['access_token']
print(access_token)

aa = kite.set_access_token("Duqf5uOk4dG9w5e5OlrKbsinCKy9C9sD")
print(aa)

access_token = "Duqf5uOk4dG9w5e5OlrKbsinCKy9C9sD"

import hashlib
a_string = 'j279yw6xbxn0b1jv+EdeT7mtJvJnk2YWzJTxHQy34pYTl2J3v+er15uqxqszizkq939e52sb7tz1zyhrpr'
hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)