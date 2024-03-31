# 인터넷 url에 접속하기 위한 모듈 import
import urllib.request as URL

# 호출하고자 하는 open api 주소
api = "http://api.openweathermap.org/data/2.5/weather?"

# 파라미 설정을 위한 변수
city = "Seoul"
mode = "json"
appid = "26262cbdee846b1b4d9d79bf51995b53"

# URL 완성
api = api + "q=" + city
api = api + "&mode=" + mode
api = api + "&appid=" + appid

print(api) #for test

# url을 전송하여 open api를 호출하고
data = URL.urlopen(api)
print(type(data))

# 해당 결과를 읽어들임
result = data.read()
print(type(result))

#결과가 출력 (json 형태)
print(result)

print()

import json

j = json.loads(result)

weather = j["weather"]
current = weather[0]["main"]

main = j["main"]
current_temp = main["temp"] - 273.15

wind = j["wind"]
speed = wind["speed"]

print("%s의 현재 날씨 : %s" %(city,current))
print("현재온도 : %.1f" %current_temp)
print("현재풍속 : %.1f" %speed)




#### 국내 Open API 서비스 사례 - 네이버 개발자 센터






















