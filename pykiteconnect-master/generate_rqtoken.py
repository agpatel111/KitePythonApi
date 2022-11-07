from kiteconnect import KiteTicker, KiteConnect

if __name__ == '__main__':
    api_key =  "j279yw6xbxn0b1jv"
    api_secret = "er15uqxqszizkq939e52sb7tz1zyhrpr"

    kite = KiteConnect(api_key=api_key)

    # Need to generate access token once a day expiration is daily   for AT
    print(kite.login_url())
    request_token = input("enter request token: ")

    def generate_access_token(request):
        try:
            data = kite.generate_session(request_token=request, api_secret=api_secret)
            kite.set_access_token(data['access_token'])

            with open("access_token.txt", 'w') as at:
                at.write(data['access_token'])
                print("write_successful")
            at.close()
        except Exception as err:
            print(str(err))

    generate_access_token(request_token)