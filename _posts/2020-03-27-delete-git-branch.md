---
layout: post
date: 2020-03-27
description: تعلم كيف يمكنك التراجع وإلغاء آخر اعتماد أو commit في جت git محليا بخطوات سريعة وعملية
title: كيفية حذف فرع git محليا ومن السيرفر
type: blog
hidden: true
---

إليك طريقة حذف فرع branch في git محليا على جهازك وعلى الجهاز البعيد أيضا أو السيرفر.

باختصار الطريقة عن طريق الأمرين التاليين الأول لحذف الفرع من السيرفر والثان لحذفه محليًا. مع استبدال `<remote_name>` و `<branch_name>` بالمطلوب:

        $ git push -d <remote_name> <branch_name>
        $ git branch -d <branch_name>

في معظم الحالات يكون الـ `<remote_name>` هو `origin` وبالتالي سيكون الأمر الأول:

        $ git push -d origin <branch_name>


ﻷي استفسار يرجى مراسلتي على الإيميل الظاهرة أيقونته أسفل الصفحة.

ترجمة وبتصرف. [المصدر](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely)

هذا المقال جزء من: [أسئلة وأجوبة حول git](/git-qa)
