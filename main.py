def check(email):
    try:
        email = email.lower()
        assert '@' in email

        assert '.' in email

        yes_in = 'qwertyuiopasdfghjklzxcvbnm' + '@-_.'
        for i in range(len(email)):
            assert email[i] in yes_in

        email_1 = email.split('@')
        assert '.' in email_1[1]

        email_2 = email.split('.')
        assert len(email_2[len(email_2)-1]) >= 2
        assert len(email_2[len(email_2)-1]) <= 4

        email_3 = email_1[1].split('.')
        assert len(email_3[0]) >= 2

        assert len(email_1[0]) >= 4

    except AssertionError:
        return(False)

    return(True)

print(check('email@lolik.0h0h0h0.ru'))