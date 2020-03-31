---
permalink: /sql/having
layout: post
date: 2020-03-31
title: سلسلة دروس SQL| عبارة HAVING
type: tutorial
lesson: 27
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة HAVING في SQL

تمت إضافة عبارة HAVING إلى SQL لأنه تعذر استخدام عبارة WHERE مع الدالات التجميعية.

## بناء عبارة HAVING

{% highlight sql %}

		SELECT column_name(s)

		FROM table_name

		WHERE condition

		GROUP BY column_name(s)

		HAVING condition

		ORDER BY column_name(s);

{% endhighlight %}

# استعراض قاعدة البيانات

فيما يلي تحديد من جدول "العملاء" في قاعدة البيانات النموذجية Northwind:

| CustomerID |	CustomerName |	ContactName |	Address |	City 	| PostalCode |	Country |
|----------- | ------------ | ------------- | --------- | --------------- | -------- | --------- |
| 1 | Alfreds Futterkiste |	Maria Anders |	Obere Str. 57 |	Berlin |	12209 |	Germany |
| 2 	| Ana Trujillo Emparedados y helados |	Ana Trujillo |	Avda. de la Constitución 2222 |	México D.F. |	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería  |	Antonio Moreno |	Mataderos 2312 |	México D.F. |	05023 |	Mexico |
| 4 | Around the Horn |	Thomas Hardy |	120 Hanover Sq. |	London 	| WA1 1DP |	UK |
| 5 |	Berglunds snabbköp |	Christina Berglund |	Berguvsvägen 8 	| Luleå |	S-958 22 |	Sweden |


# أمثلة عن HAVING في SQL

يسرد بيان SQL التالي عدد العملاء في كل بلد على أن يكون في كل منها أكثر من 5 عملاء:


{% highlight sql %}

		SELECT COUNT(CustomerID), Country

		FROM Customers

		GROUP BY Country

		HAVING COUNT(CustomerID) > 5;

{% endhighlight %}

يسرد بيان SQL التالي عدد العملاء في كل بلد ، مرتبة من الأعلى إلى الأسفل (يتضمن فقط البلدان التي بها أكثر من 5 عملاء):


{% highlight sql %}

		SELECT COUNT(CustomerID), Country

		FROM Customers

		GROUP BY Country

		HAVING COUNT(CustomerID) > 5

		ORDER BY COUNT(CustomerID) DESC;

{% endhighlight %}

# استعراض قاعدة البيانات

فيما يلي تحديد من جدول "الطلبات" في قاعدة البيانات النموذجية Northwind:

| OrderID |	CustomerID |	EmployeeID |	OrderDate |	ShipperID |
| ------- | --------------- | ---------- | -------------- | ------------- |
| 10248 |	90 |	5 |	1996-07-04 |	3 |
| 10249  |	81 |	6 |	1996-07-05 |	1 |
| 10250  |	34 |	4 |	1996-07-08 |	2 |

وتحديد من جدول "الموظفين":

| EmployeeID |	LastName |	FirstName |	BirthDate |	Photo 	Notes |
| ---------- | ---------- | ------------- | ------------ | ---------------- |
| 1 |	Davolio |	Nancy |	1968-12-08 |	EmpID1.pic |	Education includes a BA.... |
| 2 |	Fuller 	Andrew |	1952-02-19 |	EmpID2.pic |	Andrew received his BTS.... |
| 3 |	Leverling |	Janet |	1963-08-30 |	EmpID3.pic |	Janet has a BS degree.... |

# أمثلة أخرى عن HAVING

يسرد بيان SQL التالي الموظفين الذين سجلوا أكثر من 10 طلبات:


{% highlight sql %}

		SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders

		FROM (Orders

		INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)

		GROUP BY LastName

		HAVING COUNT(Orders.OrderID) > 10;

{% endhighlight %}

تسرد عبارة SQL التالية ما إذا كان الموظفون "Davolio" أو "Fuller" قد سجلوا أكثر من 25 طلبًا:

{% highlight sql %}

		SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders

		FROM Orders

		INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID

		WHERE LastName = 'Davolio' OR LastName = 'Fuller'

		GROUP BY LastName

		HAVING COUNT(Orders.OrderID) > 25;

{% endhighlight %}

التالي: [عامل Exists ](exists)
