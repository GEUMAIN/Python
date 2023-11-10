import requests

def getRank(targetDt):
    url = ('https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt='+targetDt)
    #어떻게 웹에 접속하지?
    response = requests.get(url)
    if response.status_code == 200:
        try :#시도해보고 잘 되면 이거 하고
            # 결과(json)을 어떻게(dictionary) 바꿔야지?
            mov = response.json()
            # return 결과리스트
            return mov['boxOfficeResult']['dailyBoxOfficeList']
        except: #try에서 오류가 발생하면 이쪽으로
            return []
    else :
        return[]
dt = input('날짜를 적어주세요 (예 : yyyymmdd) : ')
movies = getRank(dt) #제대로된 10개 리스트 또는 빈 리스트
if len(movies) == 0:
    print('값이 없습니다')
else :
    for movie in movies: #movies 10개의 영화 정보
        print(movie['rank']+'등 : '+movie['movieNm'])
