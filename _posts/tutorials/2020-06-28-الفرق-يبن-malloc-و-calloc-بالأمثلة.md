---
date: 2020-06-28
title: الفرق بين ()malloc و ()calloc بالأمثلة
description: شرح الفرق بين دالتي التخصيص الديناميكي للذاكرة في لغة سي malloc و calloc مع أمثلة عملية
tags: [برمجة ,تعليم]
image:
  path: /assets/articles/difference-between-malloc-and-calloc.jpg
  alt: "memory by osde8info is licensed under CC BY-SA 2.0"
---

هذا المقال متعلق بالمقال السابق: [التخصيص الديناميكي للذاكرة في سي](/التخصيص-الديناميكي-للذاكرة-في-سي)
ويجب قراءته لفهم هذا المقال

إن كلتا دالتي ()malloc و ()calloc تقومان بتخصيص جزء من الذاكر بشكل ديناميكي (قابل للتغيير). وهذا يعني أن الذاكرة يتم تخصيصها خلال زمن العمل (تنفيذ البرنامج) من الـ heap segment أو بالعربي قد نترجمها لـ "قطعة التكدس" (لايهم كيف تترجم المهم أنها جزء من الذاكرة).

الفروقات بين الدالتين المذكورتين نكمن في النقاط التالية:

* التهيئة: إن الدالة ()malloc تقوم بتخصيص حجرة (block) من الذاكرة بحجم معطى (بالبايتات) وتقوم بإرجاع مؤشر (pointer) يشير لبداية تلك الحجرة. ولا تقوم ()malloc بتهيئة الذاكرة المخصصة بقيمة محددة. لذا فإذا حاولنا الوصول لمحتوى حجرة الذاكرة التي تم تخصيصها فسنحصل على خطأ فشل تجزئة أو يسمى (segmentation fault error) أو ربما نحصل على قيم عشوائية.

        void* malloc(size_t size); 


في حين أن ()calloc تقوم بتخصيص الذاكرة وتهيئة الحجرة المخصصة بالقيمة صفر 0. فإذا حاولنا الوصول لمحتوى الحجرة المخصصة سنحصل على القيمة 0.

        void* calloc(size_t num, size_t size); 


* عدد المعطيات: المعطيات وهي "arguments" (وهي عدد المتغيرات الموجودة بين قوسين في العبارتين أعلاه) فكما لاحظنا أن ()malloc تتطلب معطى وحيد بينما ()calloc تتطلب معطيين وهما:

  1. عدد الحجرات التي سيتم تخصيصها
  2. حجم كل حجرة (جميع الحجرات ستكون متساوية ولها هذا الحجم)

* قيمة الإرجاع: أو القيمة المرجعة عند استدعاء الدالة. تقوم كلتا الدالتين ()malloc و ()calloc  بعد التخصيص الناجح للذاكرة بإرجاع مؤشر (pointer) يشير لبداية الحجرة المخصصة، أما في حالة فشل التخصيص فتُرجع القيمة NULL.

إذا أردنا على سبيل المثال تخصيص ذاكرة لمصفوفة من خمس عناصر عددية integer فسنكتب التالي:


```c

// C program to demonstrate the use of calloc() 
// and malloc() 
#include <stdio.h> 
#include <stdlib.h> 

int main() 
{ 
	int* arr; 

	// malloc() allocate the memory for 5 integers 
	// containing garbage values 
	arr = (int*)malloc(5 * sizeof(int)); // 5*4bytes = 20 bytes 

	// Deallocates memory previously allocated by malloc() function 
	free(arr); 

	// calloc() allocate the memory for 5 integers and 
	// set 0 to all of them 
	arr = (int*)calloc(5, sizeof(int)); 

	// Deallocates memory previously allocated by calloc() function 
	free(arr); 

	return (0); 
} 
```

يمكننا الحصول على نفس الوظيفة التي تقوم بها الدالة ()calloc باستخدام الدالة ()malloc متبوعة بالدالة ()memset
 

        ptr = malloc(size); 
        memset(ptr, 0, size); 

يمكنك قراءة المزيد عن ()memset [هنا](/memset)

**ملاحظة:** من الأفضل بشكل عام استخدام malloc بدلًا من calloc إلا في حال أردنا التهيئة بالقيمة صفر، ﻷن malloc أسرع من calloc. لذا إذا أردنا نسخ بعض البيانات فقط أو شيئ ما لا يتطلب ملء الحجرات بالقيمة صفر، فاستخدام malloc سيكون الخيار الأفضل.

هذا المقال مترجم وبتصرّف. يمكنك الاطلاع على [المصدر](https://www.geeksforgeeks.org/difference-between-malloc-and-calloc-with-examples/)

