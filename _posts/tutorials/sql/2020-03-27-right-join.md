---
permalink: /sql/right_join
date: 2020-03-27
title: سلسلة دروس SQL| عبارة RIGHT JOIN
lesson: 22
hidden: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

## عبارة RIGHT JOIN في SQL

تُرجع العبارة RIGHT JOIN كافة السجلات من الجدول الأيمن (الجدول 2)، والسجلات المتطابقة من الجدول الأيسر (الجدول 1). والنتيجة هي صفر من الجانب الأيسر، عندما لا يكون هناك تطابق.


## بناء جملة RIGHT JOIN

```sql

        SELECT column_name(s)

        FROM table1

        RIGHT JOIN table2

        ON table1.column_name = table2.column_name;

```

**ملاحظة:** نستعمل في بعض قواعد البيانات  عبارة RIGHT OUTER JOIN بدلا من عبارة RIGHT JOIN.

![عبارة right join sql](/assets/sql_rightjoin.gif)


## استعراض قاعدة البيانات

سنستخدم في هذا الدرس قاعدة البيانات النموذجية المعروفة Northwind.

فيما يلي تحديد من جدول "الطلبات":


|OrderID |	CustomerID 	| EmployeeID 	| OrderDate |	ShipperID |
|-----------| ---------- | ----------- | ------- |  ------- |
| 10308 |	2 |	7 	| 1996-09-18 |	3 |
| 10309 	| 37 	| 3 |	1996-09-19 	| 1 |
| 10310 |	77 |	8 	| 1996-09-20 |	2 |

وتحديد من جدول "الموظفين":


| EmployeeID |	LastName |	FirstName |	BirthDate |	Photo |
| ---------- | --------- | --------- | --------- | ------ |
| 1 |	Davolio |	Nancy |	12/8/1968 |	EmpID1.pic |
| 2 |	Fuller |	Andrew |	2/19/1952 |	EmpID2.pic |
| 3 |	Leverling |	Janet |	8/30/1963 |	EmpID3.pic |

## مثال عن RIGHT JOIN

ستُرجع عبارة SQL التالية جميع الموظفين مع طلباتهم:


```sql

        SELECT Orders.OrderID, Employees.LastName, Employees.FirstName

        FROM Orders

        RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID

        ORDER BY Orders.OrderID;

```

**ملاحظة:** تُرجع العبارة RIGHT JOIN جميع السجلات من الجدول الأيمن (الموظفون) ، حتى إن لم تكن هناك تطابقات في الجدول الأيسر (الطلبات).

التالي: [عبارة FULL JOIN ](full_join)

