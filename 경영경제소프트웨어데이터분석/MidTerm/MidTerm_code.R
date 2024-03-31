install.packages("readxl")
install.packages("ggplot2")
install.packages("dplyr")
library(readxl)
library(ggplot2)
library(dplyr)

main_data <- read_excel("2014년도 주거실태조사_공표자료(시군구 명칭 수정).xlsx")


### 1. 주택 유형에 따른 주택가격 비교
data1 <- rename(main_data, 주택유형 = q4, 주택가격 = q12_1)
data1$주택가격 <- ifelse(data1$주택가격 >= 9999999, NA, data1$주택가격)


mean_주택유형 <- data1 %>%
  filter(!is.na(주택가격) & !is.na(주택유형)) %>% 
  group_by(주택유형) %>% 
  summarise(mean_주택가격 = mean(주택가격)) %>%
  arrange(desc(mean_주택가격))


# 억 단위로 변경
mean_주택유형$mean_주택가격 <- (mean_주택유형$mean_주택가격*10000)/100000000

# 일부 주택유형 삭제
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 7, NA, mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 9, NA, mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 10, NA, mean_주택유형$주택유형)
mean_주택유형 <- mean_주택유형 %>%
  filter(!is.na(주택유형))

# 값 변경
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 1,  "일반단독", mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 2,  "다가구단독", mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 3,  "영업겸용단독", mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 4,  "아파트", mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 5,  "연립", mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 6,  "다세대주택", mean_주택유형$주택유형)
mean_주택유형$주택유형 <- ifelse(mean_주택유형$주택유형 == 8,  "오피스텔", mean_주택유형$주택유형)

# 그래프
ggplot(data = mean_주택유형, aes(x = reorder(주택유형, -mean_주택가격), y = mean_주택가격)) + geom_col()




### 2. 서울시 내 자치구에 따른 주택가격 비교
data2 <- rename(main_data, 시도 = sido, 시군구 = sigungu, 주택가격 = q12_1)
data2$주택가격 <- ifelse(data2$주택가격 >= 9999999, NA, data2$주택가격)


data2 <- data2 %>%
  filter(시도 == 11 & !is.na(주택가격)) %>% 
  select(시도, 시군구, 주택가격) %>% 
  group_by(시군구) %>% 
  summarise(mean_주택가격 = mean(주택가격)) %>% 
  arrange(desc(mean_주택가격))

# 억 단위로 변경
data2$mean_주택가격 <- (data2$mean_주택가격*10000)/100000000

data2$시군구 <- ifelse(data2$시군구 == "강동구", NA, data2$시군구)
data2 <- data2 %>%
  filter(!is.na(시군구))

# 그래프
ggplot(data = data2, aes(x = reorder(시군구, mean_주택가격), y = mean_주택가격)) +
  geom_col() + coord_flip()



### 3. 부채비율에 따른 주택가격
data3 <- rename(main_data, 총자산 = q52_4, 총부채 = q53_1_4, 주택가격 = q12_1)

data3 <- data3 %>%
  filter(!is.na(주택가격)) %>% 
  mutate(부채비율 = (총부채/총자산)*100) %>%
  select(ID, 총자산, 총부채, 부채비율, 주택가격)

data3$주택가격 <- ifelse(data3$주택가격 >= 9999999, NA, data3$주택가격)
data3$총부채 <- ifelse(data3$총부채 >= 9999999, NA, data3$총부채)
data3$총자산 <- ifelse(data3$총자산 >= 9999999, NA, data3$총자산)
data3$총부채 <- ifelse(is.na(data3$총부채), 0, data3$총부채)
data3$총자산 <- ifelse(is.na(data3$총자산), 0, data3$총자산)
data3$부채비율 <- ifelse(data3$총부채 == 0 & is.na(data3$부채비율), 0, data3$부채비율)
data3 <- data3 %>%
  filter(!is.na(주택가격))

data3 <- data3 %>% 
  mutate(부채그룹 = ifelse(부채비율 < 20, "20%미만",
                       ifelse(부채비율 < 40, "20%이상 40%미만",
                                  ifelse(부채비율 < 60, "40%이상 60%미만",
                                             ifelse(부채비율 < 80, "60%이상 80%미만", "80%이상")))))
data3 <- data3 %>% 
  group_by(부채그룹) %>% 
  summarise(주택가격 = mean(주택가격))

# 억 단위로 변경
data3$주택가격 <- (data3$주택가격*10000)/100000000

# 그래프
ggplot(data = data3, aes(x = 부채그룹, y = 주택가격)) + geom_col()



