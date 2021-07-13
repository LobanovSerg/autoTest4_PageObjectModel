
## Автоматизация тестирования с помощью Selenium и Python


[Course Link >>](https://stepik.org/course/575/promo)

***
#### 4. Применение паттерна Page Object Model

***
#### FAQ:
+ Тесты промаркированные для проверки _`need_review`_:
    * _`test_user_can_add_product_to_basket`_
    * _`test_guest_can_add_product_to_basket`_ - __параметризован__: 10 promo ссылок
    * _`test_guest_cant_see_product_in_basket_opened_from_product_page`_
    * _`test_guest_can_go_to_login_page_from_product_page`_
+ Проверки выполняются для любого языка из _`pages/languages.py`_
+ Kроме стандартных опций _`pytest`_ доступны необязательные параметры _`--language`_ и _`--browser_name`_. Например:
```shell
pytest --browser_name=firefox --language=de
```
+ Язык по умолчанию: _`en`_
    * _`en`_ == _`en-gb`_
    * Доступные параметры _`--language`_: ar ca cs da de en-gb en el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-cn
+ Браузер по умолчанию: _`chrome`_
    * Доступные параметры _`--browser_name`_: chrome firefox

***