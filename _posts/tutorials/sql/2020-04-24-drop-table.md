---
permalink: /sql/حذف-جدول
layout: post
date: 2020-04-24
title: سلسلة دروس SQL| حذف جدول
type: tutorial
lesson: 40
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

## عبارة DROP TABLE في SQL

يتم استخدام عبارة DROP TABLE لحذف جدول موجود في قاعدة بيانات.

## بناء العبارة

```sql

DROP TABLE table_name; 

```

**ملاحظة:** كن حذرا قبل حذف جدول. سيؤدي حذف جدول إلى فقدان المعلومات الكاملة المخزنة في الجدول!

## مثال عن DROP TABLE في SQL

تَحذف عبارة SQL التالية الجدول الحالي "Shippers":

**مثال**

```sql

		DROP TABLE Shippers;

```

## اقتطاع الجدول في SQL

يتم استخدام العبارة TRUNCATE TABLE لحذف البيانات داخل جدول، ولكن ليس الجدول نفسه.



```sql

		TRUNCATE TABLE table_name; 

```

التالي: [تعديل جدول](تعديل-جدول)
