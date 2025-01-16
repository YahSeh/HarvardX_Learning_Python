import sys
import requests

def main() :
    if len(sys.argv) == 2 :
        try :
            value = float(sys.argv[1])
        except :
            print("Command-line argument is not a number")
            sys.exit(1)
    else :
        print("Missing command-line argument")
        sys.exit(1)

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response = r.json()
        bit = response['bpi']['USD']['rate_float']
        print("$"'{:,}'.format(bit*value))

    except requests.RequestException:
        print("RequestException")
        sys.exit(1)

main()
