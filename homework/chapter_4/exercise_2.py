# 2. Data Quality Checker: Write a Python function that takes a list of email addresses and
# returns a dictionary with two keys: valid_emails (list) and invalid_emails (list).
# 63
# Use basic validation rules
# 1. must contain @
# 2.. must be after @
# 3. must contain text before the @
# email_list = [
# "john.doe@company.com",
# "jane.smith@email.co.uk",
# "invalid-email",
# "bob@gmail.com",
# "alice.brown@company.com",
# "john.doe@company.com", # duplicate
# "missing@domain",
# "test@example.org",
# "@nodomain.com",
# "jane.smith@email.co.uk", # duplicate
# "valid.user@site.net",
# "no-at-symbol.com",
# "another@test.io"
# ]

from typing import List, Dict


def data_quality_checker(mail_list: List[str]) -> Dict[str, List[str]]:
    """Check email quality and return valid/invalid emails."""

    data_quality_list = {'valid_mail': [], 'invalid_mail': []}
    for email in mail_list:
        email_split = email.split('@')
        if len(email_split) == 2 and not email_split[0].isnumeric() and '.' in email_split[1]:
            data_quality_list['valid_mail'].append(email)
        else:
            data_quality_list['invalid_mail'].append(email)

    return data_quality_list

email_list = [
"john.doe@company.com",
"jane.smith@email.co.uk",
"invalid-email",
"bob@gmail.com",
"alice.brown@company.com",
"john.doe@company.com", # duplicate
"missing@domain",
"test@example.org",
"@nodomain.com",
"jane.smith@email.co.uk", # duplicate
"valid.user@site.net",
"no-at-symbol.com",
"another@test.io"
]

print(data_quality_checker(email_list))