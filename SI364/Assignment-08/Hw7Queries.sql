/** Name: Zijie Ku
 ** Uniqname: kuzijie
 ** SI364  Assignement-08 
 **/




/****** Query 1 ******/
-- IDs, names, and GPAs of students with GPA > 3.6 --
SELECT sID, sName, GPA 
FROM Student
WHERE GPA > 3.6
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-1.txt';

/****** Query 2 ******/
-- Student names and majors for which they've applied - no duplicates
SELECT DISTINCT S.sName, A.major
FROM Student S, Apply A
WHERE S.sID = A.sID
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-2.txt';

/****** Query 3 ******/
-- Names and GPAs of students with sizeHS < 1000 applying to CS at Stanford,
-- and the application decision
SELECT S.sName, S.GPA, A.decision
FROM Student S, Apply A
WHERE S.sID = A.sID
AND S.sizeHS < 1000
AND A.cName = "Stanford"
AND A.major = "CS"
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-3.txt';

/****** Query 4 ******/ 
-- All large campuses (enrollment over 20000) with CS applicants -no duplicates
SELECT DISTINCT College.cName
FROM College, Apply
WHERE College.cName = Apply.cName
AND Apply.major = "CS"
AND College.enrollment > 20000
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-4.txt';

/****** Query 5 ******/
-- Application information, sorted by highest gpa
SELECT A.sID, S.sName, S.GPA, C.cName, C.enrollment
FROM College C, Student S, Apply A
WHERE C.cName = A.cName
AND S.sID = A.sID
ORDER BY S.GPA DESC, S.sName
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-5.txt';

/****** Query 6 ******/
-- Applicants to bio majors
SELECT sID, major
FROM Apply
WHERE major LIKE '%bio%'
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-6.txt';

/****** Query 7 ******/
-- Select * cross-product of Students and Colleges
SELECT *
from Student, College
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-7.txt';

/****** Query 8 ******/ 
-- Add scaled GPA based on sizeHS GPA*(sizeHS/1000.0)
SELECT S.sID, S.sNAme, S.GPA, S.sizeHS, GPA*(sizeHS/1000.0)
FROM Student S
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-8.txt';

/****** Query 9 ******/ 
-- Rename result attribute as scaledGPA and return the first 5
SELECT S.sID, S.sNAme, S.GPA, S.sizeHS, GPA*(sizeHS/1000.0) AS scaledGPA
FROM Student S
LIMIT 5
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-9.txt';

/****** Query 10 ******/
-- Show all students and the number of colleges they applied to. 
-- Make sure to use the column names Name and Applications
SELECT S.sName AS Name, count(*) AS Applications
FROM Student S, College C, Apply A
WHERE S.sID = A.sID
AND C.cName = A.cName
GROUP BY S.sID
INTO OUTFILE '/Users/kuzijie/Dropbox/SI/OpenShift/si364/Assignment-08/Hw7-10.txt';
