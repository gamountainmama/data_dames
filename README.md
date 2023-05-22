# data_dames

## Project Title: The Many Problems in Education

## Team Members:
* Kendall Sanders, 
* Carol Love, 
* Sahmirah Muhammad, 
* Kelly Schuster-Parades

## Project Background:

Education demographics is a complex and multifaceted field with various factors such as test scores, financial situations, gender, race, ethnicity, location, and parental education levels. This area of study has many problems that can make it difficult to obtain accurate and reliable data.

One of the main problems is the lack of standardization in testing and grading. Different schools, counties, and states have different standards and practices making it challenging to compare student performance. Additionally, there is a significant socioeconomic divide in education, with students from low-income families often facing greater obstacles to academic success. This divide is further exacerbated by disparities in access to resources such as quality schools, experienced teachers, and extracurricular activities.

Gender and racial biases are also prevalent in education demographics, with certain groups experiencing discrimination and systemic barriers that hinder their academic performance and opportunities. Furthermore, there are gaps in diverse representation in the teaching profession, which also affects students' experiences and outcomes. Overall, these challenges make it crucial for researchers and educators to approach education demographics with sensitivity and critical analysis, considering the multifaceted nature of the issues and the need for nuanced solutions.

## Project Objective: 

In this project, we compared and analyzed the demographics and test scores of two different schools: a private wealthy school in Ft. Lauderdale and a small rural school in Georgia. The two schools represent vastly different socioeconomic situations, and we expected to observe significant differences in their student populations. We built a NN to predict the academic success of the students and determine if they will pass or fail their classes. 

The data was cleaned to remove missing values and extraneous outliers, and we used feature engineering to extract the most meaningful factors. The cleaned data was used to create a neural network using TensorFlow and Pytorch/PySpark to predict the outcome of the students.

THe following model was used on all of the datasets to attempt to provide consistency.<img width="624" alt="neural" src="https://github.com/gamountainmama/data_dames/assets/40581033/fd2bcaae-fbc9-4232-8f89-c4bb16d19bd5">


### Data Sets:
1) Kaggle Data Set - ‘This dataset contains information on the performance of high school students in mathematics, including their grades and demographic information. The data was collected from three high schools in the United States. 
* Gender: The gender of the student (male/female)
* Race/ethnicity: The student's racial or ethnic background (Asian, African-American, Hispanic, etc.)
* Parental level of education: The highest level of education attained by the student's parent(s) or guardian(s)
* Lunch: Whether the student receives free or reduced-price lunch (yes/no)
* Test preparation course: Whether the student completed a test preparation course (yes/no)
* Math score: The student's score on a standardized mathematics test
* Reading score: The student's score on a standardized reading test
* Writing score: The student's score on a standardized writing test

2) Rural School Georgia - The Georgia Milestones data uses the following features: 
* gender, 
* ethnicity, 
* English-language learners (ELL), 
* students with disabilities (SWD), 
* economic disadvantage (ED), 
* student support team (ST), 
* gifted, absences, 
* Lexile level, and 
* previous year’s scores.


3) Private School Florida - This dataset contains over 5000 lines of information on course grades for students in 9-12 Grade. The Florida data uses the following features: 
* grade, 
* English grade, 
* math grade, 
* science grade, and 
* humanities grade. 
Since all students pass their computer science course, we considered success earning an A in the course. The accuracy of the model for Florida was 0.829.


