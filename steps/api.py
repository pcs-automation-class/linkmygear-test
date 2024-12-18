import requests
from behave import step


BASE_URL = 'https://dev.linkmygear.com/'


@step('Create new record for device with following data')
def add_new_device(context):
    endpoint = 'device-data/airguard/log/v1'
    data = {}
    for row in context.table.rows:
        data[row.cells[0]] = row.cells[1]

    message = (
        f"{data['imei']},{data['date']}191400.000,{data['jump']},3249.34,676.98,32.22,-115,1,1,"
        f"{data['date']}211429.000,"
        f"{data['latitude']},{data['longitude']},2573.600,,,1,,2.5,,,,20,4,,,28,,,|,771,-115,1723324527")

    response = requests.post(BASE_URL + endpoint, data=message)
    assert response.status_code == 201, f"{response.status_code}: {response.text}"


@step('Create new heartbeat message for device with following data')
def add_new_device_heartbeat_msg(context):
    endpoint = 'device-data/airguard/heartbeat/v1'
    data = {}
    for row in context.table.rows:
        data[row.cells[0]] = row.cells[1]

    if data['state'] == "on":
        state = 1
    elif data['state'] == "off":
        state = 2
    elif data['state'] == "alert":
        state = 3
    else:
        state = 0
    message = (f"{data['imei']},4.05,12.0,39.11,-66,ATT, {data['date']}190424.000,"
               f"{data['latitude']},{data['longitude']},9,{data['date']}190421.000,{data['battery']},{state},,,|,123;")
    response = requests.post(BASE_URL + endpoint, data=message)
    assert response.status_code == 201, f"{response.status_code}: {response.text}"