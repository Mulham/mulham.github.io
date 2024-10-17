---
date: 2019-08-28
title: تنصيب mysql وتهيئته بالشكل الصحيح 
description: تنصيب وتهيئة إعدادات mysql بالشكل الصحيح وحل مشكلة رفض الوصول للمستخدم وعدم القدرة على إجراء اتصال مع قاعدة البيانات
tags: [SQL, mysql, قواعد بيانات, لينكس]
image:
  path: /assets/posts/mysql.jpg
  alt: "Console by hermzz is licensed under CC BY-SA 2.0"
---




فيما يلي شرح لتنصيب mysql بشكل صحيح على نظام أبونتو تحديدا ويبقى الشرح ساري المفعول لباقي أنظمة لينكس وباقي الأنظمة أيضاً مع بعض التغييرات.

## التنصيب 

1. تنصيب mysql

		sudo apt install mysql-server

2. تهيئة الإعدادات

		mysql_secure_installation

## حل مشكلة الوصول المرفوض للمستخدم

بعد التنصيبة يجب عند كتابة الأمر التالي وإدخال كلمة سر النظام القدرة على الوصول لسطر أوامر mysql لكتابة أوامر sql هناك، ولكن غالبا ما يتم رفض الوصول لسطر أوامر mysql بعد التنصيب مباشرة، للتأكد أولا من وجود المشكلة أدخل التالي:

		mysql -u root -p
	
وأدخل كلمة سر النظام، جرب أيضا التالي مع استبدال user باسم المستخدم الخاص بك في النظام (والذي يكون مكتوب في الطرفية كالتالي: 

user@host:~$

		mysql -u user -p

إذا تم رفض الوصول وأعطاك الخطأ "ERROR 1698 (28000): Access denied for user" فإليك الحل:

 لحل هذه المشكلة طريقتين:

* قم بتنفيذ الأمر التالي

		sudo mysql -u root

ثم أدخل أوامر sql التالية:

		mysql> USE mysql;
		mysql> SELECT User, Host, plugin FROM mysql.user;

إذا كان الناتج مشابه للتالي:


		+------------------+-----------------------+
		| User             | plugin                |
		+------------------+-----------------------+
		| root             | auth_socket           |
		| mysql.sys        | mysql_native_password |
		| debian-sys-maint | mysql_native_password |
		+------------------+-----------------------+

أي أن المستخدم root يستخدم plugin يونكس المسمى auth_socket وهذا هو سبب المشكلة.

علينا بتغيير هذا ال plugin إلى mysql_native_password وفق الأوامر التالية:

		mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
		mysql> FLUSH PRIVILEGES;
		mysql> exit;

ثم قم بإعادة تشغيل mysql

		$ service mysql restart
	
* أو يمكن إضافة المستخدم الحالي لقاعدة البيانات وإعطائه الصلاحيات المطلوبة وفقا للأوامر التالية:

		$ sudo mysql -u root 

		mysql> USE mysql;

في الأوامر التالية قم بتغيير YOUR_SYSTEM_USER إلى اسم مستخدم النظام الموجود لديك و Password لكلمة السر التي ترغب

		mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY 'Password';
		mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
		mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
		mysql> FLUSH PRIVILEGES;
		mysql> exit;

		$ service mysql restart

وبهذا يجب أن تكون المشكلة قد حُلَّت، ﻷي استفسار اتركه في التعليقات أو راسلني عبر البريد الإلكتروني.


المراجع:

* [stackoverflow](https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost)
