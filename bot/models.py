import requests


def get_data_type_de_service(type_de_service):

    if type_de_service == "formelle":
        data = requests.get(
            "http://127.0.0.1:8000/api/service/?type_de_service=1&active=true"
        )

    else:
        data = requests.get(
            "http://127.0.0.1:8000/api/service/?type_de_service=2&active=true"
        )

    return data.json()


def get_categorie():
    return requests.get("http://127.0.0.1:8000/api/categorie").json()


def get_service(type_de_service, categorie):
    return requests.get(
        f"http://127.0.0.1:8000/api/service/?categorie={categorie}&type_de_service={type_de_service}&active=true"
    ).json()


def get_info_service(service_id):
    return requests.get(f"http://127.0.0.1:8000/api/service/{service_id}").json()


def recherche(mot_cle):
    return requests.get(
        f"http://127.0.0.1:8000/api/service/?search={mot_cle}&active=true"
    ).json()


def super_class(classe):
    return requests.get(
        f"http://127.0.0.1:8000/api/service/?classe={classe}&active=true"
    ).json()
