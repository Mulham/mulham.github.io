---
permalink: /sql/top-limit-rownum
layout: post
date: 2018-05-06
title: سلسلة دروس SQL|TOP-LIMIT-ROWNUM
hidden: true
comments: true
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة SELECT TOP في SQL

تستخدم عبارة SELECT TOP لتحديد عدد القيم المراد استخراجها من قاعدة البيانات (الحصول عليها) ، هذه العبارة مفيدة في حالة الجداول الضخمة التي تحتوي على آلاف القيم، مع ملاحظة أن استخراج عدد كبير من القيم قد يؤثر على الأداء.

> **ملاحظة**: لا تدعم جميع أنظمة قواعد البيانات عبارة SELECT TOP. وبذلك تدعم لغة MySQL العبارة LIMIT لتحديد عدد محدد من القيم، بينما تستخدم Oracle العبارة ROWNUM.

## بناء التصريح في سيرفر SQL أو ميكروسوفت Access

	SELECT TOP number|percent column_name(s)
	FROM table_name
	WHERE condition;

## بناء التصريح في MySQL

	SELECT column_name(s)
	FROM table_name
	WHERE condition
	LIMIT number;

## بناء التصريح في Oracle

	SELECT column_name(s)
	FROM table_name
	WHERE ROWNUM <= number;

# استعراض قاعدة بيانات


في الأسفل تحديد من جدول الزبائن Customers

![customers](/assets/customers.png)

# أمثلة على SQL TOP و LIMIT و ROWNUM

تحدد عبارة SQL التالية أول ثلاث قيم من جدول "Customers":

	SELECT TOP 3 * FROM Customers;

تعرض عبارة SQL التالية المثال نفسه ولكن باستخدام تصريح LIMIT:

	SELECT * FROM Customers
	LIMIT 3;

كما تعرض عبارة SQL التالية المثال نفسه ولكن باستخدام تصريح ROWNUM:

	SELECT * FROM Customers
	WHERE ROWNUM <= 3;

# مثال على SQL TOP PERCENT

تُحدِّد عبارة SQL التالية أول 50% من القيم في جدول "Customers":

	SELECT TOP 50 PERCENT * FROM Customers;

# إضافة تصريح WHERE

تُحدِّد عبارة SQL التالية أول ثلاث قيم من جدول "Customers" حيث البلد هو "Germany":

	SELECT TOP 3 * FROM Customers
	WHERE Country='Germany';

تعرض عبارة SQL التالية المثال نفسه ولكن باستخدام تصريح LIMIT:

	SELECT * FROM Customers
	WHERE Country='Germany'
	LIMIT 3;

كما تعرض عبارة SQL التالية المثال نفسه ولكن باستخدام تصريح ROWNUM:

	SELECT * FROM Customers
	WHERE Country='Germany' AND ROWNUM <= 3;


التالي: [دالات MIN و MAX](min-max)


