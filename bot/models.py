import requests


def get_data_type_de_service(type_de_service):

    if type_de_service == "formelle":
        data = requests.get("http://127.0.0.1:8000/api/service/?formelle=ok")

    else:
        data = requests.get("http://127.0.0.1:8000/api/service/?informelle=ok")

    return data.json()


def get_categorie():
    return requests.get("http://127.0.0.1:8000/api/categorie").json()
