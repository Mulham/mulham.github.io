---
date: 2021-03-02
title: الانتقال بين النوافذ في تطبيق جافا إف إكس
description: كيفية تغيير النوافذ والانتقال بينهم في تطبيق JavaFX
hidden : true
---

> هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)
{: .prompt-info }

بعد تصميم وبرمجة نافذة تسجيل الدخول قم الآن في محرر الكود IntelliJ بالضغط باليمين على مجلد view ثم New ثم FXML File وسمها main.fxml لإنشاء النافذة الرئيسية التي سيتم عرضها بعد تسجيل الدخول.

قم بفتح هذه النافذة في محرر الواجهة بالضغط على الملف باليمين واختيار Open in Scene Builder 

قم بتصميم هذه النافذة بالشكل الذي ترغب وكما هو موضح سابقًا في صفحة [تصميم الواجهة](/javafx-interface-design).

ستكون النافذة الرئيسية لدي أنا على الشكل التالي (حيث قمت بإضافة مجلد assets وإضافة الأيقونات التي أرغب بإضافتها للنافذة إليه):

![النافذة الرئيسية في تطبيق جافا إف إكس](https://raw.githubusercontent.com/Mulham/Java-Project/images/images/UI2.png)


وستكون مرتبطة بملف الجافا MainController، والربط هذا قم تم شرحه سابقا أيضًا.

لنقم الآن بعمل صنف (كلاس) جافا وظيفته تغيير النافذة المعروضة للمستخدم.

قم بالضغط باليمين على مجلد controller ثم New ثم Java Class وسمه SceneController (حيث النافذة تُدعى عمومًا Scene أو مشهد).

وسيكون محتوى الملف على الشكل التالي:

```java

package sample.controller;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.stage.Stage;

import java.io.IOException;

public class SceneController {

    public void changeScene(Button button, String scene ){
        button.getScene().getWindow().hide();   // إخفاء النافذة الحالية
        FXMLLoader loader   = new FXMLLoader();
        loader.setLocation(getClass().getResource("/sample/view/" + scene));
        try{
            loader.load();  // تحميل النافذة الجديدة
        } catch (IOException e){
            e.printStackTrace();
        }
        Parent root = loader.getRoot();
        Stage stage = new Stage();
        stage.setScene(new Scene(root));
        stage.show();   // عرض النافذة الجديدة
    }
}
```

وعلى غرار الدالة هذه (changeScene) سأضيف دالة أخرى لإمكانية استخدام صورة بدل زر (سيختلف فقط البارامتر الأول وسيصبح من نوع صورة بدل زر):


```java
  public void changeSceneImage(ImageView image, String scene ){
        image.getScene().getWindow().hide();
        FXMLLoader loader   = new FXMLLoader();
        loader.setLocation(getClass().getResource("/sample/view/" + scene));
        try{
            loader.load();
        } catch (IOException e){
            e.printStackTrace();
        }
        Parent root = loader.getRoot();
        Stage stage = new Stage();
        stage.setScene(new Scene(root));
        stage.show();
    }
```

والآن في نافذة تسجيل الدخول، وعند تسجيل الدخول بنجاح فسيتم تغيير النافذة للنافذة الرئيسية، لنبرمج ذلك. اذهب لملف LoginController، أسفل السطر:

        private DatabaseHandler databaseHandler; 

قم بإضافة السطر التالي لاستدعاء صنف تغيير النوافذ:

          private SceneController sceneController;

ثم أسفل سطر:

        databaseHandler = new DatabaseHandler();


قم بإضافة السطر التالي لإنشاء عنصر من ذلك الصنف:

        sceneController = new SceneController();


الآن أصبحنا جاهزين لاستخدام دالة changeScene الموجودة في صنف SceneController.

أسفل السطر التالي:

        System.out.println("Login Successful!!!");

أضف التالي:

        sceneController.changeScene(loginButton, "main.fxml");


وبالتالي عند تسجيل الدخول بنجاح سيتم استدعاء دالة changeScene والانتقال لنافذة main.fxml وبالتالي حققنا المطلوب.

شغل البرنامج وتأكد من عمله بالشكل المطلوب.

النافذة الرئيسية لدي هي عبارة عن أزرار تقوم فقط بنقل المستخدم لنوافذ أخرى.

كما أن زر تسجيل الخروج أيضا يقوم بنقل المستخدم لنافذة تسجيل الدخول، في الواقع فإن آلية تسجيل الخروج لا تتم بهذه الطريقة ولكنها تحتاج لشرح مستقل، لذا سنكتفي بتغيير النافذة هنا عند تسجيل الخروج. 

يمكنك معاينة الكود في الوضع الحالي من [هنا](https://github.com/Mulham/Java-Project/tree/SceneChanger)

****

**التالي:** [إدارة المستخدمين](/javafx-manage-users)



