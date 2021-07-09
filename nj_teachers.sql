

CREATE SCHEMA NJ_clean;

CREATE TABLE NJ_clean.teacher (last_name VARCHAR(50),
first_name VARCHAR(50),county VARCHAR(100),district VARCHAR(100),
school VARCHAR(300), primary_job VARCHAR(300),fte FLOAT,
salary FLOAT,certificate VARCHAR(100),subcategory VARCHAR(50),
teaching_route VARCHAR(50),highly_qualified VARCHAR(200),
experience_district FLOAT,experience_nj FLOAT,experience_total FLOAT);




SET @@GLOBAL.local_infile:= 1;


LOAD DATA INFILE '/Users/kkc/dumps/new_nj_state_teachers_salaries.csv'
INTO TABLE NJ_clean.teacher
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


SELECT 'last_name', 'first_name', 'county','district','school','primary_job', 'fte','salary','certificate','subcategory','teaching_route',
'highly_qualified', 'experience_district', 'experience_nj','experience_total'
UNION ALL
(SELECT last_name, first_name, county,district,school,primary_job, fte,salary,certificate,subcategory,teaching_route,
highly_qualified, experience_district, experience_nj,experience_total FROM NJ_clean.teacher 
ORDER BY RAND(7) 
LIMIT 777)

INTO OUTFILE '/Users/kkc/tmp/teachersample.csv' 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';





CREATE SCHEMA teacher_sample;

CREATE TABLE teacher_sample.teachers (last_name VARCHAR(50),
first_name VARCHAR(50),county VARCHAR(100),district VARCHAR(100),
school VARCHAR(300), primary_job VARCHAR(300),fte FLOAT,
salary FLOAT,certificate VARCHAR(100),subcategory VARCHAR(50),
teaching_route VARCHAR(50),highly_qualified VARCHAR(200),
experience_district FLOAT,experience_nj FLOAT,experience_total FLOAT);

LOAD DATA INFILE '/Users/kkc/tmp/teachersample.csv'
INTO TABLE teacher_sample.teachers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT COUNT(*) FROM teacher_sample.teachers;

SELECT AVG(salary) FROM teacher_sample.teachers;
SELECT COUNT(salary) FROM teacher_sample.teachers WHERE salary > 150000;
SELECT last_name FROM teacher_sample.teachers WHERE salary > 150000 AND experience_total < 5;
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%Preschool%';
#SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'School Counselor';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%School Counselor%';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%Principal%';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%School Psychologist';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%Kindergarten';

SELECT MIN(salary) FROM teacher_sample.teachers WHERE district = 'Atlantic City';
SELECT COUNT(*) FROM teacher_sample.teachers WHERE district = 'Passaic City' AND experience_total < 10;