### 4. 지역별 건설 시점별 주택가격
data4 <- rename(main_data, 시도 = sido, 건설시점 = q18, 주택가격 = q12_1)
data4$주택가격 <- ifelse(data4$주택가격 >= 9999999, NA, data4$주택가격)

data4$건설시점 <- (ifelse(data4$건설시점 == 1, "2012이후",
                      ifelse(data4$건설시점 == 2, "2009~2011",
                             ifelse(data4$건설시점 == 3, "2004~2008",
                                    ifelse(data4$건설시점 == 4, "1999~2003",
                                           ifelse(data4$건설시점 == 5, "1994~1998",
                                                  ifelse(data4$건설시점 == 6, "1989~1993",
                                                         ifelse(data4$건설시점 == 7, "1984~1988",
                                                                ifelse(data4$건설시점 == 8, "1983이전", NA)))))))))

data4$시도 <- (ifelse(data4$시도 == 11, "서울",
                      ifelse(data4$시도 == 21, "부산",
                             ifelse(data4$시도 == 22, "대구",
                                    ifelse(data4$시도 == 23, "인천",
                                           ifelse(data4$시도 == 24, "광주",
                                                  ifelse(data4$시도 == 25, "대전",
                                                         ifelse(data4$시도 == 26, "울산",
                                                                ifelse(data4$시도 == 29, "세종",
                                                                       ifelse(data4$시도 == 31, "경기",
                                                                              ifelse(data4$시도 == 32, "강원",
                                                                                     ifelse(data4$시도 == 33, "충북",
                                                                                            ifelse(data4$시도 == 34, "충남",
                                                                                                   ifelse(data4$시도 == 35, "전북",
                                                                                                          ifelse(data4$시도 == 36, "전남",
                                                                                                                 ifelse(data4$시도 == 37, "경북",
                                                                                                                        ifelse(data4$시도 == 38, "경남",
                                                                                                                               ifelse(data4$시도 == 39, "제주", NA))))))))))))))))))

data4$주택가격 <- (data4$주택가격*10000)/100000000

data4 <- data4 %>%
  filter(!is.na(주택가격) & !is.na(시도) & !is.na(건설시점)) %>%
  select(ID, 시도, 건설시점, 주택가격) %>%
  group_by(시도, 건설시점) %>%
  summarise(mean_주택가격 = mean(주택가격))

ggplot(data = data4, aes(reorder(x = 시도, mean_주택가격), y = mean_주택가격, col = 건설시점)) + geom_col() + coord_flip()



### 5. 월평균 가계 소득에 따른 집 크기(평)
data5 <- rename(main_data, 월평균소득 = q49_5, 주택사용면적 = q20_1_a)
data5$월평균소득 <- ifelse(data5$월평균소득 >= 9999999, NA, data5$월평균소득)
data5$주택사용면적 <- ifelse(data5$주택사용면적 >= 999, NA, data5$주택사용면적)

data5 <- data5 %>%
  filter(!is.na(월평균소득) & !is.na(주택사용면적))

data5 <- data5 %>% 
  mutate(월평균소득구간 = ifelse(월평균소득 < 100, "100만원 미만",
                           ifelse(월평균소득 < 300, "100~300",
                                      ifelse(월평균소득 < 500, "300~500",
                                                 ifelse(월평균소득 < 1000, "500~1,000",
                                                             ifelse(월평균소득 < 1500, "1,000~1,500",
                                                                         ifelse(월평균소득 < 2000, "1,500~2,000",
                                                                                     ifelse(월평균소득 < 5000, "2,000~5,000", "5,000만원 이상"))))))))

data5 <- data5 %>%
  select(ID, 월평균소득구간, 주택사용면적) %>%
  group_by(월평균소득구간) %>%
  summarise(mean_주택사용면적 = mean(주택사용면적))

# 그래프
ggplot(data = data5, aes(x = 월평균소득구간, y = mean_주택사용면적)) +
  geom_col() +
  scale_x_discrete(limits = c("100만원 미만", "100~300", "300~500", "500~1,000", "1,000~1,500", "1,500~2,000", "2,000~5,000", "5,000만원 이상"))




### 6. 주택가격에 따른 전반적 주거환경 만족도
data6 <- rename(main_data, 주택가격 = q12_1, 전반적_주거환경_만족도 = q24_1)
data6$주택가격 <- ifelse(data6$주택가격 >= 9999999, NA, data6$주택가격)
data6$전반적_주거환경_만족도 <- ifelse(data6$전반적_주거환경_만족도 > 3 & data6$전반적_주거환경_만족도 < 1, NA, data6$전반적_주거환경_만족도)

