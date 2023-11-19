import json

TITLE = "1973_oil_crisis"
OUTPUT_FILE_NAME = "oil_crisis.json"

# 파일 열기
with open('dev-v2.0.json', 'r') as file:
    json_data = json.load(file)

    filtered_data = []

    # 'data' 리스트 안에서 'title'이 "computational theory"인 데이터 찾기
    for item in json_data['data']:
        if 'title' in item and item['title'] == TITLE:
            filtered_data.append(item)

    # 새 JSON 파일에 저장
    with open(OUTPUT_FILE_NAME, 'w') as new_file:
        json.dump({'data': filtered_data}, new_file, indent=4)