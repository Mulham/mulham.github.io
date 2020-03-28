---
permalink: /sql/left_join
layout: post
date: 2020-03-25
title: سلسلة دروس SQL| عبارة LEFT JOIN
type: tutorial
lesson: 21
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}



# عبارة LEFT JOIN في SQL  

يرجع الكود LEFT JOIN كافة السجلات من الجدول الأيسر (الجدول 1) ، والسجلات المتطابقة من الجدول الأيمن (الجدول 2). والنتيجة هي صفر من الجانب الأيمن، إذا لم يكن هناك تطابق.

**بناء جملة LEFT JOIN**

        SELECT column_name(s)
        FROM table1
        LEFT JOIN table2
        ON table1.column_name = table2.column_name;

**ملاحظة:** في بعض قواعد البيانات نستعمل LEFT OUTER JOIN بدلا من LEFT JOIN .

<amp-img src="/assets/sql_left-join.gif" alt="عبارة left join sql" width="200" height="145"></amp-img>

# استعراض قاعدة البيانات

سنستخدم قاعدة البيانات النموذجية Northwind المعروفة.

فيما يلي تحديد من جدول "العملاء":


| CustomerID |	CustomerName |	ContactName 	| Address | 	City 	| PostalCode 	| Country |
| -------------- | --------------- | ------------------ | ------------- | -------------- | ---------------- | ------------------ |
| 1 |  Alfreds Futterkiste 	| Maria Anders |	Obere Str. 57 	| Berlin |	12209  |	Germany |
| 2 | 	Ana Trujillo Emparedados y helados |  	Ana Trujillo |	Avda. de la Constitución 2222  | 	México D.F. | 	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería |	Antonio Moreno  | 	Mataderos 2312 |	México D.F. 	| 05023 	| Mexico |


و مجموعة من جدول "الطلبات":


| OrderID |	CustomerID 	| EmployeeID | 	OrderDate  |	ShipperID |
|----------- | ---------------------- | ----------------- | ------------------- | ---------------- |
| 10308 |  	2  | 	7  |	1996-09-18 	 | 3 |
| 10309 |	37 |	3 |	1996-09-19 |	1 |
| 10310 |	77 | 	8 	| 1996-09-20 	 | 2 |


# مثال  على LEFT JOIN

ستحدد عبارة SQL التالية جميع العملاء و طلباتهم 


		SELECT Customers.CustomerName, Orders.OrderID
        FROM Customers
        LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
        ORDER BY Customers.CustomerName;

**ملاحظة:** يُرجع الكود LEFT JOIN جميع السجلات من الجدول الأيسر (العملاء)، حتى في حالة عدم وجود تطابقات في الجدول الأيمن (الطلبات).


التالي: [عبارة RIGHT JOIN ](right_join)

