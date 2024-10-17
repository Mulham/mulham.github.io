---
permalink: /sql/inner_join
date: 2020-03-25
title: سلسلة دروس SQL| عبارة INNER JOIN
lesson: 20
hidden: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}


## عبارة INNER JOIN في SQL 


العبارة `INNER JOIN` تُسجّل القيم المتطابقة في كلا الجدولين 

بناء عبارة INNER JOIN

```sql

		SELECT column_name(s)
        FROM table1
        INNER JOIN table2
        ON table1.column_name = table2.column_name;

```

![عبارة inner join sql](/assets/sql_inner-join.gif)


## استعراض قاعدة البيانات

سنستخدم قاعدة البيانات النموذجية Northwind المعروفة.

فيما يلي تحديد من جدول "Orders":

| OrderID |  	CustomerID |	EmployeeID |	OrderDate |	ShipperID |
| --------- | ------------------- | ------------------ | -------------- | ------------ |
| 10308 |	2 	| 7 |	1996-09-18 |	3 |
| 10309 	| 37 |	3 	| 1996-09-19 	| 1 |
| 10310 |	77 |	8 |	1996-09-20 |	2 |

وتحديد من جدول "Customers":

| CustomerID |	CustomerName |	ContactName |	Address |	City |	PostalCode |	Country |
| ------------- | -------------------------------- | ----------------- | ---------------- | ------ | ------------------- | ------------- | 
| 1 | Alfreds Futterkiste |	Maria Anders |	Obere Str. 57 | 	Berlin  |	12209 | 	Germany |
| 2 |	Ana Trujillo Emparedados y helados |	Ana Trujillo |	Avda. de la Constitución 2222 |	México D.F. |	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería |	Antonio Moreno |	Mataderos 2312 |	México D.F.  | 	05023  | 	Mexico |

## مثال  على INNER JOIN

تُحدِّد عبارة SQL التالية جميع الطلبات التي تحتوي على معلومات العملاء:

```sql

		SELECT column_name(s)
        FROM table1
        INNER JOIN table2
        ON table1.column_name = table2.column_name;

```

**ملاحظة:** يحدد الكود INNER JOIN جميع الصفوف من كلا الجدولين طالما هناك تطابق بين الأعمدة. إذا كانت هناك سجلات في جدول "الطلبات" لا تحتوي على تطابقات في "العملاء" ، فلن يتم عرض هذه الطلبات!

## ربط ثلاثة جداول

تحدد عبارة SQL التالية جميع الطلبات التي تحتوي على معلومات العميل والمرسل:

```sql

		SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
        FROM ((Orders
        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
        INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID); 

```


التالي: [عبارة LEFT JOIN](left_join)

