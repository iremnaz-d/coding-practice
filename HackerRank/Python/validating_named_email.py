#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import email.utils
import re

if __name__ == '__main__':
    pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

    for _ in range(int(input())):
        mail = input()
        parsed_email = email.utils.parseaddr(mail)

        email_address = parsed_email[1]

        if re.match(pattern, email_address):
            print(email.utils.formataddr(parsed_email))

