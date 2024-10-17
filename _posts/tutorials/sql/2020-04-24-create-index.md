---
permalink: /sql/create-index
layout: post
date: 2020-04-24
title: سلسلة دروس SQL| Create Index
type: tutorial
lesson: 49
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}


## عبارة SQL  CREATE INDEX

يتم استخدام عبارة CREATE INDEX لإنشاء فهارس في الجداول.

يتم استخدام الفهارس لاسترداد البيانات من قاعدة البيانات بشكل أسرع من غير ذلك. لا يمكن للمستخدمين رؤية الفهارس ،يتم استخدامها فقط لتسريع عمليات البحث / الاستعلامات.

**ملاحظة:** تحديث الجدول باستخدام الفهارس يستغرق وقتًا أطول من تحديث الجدول بدون (لأن الفهارس تحتاج أيضًا إلى تحديث). لذا، قم فقط بإنشاء فهارس على الأعمدة التي سيتم البحث عنها بشكل متكرر.

## بناء جملة CREATE INDEX

إنشاء فهرس على جدول يسمح بقيم مكررة:

```sql

		CREATE INDEX index_name

		ON table_name (column1, column2, ...); 

```

## بناء جملة CREATE UNIQUE INDEX

إنشاء فهرس فريد على جدول. القيم المكررة غير مسموح بها:

```sql

		CREATE UNIQUE INDEX index_name

		ON table_name (column1, column2, ...); 

```

**ملاحظة:** تختلف بنية إنشاء الفهارس بين قواعد البيانات المختلفة. لذلك: تحقق من بناء الجملة لإنشاء فهارس في قاعدة البيانات الخاصة بك.

## مثال عن CREATE INDEX

تقوم جملة SQL أدناه بإنشاء فهرس باسم "idx_lastname" في عمود "اسم العائلة" في جدول "الأشخاص":

```sql

		CREATE INDEX idx_lastname

		ON Persons (LastName); 

```

إذا كنت تريد إنشاء فهرس على مجموعة من الأعمدة، يمكنك إدراج أسماء الأعمدة داخل الأقواس، مفصولة بفواصل:

```sql

		CREATE INDEX idx_pname

		ON Persons (LastName, FirstName); 

```

## حذف عبارةINDEX

يتم استخدام عبارة DROP INDEX لحذف فهرس في جدول.

**MS Access:**

```sql

DROP INDEX index_name ON table_name; 

```

**SQL Server:**

```sql

DROP INDEX table_name.index_name; 

```

**DB2/Oracle:**

```sql

DROP INDEX index_name; 

```

**MySQL:**

```sql

		ALTER TABLE table_name

		DROP INDEX index_name; 

```


التالي: [Auto Increment](auto-increment)
