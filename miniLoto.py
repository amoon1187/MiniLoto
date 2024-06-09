import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_miniloto_results(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 結果を格納するリスト
    results = []

    # 各行をループしてデータを抽出
    for row in soup.find_all('tr')[8:]:  # 余分な行と第0回を除く
        cols = row.find_all('td')
        if cols:  # 空の行を無視
            if '％' in str(cols):
                continue
            draw_number = cols[0].text.strip()  # 抽選回
            main_number1 = cols[1].text.strip()  # 本数字1
            main_number2 = cols[2].text.strip()  # 本数字2
            main_number3 = cols[3].text.strip()  # 本数字3
            main_number4 = cols[4].text.strip()  # 本数字4
            main_number5 = cols[5].text.strip()  # 本数字5
            bonus_number = cols[6].text.strip()  # B数字
            set_number = cols[7].text.strip()  # セット
            results.append([draw_number, main_number1, main_number2, main_number3, main_number4, main_number5, bonus_number, set_number])

    # 結果をpandas DataFrameに変換
    df = pd.DataFrame(results, columns=['抽選会', '本数字1', '本数字2', '本数字3', '本数字4', '本数字5', 'B数字', 'セット'])
    return df

# URLの指定
url = "http://sougaku.com/miniloto/data/list1/"

# 結果の抽出
miniloto_df = fetch_miniloto_results(url)

# 結果の表示
print(miniloto_df)