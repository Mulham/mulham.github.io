---
permalink: /sql/right_join
layout: post
date: 2020-03-27
title: سلسلة دروس SQL| عبارة RIGHT JOIN
type: tutorial
lesson: 22
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة RIGHT JOIN في SQL

تُرجع العبارة RIGHT JOIN كافة السجلات من الجدول الأيمن (الجدول 2)، والسجلات المتطابقة من الجدول الأيسر (الجدول 1). والنتيجة هي صفر من الجانب الأيسر، عندما لا يكون هناك تطابق.


# بناء جملة RIGHT JOIN

{% highlight sql %}

        SELECT column_name(s)

        FROM table1

        RIGHT JOIN table2

        ON table1.column_name = table2.column_name;

{% endhighlight %}

**ملاحظة:** نستعمل في بعض قواعد البيانات  عبارة RIGHT OUTER JOIN بدلا من عبارة RIGHT JOIN.

<amp-img layout="responsive" src="/assets/sql_rightjoin.gif" alt="عبارة left join sql" width="200" height="145"></amp-img>

# استعراض قاعدة البيانات

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

# مثال عن SQL RIGHT JOIN

سترجع عبارة SQL التالية جميع الموظفين مع طلباتهم:


{% highlight sql %}

        SELECT Orders.OrderID, Employees.LastName, Employees.FirstName

        FROM Orders

        RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID

        ORDER BY Orders.OrderID;

{% endhighlight %}

**ملاحظة:** تُرجع العبارة RIGHT JOIN جميع السجلات من الجدول الأيمن (الموظفون) ، حتى إذا لم تكن هناك تطابقات في الجدول الأيسر (الطلبات).


