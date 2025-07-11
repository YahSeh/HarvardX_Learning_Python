'''
def convert(inpt) :
    #verif = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", inpt)
    check_format(verif)
    y,m,d = inpt.split("-")
    check_date(inpt,y,m,d)
    t = date.today()
    z = inpt.date
    x = operator.__sub__(t, inpt)
    print(x)


def check_format(date) :
    if not date :
        sys.exit("Invalid date")

def check_date(inpt,y,m,d) :
    today = str(date.today())
    splits = today.split("-")
    if inpt > today :
        sys.exit("Invalid date")
    if m[0] == '0' :
        m = m.replace("0", "")
    if d[0] == '0' :
        d = d.replace("0", "")
    try :
        datetime.datetime(int(y), int(m), int(d))
    except (ValueError, SyntaxError) :
        sys.exit("Invalid date")
'''
