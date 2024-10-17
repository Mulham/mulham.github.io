---
permalink: /sql/select-into
date: 2020-04-13
title: سلسلة دروس SQL| عبارة SELECT INTO
lesson: 30
hidden: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}
## عبارة SELECT INTO في SQL

تقوم عبارة SELECT INTO بنسخ البيانات من جدول واحد إلى جدول جديد.

## بناء جملة SELECT INTO

نسخ كل الأعمدة إلى جدول جديد:

```sql

		SELECT *

		INTO newtable [IN externaldb]

		FROM oldtable

		WHERE condition;

```

نسخ بعض الأعمدة فقط إلى جدول جديد:

```sql


		SELECT column1, column2, column3, ...

		INTO newtable [IN externaldb]

		FROM oldtable

		WHERE condition; 

```

سيتم إنشاء الجدول الجديد باستخدام أسماء الأعمدة وأنواعها كما هو محدد في الجدول القديم. يمكنك إنشاء أسماء أعمدة جديدة باستخدام عبارة AS.

## أمثلة عن SELECT INTO في SQL

تقوم جملة SQL التالية بإنشاء نسخة احتياطية من العملاء:

```sql

		SELECT * INTO CustomersBackup2017

		FROM Customers; 

```

تستخدم جملة SQL التالية عبارة IN لنسخ الجدول إلى جدول جديد في قاعدة بيانات أخرى:

```sql

		SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'

		FROM Customers;

```

تنسخ جملة SQL التالية بضعة أعمدة فقط في جدول جديد:

```sql

		SELECT CustomerName, ContactName INTO CustomersBackup2017

		FROM Customers;
  
```

تقوم عبارة SQL التالية بنسخ العملاء الألمان فقط إلى جدول جديد:

```sql

		SELECT * INTO CustomersGermany

		FROM Customers

		WHERE Country = 'Germany'; 

```

تقوم عبارة SQL التالية بنسخ البيانات من أكثر من جدول إلى جدول جديد:

```sql

		SELECT Customers.CustomerName, Orders.OrderID

		INTO CustomersOrderBackup2017

		FROM Customers

		LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

```

**نصيحة:** يمكن أيضًا استخدام SELECT INTO لإنشاء جدول جديد وفارغ باستخدام مخطط جدول آخر, ما عليك سوى إضافة جملة WHERE التي تؤدي إلى عدم إرجاع الاستعلام لأي بيانات:

```sql

		SELECT * INTO newtable

		FROM oldtable

		WHERE 1 = 0;

```

التالي: [عبارة Insert Into Select ](insert-into-select)
