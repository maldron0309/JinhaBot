
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
        '20240110':"셀프충무김밥(밥&김)\n가락국수(미니)\n유채나물무침\n오징어어묵볶음\n야채튀김\n석박지",
        '20240111':"백미밥\n조랭이떡국\n열무무침\n감자채볶음\n돼지갈비맛후라이드&고추마요\n배추김치",
    }
    data2 = {
        '20231205':"급식 정보가 없습니다.",
        '20231206':"급식 정보가 없습니다.",
    }

    if content == "오늘 급식" or content == "오늘급식" or content == "ㅇㄴ" or content == "ㅂ" or content == "ds":
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
    elif content == "내일 급식" or content == "내일급식" or content == "ㄴㅇ" or content == "ㄴㅂ" or content == "sq":
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
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "잘못된 발화입니다.\n'도움말'을 보내서 발화 방법을 확인해주세요."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)