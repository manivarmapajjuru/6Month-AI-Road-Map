
use mb;
create table customers(
customer_id int,
first_name varchar(100),
last_name varchar(100)
);
describe customers;


-- adding keys

alter table customers add primary key(customer_id);

select  * from customers;

-- adding columns
 
 
alter table customers add column e_mail_address varchar(100);
select * from customers;
alter table customers add unique(e_mail_address);


-- changing columns 


alter table customers change column e_mail_address e_mail varchar(100);##

select * from customers;
alter table customers add column phn_no int  null;
select  * from customers;

create table sale(
purchase_no int,
date_of_purchase date,
customer_id int,
foreign key(customer_id) references customers(customer_id) on delete cascade);
insert into  customers( customer_id,first_name,last_name,e_mail,phn_no) values
(2,'kajal','agarwal','kaju@gmail.com',987654321),
(3,'mahesh','babu','mahi@gmail.com',567891234);
 select * from customers;
 ## we can use insert into customer values()

select * from sale;
INSERT INTO sale (purchase_no, date_of_purchase, customer_id)
VALUES 
    (123, '2025-09-12', 1),
    (476, '2023-08-01', 3),
    (399, '2023-01-09', 2),
    (222, '2024-05-05', 2),
    (232, '2021-02-10', 2);
    select * from sale;
    select 
    s.purchase_no,
    c.first_name,
    c.phn_no
    from sale s
    join 
    customers c on s.customer_id=c.customer_id;   ### very imp
    
    select * from customers;
    TRUNCATE customers;
INSERT INTO customers(customer_id, first_name, last_name, e_mail, phn_no) VALUES
(4, 'Emily', 'Williams', 'emily.w@example.com', 4567890123),
(5, 'David', 'Brown', 'david.b@example.com', 5678901234),
(6, 'Sarah', 'Jones', 'sarah.j@example.com', 6789012345),
(7, 'Robert', 'Garcia', 'robert.g@example.com', 7890123456),
(8, 'Jennifer', 'Miller', 'jennifer.m@example.com', 8901234567),
(9, 'William', 'Davis', 'william.d@example.com', 9012345678),
(10, 'Lisa', 'Rodriguez', 'lisa.r@example.com', 1234509876),
(11, 'James', 'Martinez', 'james.m@example.com', 2345610987),
(12, 'Jessica', 'Hernandez', 'jessica.h@example.com', 3456721098),
(13, 'Thomas', 'Lopez', 'thomas.l@example.com', 4567832109),
(14, 'Karen', 'Gonzalez', 'karen.g@example.com', 5678943210),
(15, 'Richard', 'Wilson', 'richard.w@example.com', 6789054321),
(16, 'Nancy', 'Anderson', 'nancy.a@example.com', 7890165432),
(17, 'Daniel', 'Thomas', 'daniel.t@example.com', 8901276543),
(18, 'Patricia', 'Taylor', 'patricia.t@example.com', 9012387654),
(19, 'Matthew', 'Moore', 'matthew.m@example.com', 1234598765),
(20, 'Elizabeth', 'Jackson', 'elizabeth.j@example.com', 2345609876);
select * from customers;
ALTER TABLE customers MODIFY phn_no BIGINT;
select * from customers;
commit;
update customers set e_mail='babu@gmail.com' where customer_id=3;
select  * from  customers;
delete  from  customers where  customer_id=13;
select * from customers;
rollback;
select* from Customers limit 10;
select * from customers limit 5 offset 10;

-- order by
select * from customers order by phn_no asc limit 5;
select * from customers order by phn_no  desc limit 10;
-- comparision
select * from customers where customer_id>9;
select * from customers where customer_id<>2;
delete  from customers where  customer_id>=5;
select * from customers;
alter table customers add column year Date;
select * from customers;

-- modify
alter table customers modify year int;

-- update
update customers set   year=2003  where customer_id=1;
update customers set year=2004 where customer_id in (2,3);
update customers set year=1999 where customer_id=4;
select * from customers;
/* between */
select * from customers where  year  between 2001 and 2003;
select * from customers where year between 2003 and 2010;
-- AS
select first_name AS name from customers;
select * from customers;
-- IN
select first_name , last_name from customers where year in (2002,2003); 
 -- MULIPLE VALUES   IN IS USED

select * from customers;
-- IN IS USED TO CHECT NULL AND NOT NULL

select * from customers where year is null;
select* from customers where year is not null;

-- Aggereation Function

select max(year) from customers;
select min(year) from customers;
-- Count to count the number of rows 
select count(*) from customers ; -- entire dataset
-- group by
select year ,count(year) from customers group by year; -- the columns has to depend on it 
select year,count(year) from customers group by  year order by year asc;
select year,count(year) as year_count from customers group by year order by year_count desc;

-- having is used after group by only
select * from customers group by year having year>2002;
/*The query you've written has a syntax issue. In SQL, when using GROUP BY, any column in the SELECT clause must either be:

Included in the GROUP BY clause, or

An aggregate function (like COUNT, SUM, etc.)

Here are corrected versions depending on what you want */

select year,count(*) from customers group by year having year >2002;

commit;


----- joins

create table student1(
stu_id int primary key,
name varchar(100));
create table  student2(
sport_id int primary key ,
amount int,
no_of_students int);
-- adding keys 
alter table student1 add  primary key (stu_id);
insert into student1(stu_id,name)  values(1,'Ronaldo'),
                                 (2,'Mahesh'),
                                 (3,'Vasanthi'),
                                 (4,'Rukmini'),
                                 (5,'Chinni');
select * from student1;                                 
insert into student2 (sport_id,amount,no_of_students) values(1,1000,24),(2,450,400),(3,500,90);
select * from student2;
select student1.stu_id,student1.name,student2.amount,student2.no_of_students from student1 join student2 on student1.stu_id = student2.sport_id;

-- innerjoin--- common column
select student1.stu_id,student1.name,student2.amount,student2.no_of_students from student1 join student2 on student1.stu_id = student2.sport_id;
-- left join -- same columns and left table
select student1.stu_id,student1.name,student2.amount,student2.no_of_students from student1 left join student2 on student1.stu_id = student2.sport_id;

-- right join  same colums and right table

select student1.stu_id,student1.name,student2.amount,student2.no_of_students from student1 right join student2 on student1.stu_id = student2.sport_id;

-- full outer join -- same columns and both the table

select student1.stu_id,student1.name,student2.amount,student2.no_of_students from student1  full outer join student2 on student1.stu_id = student2.sport_id;
-- not supprting 
SELECT 
    student1.stu_id,
    student1.name, 
    student2.amount,
    student2.no_of_students
FROM student1
LEFT JOIN student2 ON student1.stu_id = student2.sport_id

UNION

SELECT 
    student1.stu_id,
    student1.name, 
    student2.amount,
    student2.no_of_students
FROM student1
RIGHT JOIN student2 ON student1.stu_id = student2.sport_id
WHERE student1.stu_id IS NULL;

-- cross join m*n columns 
select student1.stu_id,student1.name,student2.amount ,student2.no_of_students from student1 cross join student2;

-- wild characters %-
select * from student1  where name like 'r%'; -- start with r
select * from student1 where name like '%i';
select * from student1 where name like 'r_______'; -- start with r with specified poistion where it is represent by -
select * from student1 where name like 'R[uo]%'; -- start with r followed by either u or o
SELECT * FROM student1 
WHERE name LIKE 'Ru%' OR name LIKE 'Ro%';

 ---------- THE END ---------------
 