def __get_item(url):
    response = dict()
    data = dict()
    response["status"] = "OK"
    data["name"] = "Product"
    data["id"] = 1

    response["data"] = data
    return response