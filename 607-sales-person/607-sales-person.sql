# Write your MySQL query statement below
select SalesPerson.name from SalesPerson where SalesPerson.sales_id not in (select Orders.sales_id from SalesPerson join Orders on SalesPerson.sales_id=Orders.sales_id join Company on  Orders.com_id=Company.com_id where Company.name='RED'  );
