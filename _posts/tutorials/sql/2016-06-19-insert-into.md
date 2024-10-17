---
permalink: /sql/insert-into
date: 2016-06-19
title: سلسلة دروس SQL|تصريح INSERT INTO
hidden: true
lesson: 8
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

يستخدم تصريح INSERT INTO لإدراج تسجيلات جديدة في جدول.



## بناء INSERT INTO


من الممكن كتابة تصريح INSERT INTO بشكلين مختلفين.


* الشكل الأول لا يحدد أسماء الأعمدة التي ستدرج البيانات بداخلها، بل يحدد القيم التي سيتم إدراجها فقط


		INSERT INTO table_name

		VALUES (value1,value2,value3,...);

* الشكل الثاني يحد كلاً من أسماء الأعمدة والقيم التي سيتم إدراجها


		INSERT INTO table_name (column1,column2,column3,...)

		VALUES (value1,value2,value3,...);


## استعراض قاعدة بيانات 



سنستخدم قاعدة البيانات المعروفة جيداً: Northwind


في الأسفل تحديد من جدول الزبائن Customers

![دروس SQL](/assets/customers.png)


## مثال على INSERT INTO


على افتراض أننا نريد إدراج صف جديد في جدول الزبائن ، فيمكننا استخدام تصريح SQL التالي لذلك


		INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)

		VALUES ('Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway'); 

الآن ، سيبدو التحديد من جدول الزبائن على الشكل التالي

![دروس SQL](/assets/customers1.png)


هل لاحظت أننا لم نقم بإدراج أي رقم في حقل CustomerID؟

إن عمود CustomerID يتم تحديثه بشكل تلقائي برقم تعدادي لكل تسجيل في الجدول.


# إدراج بيانات في جداول محددة فقط


من الممكن أيضاً إدراج بيانات في جداول محددة فقط.


تصريح SQL التالي سيقوم بإدراج صف جديد ، ولكن سيدرج بيانات فقط في الأعمدة CustomerName , City , Country ( وبالطبع حقل CustomerID سيتم تحديثه تلقائياً ) 


		INSERT INTO Customers (CustomerName, City, Country)

		VALUES ('Cardinal', 'Stavanger', 'Norway');

الآن ، سيبدو التحديد من جدول الزبائن على الشكل التالي

![دروس SQL](/assets/customers2.png)


التالي: [تصريح UPDATE](update)
