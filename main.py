email = input()

if '@' not in email:
    print(False)
    exit()

if '.' not in email:
    print(False)
    exit()

yes_in = 'qwertyuiopasdfghjklzxcvbnm' + '@-_.'
for i in range(len(email)):
    if email[i] not in email:
        print(False)
        exit()

email_1 = email.split('@')
if '.' not in email_1[1]:
    print(False)
    exit()

email_2 = email.split('.')
if len(email_2[len(email_2)-1]) < 2 or len(email_2[len(email_2)-1]) > 4:
    print(False)
    exit()

email_3 = email_1[1].split('.')
if len(email_3[0]) < 2:
    print(False)
    exit()

if len(email_1[0]) < 4:
    print(False)
    exit()

print(True)