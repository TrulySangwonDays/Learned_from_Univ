# 20201929 이상원

#1.
install.packages("dplyr")
install.packages("ggplot2")
install.packages("readxl")
library(dplyr)
library(ggplot2)
library(readxl)


#2.
exam_data <- read_excel("data.xlsx", sheet = 1)
exam_data <- rename(exam_data, assignment = p1)
exam_data <- rename(exam_data, attendance = p2)
exam_data <- rename(exam_data, midterm = p3)
exam_data <- rename(exam_data, final = p4)
exam_data <- rename(exam_data, sum = p5)
exam_data <- rename(exam_data, grade = p6)
exam_data


#3.
student_info <- read_excel("data.xlsx", sheet = 2)
exam_data <- left_join(exam_data, student_info, by = "student_id")
exam_data


#4.
exam_data$sum <- (exam_data$assignment + exam_data$attendance + exam_data$midterm + exam_data$final)
exam_data$grade <- ifelse(exam_data$sum >= 90, "A",
                          ifelse(exam_data$sum >= 80, "B",
                                 ifelse(exam_data$sum >= 70, "C",
                                        ifelse(exam_data$sum >= 60, "D", "F"))))
exam_data


#5.
exam_data %>% 
  filter(student_grade == 1 & depart == "경영" | depart == "무역" & grade == "C") %>% 
  select(name, sum) %>%
  arrange(desc(sum))


#6.
sg_mean <- exam_data %>% 
  group_by(student_grade) %>% 
  summarise(mean_sum = mean(sum))

ggplot(data = sg_mean, aes(x = student_grade, y = mean_sum)) +
  geom_col()


#7.
exam_data$sex <- ifelse(exam_data$sex == 1, "male",
                        ifelse(exam_data$sex == 2, "female", NA))

sex_grade <- exam_data %>% 
  select(sex, grade) %>% 
  group_by(sex, grade) %>% 
  summarise(count_grade = n())

ggplot(data = sex_grade, aes(x = grade, y = count_grade, fill = sex)) +
  geom_col(position = "dodge") +
  scale_x_discrete(limits = c("A", "B", "C", "D", "F"))


#8.
depart_top3 <- bind_rows(exam_data %>% 
                           filter(depart == "경영") %>% 
                           arrange(desc(sum)) %>% 
                           head(3),
                         exam_data %>% 
                           filter(depart == "경제") %>% 
                           arrange(desc(sum)) %>% 
                           head(3),
                         exam_data %>% 
                           filter(depart == "무역") %>% 
                           arrange(desc(sum)) %>% 
                           head(3))
depart_top3


#9.
ratio_grade <-
  exam_data %>% 
  group_by(grade) %>% 
  summarise(count_grade = n())
ratio_grade <-
  ratio_grade %>% 
  mutate(ratio = (count_grade/sum(count_grade))*100) %>% 
  select(grade, ratio)

ggplot(data = ratio_grade, aes(x = grade, y = ratio)) +
  geom_col()


#10.
depart_sex_mean <-
  exam_data %>% 
  group_by(depart, sex) %>% 
  summarise(mean_grade = mean(sum))

ggplot(data = depart_sex_mean, aes(x = depart, y = mean_grade, fill = sex)) +
  geom_col(position = "dodge") +
  scale_x_discrete(limits = c("경영", "경제", "무역", "회계"))


