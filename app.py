from flask import Flask, json, request, jsonify
import sys
import datetime

app = Flask(__name__)

@app.route('/schoolmeal', methods=['POST'])
def schoolmeal():
    content = request.get_json()
    content = content['userRequest']['utterance']
    content = content.replace("\n","")
    print(content)
    today = datetime.date.today()
    tmrw = today + datetime.timedelta(days = 1)
    date_today = today.strftime("%Y%m%d")
    date_tmrw = tmrw.strftime("%Y%m%d")
    data1 = {
        '20240110':"셀프충무김밥(밥&김)\n가락국수(미니)\n유채나물무침\n오징어어묵볶음\n야채튀김\n석박지\n(936kcal)",
        '20240111':"백미밥\n조랭이떡국\n열무무침\n감자채볶음\n돼지갈비맛후라이드&고추마요\n배추김치\n(887kcal)",
        '20240112':"오므라이스&하이스S\n유부장국\n참나물오리엔탈무침\n배추김치\n귤\n떡갈비&돈가스소스\n(1069kcal)",
        '20240115':"백미밥\n근대된장국\n돈육김치두루치기&두부\n총각김치\n팽이버섯전(오븐)\n애호박볶음\n(681kcal)",
        '20240116': "현미밥\n고추장찌개\n꿀마늘수육\n콩나물무침\n배추겉절이\n상추쌈&쌈장\n(795kcal)",
        '20240117': "매운닭치즈덮밥\n감자양파국\n오이김치\n쥬시쿨\n붕어빵1개\n콘피어&연유\n(1072kcal)",
    }
    data2 = {
        '20240113':"급식 정보가 없습니다.",
        '20240114':"급식 정보가 없습니다.",
        '20240118':"졸업식",
    }
    data3 = {
        'Monday':"백미밥\n카레소스\n마늘쫑고추장볶음\n고구마치즈롤까스&돈까스소스\n배추김치\n숙주나물샐러드\n(844kcal)",
        'Tuesday':"혼합잡곡밥\n북어무국\n깨나물들깨볶음\n닭볶음탕\n에그랑땡&케찹\n배추김치\n(864kcal)",
        'Wednesday':"셀프충무김밥(밥&김)\n가락국수(미니)\n유채나물무침\n오징어어묵볶음\n야채튀김\n석박지\n(936kcal)",
        'Thursday':"백미밥\n조랭이떡국\n열무무침\n감자채볶음\n돼지갈비맛후라이드&고추마요\n배추김치\n(887kcal)",
        'Friday':"오므라이스&하이스S\n유부장국\n참나물오리엔탈무침\n배추김치\n귤\n떡갈비&돈가스소스\n(1069kcal)",
    }

    if content == "오늘 급식" or content == "오늘급식":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text": data1[date_today]
                        }
                    }
                ]
            }
        }
    elif content == "내일 급식" or content == "내일급식":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : data1[date_tmrw]
                        }
                    }
                ]
            }
        }
    elif content == "일주일 급식" or content == "일주일급식" or content == "일주일" :
        week_meal = ""
        for date, meal in data3.items():
            week_meal += f"{date}:\n{meal}\n\n"
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : week_meal
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "잘못된 명령어입니다."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
