---
layout: post
date: 2019-08-04
title: كيفية تصحيح بعض أخطاء الفيديوهات 
description: تصحيح أخطاء عدم تطابق الصوت مع الصورة وخروج الصوت من سماعة واحدة وما إلى ذلك باستخدام برنامج vlc
type: tutorial
comments: true
---

مرحبًا، هناك العديد من الفيديوهات القديمة نوعا ما والموجودة على اليوتيوب مثلا والتي يكون فيها الصوت متأخر قليلا عن الصورة أو العكس، أو يكون الصوت يخرج من سماعة واحد أو مكبر صوت واحد (أي يمين مثلا دون اليسار)، يمكن تصحيح هذه الأخطاء بشكل مباشر للمشاهدة مباشرة دون التعديل على الفيديو، ويمكن أيضًا إن أردنا تصحيحه بشكل دائم وإعادة نشره عبر محررات الفيديو. ولكننا هنا سنتحدث عن التصحيح باستخدام برنامج vlc للمشاهدة فقط، فمن يعمل على محررات الفيديو يعرف كيف يمكنه تصحيح ذلك وتصدير الفيديو بعد تصحيح أخطائه..

* Toc
{:toc}


# تصحيح عدم تطابق الصوت مع الصورة

## ﻷنظمة الحاسوب (ويندوز، لينكس، ماك)

نستخدم لهذا الغرض [مشغل الفيديو الشهير والمجاني vlc](https://www.videolan.org/vlc/index.html) والذي يعمل على جميع أنظمة الحاسوب والمحمول.
وهنا إما نقوم بتنزيل الفيديو المطلوب والذي يحوي الأخطاء التي ذكرناها من الإنترنت ليصبح لدينا على الجهاز ومنه نشغله مباشرة باستخدام برنامج vlc أو إذا كان الفيديو على اليوتيوب أو موقع شبيه به يدعم البث video stream فنقوم بتشغيله مباشرة من النت بفتح برنامج vlc والذهاب لـ Media > Open Network Stream كما في الصورة:

![open network stream vlc](/assets/vlc1.png)

ثم نضع رابط الفيديو كما في الصورة أدناه ونضغط على play
![open network stream vlc - 2](/assets/vlc2.png)

والآن بعد تشغيل الفيديو سواء بعد تنزيله من النت أي من الجهاز مباشرة أو من الإنترنت مباشرة، لتصحيح خطأ عدم تزامن الصوت مع الصورة على نظامي الويندوز واللينكس نضغط على الكيبورد على أحد زري <kbd>J</kbd> و <kbd>K</kbd> لتأخير وتسبيق الصوت عن الصورة على التوالي. على نظام الماك تكون الاختصارات <kbd>G</kbd> و <kbd>F</kbd>
نستمر في الضغط على أحد هذه الأزرار بحسب الخطأ في الفيديو لنحصل على النتيجة المطلوبة.

## على اﻷندرويد

1. قم بتحميل تطبيق vlc من [Google play](https://play.google.com/store/apps/details?id=org.videolan.vlc).

2. قم بفتح الفيديو الموجود على الهاتف أو بنسخ رابط الفيديو من اليوتيوب أو مايشبهه من مواقع الفيديو والذهاب للقائمة الجانبية للبرنامج ثم Stream ولصق الرابط هناك

3. من الخيارات في الأسفل اضغط على الأيقونة الظاهرة في الصورة ثم Audio delay

![Audio delay option in vlc Android](/assets/vlc3.jpg)

4. اضغط على زري `+` و `-` للتعديل والحصول على النتيجة المطلوبة


# تصحيح خروج الصوت من جهة واحدة

بعض الفيديوهات تحوي على خطأ في الصوت وهو خروجه من جهة واحدة (اليمين أو اليسار) ويتضح هذا الخطأ تمامًا عند ارتداء سماعات. لتصحيح هذا الخطأ ضمن برنامج vlc ( ﻷنظمة الحاسوب فقط حيث أنني لم أعثر على هذا الخيار في النسخة المخصصة ﻷندرويد) بعد فتح الفيديو المطلوب نضغط باليمين على الشاشة ثم Audio > Stereo Mode > Left كما هو مبين في الصورة:

![حل مشكلة خروج الصوت من جهة أو منفذ واحد](/assets/vlc4.jpg)


يجدر الإشارة في النهاية إلى أننا قمنا بتغطية ميزتين فقط من مزايا مشغل الفيديو العملاق VLC والذي يحوي مزايا أخرى مثل التحويل بين صيغ الصوت والصورة وتسجيل فيديو للشاشة لعمل فيديوهات تعليمية مثلا وغيرها من المزايا..