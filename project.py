import random

urls = {}

symbols = 'abcdefghijklmnopqrstuvwxyz1234567890'

#symbols = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,'.split(',')


def generate_code():
    number_of_symbols = 7
    code = ''
    for i in range(7):
        code += symbols[random.randint(0,len(symbols)-1)]    
    return code
 
def add_to_urls(code):
    url = input('Введите ссылку: \n')
    if code not in urls:
        urls.update({generate_code():url})
        print('Код к вашей ссылке:',urls)
    else:
        return None

def get_by_code(code):
    code_verification = input('Введите код: \n')
    if code_verification in urls:
        print('Полная ссылка вашего сайта:',urls.get(code_verification))
    else:
        print('Ссылка не найдена!')
        add_to_urls(code)

text_menu = '''
1.Что бы сгенерировать ссылку в короткий код
2.Получить полную ссылку из короткого кода
3.Выйти
'''

while True:
    code = generate_code()
    choice = input(text_menu)
    if choice == '1':
        add_to_urls(code)
    if choice == '2':
        get_by_code(code)
    if choice == '3':
        break
