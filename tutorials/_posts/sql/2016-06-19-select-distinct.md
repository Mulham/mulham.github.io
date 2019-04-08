---
permalink: /sql/select-distinct
layout: post
date: 2016-06-18
title: سلسلة دروس SQL|تصريح SELECT DISTINCT
hidden: true
type: tutorial
comments: true
---

{% include sql-content.html %}

يستخدم تصريح `SELECT DISTINCT` للحصول على القيم المختلفة فقط .

* Toc
{:toc}

# تصريح SELECT DISTINCT


إن عمود ما في جدول قد يحوي  على قيم متطابقة ، ولذلك قد تريد في بعض الأحيان عرض القيم المختلفة فقط .

عبارة `DISTINCT` يمكن أن تستخدم لاستدعاء القيم المختلفة فقط .


# بناء تصريح SELECT DISTINCT


        SELECT DISTINCT column_name,column_name

        FROM table_name;


# استعراض قاعدة بيانات


سنستخدم في هذا الشرح قاعدة البيانات المعروفة جيداً `Northwind`


في الأسفل تحديد من جدول الزبائن `Customers`

![customers](/assets/customers.png)

# مثال لتصريح SELECT DISTINCT


تصريح SQL التالي يحدد القيم المختلفة فقط من عمود City في جدول الزبائن Customers 

        SELECT DISTINCT City FROM Customers;


التالي: [عبارة WHERE](where)
