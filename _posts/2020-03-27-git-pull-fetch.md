---
layout: post
date: 2020-03-27
description: تعرف على الفرق بين الأمرين git pull و git fetch
title: الفرق بين git pull و git fetch
type: blog
hidden: true
---

إليك الفرق بين الأمرين `git pull` و `git fetch`:

أبسط عبارة يمكن أن نقولها هو أن الأمر `git pull` ينفّذ الأمر `git fetch` متبوعًا بتنفيذ الأمر `git merge`.

يمكن تنفيذ `git fetch` في أي وقت لتحديث الأفرع على السيرفر في refs/remotes/<remote>/. ولا تغير هذه العملية أي فرع (branch) من أفرعك المحلية في refs/heads . وهي آمنة للتنفيذ بدون تغيير النسخة التي تعمل عليها. وهناك بعض الأشخاص الذين يستخدمون الأمر `git fetch` بشكل دوري في الأعمال المُجدولة (cron jobs) رغم أن ذلك غير مستحسن.

أما الأمر `git pull` فهو الذي نقوم به عندما نريد تحديث أو مزامنة الفرع المحلي مع الفرع البعيد على السيرفر.



ﻷي استفسار يرجى مراسلتي على الروابط الظاهرة أسفل الصفحة.

ترجمة وبتصرف. [المصدر](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)

هذا المقال جزء من: [أسئلة وأجوبة حول git](/git-qa)
