---
date: 2021-03-02
title: بناء هيكلية تطبيق جافا
description: تنفيذ هيكلية وبناء التطبيق وتقسيم الحزم (المجلدات) لتطبيق جافا إف إكس
hidden : true
---


> هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)
{: .prompt-info }

هناك عدة طرق معروفة لتنظيم المشروع البرمجي لدينا وذلك وفق تقسيم الملفات البرمجية ضمن مجلدات بحيث يكون لكل مجلد وظيفة معينة، وللاختصار لن أخوض في أنواع التنسيق تلك بل يكفي أن نطبق الهيكلية التي سنسير عليها والتي شرحتها في الدرس الأول في فقرة "[تخطيط البرنامج](/java-project-from-scratch/#تخطيط-البرنامج)".


وللقيام بذلك ستجد ضمن تطبيق IntelliJ وفي المشروع لديك ضمن مجلد src مجلد باسم sample، قم بالضغط عليه باليمين ثم اختر New ثم Package وقم بتسمية الحزمة (المجلد) الجديد باسم controller (لاتحذف .sample من الحقل)

كرر العملية لإنشاء مجلد جديد باسم view 

كرر العملية لإنشاء مجلد جديد باسم model (والذي سيبقى فارغا حاليا) 

قم بنسخ ملف sample.fxml لمجلد view (بالسحب والإفلات والضغط على زر Refactor)

قم بنسخ ملف Controller لمجلد controller

الآن قم بإضافة السطر التالي لملف "module-info.java":

           exports sample.controller;

وقم بتشغيل البرنامج للتأكد بأن كل شيئ مايزال على مايرام.

سيتطلب منك لكل مجلد تنشؤه ويحوي ملفات جافا توضيحه في ملف "module-info.java" كما في السطر أعلاه. لذا لعدم الوقوع في مشاكل لاحقة سأطلعك على الكود النهائي لهذا الملف ويمكنك نسخه ولصقه لديك في ذلك الملف:

        requires javafx.fxml;
        requires javafx.controls;
        requires javafx.graphics;
        exports sample.controller;
        opens sample;
        requires javafx.base;
        requires java.sql;
        requires java.desktop;
        opens sample.controller;
        opens sample.model;
 




يمكنك معاينة ملفات المشروع حتى الوضع الحالي على [هذا الرابط](https://github.com/Mulham/Java-Project/tree/initialize)

****

**التالي:** [تصميم الواجهة](/javafx-interface-design)

