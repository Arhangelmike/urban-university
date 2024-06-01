def test_function():
    print('Я в test_function')
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()