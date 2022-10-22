---
layout: post
date: 2021-03-02
title: آلية تسجيل الدخول في تطبيق جافا إف إكس
description: شرح كيفية التأكد من بيانات المستخدم في قاعدة البيانات وتسجيل الدخول في تطبيق جافا FX
type: tutorial
hidden : true
---

{: .notice} 
هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)


الآن وبعد [تصميم الواجهة](/javafx-interface-design) و [ربط التطبيق مع قاعدة البيانات](/java-database-handler)، سننشئ دالة لزر تسجيل الدخول، بحيث عندما يضغط المستخدم عليه نأخذ القيم من حقلي اسم المستخدم وكلمة المرور ونرسلها لقاعدة البيانات للتحقق من صلاحياتها، وإذا كانت تلك البيانات صالحة نقوم بتحويل المستخدم للنافذة الرئيسية ويكون بذلك قد أتم تسجيل الدخول.

لنبدأ أولًا بكتابة الدالة "getUser" التي تأخذ اسم المستخدم وكلمة المرور وتبحث عنهم في قاعدة البيانات:


{% highlight java %}

public ResultSet getUser(String username, String password){
                ResultSet resultset = null;
               String query = "SELECT * FROM " + dbName + "." + Const.USERS_TABLE + " where " + Const.USERS_FIRSTNAME +"=? and " + Const.USERS_PASSWORD + " =?";
                try {
                    PreparedStatement preparedStatement = getDbConnection().prepareStatement(query);
                    preparedStatement.setString(1, username);
                    preparedStatement.setString( 2, password);
                    resultset = preparedStatement.executeQuery();
                } catch (SQLException | ClassNotFoundException e) {
                    e.printStackTrace();
                }
                return resultset;
            }
{% endhighlight %}

لاحظ أننا استخدمنا المعطيات في ملف Const كما ذكرنا سابقا، وللعلم فإننا نضع إشارة استفهام في عبارة SQL كما ترى في متغير query أعلاه، ثم لاحظ السطر:

        preparedStatement.setString(1, username);

أي قم باستبدال إشارة الاستفهام الأولى بالمتغير username، وهكذا.

الدالة تُرجع Resultset وهي تعني مجموعة من النتائج، أي إذا أردنا إرجاع عدة مستخدمين يشتركون في نفس المعلومات المعطاة، قد لا يتطلب هنا فعليا إرجاع resultset وإنما يمكن جعلها فقط ترجع صح true أو خطأ false أي تُرجع فقط المعلومة فيما إذا كان المستخدم موجود في قاعدة البيانات أم لا، يمكنك تغيير الدالة لتعمل بهذا الشكل أو بالشكل الذي تريد، سأترك ذلك كتمرينا لك.

ولنذهب الآن لملف LoginController، في البداية لنقم باستدعاء الصنف DatabaseHandler، لذا وقبل السطر:


        public class LoginController {

أضف التالي:

        import sample.Database.DatabaseHandler;
        import java.sql.ResultSet;


وقبل سطري

        @FXML
         void initialize() {

لنقم بإضافة السطر التالي (حيث سنقوم بإنشاء عنصر من صنف DatabaseHandler):

          private DatabaseHandler databaseHandler;



ولنقم الآن بإضافة التالي للصنف (بين القوسين):

{% highlight java %}

 void initialize() {
        databaseHandler = new DatabaseHandler();    // إنشاء عنصر من صنف قواعد البيانات
        loginButton.setOnAction(event -> {  // هذه الدالة تعني أنه عند الضغط على زر تسجيل الدخول افعل ما بداخلها

            String loginText = loginUsername.getText().trim();  //خذ محتوى حقل اسم المستخدم واحفظه في المتغير هذا
            String loginpwd = loginPassword.getText().trim();   // ﻷخذ محتوى حقل كلمة السر

   
         if(!loginText.equals("") || !loginpwd.equals("")) {       
         // لاحظ إشارة التعجب للنفي، أي إذا كان الحقلين غير فارغين
                ResultSet userRow = databaseHandler.getUser(loginText, loginpwd);
        //كون الدالة getUser تُرجع مجموعة نتائج فيجب حفظها في مجموعة نتائج هنا
                int counter = 0;
                try {
                    while (userRow.next()) {    //بينما يوجد نتيجة تالية في مجموعة النتائج
                        counter++;
                    }
                    if (counter == 1) { // يجب أن يكون لدينا نتيجة واحدة أي مستخدم واحد
                        System.out.println("Login Successful!!!");
                    } else {    // غير ذلك أي أننا لم نحصل على ناتج من قاعدة البيانات التي أعطت مجموعة النتائج فارغة
                        label.setText("wrong username or password!");
                        Shaker shaker = new Shaker(loginUsername);  //اهتزاز حقل اسم المستخدم 
                        shaker.shake();
                        Shaker shaker1 = new Shaker(loginPassword);
                        shaker1.shake();
                    }
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
});
    }
{% endhighlight %}


قم الآن بتشغيل الكود وأدخل معلومات المستخدم الذي أدخلته سابقا في جدول Users في قاعدة البيانات، أنا لدي البيانات "admin" لكلا اسم المستخدم وكلمة المرور، اضغط على تسجيل الدخول، إذا ظهرت في طرفية IntelliJ رسالة "Login Successful!!!" فهذا يعني أن كل شيئ على مايرام.

يمكنك معاينة الكود حتى الوضع الحالي من [هنا](https://github.com/Mulham/Java-Project/tree/login)

*****

**التالي:** [الانتقال بين النوافذ](/javafx-scene-changer)



