---
permalink: /sql/full_join
layout: post
date: 2020-03-27
title: سلسلة دروس SQL| عبارة FULL OUTER JOIN
type: tutorial
lesson: 23
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

# عبارة FULL OUTER JOIN في SQL

تُرجع العبارة FULL OUTER JOIN كافة السجلات عندما يكون هناك تطابق في سجلات الجدول الأيسر (الجدول 1) أو الأيمن (الجدول 2).

**ملاحظة:** من المحتمل أن يرجع FULL OUTER JOIN مجموعات نتائج كبيرة جدًا!

<amp-img src="/assets/sql_full-join.gif" alt="عبارة full join sql" width="100" height="72"></amp-img>

# بناء جملة FULL OUTER JOIN

{% highlight sql %}

        SELECT column_name(s)

        FROM table1

        FULL OUTER JOIN table2

        ON table1.column_name = table2.column_name

        WHERE condition; 

{% endhighlight %}


# استعراض قاعدة البيانات

سنستخدم في هذا الدرس قاعدة البيانات النموذجية المعروفة Northwind.

فيما يلي مجموعة مختارة من جدول "العملاء":

| CustomerID |	CustomerName |	ContactName |	Address |	City |	PostalCode |	Country |
|---------- | ------------- | ------------ | ---------- | ------ | ---------- | ---------- |
| 1 | Alfreds Futterkiste |	Maria Anders |	Obere Str. 57 | 	Berlin 	| 12209 	| Germany
| 2 |	Ana Trujillo Emparedados y helados | 	Ana Trujillo |	Avda. de la Constitución 2222 |	México D.F. |	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería 	| Antonio Moreno |	Mataderos 2312 |	México D.F. |	05023 |	Mexico |

ومجموعة مختارة من جدول "الطلبات":

| OrderID |	CustomerID | 	EmployeeID |	OrderDate |	ShipperID |
|---------- | --------- | ----------- | ------------- | -------- |
| 10308 |	2 |	7 |	1996-09-18 |	3 |
| 10309 |	37 	| 3 |	1996-09-19 |	1 |
| 10310 |	77 |	8 |	1996-09-20 |	2 |

# مثال عن FULL OUTER JOIN في SQL

تحدد عبارة SQL التالية جميع العملاء وجميع الطلبات:


{% highlight sql %}

        SELECT Customers.CustomerName, Orders.OrderID

        FROM Customers

        FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID

        ORDER BY Customers.CustomerName;

{% endhighlight %}

قد تبدو النتائج كما يلي:

| CustomerName |	OrderID |
| ------------- | --------- |
| Alfreds Futterkiste |	Null |
| Ana Trujillo Emparedados y helados |	10308 |
| Antonio Moreno Taquería 	| 10365 |

**ملاحظة:** ترجع العبارة FULL OUTER JOIN جميع السجلات المطابقة من كلا الجدولين سواء كان الجدول الآخر يطابق أم لا. لذا، إذا كانت هناك صفوف في "العملاء" لا تحتوي على تطابقات في "الطلبات"، أو إذا كانت هناك صفوف في "الطلبات" لا تحتوي على تطابقات في "العملاء"، فسيتم إدراج هذه الصفوف أيضًا.

التالي: [عبارة SELF JOIN ](self_join)
