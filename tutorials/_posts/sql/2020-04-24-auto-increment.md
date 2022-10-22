---
permalink: /sql/auto-increment
layout: post
date: 2020-04-24
title: سلسلة دروس SQL| Auto Increment
type: tutorial
lesson: 50
hidden: true
comments: true
author: husam
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

# عبارة SQL AUTO INCREMENT

تسمح الزيادة التلقائية بإنشاء رقم فريد تلقائيًا عند إدراج سجل جديد في جدول.

غالبًا ما يكون هذا هو حقل primary key الذي نود إنشاؤه تلقائيًا في كل مرة يتم فيها إدخال سجل جديد.

# بناء الجملة لـ MySQL

تعرّف عبارة SQL التالية عمود "Personid" ليكون حقل primary key لزيادة تلقائية في جدول "الأشخاص":

{% highlight sql %}

		CREATE TABLE Persons (

		    Personid int NOT NULL AUTO_INCREMENT,

		    LastName varchar(255) NOT NULL,

		    FirstName varchar(255),

		    Age int,

		    PRIMARY KEY (Personid)

		); 

{% endhighlight %}

يستخدم MySQL عبارة AUTO_INCREMENT لإجراء ميزة الزيادة التلقائية.

بشكل افتراضي، تكون قيمة البدء لـAUTO_INCREMENT هي 1 ،وستزيد بمقدار 1 لكل سجل جديد.

لجعل تسلسل AUTO_INCREMENT يبدأ بقيمة أخرى، استخدم عبارة SQL التالية:

{% highlight sql %}

ALTER TABLE Persons AUTO_INCREMENT=100; 

{% endhighlight %}

لإدراج سجل جديد في جدول "الأشخاص"، لن نضطر إلى تحديد قيمة لعمود "الشخص" (ستتم إضافة قيمة فريدة تلقائيًا)

{% highlight sql %}

		INSERT INTO Persons (FirstName,LastName)

		VALUES ('Lars','Monsen'); 

{% endhighlight %}

ستقوم عبارة SQL أعلاه بإدراج سجل جديد في جدول "الأشخاص" و سيتم تعيين قيمة فريدة لعمود "Personi" و سيتم تعيين عمود "الاسم الأول" على "لارس" وسيتم تعيين عمود "الاسم الأخير" على "مونسن".

#بناء جملة SQL Server

تعرّف عبارة SQL التالية عمود "Personid" ليكون حقل primary key للزيادة التلقائية في جدول "الأشخاص":

{% highlight sql %}

		CREATE TABLE Persons (

   		 Personid int IDENTITY(1,1) PRIMARY KEY,

		    LastName varchar(255) NOT NULL,

		    FirstName varchar(255),

		    Age int

		); 

{% endhighlight %}

يستخدم MS SQL Server كلمة IDENTITY لإجراء ميزة الزيادة التلقائية.

في المثال أعلاه ،قيمة البداية لـ IDENTITY هي 1 ،وستزداد بمقدار 1 لكل سجل جديد.

**نصيحة:** لتحديد أنه يجب أن يبدأ عمود "Personid" بالقيمة 10 و يزداد بمقدار 5 قم بتغييره إلى IDENTITY (10،5).

لإدراج سجل جديد في جدول "الأشخاص"، لن نضطر إلى تحديد قيمة لعمود "Personid" (سيتم إضافة قيمة فريدة تلقائيًا):

{% highlight sql %}

		INSERT INTO Persons (FirstName,LastName)

		VALUES ('Lars','Monsen'); 

{% endhighlight %}

ستقوم عبارة SQL أعلاه بإدراج سجل جديد في جدول "الأشخاص". سيتم تعيين قيمة فريدة لعمود "Personid". سيتم تعيين عمود "الاسم الأول" على "لارس" وسيتم تعيين عمود "الاسم الأخير" على "مونسين".

# بناء الجملة في Access

تعرّف عبارة SQL التالية عمود "Personid" ليكون حقل primary key لزيادة تلقائية في جدول "الأشخاص":

{% highlight sql %}

		CREATE TABLE Persons (

		    Personid AUTOINCREMENT PRIMARY KEY,

		    LastName varchar(255) NOT NULL,

		    FirstName varchar(255),

		    Age int

		); 

{% endhighlight %}

يستخدم MS Access الكلمة الأساسية AUTOINCREMENT لإجراء ميزة الزيادة التلقائية.

بشكل افتراضي ، تكون قيمة البدء لـ AUTOINCREMENT  هي 1 ، وستزداد بمقدار 1 لكل سجل جديد.

نصيحة: لتحديد أنه يجب أن يبدأ عمود "Personid" بالقيمة 10 و يزداد بمقدار 5 ، قم بتغيير قيمة AUTOINCREMENT  إلى AUTOINCREMENT (10،5).

لإدراج سجل جديد في جدول "الأشخاص" ، لن نضطر إلى تحديد قيمة لعمود "Personid" (سيتم إضافة قيمة فريدة تلقائيًا):

{% highlight sql %}

		INSERT INTO Persons (FirstName,LastName)

		VALUES ('Lars','Monsen'); 

{% endhighlight %}

ستقوم عبارة SQL أعلاه بإدراج سجل جديد في جدول "الأشخاص". سيتم تعيين قيمة فريدة لعمود "Personid". سيتم تعيين عمود "الاسم الأول" على "لارس" وسيتم تعيين عمود "اسم العائلة" على "مونسين".

# بناء الجملة لOracle

في أوراكل الكود أكثر صعوبة.

سيكون عليك إنشاء حقل زيادة تلقائية باستخدام كائن التسلسل (يقوم هذا الكائن بإنشاء تسلسل رقمي).

استخدم بناء جملة CREATE SEQUENCE التالي:

{% highlight sql %}

CREATE SEQUENCE seq_person

MINVALUE 1

START WITH 1

INCREMENT BY 1

CACHE 10; 

{% endhighlight %}

ينشئ الكود أعلاه كائن تسلسل يسمى seq_person ، يبدأ بـ 1 وسيزداد بمقدار 1. وسيعمل أيضًا على تخزين ما يصل إلى 10 قيم للأداء. يحدد خيار ذاكرة التخزين المؤقت عدد قيم التسلسل التي سيتم تخزينها في الذاكرة للوصول إليها بشكل أسرع.

لإدراج سجل جديد في جدول "الأشخاص" ، سيتعين علينا استخدام دالة nextval (تسترد هذه الوظيفة القيمة التالية من تسلسل seq_person):

{% highlight sql %}

INSERT INTO Persons (Personid,FirstName,LastName)

VALUES (seq_person.nextval,'Lars','Monsen'); 

{% endhighlight %}

ستقوم عبارة SQL أعلاه بإدراج سجل جديد في جدول "الأشخاص". سيتم تعيين الرقم التالي من تسلسل seq_person لعمود "Personid". سيتم تعيين عمود "الاسم الأول" على "لارس" وسيتم تعيين عمود "الاسم الأخير" على "مونسين".

التالي: [التواريخ](التواريخ)
