---
permalink: /sql/count-avg-sum
layout: post
date: 2018-05-09
title: سلسلة دروس SQL|دالات COUNT و AVG و SUM
hidden: true
type: tutorial
lesson: 13
comments: true
---

هذه المقالة جزء من سلسلة دروس SQL، يمكنك الاطلاع على [الفهرس](intro)

* Toc
{:toc}

# دالّات COUNT() و AVG() و SUM() في SQL

تُعطي دالة COUNT() عدد الأسطر من جدول ما والتي تُطابق معيار محدد.

وتُعطي دالة AVG() القيمة المتوسطة لعمود رقمي (يحوي أرقام).

كما تُعطي دالة SUM() المجموع الكُلّي لعمود رقمي.

# استخدام دالة COUNT()

	SELECT COUNT(column_name)
	FROM table_name
	WHERE condition;


# استخدام دالة AVG()

	SELECT AVG(column_name)
	FROM table_name
	WHERE condition;

# استخدام دالة SUM()

	SELECT SUM(column_name)
	FROM table_name
	WHERE condition;

# استعراض قاعدة البيانات

في الأسفل تحديد من جدول "Products" (المنتجات) في قاعدة البيانات النموذجية Northwind


|ProductID |	ProductName	| SupplierID	| CategoryID	| Unit	| Price|
|----------|--------------------|----------------|------------|------|-------|
|1	| Chais	| 1	| 1	| 10 boxes x 20 bags	| 18
|2	| Chang	| 1	| 1	| 24 - 12 oz bottles	| 19
|3	| Aniseed Syrup	| 1	| 2	| 12 - 550 ml bottles	| 10
|4	| Chef Anton's Cajun Seasoning	| 2	| 2	| 48 - 6 oz jars	| 22
|5	| Chef Anton's Gumbo Mix	| 2	| 2	| 36 boxes	| 21.35

# مثال على استخدام COUNT()

تُعطي عبارة SQL التالية عدد المنتجات:

	SELECT COUNT(ProductID)
	FROM Products;

<amp-ad width="100vw" height="320"
     type="adsense"
     data-ad-client="ca-pub-4752855256699204"
     data-ad-slot="3888202602"
     data-auto-format="rspv"
     data-full-width="">
  <div overflow=""></div>
</amp-ad>

# مثال على استخدام AVG()

تُعطي عبارة SQL التالية القيمة المتوسطة ﻷسعار جميع المنتجات:

	SELECT AVG(Price)
	FROM Products;

# استعراض قاعدة البيانات 

فيما يلي تحديد من جدول "OrderDetails" أو تفاصيل الطلب في قاعدة البيانات النموذجية Northwind، والذي يعرض رقم الطلب ورقم المنتَج والكمية

|OrderDetailID|	OrderID	| ProductID	| Quantity
|----------|-------|------------|------------
|1	|10248	|11	|12
|2	|10248	|42	|10
|3	|10248	|72	|5
|4	|10249	|14	|9
|5	|10249	|51	|40

# مثال على استخدام SUM()

تُعطي عبارة SQL التالية مجموع القيم في عمود Quantity أي الكمية في الجدول أعلاه

	SELECT SUM(Quantity)
	FROM OrderDetails;

التالي: [عامل LIKE](like)
