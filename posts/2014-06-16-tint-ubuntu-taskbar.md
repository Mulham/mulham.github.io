---
layout: post 
date: 2014-06-16
type: blog
title: كيفية إضافة شريط مهام مشابه لويندوز في أبونتو
comments: true
---


![شريط مهام أبونتو tint2](/assets/00_lead_image_taskbar.jpg)


إلى كل من يفتقد لشريط المهام في واجهة يونيتي Unity على أبونتو، إليك هذه الطريقة البسيطة جدأ لإضافة شريط مهام للنوافذ المفتوحة وذلك عبر أداة تدعى Tint2

كل ما عليك فعله هو تنصيب الأداة وجعلها تعمل تلقائياً عند بدء التشغيل .

# تنصيب أداة Tint2

يمكنك القيام بذلك إما عن طريق الـ Synaptic أو قم بفتح الطرفية (terminal) من القائمة أو بالضغط على <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> واكتب الأمر :

		sudo apt-get install tint2

أدخل كلمة السر الخاصة بك ، واضغط y عند السؤال

![installing tint task bar](/assets/02_do_you_want_to_continue1.jpg)

# إضافة الأداة لبرامج بدء التشغيل :

بعد الانتهاء من التنصيب أغلق التيرمينال ، ثم اذهب لقائمة البحث الخاصة بيونيتي وابحث عن "startup app" وقم بفتحه


![running tint for ubuntu](/assets/05_opening_startup_apps.jpg)

اضغط على زر Add لإضافة الأداة للبرامج التي تبدأ مع بدء التشغيل

![making tint as startup app in ubuntu](/assets/06_clicking_add.jpg)

 الآن اكتب في حقل command العبارة `tint2` والباقي اختياري

![adding tint to startup menu](/assets/07_entering_startup_app_info.jpg)

اضغط على Add ثم إغلاق (close)، الآن قم بتسجيل الخروج من أبونتو  Log out ثم سجل الدخول من جديد  لترى الشريط كما في الصورة

![tint preview windows taskbar in ubuntu](/assets/09_taskbar.png)

إذا قررت لاحقاً بأنك لا تحتاج لبدء الشريط عند كل دخول فكل ما عليك فعله هو إلغاء علامة الصح بجانب اسم الأداة في قائمة البرامج startup application، أي بإمكانك فقط إلغاء بدءها مع بدء التشغيل بإزالة العلامة دون حذف الأداة من القائمة.
