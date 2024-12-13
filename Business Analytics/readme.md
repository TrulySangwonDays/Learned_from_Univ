# Business Analytics
*경영학 전공 과목. 데이터분석을 통해 유의미한 비즈니스 인사이트 도출의 체계적인 방법론에 관한 강의*  
*빅데이터의 기초, 데이터 탐색, 성능평가, 지도/비지도학습, 크롤링과 텍스트마이닝, 딥러닝 기초 등을 심도있고 체계적으로 배울 수 있었습니다.*

### 학습 및 실습 내용
- Data handling(Pandas, Numpy)
- 데이터 탐색 및 이상치&결측치 처리
- Association(연관규칙분석)
- Clustering(클러스터링)
- Classification(분류 모델)
- Regression(회귀분석)
- 성능평가 방법론
- Crawling(크롤링)
- NLP & Textmining
- 딥러닝 기초

<br>

# 최종 프로젝트 명 : 유행어 크롤링을 통한 문화현상분석 및 워드클라우드, 예측모델

### 주제
**1. 유행어의 사회문화현상을 분석을 통한 유행어 성공가능성 파악**  
**2. 유행어의 사용 맥락 파악**  
**3. 딥러닝 예측모델을 활용한 유행어 성공가능성 파악**


### 문제해결 과정
1. 유행어 단어 100개를 선정하여 Selenium, ChromeDriver 동적 크롤링을 통해 네이버블로그에 등장하는 유행어의 시초를 찾아나가며, 분석을 위해 크롤링을 통해 수집한 게시글을 데이터프레임화했다.
2. 유행어의 기준을 "월별 등장 횟수 150회 이상", 급상승의 기준을 "최초 150회 달성한 시점과 시작점의 기울기가 6 이상"으로 정의했다.
3. 150회 기준에 따라 성공한 유행어와 성공하지 못한 유행어를 비교분석 했다.
4. 단어 사용 빈도 slope에 따라 단어를 그룹핑한 후, 단어 사용 급상승 요인을 비교분석 했다.
5. 유행어의 사용 맥락을 파악하기 위해 불용어 제거, TF-IDF 등 전처리 과정을 거친 후 텍스트마이닝을 통한 위드클라우드 시각화를 진행했다.
6. KoNLPY&TF-IDF를 사용한 워드클라우드 결과와 KRWordRank를 사용한 워드클라우드 결과를 비교하며 두 방식의 성능을 비교하여 KRWordRank 활용 방식이 더 효과적임을 확인했다.
7. 유행어 성공가능성 파악을 위해 LSTM 시계열 예측 모델을 활용하여 모델링을 진행했으나, 크롤링하여 수집한 데이터의 양과 종류가 적어 신뢰도 높은 결과를 가져오기에는 한계가 있었다.


### 프로젝트 인사이트 · 결론
1. 성공하지 못한 유행어의 특징
    - 뜻을 유추하기 어려움
    - 특정 대상에 대한 혐오표현
    - 특정 연령층에서만 유행
2. 성공한 유행어
    - 메이저 미디어플래폼에 등장하거나 유명인이 사용한 유행어의 급증 추세가 가팔랐음
    - 사회적 배경 혹은 트렌드를 반영한 유행어가 가장 가파른 추세를 보임
    - 성공한 유행어 중에서는 자존감을 증대시키는 단어가 다수 있음
    - 인사이트: 특정 유행어를 빠르게 유행시키고자 한다면 사회적 배경, 트렌드를 이용하는 것이 가장 효과적임 방법이다.
3. 워드클라우드를 통해 유행어 사용의 맥락 파악: 특정 유행어와 많이 쓰이는 단어를 분석하여 마케팅에 활용할 수 있을 것이다. (점메추: 직장인, 샐러드, 간편식, 배달 드으이 단어와 함께 사용됨)
4. LSTM 예측모델을 사용하여 유의미한 인사이트를 얻지 못했지만, 우리 연구주제에 맞게 개발해 나간다면, 향후 새로 등장한 단어가 유행어가 될 가능성이 있는지 여부에 대한 예측을 하고 그에 대비해 여러 분야에 활용할 수 있을 것으로 기대된다.


### 깨달은 점 · 배운 점
- 현실 세계에는 텍스트와 이미지 같은 비정형 데이터가 80% 이상을 차지하며, 이러한 비정형 데이터를 얼마나 잘 이해하고 전처리하느냐에 따라 비즈니스적 인사이트 도출의 효과성이 크게 달라진다는 점을 깨달았다.
- Selenium과 Chromedriver를 활용해 HTML크롤링을 프로젝트에 실제로 적용해보는 경험이었다. 그 과정에서 수많은 오류와 시간을 필요로 했지만, 코드를 수정해 나가며 프로젝트가 앞으로 나가갈 때 성취감을 느꼈다.
- 워드클라우드 구현 방식에 `KoNLPY 및 TF-IDF`와 `KRWordRank` 방식을 적용하여 두 결과를 비교분석해보았는데, `KRWordRank`을 적용한 방식에 유의미한 정보가 더욱 효과적으로 드러남을 확인했다.


### 데이터 수집 방식
- 네이버 블로그, VIEW 기준 월별 게시글의 개수, 제목, 내용, 게시날짜 등을 크롤링하여 수집
- Selenium 라이브러리, ChromeDriver을 활용한 동적 크롤링


<br>

---

### 결과물
1. 발표자료
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-1.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-2.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-3.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-4.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-5.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-6.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-7.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-8.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-9.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (3. 최종발표)-10.jpg>)

<br>

---

<br>

2. 보고서
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-01.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-02.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-03.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-04.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-05.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-06.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-07.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-08.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-09.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-10.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-11.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-12.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-13.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-14.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-15.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-16.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-17.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-18.jpg>)
![alt text](<asset/07_Catch_Phrase_Pattern_Model (4. 파이널 리포트)-19.jpg>)





