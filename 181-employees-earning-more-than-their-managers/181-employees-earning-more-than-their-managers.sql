# Write your MySQL query statement below
select name as "Employee" from  Employee as d where salary>(select (salary) from Employee as n where d.managerId =n.id);