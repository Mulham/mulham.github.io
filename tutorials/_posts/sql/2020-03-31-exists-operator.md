---
permalink: /sql/exists
layout: post
date: 2020-03-31
title: سلسلة دروس SQL| عبارة EXISTS
type: tutorial
lesson: 28
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة EXISTS في SQL

تستخدم عبارة EXISTS لاختبار وجود أي سجل في استعلام فرعي.

تُرجع عبارة EXISTS القيمة TRUE (صح) في حال قام الاستعلام الفرعي بإرجاع سجل (نتيجة) واحد أو أكثر.

# بناء عبارة EXISTS

{% highlight sql %}

		SELECT column_name(s)

		FROM table_name

		WHERE EXISTS

		(SELECT column_name FROM table_name WHERE condition); 

{% endhighlight %}

# استعراض قاعدة البيانات

فيما يلي تحديد من جدول "المنتجات" في  قاعدة البيانات النموذجية Northwind:

| ProductID |	ProductName |	SupplierID |	CategoryID |	Unit |	Price |
| --------- | ------------- | -------------- | ---------- | ---------- | ------- |
| 1 	| Chais |	1 |	1 	| 10 boxes x 20 bags |	18 |
| 2 |	Chang |	1 |	1 |	24 - 12 oz bottles |	19 |
| 3 |	Aniseed Syrup |	1 |	2  |	12 - 550 ml bottles  |	10 |
| 4 |	Chef Anton's Cajun Seasoning |	2  |	2  |	48 - 6 oz jars |	22 |
| 5 |	Chef Anton's Gumbo Mix |	2  |	2  |	36 boxes  |	21.35 |

وتحديد من جدول "الموردين":

| SupplierID |	SupplierName |	ContactName |	Address |	City  | PostalCode  |	Country |
| ---------- | ----------- | ------------- | --------- | --------- | --------- | ------------- |
| 1 |	Exotic Liquid |	Charlotte Cooper  |	49 Gilbert St. |	London 	EC1 4SD  |	UK |
| 2 |	New Orleans Cajun Delights |	Shelley Burke |	P.O. Box 78934 |	New Orleans |	70117 |	USA |
| 3 |	Grandma Kelly's Homestead  |	Regina Murphy |	707 Oxford Rd. |	Ann Arbor  |	48104 |	USA |
| 4 |	Tokyo Traders |	Yoshi Nagase |	9-8 Sekimai Musashino-shi |	Tokyo |	100 |	Japan |

# أمثلة عن EXISTS في SQL

تقوم عبارة SQL التالية بإرجاع القيمة TRUE  وتسرد الموردين بسعر منتج أقل من 20:


{% highlight sql %}

		SELECT SupplierName

		FROM Suppliers

		WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20); 

{% endhighlight %}

تقوم عبارة SQL التالية بإرجاع القيمة TRUE وتسرد الموردين بسعر منتج يساوي 22:

{% highlight sql %}

		SELECT SupplierName

		FROM Suppliers

		WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22); 

{% endhighlight %}