# 억 단위로 변경
data6$주택가격 <- (data6$주택가격*10000)/100000000

data6 <- data6 %>%
  filter(!is.na(주택가격) & !is.na(전반적_주거환경_만족도))

data6 <- data6 %>% 
  mutate(주택가격그룹 = ifelse(주택가격 < 1, "1억원 미만",
                               ifelse(주택가격 < 3, "1~3억원",
                                           ifelse(주택가격 < 5, "3~5억원",
                                                       ifelse(주택가격 < 7, "5~7억원",
                                                                   ifelse(주택가격 < 10, "7~10억원",
                                                                               ifelse(주택가격 < 15, "10~15억원",
                                                                                           ifelse(주택가격 < 30, "15~30억원", "30억원 이상"))))))))

data6 <- data6 %>%
  select(ID, 주택가격그룹, 전반적_주거환경_만족도) %>%
  group_by(주택가격그룹, 전반적_주거환경_만족도) %>% 
  summarise(n = n()) %>% 
  mutate(tot_group = sum(n)) %>% 
  mutate(pct = round(n/tot_group*100, 2)) %>% 
  select(주택가격그룹, 전반적_주거환경_만족도, pct)

# 그래프
ggplot(data = data6, aes(x = 주택가격그룹, y = pct, fill = 전반적_주거환경_만족도)) +
  geom_col() +
  scale_x_discrete(limits = c("1억원 미만", "1~3억원", "3~5억원", "5~7억원", "7~10억원", "10~15억원", "15~30억원", "30억원 이상"))



### 7. 통근 시간에 따른 교통편 접근성 만족도 및 주택가격과의 관계
data7 <- rename(main_data, 통근시간_분 = dq2_4_m, 대중교통_접근만족도 = q23_5, 주차시설_접근만족도 = q23_6, 주택가격 = q12_1)
data7$통근시간_분 <- ifelse(data7$통근시간_분 >= 99, NA, data7$통근시간_분)
data7$대중교통_접근만족도 <- ifelse(data7$대중교통_접근만족도 > 3 & data7$대중교통_접근만족도 < 1, NA, data7$대중교통_접근만족도)
data7$주차시설_접근만족도 <- ifelse(data7$주차시설_접근만족도 > 3 & data7$주차시설_접근만족도 < 1, NA, data7$주차시설_접근만족도)
data7$주택가격 <- ifelse(data7$주택가격 >= 9999999, NA, data7$주택가격)

data7 <- data7 %>%
  filter(!is.na(통근시간_분) & !is.na(대중교통_접근만족도) & !is.na(주차시설_접근만족도) & !is.na(주택가격)) %>% 
  mutate(교통_만족도 = (대중교통_접근만족도 + 주차시설_접근만족도)/2) %>% 
  mutate(통근시간대_분 = ifelse(통근시간_분 < 10, "10분 미만",
                                ifelse(통근시간_분 < 20, "10~19분",
                                             ifelse(통근시간_분 < 30, "20~29분",
                                                          ifelse(통근시간_분 < 40, "30~39분",
                                                                       ifelse(통근시간_분 < 50, "40~49분",
                                                                                    ifelse(통근시간_분 < 60, "50~59분", "60분 이상"))))))) %>% 
  select(ID, 통근시간대_분, 교통_만족도, 주택가격)

# 억 단위로 변경
data7$주택가격 <- (data7$주택가격*10000)/100000000

data7_교통 <- data7 %>%
  group_by(통근시간대_분) %>% 
  summarise(mean_교통_만족도 = mean(교통_만족도))

data7_주택 <- data7 %>%
  group_by(통근시간대_분) %>% 
  summarise(mean_주택가격 = mean(주택가격))

data7_total <- left_join(data7_교통, data7_주택, by = "통근시간대_분")


# 엑셀 파일로 저장
install.packages("writexl")
library(writexl)
write_xlsx(data7_total, path = "통근 시간에 따른 교통편 접근성 만족도 및 주택가격과의 관계.xlsx")




# 8. 2인 부부 가구의 주요 주택 유형
data8 <- rename(main_data,
                구성원1관계 = q47_a1_1,
                구성원2관계 = q47_a1_2,
                구성원3관계 = q47_a1_3,
                구성원4관계 = q47_a1_4,
                구성원5관계 = q47_a1_5,
                구성원6관계 = q47_a1_6,
                구성원7관계 = q47_a1_7,
                구성원8관계 = q47_a1_8,
                구성원9관계 = q47_a1_9,
                구성원10관계 = q47_a1_10,
                구성원11관계 = q47_a1_11,
                구성원_총수 = q47,
                주택유형 = q4) %>% 
  select(ID,
         구성원1관계,
         구성원2관계,
         구성원3관계,
         구성원4관계,
         구성원5관계,
         구성원6관계,
         구성원7관계,
         구성원8관계,
         구성원9관계,
         구성원10관계,
         구성원11관계,
         구성원_총수,
         주택유형)

