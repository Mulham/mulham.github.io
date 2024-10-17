---
permalink: /github/keep-your-email-private
date: 2016-06-16
title: سلسلة دروس جِت هَب|الحفاظ على خصوصية البريد الإلكتروني
hidden: true
---
 
الفهرس:

[الدرس الأول: التعريف بـ جِت هَب](intro)

[الدرس الثاني:إنشاء حزمة في Github](create-repo)

[الدرس الثالث: نسخ حزمة في Github](fork-repo)

[الدرس الرابع: كيف تكون اجتماعياً في Github](being-social)

الدرس الخامس: كيف تجعل عنوان بريدك الإلكتروني خاصاً في Github

* Toc
{:toc}

إن أي تغيير على مشروع ما باستخدام `Git` يقوم بتعريفك باستخدام عنوان بريدك الإلكتروني. على الرغم من أن Github لم تتلقى تبليغات عديدة حول رسائل ضارّة يتم إرسالها لعناوين البريد لإلكتروني في تغييرات `Git`. إلا أنه يمكنك دائماً استخدام عنوان جت هب خاص بديل، وذلك إذا كنت قلق من إظهار بريدك الإلكتروني أو لديك مخاوف تتعلق بالخصوصية .

سنشرح هنا كيفية عمل ذلك عن طريق استخدام عنوان البريد التالي :

    <username>@users.noreply.github.com

وذلك لجميع العمليات المدعومة من قبل تدفق جت هب في المتصفح .

## أولاً : أخبر جت هب بإبقاء بريدك الإلكتروني خاص

1.اضغط على زر الإعدادات  في الزاوية اليمنى ﻷي صفحة

![git-1](https://help.github.com/assets/images/help/settings/userbar-account-settings.png)

2.اضغط على زر "Emails" في الشريط الجانبي الأيسر

![git-2](https://help.github.com/assets/images/help/settings/settings-sidebar-emails.png)

3.قم بالتأشير على خيار الحفاظ على خصوصية بريدك الإلكتروني " Keep my email address private."

![git-3](https://help.github.com/assets/images/help/settings/email_privacy.png)

## ثانياً : أخبر جت باستخدام عنوان بريدك الإلكتروني الخاص

1. قم بفتح موجه الأوامر

2. حدد بريدك الإلكتروني باستخدام الأمر التالي

		git config --global user.email

3. تأكد من تحديدك لبريدك الإلكتروني بشكل صحيح باستعمال الأمر :

        git config --global user.email
        # username@users.noreply.github.com

أي أدخل الأمر في السطر الأول ، ويجب أن يكون الناتج كما في السطر الثاني .


## استخدام عنوان بريدك الخاص لحزمة محددة


1. قم بالانتقال للحزمة من خلال سطر الأوامر .

2. حدد عنوان بريدك باستخدام الأمر :


        git config user.email "username@users.noreply.github.com" 

3. تأكد من تحديدك لعنوان بريدك بشكل صحيح من خلال الأمر :


        git config user.email
        # username@users.noreply.github.com

انتهى بعون الله.

