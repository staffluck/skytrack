# ShopAggregator

skytrack

## Установка

```sh
git clone https://github.com/staffluck/skytrack.git
pip(venv) install -r requirements.txt
```

## Запуск
```sh
python init_db.py - инициализация ДБ и её наполнение
python main.py
```

## Эндпоинты
```sh
[GET] http://127.0.0.1:1111/users/<int:pk>/ - Получение данных пользователя
[GET] http://127.0.0.1:1111/users/<int:pk>/orders/ - Просмотр истории заказов пользователя
[GET] http://127.0.0.1:1111/orders/<int:pk>/ - Получение данных определенного заказа

[POST] http://127.0.0.1:1111/orders/
    body:
        {
           "user_id": <int: pk>,
           "items":[
              {
                 "book_id": <int: pk>,
                 "shop_id": <int: pk>,
                 "quantity": <int: quantity>,
              },
           ]
        }
```

