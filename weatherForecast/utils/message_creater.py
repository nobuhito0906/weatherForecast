import requests


def create_single_text_message(message):
    if message == 'やあ':
        message = 'なんすか'
    elif message == '現在地':
        print('geo Request!!')
        geo_req_url = 'https://get.geojs.io/v1/ip/geo.json'
        data = requests.get(geo_req_url).json()
        latitude = data['latitude']
        longitude = data['longitude']
        print("都道府県:", data['region'])
        print("市区町村:", data['city'])
        print("緯度:", latitude)
        print("経度:", longitude)
        message = '緯度:'+latitude+'\n' + '経度:'+longitude
    test_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return test_message
