install.packages("readxl")
install.packages("dplyr")
install.packages("ggplot2")
library(readxl)
library(dplyr)
library(ggplot2)

data <- read_excel("2014년도 주거실태조사_공표자료(시군구 명칭 수정).xlsx")
data$q12_1 <- ifelse(data$q12_1 >= 9999999, NA, data$q12_1) #주택가격 이상치 제거
data$q49_5 <- ifelse(data$q49_5 >= 9999999, NA, data$q49_5) #월평균소득 이상치 제거
data$q52_4 <- ifelse(data$q52_4 >= 9999999, NA, data$q52_4) #총자산 이상치 제거
data$q20_1_a <- ifelse(data$q20_1_a >= 999, NA, data$q20_1_a) #주택크기_평 이상치 제거
data$q12_1 <- (data$q12_1*10000)/100000000 #주택가격 억 단위로 변경



### 1. t-test 광주 vs. 대전 평균 아파트 가격 차이
q1_data <- data

q1_data <- rename(q1_data, 주택유형 = q4, 시도 = sido, 주택가격 = q12_1)
q1_data <- q1_data %>% 
  select(주택유형, 시도, 주택가격) %>% 
  filter(주택유형 == 4) %>% 
  filter(시도 == 24 | 시도 == 25) %>% 
  filter(!is.na(주택가격))

q1_data$시도 <- ifelse(q1_data$시도 == 24, "광주", "대전")
boxplot(주택가격~시도, data = q1_data)

q1_data_gwangju <- q1_data %>% 
  filter(시도 == "광주") %>% 
  select(주택가격)

q1_data_daejeon <- q1_data %>% 
  filter(시도 == "대전") %>% 
  select(주택가격)

t.test(q1_data_gwangju, q1_data_daejeon, paired = F)



### 2. One-way ANOVA 서울특별시 가구주 학력수준에 따른 평균 아파트 크기 차이
q2_data <- data

q2_data <- rename(q2_data, 주택유형 = q4, 시도 = sido, 학력 = dq1, 주택가격 = q12_1)
q2_data <- q2_data %>% 
  select(주택유형, 시도, 학력, 주택가격) %>% 
  filter(주택유형 == 4 & 시도 == 11) %>% 
  filter(!is.na(주택유형) & !is.na(시도) & !is.na(학력) & !is.na(주택가격)) %>% 
  select(학력, 주택가격)

q2_data <- q2_data %>% 
  mutate(학력수준 = ifelse(학력 == 1, "초졸",
                               ifelse(학력 == 2, "중졸",
                                           ifelse(학력 == 3, "고졸", "대졸"))))

q2_data <- q2_data %>%
  select(학력수준, 주택가격) %>%
  arrange(학력수준)

ggplot(data = q2_data, aes(x = 학력수준, y = 주택가격)) +
  geom_boxplot() +
  scale_x_discrete(limits = c("초졸", "중졸", "고졸", "대졸"))

bartlett.test(주택가격~학력수준, data = q2_data)

q2_anova = aov(주택가격~학력수준, data = q2_data)
q2_anova
summary(q2_anova)



### 3. Regression analysis 총소득, 총자산, 가구원총수, 아파트크기에 따른 집 가격 예측
q3_data <- data

q3_data <- rename(q3_data, 주택유형 = q4, 월소득 = q49_5, 총자산 = q52_4, 인원 = q47, 크기_평 = q20_1_a, 주택가격 = q12_1)
q3_data <- q3_data %>% 
  select(주택유형, 월소득, 총자산, 인원, 크기_평, 주택가격) %>% 
  filter(주택유형 == 4) %>% 
  filter(!is.na(월소득) & !is.na(총자산) & !is.na(인원) & !is.na(크기_평) & !is.na(주택가격)) %>% 
  select(월소득, 총자산, 인원, 크기_평, 주택가격)

summary(q3_data)

ggplot(data = q3_data, aes(x = 월소득, y = 주택가격)) +
  geom_point(shape = 21, size = 1.5, color = "blue" ) +
  coord_cartesian(xlim = c(0, 1500), ylim = c(0, 15))

ggplot(data = q3_data, aes(x = 총자산, y = 주택가격)) +
  geom_point(shape = 21, size = 1.5, color = "blue" ) +
  coord_cartesian(xlim = c(2300, 200000), ylim = c(0, 15))

ggplot(data = q3_data, aes(x = 인원, y = 주택가격)) +
  geom_point(shape = 21, size = 1.5, color = "blue" ) +
  coord_cartesian(xlim = c(1, 10), ylim = c(0, 15))

ggplot(data = q3_data, aes(x = 크기_평, y = 주택가격)) +
  geom_point(shape = 21, size = 1.5, color = "blue" ) +
  coord_cartesian(xlim = c(0, 70), ylim = c(0, 15))


q3_regression = lm(주택가격~월소득+총자산+인원+크기_평, data = q3_data)
summary(q3_regression)

