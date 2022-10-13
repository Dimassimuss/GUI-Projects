import requests as rq
from datetime import datetime as dt
pixela_endpoint = 'https://pixe.la/v1/users'

USER_NAME = 'YOUR USER NAME'
TOKEN = 'YOUR TOKEN'

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#
# response = rq.post(url=pixela_endpoint, json=user_params)
# print(response.text)

pixela_endpoint_graph = f'{pixela_endpoint}/{USER_NAME}/graphs'

graph_params = {
      'id': 'graph1',
      'name': 'Programming Habit',
      'unit': 'H',
      'type': 'int',
      'color': 'ajisai'
}

headers = {
      'X-USER-TOKEN': TOKEN
}

# response = rq.post(url=pixela_endpoint_graph, json=graph_params, headers=headers)
# print(response.text)

pixela_endpoint_add_pixel = f'{pixela_endpoint_graph}/graph1'
today = dt.today()
pixel_config = {
      'date': '20220827',
      'quantity': '3'
}

# response = rq.post(url=pixela_endpoint_add_pixel, json=pixel_config, headers=headers)
# print(response.text)

pixela_endpoint_update_pixel = f'{pixela_endpoint_graph}/graph1/20220827'
pixel_update_conf = {
    'quantity': '2'
}
response = rq.delete(url=pixela_endpoint_update_pixel, headers=headers)
print(response.text)