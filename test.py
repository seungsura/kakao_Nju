import pandas as pd

data = pd.DataFrame(columns = ['id', 'name', 'year', 'month', 'day'])


dict1 = {'n1' : {'m1' : 1, 'm2' : 2}, 'n2' : {'m3' : '띄어쓰기 있는 문자1', 'm4' : '띄어쓰기 217.123.213'}}
dict2 = {'n1' : {'m1' : 3, 'm2' : 4}, 'n2' : {'m3' : '띄어쓰기 있는 문자2', 'm4' : '띄어쓰기 217.123.21123123123'}}

def check(x):
    
    global data
    
    #이름과 날짜 분리
    new_date = x['n2']['m4']
    n1, d1 = map(str, new_date.split())
    
    #날짜 상세 분리
    new_year, new_month, new_day = map(int, d1.split('.'))
    print(new_year, new_month, new_day)
    
    #데이터 추가
    input_data = pd.DataFrame({'id' : [x['n1']['m1']], 'name': [n1], 'year': [new_year], 'month': [new_month], 'day': [new_day]})
    new_df = pd.concat([data, input_data], ignore_index = True)
    
    #데이터 id순으로 정렬
    sort_df = new_df.sort_values(by = ['id'])
    data = sort_df
    
    #데이터 저장
    data.to_csv("./text.csv")

check(dict2)


