---
layout: post
date: 2019-09-24
title: ضبط أبونتو للعمل كراوتر
type: tutorial
comments: true
tags: [شبكات, إنترنت, لينكس]
---


هل تعلم أنه يمكن ضبط نظام أوبونتو الخاص بك ليكون بمثابة جهاز راوتر(مودم) قوي للغاية؟ تابع القراءة لاكتشاف كيفية تحقيق ذلك من خلال بضع خطوات بسيطة.
إذا كان لديك بطاقتي واجهة شبكة مثبتتان في نظام Ubuntu (مثلا كرت شبكة سلكي ethernet وآخر وايفاي) أحدهما يوصلك بالإنترنت والآخر بشبكة محلية ، يمكن تحويل نظامك إلى جهاز راوتر قوي للغاية. يمكنك إنشاء NAT (ترجمة عنوان الشبكة) الأساسية ، وتنشيط إعادة توجيه المنفذ ، وتشكيل بروكسي ، وتحديد أولويات حركة المرور من وإلى نظامك حتى لا يتعارض التنزيل مع الألعاب الخاصة بك. توضح هذه المقالة كيفية إعداد نظام Ubuntu الخاص بك كراوتر ، والذي يمكن تهيئته لاحقًا كجدار حماية. سيساعدك الإعداد الناتج على التحكم في حركة المرور عبر المنافذ وجعل نظامك أقل عرضة للمخاطر الأمنية.

![Ubuntu as a router](/assets/ubuntu-as-router1.jpg)


* Toc
{:toc}

# انشاء بوابة

الشروط المسبقة لإعداد بوابة هي:

* كمبيوتر مع نظام التشغيل Ubuntu
* اثنين من بطاقات الشبكة
* الاتصال بشبكة الإنترنت

يجب تثبيت بطاقتي الشبكة في الكمبيوتر. أحدهما يتصل بالإنترنت ، والذي سوف نسميه eth1، والآخر يتصل بشبكتنا المحليّة.وسوف نسميه هنا eth0

        Host A (192.168.1.8) ? ? Eth1 ? ? Ubuntu Gateway ? ? Eth0 ? ?
        Host B (10.10.6.205)

للتلخيص:

eth1 = محول الشبكة المتصل بالإنترنت (خارجي)
eth0 = محول الشبكة المتصل بجهاز كمبيوتر في نفس الشبكة الفرعية (الداخلية)
10.10.6.0 = الشبكة الفرعية لـ eth0
192.168.1.8 = عنوان IP للمضيف أ ، أي جهاز كمبيوتر على الإنترنت
10.10.6.203 = عنوان IP الخاص بـ eth0.
10.10.6.204 = عنوان IP الخاص بـ eth1.
10.10.6.205 = عنوان IP للمضيف B ، أي كمبيوتر في نفس الشبكة الفرعية.

![Ubuntu as a router - Configuration of eth0](/assets/ubuntu-as-router2.png)

![Setting up network on eth0](/assets/ubuntu-as-router3.png)

![Configuration of eth 1](/assets/ubuntu-as-router4.png)

![Setting up network on eth 1](/assets/ubuntu-as-router5.png)

# ضبط بطاقات واجهة الشبكة

يجب تعيين عنوان IP ثابت لكل واجهة شبكة. تختلف الخطوات باختلاف إصدار سطح المكتب وإصدار خادم Ubuntu. سنوضح كلتا الطريقتين أدناه. يمكنك الرجوع للشكل 2 إلى 5

* لإصدار سطح المكتب الخاص بـ Ubuntu: انقر فوق "إعدادات النظام" ، الشبكة ، حدد "خيارات الواجهة"
* بالنسبة إلى إصدار خادم Ubuntu: يلزمك اتباع الخطوات الموضحة أدناه.
1. افتح الجهاز ، عن طريق الضغط على Ctrl + Alt + T
2. أدخل الأمر التالي لتحرير ملف "الواجهات":

        sudo vim /etc/network/interfaces
ثم قم بتحرير الملف مع الأسطر التالية:

        auto lo  
        iface lo inet loopback  
        auto eth0  
        iface eth0 inet static  
        address 10.10.6.203  
        netmask 255.255.255.0  
        gateway 10.10.6.203
        auto eth1  
        iface eth1 inet static  
        address 10.10.6.204  
        netmask 255.255.255.0  
        gateway 10.10.6.2

# تمكين إعادة توجيه IP

قم بتكوين نظام Ubuntu لبدء التوجيه بين واجهتين عن طريق تمكين إعادة توجيه IP:

        sudo sh -c echo 1 /proc/sys/net/ipv4/ip forward

قم بتحرير الملف /etc/sysctl.conf ، وإضافة الأسطر التالية (للإصدارات حتى Ubuntu 10.04):

        net.ipv4.conf.default.forwarding=1  
        net.ipv4.conf.all.forwarding=1

بدءًا من Ubuntu 10.10 وما بعده ، يكفي تعديل الملف /etc/sysctl.conf و حذف المربع # من السطر التالي:

        # net.ipv4.ip forward=1

# تخفي الـ IP

لتمكين تخفي IP ، أدخل مجموعة الأوامر التالية في الجهاز:

        sudo iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
        sudo iptables -A FORWARD -i eth1 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
        sudo iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT

لا تنس حفظ قواعد iptables هذه ، أو ستضيع بعد إعادة تشغيل النظام

        # iptables-save > /etc/iptables.rules

سيقوم الأمر أعلاه بتنشيط قواعد iptables المحفوظة مسبقًا عند إعادة تشغيل النظام ، مما يجعل التغييرات دائمة.

هذا المقال مترجم بتصرّف. [المصدر](https://opensourceforu.com/2015/04/how-to-configure-ubuntu-as-a-router/)
