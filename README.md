# EgeAltinsoyCarlaTask
This task had been provided to me by Carla for a job application for backend position. I picked up option A. It consist of a solution for the provided project which is done by Ege Altınsoy

Firstly let's talk about my journey on this task. At the beginning of the project I decided to use SpringToolSuite 4. To connect the database I had been planning to use H2 table. To be able to start the project I used Spring Initializer Tool whose URL is https://start.spring.io so I asked GPT which dependencies to use for my project and it suggested to me use: Spring Web, Spring Data JPA, H2 Database dependencies. Unfourtunately I couldn't run the template provided me from Spring Initializer Tool on Spring Tool Suite. So I 
changed my compiler to VSCode and installed extensions. I installed Java Extension Pack and Spring Boot Extension Pack. Then I was ready to start. Somehow I couldn't handle to use it. Previously I had a taken course Cyber Securtiy in that course we developed a project to show vulnerabilities on a website. Our purpose was to show 5 vulnerabilites from OWASP's top 10 Vulnerability in 2023. We developed that website with Flask. Also in my internship during Vakıfbank they had been using Flask which is Python Framework. Firstly I did not want to use MongoDB and Postman because during our Mobile Application Course we had very tough situation to connect servers. Even professors couldn't find solution in some cases. But I hadn't any option in my mind to develop the project. So I started with Flask and Postman. Then I initialized my environment to use Flask. Moved to virtual environemnt and installed Flask from my terminal then activated it.
I developed my project step by step and made queries from Postman step by step. First two task was done and but while developing task 3 my code had been kinda mixed. I couldn't run couple of queries but for the working queries I had screen shots. So I added them. Untill step 2 all queries had been working but after development of step 3. It is kinda confused. But then I developed task 3 succesfully. At the end I completed the project. I commented my previous code for Task1 and Task2 to project. Finally moved to task3 and pushed it to Github. I took screenshots for every step and substep added them on read.me below as can be seen.

TASK 1
list compensation data via API GET request

Filter by one or more fields/attributes
I filtered by Job Title column which is Senior Specialist row
<img width="1440" alt="filter_by_one_attribute" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/8553abf8-addf-475c-a8a0-6ec01df572ee">


Sort by one or more fields/attributes 

I sorted the dataset according to Salary column by ascending 
<img width="1440" alt="sort_by_one_attribute" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/48e2c163-c690-431a-8b57-9acf95ac3a02">

<img width="1440" alt="sort_by_one_attribute2" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/fde7ad8f-26e5-4f4c-8d0f-6222da9db5b4">


I also applied both operations filter and sort

Sorted salaries by ascending but filtered it according to whose job title is Senior Specialist
<img width="1440" alt="sort_and_filter_attribute" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/de1927f6-6abc-494a-9429-2c11d0a1e195">

<img width="1440" alt="sort_and_filter_attribute2" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/0bb84512-caa1-462c-9592-b2f84cb68f8f">


TASK 2

Fetch a single record via GET request
Return a sparse fieldset

I sparsed the dataset according to How old are you column. 
So data returned us only according to How old are you columns.

<img width="1440" alt="return_sparse_fieldset" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/05b32d65-27ee-46b1-837c-a282ec1ab98e">

<img width="1440" alt="return_sparse_fieldset2" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/fba99f40-7541-4b04-a0e0-d5185dadbc79">

TASK 3

Have the JSON response be normalized into a uniform schema via a serializer or json template
Serialize more than one compensation data set

For this task I used Online JSON to JSON Schema Converter whose URL is below
https://www.liquid-technologies.com/online-json-to-schema-converter

With the assistance of tool I decided to how to create JSON Schema. I pasted couple of rows from dataset 1 and dataset 2
dataset 1 is salary_survey-1.csv and dataset 2 is salary_survey-2.csv

So according to that output I modified my code according to it.

<img width="1440" alt="serialize1" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/3e94b3c9-b29f-448f-9913-d1e354c993cb">

<img width="1440" alt="serialize2" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/dd4b73d3-117c-42d2-8ccb-44333cc93384">


<img width="1440" alt="serialize3" src="https://github.com/ege6nsoy/EgeAltinsoyCarlaTask/assets/69108759/3883ac00-333a-4f4f-b4d9-a2af493d99c9">




