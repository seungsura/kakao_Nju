from flask import Flask, request, jsonify
import pandas as pd

data = pd.DataFrame(columns = ['id', 'name', 'year', 'month', 'day'])

def check(x):
    
    global data
    
    #이름과 날짜 분리
    new_date = x['utterance']
    n1, d1 = map(str, new_date.split())
    
    #날짜 상세 분리
    new_year, new_month, new_day = map(int, d1.split('.'))
    print(new_year, new_month, new_day)
    
    #데이터 추가
    input_data = pd.DataFrame({'id' : [x['user']['id']], 'name': [n1], 'year': [new_year], 'month': [new_month], 'day': [new_day]})
    new_df = pd.concat([data, input_data], ignore_index = True)
    
    #데이터 id순으로 정렬
    sort_df = new_df.sort_values(by = ['id'])
    data = sort_df
    
    #데이터 저장
    data.to_csv("./data.csv", encoding = 'cp949')

def check_birthday(x):
    
    global data
    
    data1 = pd.read_csv("./data.csv", encoding = 'cp949')
    
    
    
application = Flask(__name__)

#연습 : 안녕하세요 대답하기
@application.route("/hello", methods=['POST'])
def hello_():
    req = request.get_json()
    
    hello = req["action"]["detailParams"]["hello"]["value"]
    
    answer = hello
    
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : answer
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

#생일 추가 태그 : 바로연결 '도움말'용
@application.route("/add_people", methods=['POST'])
def add_people_():
    
    req = request.get_json()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : "이름, 날짜를 입력해주세요 (예시:홍길동, 1999.01.01)"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

#정보 등록 칸 : 엔티티에 필수 파라미터 등록해서 옳은 입력만 반응
@application.route("/add_people_day", methods=['POST'])
def add_people_day_():
    req = request.get_json()
    
    people_info = req["userRequest"] #print(people_info['user']['id'])  
    
    check(people_info)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : "저장되었습니다!"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

#아직 생일 안 지난 사람들 알려주기
@application.route("/brithday_yet", methods=['POST'])
def brithday_yet_():
    req = request.get_json()
    
    people_info = req["userRequest"] #print(people_info['user']['id'])  
    id_ = people_info['user']['id']
    
    #id가 변수로 남은 일자 사람 이름/ 생일 반환

    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : "여기에 텍스트를 쓰세요!"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


if __name__ == "__main__":
	application.run(host='0.0.0.0', port = 5000, threaded=True)
    
    