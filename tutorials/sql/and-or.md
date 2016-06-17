---
layout: post
date: 2016-06-18
title: سلسلة دروس SQL|عمليات AND & OR
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

تستخدم عمليات AND (و) ، OR (أو) لتشريح (فلترة) التسجيلات بناء على أكثر من شرط واحد .


عمليات AND & OR في SQL 


عملية AND تعرض التسجيل إذا كان كلاً من الشرط الأول والشرط الثاني محققين

عملية OR تعرض التسجيل اذا كان الشرط الأول أو الشرط الثاني فقط محقق ، أي اذا تحقق أحد الشرطين فقط .

* Toc
{:toc}


**استعراض قاعدة بيانات**


سنستخدم قاعدة البيانات المعروفة جيداً : Northwind


في الأسفل تحديد من جدول الزبائن Customers


![](http://3.bp.blogspot.com/-txe3CmsAcew/VODvNYC9AII/AAAAAAAABpg/lpoMB6Uu2Eo/s1600/Screenshot%2Bfrom%2B2015-02-15%2B21%3A09%3A44.png)

# مثال على عملية AND


تصريح SQL التالي يحدد جميع الزبائن من دولة Germany و مدينة Berlin ضمن جدول الزبائن


        SELECT * FROM Customers

        WHERE Country='Germany'

        AND City='Berlin';

# مثال على عملية OR


تصريح SQL التالي يحدد جميع الزبائن من مدينة Berlin أو مدينة München ضمن جدول الزبائن


        SELECT * FROM Customers

        WHERE City='Berlin'

        OR City='München';


# اجتماع AND & OR


يمكنك أيضاً جمع AND و OR في تصريح واحد (استخدم الأقواس لتشكيل تعبيرات مركبة )


تصريح SQL التالي يحدد جميع الزبائن من دولة Germany والمدينة يجب أن تكون مساوية لـ Berlin أو München ضمن جدول الزبائن .

        SELECT * FROM Customers

        WHERE Country='Germany'

        AND (City='Berlin' OR City='München');


التالي: [دالة ORDER BY](order-by)
