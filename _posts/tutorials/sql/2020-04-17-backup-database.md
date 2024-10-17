---
permalink: /sql/نسخ-قاعدة-بيانات
date: 2020-04-17
title: سلسلة دروس SQL| نسخ قاعدة بيانات
lesson: 38
hidden: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

## عبارة BACKUP DATABASE في SQL

يتم استخدام عبارة BACKUP DATABASE في SQL Server لإنشاء نسخة احتياطية كاملة من قاعدة بيانات SQL الموجودة.


```sql

		BACKUP DATABASE databasename

		TO DISK = 'filepath'; 

```

## عبارة BACKUP WITH DIFFERENTIAL في SQL "النسخ الاحتياطي التفاضلي"


يقوم النسخ الاحتياطي التفاضلي (أو التمايزي/الاختلافي) بنسخ فقط أجزاء قاعدة البيانات التي تغيرت منذ آخر نسخة احتياطية كاملة لها.



```sql

		BACKUP DATABASE databasename
		TO DISK = 'filepath'
		WITH DIFFERENTIAL; 

```

## مثال عن BACKUP DATABASE في SQL

تقوم جملة SQL التالية بإنشاء نسخة احتياطية كاملة لقاعدة البيانات الموجودة "testDB" إلى القرص D:

```sql

		BACKUP DATABASE testDB

		TO DISK = 'D:\backups\testDB.bak'; 

```

**تلميح:** قم دائمًا بنسخ قاعدة البيانات احتياطيًا إلى محرك أقراص مختلف عن محرك الأقراص الفعلي. بعد ذلك، إذا حدث عطل في القرص، فلن تفقد ملف النسخ الاحتياطي مع قاعدة البيانات.

التالي: [إنشاء-جدول](إنشاء-جدول)

