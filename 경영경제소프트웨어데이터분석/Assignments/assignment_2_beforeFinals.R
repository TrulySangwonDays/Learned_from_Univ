install.packages("readxl")
install.packages("dplyr")
library(readxl)
library(dplyr)

data <- read_excel("data-2.xlsx")

### test 1. 남성들 평균 신장이 170cm인지에 관한 가설검정
q1_data <- data %>% 
  filter(성별 == 1) %>% 
  select(성별, 신장)

t.test(q1_data$신장, mu = 170)


### test 2. 교육전_판매실적과 교육후_판매실적의 평균 차이 가설검정
q2_data <- data %>% 
  select(교육전_판매실적, 교육후_판매실적)

t.test(q2_data$교육전_판매실적, q2_data$교육후_판매실적, paired = T)


### test 3. 교육방법(2가지)에 따른 교육후_판매실적의 평균 차이 가설검정
q3_data <- data

q3_data$교육방법 <- 
  ifelse(data$교육방법 == "교재", 1,
         ifelse(data$교육방법 == "영상", 2,
                ifelse(data$교육방법 == "멘토링", 3,
                       ifelse(data$교육방법 == "참여", 4, NA))))

q3_data <- q3_data %>%
  filter(교육방법 == 1 | 교육방법 == 3) %>% 
  select(교육방법, 교육후_판매실적)


q3_data_book <- q3_data %>% 
  filter(교육방법 == 1)
q3_data_book <- rename(q3_data_book, 교육후_판매실적_교재 = 교육후_판매실적)
q3_data_book <- q3_data_book %>%
  select(교육후_판매실적_교재)

q3_data_mento <- q3_data %>% 
  filter(교육방법 == 3)
q3_data_mento <- rename(q3_data_mento, 교육후_판매실적_멘토링 = 교육후_판매실적)
q3_data_mento <- q3_data_mento %>%
  select(교육후_판매실적_멘토링)

var.test(q3_data_book$교육후_판매실적_교재, q3_data_mento$교육후_판매실적_멘토링)
t.test(q3_data_book$교육후_판매실적_교재, q3_data_mento$교육후_판매실적_멘토링, var.equal = T)


### test 4. 교육방법(3가지)에 따른 교육후_판매실적의 평균 차이 가설검정
q4_data <- data

q4_data$교육방법 <- 
  ifelse(data$교육방법 == "교재", "1. 교재",
         ifelse(data$교육방법 == "영상", "2. 영상",
                ifelse(data$교육방법 == "멘토링", "3. 멘토링",
                       ifelse(data$교육방법 == "참여", "4. 참여", NA))))

q4_data <- q4_data %>%
  filter(교육방법 == "1. 교재" | 교육방법 == "3. 멘토링" | 교육방법 == "4. 참여") %>% 
  select(교육방법, 교육후_판매실적)

boxplot(교육후_판매실적~교육방법, data = q4_data)

bartlett.test(교육후_판매실적~교육방법, data = q4_data)
oneway.test(교육후_판매실적~교육방법, data = q4_data, var.equal = T)

anova = aov(교육후_판매실적~교육방법, data = q4_data)
anova
summary(anova)

# 대립가설 기각 귀무가설 채택 p값이 0.8665이므로


### test 5. 성별(2가지)과 교육방법(3가지)에 따른 교육후_판매실적의 평균 차이 가설검정
q5_data <- data

q5_data$교육방법 <- 
  ifelse(data$교육방법 == "교재", "1. 교재",
         ifelse(data$교육방법 == "영상", "2. 영상",
                ifelse(data$교육방법 == "멘토링", "3. 멘토링",
                       ifelse(data$교육방법 == "참여", "4. 참여", NA))))
q5_data$성별 <- 
  ifelse(data$성별 == 1, "남성",
         ifelse(data$성별 == 2, "여성", NA))

q5_data <- q5_data %>%
  filter(교육방법 == "1. 교재" | 교육방법 == "2. 영상" | 교육방법 == "3. 멘토링") %>% 
  select(성별, 교육방법, 교육후_판매실적)

boxplot(교육후_판매실적~성별, data = q5_data)
boxplot(교육후_판매실적~교육방법, data = q5_data)
boxplot(교육후_판매실적~성별+교육방법, data = q5_data)

anova = aov(교육후_판매실적~성별+교육방법+성별:교육방법, data = q5_data)
anova
summary(anova)

interaction.plot(q5_data$교육방법, q5_data$성별, q5_data$교육후_판매실적)


### test 6. 학력(2가지), 입사성적, 교육시간을 이용하여 근무성적 예측 회귀분석
q6_data <- data %>% 
  select(학력, 입사성적, 교육시간, 근무성적)

plot(근무성적~입사성적, data = q6_data)
plot(근무성적~교육시간, data = q6_data)

regression = lm(근무성적~학력+입사성적+교육시간, data = q6_data)
summary(regression)

# y = 36.75394 + 17.92738D - 0.01095입사성적 + 0.76117교육시간 [이므로]

# y = 54.68132 - 0.01095입사성적 + 0.76117교육시간 (대졸)
# y = 36.75394 - 0.01095입사성적 + 0.76117교육시간 (고졸)