data8 <- data8 %>% 
  filter((구성원1관계 == 1 & 구성원2관계 == 2) | (구성원1관계 == 2 & 구성원2관계 == 1)) %>% 
  filter(구성원_총수 == 2)
data8 <- rename(data8,
                부부_가구 = 구성원_총수)

data8$주택유형 <- ifelse(data8$주택유형 == 1,  "일반단독", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 2,  "다가구단독", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 3,  "영업겸용단독", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 4,  "아파트", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 5,  "연립", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 6,  "다세대", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 7,  "다가구단독", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 8,  "상가/공장 내", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 9,  "판잣집", data8$주택유형)
data8$주택유형 <- ifelse(data8$주택유형 == 10,  "기타", data8$주택유형)

# 그래프
ggplot(data = data8, aes(x = 주택유형)) + geom_bar()



# 9. 가구구성원 수에 따른 집 크기(평)
data9 <- rename(main_data, 구성원_총수 = q47, 주택사용면적 = q20_1_a)

data9$구성원_총수 <- ifelse(data9$구성원_총수 > 8, NA, data9$구성원_총수)
data9$주택사용면적 <- ifelse(data9$주택사용면적 >= 999, NA, data9$주택사용면적)

data9 <- data9 %>% 
  filter(!is.na(주택사용면적)) %>% 
  filter(!is.na(구성원_총수)) %>% 
  select(ID, 구성원_총수, 주택사용면적) %>% 
  group_by(구성원_총수) %>% 
  summarise(mean_주택사용면적 = mean(주택사용면적))

# 그래프
ggplot(data = data9, aes(x = 구성원_총수, y = mean_주택사용면적)) + geom_col()



# 10. 선호하는 생활양식과 선호하는 이사 지역
data10 <- rename(main_data, 선호_생활양식 = q42_2, 선호_이사지역 = q35)

data10$선호_생활양식 <- ifelse(data10$선호_생활양식 > 2 & data10$선호_생활양식 < 1, NA, data10$선호_생활양식)
data10$선호_이사지역 <- ifelse(data10$선호_이사지역 > 18 & data10$선호_이사지역 < 1, NA, data10$선호_이사지역)

data10 <- data10 %>% 
  filter(!is.na(선호_생활양식) & !is.na(선호_이사지역)) %>% 
  select(ID, 선호_생활양식, 선호_이사지역)

data10$선호_생활양식 <- (ifelse(data10$선호_생활양식 == 1, "도시적_생활", "전원생활"))
data10$선호_이사지역 <- (ifelse(data10$선호_이사지역 == 1, "서울",
                    ifelse(data10$선호_이사지역 == 2, "부산",
                           ifelse(data10$선호_이사지역 == 3, "대구",
                                  ifelse(data10$선호_이사지역 == 4, "인천",
                                         ifelse(data10$선호_이사지역 == 5, "광주",
                                                ifelse(data10$선호_이사지역 == 6, "대전",
                                                       ifelse(data10$선호_이사지역 == 7, "울산",
                                                              ifelse(data10$선호_이사지역 == 8, "세종",
                                                                     ifelse(data10$선호_이사지역 == 9, "경기",
                                                                            ifelse(data10$선호_이사지역 == 10, "강원",
                                                                                   ifelse(data10$선호_이사지역 == 11, "충북",
                                                                                          ifelse(data10$선호_이사지역 == 12, "충남",
                                                                                                 ifelse(data10$선호_이사지역 == 13, "전북",
                                                                                                        ifelse(data10$선호_이사지역 == 14, "전남",
                                                                                                               ifelse(data10$선호_이사지역 == 15, "경북",
                                                                                                                      ifelse(data10$선호_이사지역 == 16, "경남",
                                                                                                                             ifelse(data10$선호_이사지역 == 17, "제주", "국외"))))))))))))))))))


data10 <- data10 %>%
  group_by(선호_이사지역, 선호_생활양식) %>% 
  summarise(count = n())

# 그래프
ggplot(data = data10, aes(reorder(x = 선호_이사지역, -count), y = count, fill = 선호_생활양식)) +
  geom_col(position = "dodge")







