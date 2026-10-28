products = {
    "car items": [
        {"name": "car cover", "price": 1200, "stock": 5},
        {"name": "car perfume", "price": 250, "stock": 10},
        {"name": "car washer", "price": 500, "stock": 3}
    ],
    "school items": [
        {"name": "notebook", "price": 50, "stock": 100},
        {"name": "pen", "price": 10, "stock": 200}
    ],
    "home items": [
        {"name": "bucket", "price": 150, "stock": 20},
        {"name": "mop", "price": 300, "stock": 15}
    ],
    "office items": [
        {"name": "printer paper", "price": 400, "stock": 50},
        {"name": "stapler", "price": 80, "stock": 25}
    ]
}

def update_stock():
    for category in products:
        for item in products[category]:
            if item["stock"] < 5:
                item["stock"] = 20

    print("Stock updated successfully")

update_stock()
print(products)