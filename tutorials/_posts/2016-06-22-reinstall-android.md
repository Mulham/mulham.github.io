---
layout: post
date: 2016-06-22
title: إعادة تنصيب أندرويد
description: شرح مُبسَّط لطريقة تنصيب أندرويد على الأجهزة اللوحية والجوالات 
type: tutorial
comments: true
tags: أندرويد
---





إذا قمت [بتنصيب أبونتو](/installing-ubuntu-touch) (أو أي نظام آخر) على جهازك اللوحي أو هاتفك، فبإمكانك إعادة تنصيب أندرويد (والذي سيحذف أبونتو). طبعاً إعادة التنصيب يكون من خلال وصل الجهاز مع حاسوب يعمل على نظام لينكس (والشرح هنا على توزيعة أبونتو).

تحذير: سيتم حذف جميع تطبيقات وبيانات أبونتو، بما في ذلك بيانات المستخدم.
{: .notice}

* Toc
{:toc}

# تحميل ملفات نسخة أندرويد

يمكنك في أي وقت تحميل ملفات أندرويد المطلوبة لاستعادة نظامك.
يعرض هذا الجدول روابط لإصدارات أندرويد الشائعة (إذا لم تجد جهازك في الجدول فاطلب رابط النسخة الخاصة لجهازك هنا أو من خلال مراسلتي - على العموم يمكنك البحث بعد إدخال القيم المطلوبة الخاصة بجهازك والحبث عن نسخة أندرويد له).

|	الجهاز	| نسخة أندرويد بحسب النوع		|
| ----- | ----- |
|	Nexus 4	|	[occam](https://developers.google.com/android/nexus/images#occam)	|
|	Nexus 10	|	[mantaray](https://developers.google.com/android/nexus/images#mantaray)	|
|	Nexus 7 2013 WiFi	|	[razor](https://developers.google.com/android/nexus/images#razor)	|
|	Galaxy Nexus	|	[takju](https://developers.google.com/android/nexus/images#takju) أو [yakju](https://developers.google.com/android/nexus/images#yakju)	|
|	Nexus 7	|	[nakasi](https://developers.google.com/android/nexus/images#nakasi) أو [nakasig](https://developers.google.com/android/nexus/images#nakasig)	|
 
قم بتحميل النسخة المطلوبة، مع ملاحظة أنه يجب اختيار رقم الإصدار (build version) والذي كان موجود أصلاً على جهازك. ومنه يمكنك تحديثه بعد تنصيب أندرويد.

# استخراج الملفات

1. قم باستخراج النظام المُحمل. مثلاً إذا كان اسم الملف الذي تم تحميله `razor-kot49h-factory-ebb4918e.tgz` فاستخرجه بالأمر:

		$ tar -xzf razor-kot49h-factory-ebb4918e.tgz

2. انتقل للمجلد المستخرج

		$ cd razor-kot49h

# الذهاب لمُحمل الإقلاع

1. قم بوصل جهازك اللوحي بحاسوب أبونتو عبر الـ USB .

2. تأكد من أن النظام (أو بالأحرى أداة adb) تعرف على الجهاز

		$ adb devices
		List of devices attached
		025d138e2f521413 device

	أي يجب ان يكون ناتج الأمر في السطر الأول شبيه بالسطرين الثاني والثالث.

3. قم بإعادة تشغيل الجهاز اللوحي لمُحمِّل الإقلاع 

		$ adb reboot bootloader

# إعادة تنصيب أندرويد

يجب أن تكون في المجلد المستخرج لنسخة أندرويد لبدء العملية.


نفذ الأمر:

		$ sudo ./flash-all.sh

انتظر حتى اكتمال العملية وإقلاع أندرويد لشاشة الترحيب.

# استعادة بيانات وتطبيقات أندرويد (اختياري)

إذا قمت سابقاً بعمل نسخة احتياطية لتطبيقات وبيانات أندرويد، كما هو موضح هنا، فيمكنك استعادة هذه النسخة الاحتياطية :
1. يجب أن تقوم أولاً بتفعيل وضع تحسين أخطاء USB في نظام أندرويد ، وتوصيل جهاز أندرويد لسطح مكتب أبونتو عبر USB (انظر [هنا](https://mulham.github.io/installing-ubuntu-touch#usb)).

2. افتح الطرفية في سطح مكتب أبونتو Ctrrl + Alt + T

3. اذهب باستخدام الأمر cd للمجلد الذي يحوي ملف النسخة الاحتياطية backup.ab.

4. قم باستعادة ملف backup.ab لأندرويد :

		$ adb restore backup.ab

# قفل الجهاز (اختياري)

لقد قمت سابقاً لتنصيب أبونتو بإلغاء قفل الجهاز، يمكنك الآن اختيارياً قفله.

1. أطفئ الجهاز من زر الطاقة.

2. أعد التشغيل لمحمل الإقلاع بالضغط على مجموعة الأزرار الصحيحة لنوع جهازك كما هو مذكور [هنا](https://source.android.com/source/building-devices.html#booting-into-fastboot-mode) (بالإنجليزية) :

	تأكد من أن الجهاز متصل بوضع fastboot كالتالي:

		$ fastboot devices
		025d138e2f521413 fastboot

3. اقفل الجهاز :


		$ fastboot oem lock

4. أعد التشغيل لأندرويد :

		$ fastboot reboot


