# import requests
# year = input('년도를 입력해주세요 : ')
# today = input('오늘의 날짜를 입력해주세요 : ')
# today = year+today
# url = ('https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7530167&MLSV_YMD=%s')%(today)

# result = requests.get(url)
# #정상 접속이 되었다면 정보 받아오기
# if result.status_code == 200:
#     meals = result.json() #결과를 json => dictonary 로 변환인식
#     meal = meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
#     meal = str(meal).replace('<br/>','\n')
#     print(meal)

# =================================================================

import requests

def get_meals(dt):
    param = {
        'Type':'json',
        'ATPT_OFCDC_SC_CODE' : 'J10',
        'SD_SCHUL_CODE' : '7530167',
        'MLSV_YMD' : dt
    }
    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    result = requests.get(url, params=param)

    try :
        if result.status_code == 200:
            meals = result.json()  # 결과를 json => dictonary 로 변환인식
            meal = meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
            # meal = str(meal).replace('<br/>', '\n')
            meal = str(meal).split('<br/>')
        else:
            meal = ''
        return meal
    except:
        return ''



year = input('급식년도를 입력해주세요(예 : 2023) : ')
date = input('급식일자를 입력해주세요(예 : 1107) : ')
date = year+date
meal = get_meals(dt=date)
if meal == '':
    print('자료가 없습니다.')
else :
    for i in meal:
        print(i)
