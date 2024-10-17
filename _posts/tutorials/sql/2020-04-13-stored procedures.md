---
permalink: /sql/stored_procedures
date: 2020-04-13
title: سلسلة دروس SQL| الإجراءات المخزنة
lesson: 34
hidden: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

## إجراءات SQL المخزنة لـ SQL Server

## ما هو الإجراء المخزن؟

الإجراء المُخَزَّن هو كود SQL جاهز يمكنك حفظه، بحيث يمكن إعادة استخدام الرمز مرارًا وتكرارًا.

لذا إذا كان لديك استعلام SQL تكتبه مرارًا وتكرارًا، فاحفظه كإجراء مخزن، ثم قم باستدعائه فقط لتنفيذه.

يمكنك أيضًا تمرير المعاملات (parameters) إلى إجراء مخزن، بحيث يمكن أن يعمل الإجراء المخزن بناءً على قيمة أو قيم المعاملات التي تم تمريرها.


## بناء جملة الإجراء المخزن

```sql

		CREATE PROCEDURE procedure_name

		AS

		sql_statement

		GO; 

```

## تنفيذ إجراء مخزّن

```sql

		EXEC procedure_name;

```

## استعراض قاعدة البيانات

فيما يلي تحديد من جدول "العملاء" في قاعدة البيانات النموذجية Northwind:

| CustomerID |	CustomerName |	ContactName |	Address |	City |	PostalCode |	Country |
|----------- | --------------- | ---------- | -------- | ---------- | ------------ | --------- |
| 1 | Alfreds Futterkiste |	Maria Anders |	Obere Str. 57 |	Berlin 	| 12209 |	Germany |
| 2 |	Ana Trujillo Emparedados y helados |	Ana Trujillo |	Avda. de la Constitución 2222 |	México D.F. |	05021 |	Mexico |
| 3 |	Antonio Moreno Taquería |	Antonio Moreno |	Mataderos 2312 |	México D.F. |	05023 |	Mexico |
| 4 | Around the Horn |	Thomas Hardy 	| 120 Hanover Sq. |	London 	WA1 1DP |	UK |
| 5 |	Berglunds snabbköp |	Christina Berglund |	Berguvsvägen 8 |	Luleå |	S-958 22 |	Sweden |

## مثال عن الإجراء المخزن

تقوم جملة SQL التالية بإنشاء إجراء مخزن باسم "SelectAllCustomers" والذي يحدد كافة السجلات من جدول "العملاء":


```sql

		CREATE PROCEDURE SelectAllCustomers

		AS

		SELECT * FROM Customers

		GO;

```

نفِّذ الإجراء المخزن أعلاه على النحو التالي:

```sql

		EXEC SelectAllCustomers;

```

## الإجراء المخزن مع معلمة واحدة

تقوم جملة SQL التالية بإنشاء إجراء مخزن يحدد العملاء من مدينة معينة من جدول "العملاء":


```sql

		CREATE PROCEDURE SelectAllCustomers @City nvarchar(30)

		AS

		SELECT * FROM Customers WHERE City = @City

		GO;

```

نفذ الإجراء المخزن أعلاه على النحو التالي:


```sql

		EXEC SelectAllCustomers @City = 'London'; 

```

## الإجراء المخزن مع معلمات متعددة

من السهل جدًا إعداد معلمات متعددة. ما عليك سوى إدراج كل معلمة ونوع البيانات مفصولة بفواصل كما هو موضح أدناه.

تقوم جملة SQL التالية بإنشاء إجراء مخزن يحدد العملاء من مدينة معينة برمز بريدي معين من جدول "العملاء":

```sql

		CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)

		AS

		SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode

		GO;

```

نفذ الإجراء المخزن أعلاه على النحو التالي:


```sql

EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP'; 

```

التالي: [التعليقات](comments)

