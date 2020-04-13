---
permalink: /sql/insert-into-select
layout: post
date: 2020-04-13
title: سلسلة دروس SQL| عبارة Insert Into Select
type: tutorial
lesson: 31
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة INSERT INTO SELECT في SQL

تقوم عبارة INSERT INTO SELECT بنسخ البيانات من جدول واحد وإدراجها في جدول آخر.


* يتطلب INSERT INTO SELECT تطابق أنواع البيانات في جداول كل من المصدر والهدف

* لا تتأثر السجلات الموجودة في جدول الهدف

# بناء جملة INSERT INTO SELECT

انسخ جميع الأعمدة من جدول إلى جدول آخر:

{% highlight sql %}

		INSERT INTO table2

		SELECT * FROM table1

		WHERE condition;

{% endhighlight %}

انسخ بعض الأعمدة فقط من جدول واحد إلى جدول آخر:

{% endhighlight %}

		INSERT INTO table2 (column1, column2, column3, ...)

		SELECT column1, column2, column3, ...

		FROM table1

		WHERE condition; 

{% endhighlight %}

# استعراض قاعدة البيانات

فيما يلي  مجموعة مختارة من جدول "العملاء"في قاعدة البيانات النموذجية Northwind:


| CustomerID |	CustomerName |	ContactName |	Address |	City |	PostalCode |	Country |
| --------- | ------------- | ------------   | -------- | ----------- | --------- | ----------- |
| 1 | Alfreds Futterkiste |	Maria Anders |	Obere Str. 57 |	Berlin |	12209 |	Germany |
| 2 |	Ana Trujillo Emparedados y helados |	Ana Trujillo |	Avda. de la Constitución| 2222 | México D.F. |	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería  |	Antonio Moreno |	Mataderos 2312 |	México D.F. |	05023 |	Mexico |

واختيار من جدول "الموردين":

| SupplierID |	SupplierName |	ContactName |	Address  |	City |	Postal Code |	Country |
| ---------- | ------------- | ------------- | --------- | ----------- | ---------- | --------- |
| 1 |	Exotic Liquid |	Charlotte Cooper |	49 Gilbert St. |	Londona |	EC1 4SD |	UK |
| 2 |	New Orleans Cajun Delights |	Shelley Burke |	P.O. Box 78934 |	New Orleans |	70117 |	USA |
| 3 |	Grandma Kelly's Homestead |	Regina Murphy |	707 Oxford Rd. |	Ann Arbor |	48104 |	USA |

# أمثلة عن INSERT INTO SELECT في SQL

تقوم عبارة SQL التالية بنسخ "الموردين" إلى "العملاء" (ستحتوي الأعمدة التي لم يتم تعبئتها بالبيانات على NULL):


{% highlight sql %}

		INSERT INTO Customers (CustomerName, City, Country)

		SELECT SupplierName, City, Country FROM Suppliers;

{% endhighlight %}

تقوم جملة SQL التالية بنسخ "الموردين" إلى "العملاء" (املأ جميع الأعمدة):

{% endhighlight %}

		INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)

		SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;

{% endhighlight %}

تقوم عبارة SQL التالية بنسخ الموردين الألمان فقط إلى "العملاء":


{% highlight sql %}

		INSERT INTO Customers (CustomerName, City, Country)

		SELECT SupplierName, City, Country FROM Suppliers

		WHERE Country='Germany';

{% endhighlight %}


