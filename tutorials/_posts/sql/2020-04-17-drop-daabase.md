---
permalink: /sql/حذف-قاعدة-بيانات
layout: post
date: 2020-04-17
title: سلسلة دروس SQL| حذف قاعدة بيانات
type: tutorial
lesson: 37
hidden: true
comments: true
author: husam
---

{% include sql-content.html %}

* Toc
{:toc}

# عبارة DROP DATABASE في SQL

يتم استخدام عبارة DROP DATABASE لحذف قاعدة بيانات موجودة.

# بناء الجملة

{% highlight sql %}

		DROP DATABASE databasename;

{% endhighlight %}

**ملاحظة:** كن حذرا قبل حذف قاعدة البيانات. سيؤدي حذف قاعدة البيانات إلى فقدان المعلومات الكاملة المخزنة في قاعدة البيانات!

# مثال عن DROP DATABASE

تَحذف عبارة SQL التالية قاعدة البيانات الموجودة "testDB":


{% highlight sql %}

DROP DATABASE testDB;

{% endhighlight %}

**نصيحة:** تأكد من امتلاكك صلاحية المشرف قبل حذف أي قاعدة بيانات. بمجرد حذف قاعدة البيانات، يمكنك التحقق من ذلك في قائمة قواعد البيانات باستخدام أمر SQL التالي:

         SHOW DATABASES؛


