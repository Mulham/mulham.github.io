---
permalink: /sql/inner_join
layout: post
date: 2020-03-25
title: سلسلة دروس SQL| عبارة INNER JOIN
type: tutorial
lesson: 20
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}


# عبارة INNER JOIN في SQL 


العبارة `INNER JOIN` تُسجّل القيم المتطابقة في كلا الجدولين 

بناء عبارة INNER JOIN
{% highlight sql %}

		SELECT column_name(s)
        FROM table1
        INNER JOIN table2
        ON table1.column_name = table2.column_name;

{% endhighlight %}

<amp-img layout="responsive" src="/assets/sql_inner-join.gif" alt="عبارة inner join sql" width="200" height="145"></amp-img>

# استعراض قاعدة البيانات

سنستخدم قاعدة البيانات النموذجية Northwind المعروفة.

فيما يلي تحديد من جدول "Orders":

| OrderID |  	CustomerID |	EmployeeID |	OrderDate |	ShipperID |
| --------- | ------------------- | ------------------ | -------------- | ------------ |
| 10308 |	2 	| 7 |	1996-09-18 |	3 |
| 10309 	| 37 |	3 	| 1996-09-19 	| 1 |
| 10310 |	77 |	8 |	1996-09-20 |	2 |

و تحديد من جدول "Customers":

| CustomerID |	CustomerName |	ContactName |	Address |	City |	PostalCode |	Country |
| ------------- | -------------------------------- | ----------------- | ---------------- | ------ | ------------------- | ------------- | 
| 1 | Alfreds Futterkiste |	Maria Anders |	Obere Str. 57 | 	Berlin  |	12209 | 	Germany |
| 2 |	Ana Trujillo Emparedados y helados |	Ana Trujillo |	Avda. de la Constitución 2222 |	México D.F. |	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería |	Antonio Moreno |	Mataderos 2312 |	México D.F.  | 	05023  | 	Mexico |

# مثال  على INNER JOIN

تُحدِّد عبارة SQL التالية جميع الطلبات التي تحتوي على معلومات العملاء:

{% highlight sql %}

		SELECT column_name(s)
        FROM table1
        INNER JOIN table2
        ON table1.column_name = table2.column_name;

{% endhighlight %}

**ملاحظة:** يحدد الكود INNER JOIN جميع الصفوف من كلا الجدولين طالما هناك تطابق بين الأعمدة. إذا كانت هناك سجلات في جدول "الطلبات" لا تحتوي على تطابقات في "العملاء" ، فلن يتم عرض هذه الطلبات!

# ربط ثلاثة جداول

تحدد عبارة SQL التالية جميع الطلبات التي تحتوي على معلومات العميل والمرسل:

{% highlight sql %}

		SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
        FROM ((Orders
        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
        INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID); 

{% endhighlight %}


التالي: [عبارة LEFT JOIN](left_join)

