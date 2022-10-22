---
layout: post
date: 2021-02-28
title: الربط مع قاعدة بيانات SQL في جافا
description: كيفية إنشاء اتصال مع قاعدة بيانات SQL من تطبيق جافا والتعامل منه مع قاعدة البيانات
type: tutorial
hidden : true
---

{: .notice}
هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)


بعد إنشاء قاعدة البيانات في MySQL Server عن طريق تطبيق MySQL Workbench يمكننا ربطها مع تطبيقنا الذي نعمل عليه.

* Toc
{:toc}

# تهيئة الاعتماديات

لإمكانية الاتصال بقاعدة البيانات (بشكل أدق بسيرفر MySQL) سيتطلب مننا إضافة حزمة MySQL Connector التي قمت بتنزيلها في [بداية هذه الشروحات](/java-project-from-scratch/#البرامج-والمكتبات-المستخدمة). وللقيام بذلك قم بالذهاب ضمن برنامج IntelliJ للقائمة File ثم Project Structure ثم اتبع التالي:


  {% include image.html layout="responsive" width="400" height="400" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/add-mysql-connector-intelliJ.png" alt="إضافة مكتبة MySQL Connector لبرنامج IntelliJ" %}


1. قم بالضغط من القائمة اليسارية على خيار Modules 
2. اضغط على تبويبة Dependencies من أعلى النافذة اليمينية
3. اضغط في الأسفل على زر + ثم اختر JARs or Directories، سيظهر لك مستعرض الملفات، قم باختيار ملف MySQL Connector ذو اللاحقة jar 
4. بعد ذلك ستظهر لك الحزمة التي اخترتها في القائمة، قم بالضغط على المربع بجانبها ليظهر إشارة صح 
5. اضغط على OK


# ملف الإعدادات

ضمن محرر الكود IntelliJ اضغط باليمين على مجلد sample ثم New ثم Package وسمها Database (مع الإبقاء على .sample) ثم انقر باليمين على المجلد الجديد الأخير واختر New ثم Java Class وسمه Configs حيث سنقوم بحفظ إعدادات قاعدة البيانات فيه.

سترى أن الصنف (Class) الجديد المنشأ "Configs" يحوي عدة أسطر، أولها مسار الحزمة، ثم تعريف الصنف على الشكل:

        package sample.Database;

        public class Configs {

        }

**أضف** التالي ضمن قوسي تعريف الصنف:



        protected String dbHost = "localhost";
        protected String dbPort= "3306";
        protected String dbUser = "root";
        protected String dbPass = "Enter-password-here";
        protected String dbName = "mydb";

وقم بتغيير dbPass لكلمة سر قاعدة البيانات لديك (كلمة سر MySQL Server)، وإن كانت قاعدة البيانات تحمل اسما مختلفا غير mydb فغير اسمها في dbName.

# الثوابت

انقر باليمين على مجلد Database واختر New ثم Java Class وسمه Const حيث سنقوم بحفظ ثوابت قاعدة البيانات فيه، وأعني بالثوابت أسماء الجداول والأعمدة في قاعدة البيانات.

## لماذا ننشئ هذا الملف؟

يمكن الاستغناء عن هذا الملف وكتابة أسماء الجداول والأعمدة مباشرة في عبارات SQL ولكن لا يُنصح بذلك، ﻷنه وعند كتابة الكثير من الدالات التي تحوي الكثير من عبارات SQL، وعندما تقوم بتغيير اسم عمود مثلا في أحد الجداول ضمن قاعدة البيانات، فسيتطلب منك البحث عن كل استخدام لهذا العمود في الكود البرمجي وهذا أمر طويل، بينما عندما تقوم بحفظ أسماء الجداول والأعمدة بملف مستقل وكمتغييرات ثم تستخدم أسماء المتغييرات في عبارات SQL فستقوم فقط بتغيير اسم العمود أو الجدول لذلك المتغير في هذا الملف وينتهي الأمر ولن تضطر للبحث عن كل استخدام له وتغيير الاسم في الكثير من الأماكن في الكود.


في هذا الملف سأقوم بتعريف أسماء الجداول وأسماء الأعمدة في كل جدول، وكمثال بسيط فسيكون الصنف على الشكل التالي:


        package sample.Database;

        public class Const {
            // tables
            public static final String RADIOGRAPHER_TABLE = "Betreiber";
            public static final String EVALUATOR_TABLE = "Bewerter";
            public static final String CONFIRMATOR_TABLE = "Genehmiger";
            public static final String USERS_TABLE = "Users";
            //VARIABLES FOR ALL USERS TABLE

            public static final String USERS_FIRSTNAME = "Name";
            public static final String USERS_LASTNAME = "Nachname";
            public static final String USERS_LEVEL = "Level";
            public static final String USERS_CERTIFICATE_DATE = "Zertifikat_datum";
            public static final String USERS_PASSWORD = "password";

        }

# الدالات

لنقم الآن بإنشاء الملف الذي سنستدعه كثيرا من باقي الملفات، والذي سيحوي كل عبارات SQL وكل الدالات التي تتعامل مباشرة مع قاعدة البيانات.

انقر باليمين على مجلد Database واختر New ثم Java Class وسمه DatabaseHandler.


{: .notice}
**ملاحظة:** من المهم جدا جعل كل الدالات التي تتعامل مع قاعدة البيانات في ملف واحد وعدم كتابة عبارات SQL في عدة ملفات، فالسلوك الأخير يتنافي مع مبدأ البرمجة كائنية التوجه (OOP)، ويعقد الكود لديك ويجعل عملية تصحيح الأخطاء لاحقا صعبة جدا.

**للتوضيح** فإن البرمجة كائنية التوجه تتطلب أن يكون لكل صنف ولكل دالة وظيفة واحدة موضحة باسم الصنف أو الدالة، هنا لدينا صنف واحد محدد وظيفته واحدة وهي التعامل مع قاعدة البيانات (أيا كان شكل التعامل سواء استخراج أو إضافة أو حذف بيانات ولكنها واحدة في النهاية)، وعندما نكتب دالات خارج هذا الصنف تتعامل مع قاعدة البيانات، مثلا في صنف LoginController فسيكون لذلك الصنف أكثر من وظيفة (حيث وظيفته التحكم بنافذة تسجيل الدخول وليس التعامل مباشرة مع قواعد البيانات)، وبالتالي سيكون هذا خاطئًا.


هنا في هذا الملف سنقوم باستدعاء بعض المكتبات وسنجعل الصنف جزءا من صنف الإعدادات Configs على الشكل التالي


        package sample.Database;

        import sample.model.*;

        import java.sql.*;

        public class DatabaseHandler extends Configs {


        }

وسنكتب لاحقا جميع الدالات التي تتعامل مع قاعدة البيانات ضمن قوسي الصنف الموضحين أعلاه.

ولكن يتطلب في البداية كتابة الدالة التي تقوم بإنشاء الاتصال بقاعدة البيانات، لذا قم بكتابة التالي ضمن الصنف أعلاه أي بين القوسين (لاحظ استخدام المعطيات dbHost و dbPort وغيرهم من ملف Configs):


{% highlight java %}

    Connection dbConnection;

    public Connection getDbConnection() throws ClassNotFoundException, SQLException {
        String connectionString = "jdbc:mysql://" + dbHost + ":"
                + dbPort + "/"
                + dbName + "?autoReconnect=true&useSSL=false";
        Class.forName("com.mysql.cj.jdbc.Driver");

        dbConnection = DriverManager.getConnection(connectionString, dbUser, dbPass);
        System.out.println(dbConnection);
        return dbConnection;
    }

{% endhighlight %}

الدالة أعلاه ثابتة عموما في كل البرامج لإنشاء الاتصال بقاعدة البيانات.

الخطوة الأخيرة هنا هي إضافة مستخدم، مثلا باسم مستخدم "admin" وكلمة سر مماثلة، إلى قاعدة البيانات، لنتمكن لاحقا من تسجيل الدخول من هذا المستخدم.

قم بفتح برنامج MySQL Workbench، وقم بالاتصال بقاعدة البيانات عبر الضغط على الاتصال كما يظهر في الصورة:

{% include image.html layout="responsive" width="400" height="300" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/mysql-workbench-connection.png" alt="شرح الاتصال بقاعدة البيانات من برنامج MySQL Workbench" %}

سيطلب منك كلمة السر التي أدخلتها عند التنصيب، قم بإدخالها، ثم على القائمة اليسارية قم بتوسيع قاعدة البيانات الخاصة بتطبيقنا واضغط باليمين على الجدول Users ثم أول خيار Select Rows.

{% include image.html layout="responsive" width="400" height="600" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/mysql-workbench-tables.png" alt="شرح عرض جداول قاعدة البيانات في برنامج MySQL Workbench" %}

قم بإدخال الاسم وكلمة السر على أنهم admin مثلا وباقي المعلومات غير مهمة حاليا (ولكن لاتتركها فارغة لكي لايحدث خطأ عند تشغيل البرنامج والتي تنتج عن تمرير قيم فارغة في عبارات sql)، ثم اضغط على Apply كما في الصورة:

{% include image.html layout="responsive" width="400" height="200" src="https://raw.githubusercontent.com/Mulham/Java-Project/images/images/mysql-workbench-insert.png" alt="إضافة بيانات لقواعد البيانات عبر برنامج MySQL Workbench" %}

يمكنك الآن إغلاق البرنامج.

لنبدأ الآن بكتابة الدالة التي تستدعي مستخدم من قاعدة البيانات وفق البيانات المعطاة، وذلك لإتمام عملية تسجيل الدخول، وذلك في الصفحة التالية..

*******

**التالي:** [تسجيل الدخول](/java-sign-in)


