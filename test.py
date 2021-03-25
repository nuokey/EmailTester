#filename - имя файла с программой, (имя файла может быть любым, которое вам нравится, просто это пример использования)
#check - название функции, которая проверяет и возвращает только True или False

from main import check

def test_1():
    assert check('hello@mail.ru') == True,'придумал ОГ'
    assert check('h@llo@mail.ru') == False,'придумал ОГ'
    assert check('Жhello@mail.ru') == False,'придумал ОГ'

# (By KruASe) (Вроде все стандартное...)
def test_2(): 
    assert check('')==False
    assert check('123')==False
    assert check('sm th@email.com')==False
    assert check('#1535@email.ru')==False
    assert check('smth@email.emaillllll')==False
    assert check('smth@email.em7')==False
    assert check('smth@.ru')==False

# Kletcka - Воронков Михаил

def test_3():     
    assert check('capybara@capy.bara') == True  #правильная почта
    assert check('capybara@capy.ba.ra')  == True  #правильная почта
    assert check('capybara.capy.bara') == False  #без собаки
    assert check('capybara@capy@bara') == False  #две собаки
    assert check('capybara!@capy.bara')  == False  #доп. символ
    assert check('капибара@capy.bara')  == False  #русские символы
    assert check('capy bara@capy.bara')  == False  #пробел
    assert check('capybara@capy')  == False  #доменное имя первого уровня
    assert check('capybara@c.apybara')  == False #слишком короткая часть после собаки
    assert check('capybara@capy.ba.ra1')  == False #цифра в последней части 
    assert check('capybara@ca.pybara')  == False #слишком длинная последняя часть
    assert check('capybara@capybar.a')  == False #слишком короткая последняя часть
    assert check('cap@ybaracapy.bara')  == False #слишком короткая часть перед собакой



# NuoKey - Тимофей Ганицев
def test_4():
    assert check('hello.sdf.qsdf@gmail.com') == True

#(EndToper(Львов Максим))
def test_5(): 
    assert check("Email@123@lol@email.ru") == False
    assert check('Email@lol\ru') == False
    assert check('Email\n@lol.ru') == False
    assert check('Email\a@lol.ru') == False
    assert check('email@lolik.ahahaha.ru') == True
    assert check('True') == False
    assert check('email@lolik.0h0h0h0.ru') == False
    assert check('email@lolik.0h0h0h0.ru2') == False




# Пишите пожалуйста так, чтобы можно было просто копировать и вставить
# То есть комментариями
