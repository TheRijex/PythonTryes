def pr_hello(name = 'Zero'):
    '''
    :param name
    :return: None
    just print helle with your name
    '''
    print('Hi ' +  name + " I am glad to see you)")

def is_hello_in_text(text = 'none'):
    if "hello" in text.lower():
        return True
    else:
        return False
#faster
def is_hello_in_text2(text = 'none'):
    return 'hello' in text.lower()

def search_word_in_text(word = '', text = 'qwerty'):
    return word in text.lower()


pr_hello('Yan')
pr_hello()
print(is_hello_in_text('Hi my friends'))
