---
layout: post
date: 2016-06-18
title: سلسلة دروس SQL|تصريح SELECT DISTINCT
---

الفهرس :


الدرس الأول : التعريف بـ SQL

الدرس الثاني : بناء SQL

الدرس الثالث : تصريح SELECT

الدرس الرابع : تصريح تحديد الاختلاف في SQL

الدرس الخامس : عبارة WHERE في SQL

الدرس السادس : عمليات AND & OR في SQL

الدرس السابع : دالة ORDER BY في SQL

الدرس الثامن: تصريح INSERT INTO في SQL

الدرس التاسع: تصريح UPDATE في SQL

الدرس العاشر: تصريح DELETE في SQL

*****************

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

![](http://1.bp.blogspot.com/-txe3CmsAcew/VODvNYC9AII/AAAAAAAABpc/-n-9ly6Kz74/s1600/Screenshot%2Bfrom%2B2015-02-15%2B21%3A09%3A44.png)

# مثال لتصريح SELECT DISTINCT


تصريح SQL التالي يحدد القيم المختلفة فقط من عمود City في جدول الزبائن Customers 

        SELECT DISTINCT City FROM Customers;


التالي: [عبارة WHERE](where)
