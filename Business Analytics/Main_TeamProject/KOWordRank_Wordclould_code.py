from krwordrank.word import KRWordRank
import pandas as pd
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def special_symbol(column):
        df[column] = df[column].str.replace(pat=r'[^\w]',repl=r' ',regex=True)
        return df

min_count = 5   # 단어의 최소 출현 빈도수 (그래프 생성 시)
max_length = 10 # 단어의 최대 길이
wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)

title = '제목'
content = '내용'
dict_key = []

for file in os.listdir("dataset"):
    file_name = str(file[:-4])
    dict_key.append(file_name)
    # print(file_name)

# with os.scandir('dataset') as entries:
#     for entry in entries:
#         print(entry.name)


# Rawdata_dict = dict()
# with os.scandir('dataset') as entries:
#     for entry in entries:
#         Rawdata_dict[entry] = pd.read_csv(entry)

# dict_key = list(Rawdata_dict.keys())

# print(dict_key)

num = 7

item = dict_key[num]

df = pd.read_csv('dataset/' + item + '.csv')


# df['내용'] = df['내용'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣0-9 ]', '')

special_symbol(title)
special_symbol(content)

texts = df[title].values.tolist() + df[content].values.tolist()


beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10
# texts = ['예시 문장 입니다', '여러 문장의 list of str 입니다', ... ]
keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
        print('%8s:\t%.4f' % (word, r))


# titleword = str(item)[:-4]

stopwords = {item}
passwords = {word:score for word, score in sorted(
    keywords.items(), key=lambda x:-x[1])[:300] if not (word in stopwords)}



font_path = 'KR-WordRank/font/NanumSquareRoundR.ttf'

krwordrank_cloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color="white"
)

krwordrank_cloud = krwordrank_cloud.generate_from_frequencies(passwords)


fig = plt.figure(figsize=(10, 10))
plt.imshow(krwordrank_cloud, interpolation="bilinear")
# plt.show()

fig.savefig(f'{item}.png')
plt.close(fig)
    