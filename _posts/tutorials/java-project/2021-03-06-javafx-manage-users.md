---
date: 2021-03-02
title: إدارة المستخدمين في تطبيق جافا إف إكس
description: كيفية برمجة تطبيق جافا إف إكس لحذف وتعديل وإضافة مستخدمين وباستخدام قواعد بيانات MySQL
hidden : true
---


> هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)
{: .prompt-info }

لنقم الآن بإنشاء نافذة إدارة المستخدمين حيث يمكن للمدير أن يضيف أو يعدل أو يحذف مستخدما ما.

وبالتالي سنقوم بعمل نافذتين، نافذة لعرض المستخدمين الموجودين ونافذة لإضافة مستخدم، وسنستخدم الأخيرة (نسخة منها) لتعديل بيانات المستخدم حيث ستظهر بياناته في نموذج الإضافة نفسه لإمكانية تعديلها.

اضغط باليمين على المجلد view واختر New ثم FXML File وسمه users وهي النافذة التي سنعرض فيها المستخدمين الموجودين في قاعدة البيانات.

الجديد في النافذة هذه والتي تعرض المستخدمين الموجودين، هو الجدول، وهو في محرر الواجهة باسم TabelView وستجد أنك عندما تضيفه سيحوي عمودَين، يمكنك النقر باليمين على أحد الأعمدة واختيار Duplicate لإضافة عمود جديد أو Delete لحذفه، كما يمكنك تغيير عرض أحد الأعمد بالنقر على حافته اليمنى أو اليسرى والسحب. وبالنسبة لتغيير اسمه ومعلوماته وإعطائه id مخصص فيتم من قائمة الخصائص على اليمين (حيث يجب إعطاء id لكل عمود). ستكون النافذة لدي على الشكل التالي:

![نافذة إدارة المستخدمين في تطبيق جافا إف إكس](https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-users-window.png)

طبعا تلك النافذة يجب أن يتم ربطها مع controller لذا بعد نسخ المحتوى من محرر الواجهة (من خيار sample skeleton الموضح سابقا في صفحة [تصميم الواجهة](/javafx-interface-design/#إضافة-مايلزم-للبرمجة)) اضغط (في محرر الكود IntelliJ) باليمين على المجلد controller ثم New ثم Java Class وسمه UserController والذي ستلصق الكود الخاص به من محرر الواجهة كما ذكرنا.

ولكن هنا يجب تغيير محتوى UserController قليلًا..فمثلا سيقوم محرر الواجهة بإعطائك حقل الجدول على الشكل التالي:

        @FXML
        private TableView<?> table;

إشارة الاستفهام هذه يجب تبديلها بنوع الكائن الذي سيحتويه الجدول، والذي سيكون في حالتنا User، كذلك بالنسبة للأعمدة، فمثلا أول عمود تجده في الصورة أعلاه هو الـ id الخاص بالمستخدم والذي سيعطيه محرر الواجهة بالشكل التالي:

         @FXML
            private TableColumn<?, ?> tableId;

قم باستبدال إشارة الاستفهام الأولى بنوع الكائن كما ذكرنا وهو User والثانية بنوع المتغير الذي سيحتويه العمود وهو في هذا العمود سيكون رقم صحيح أي Integer وبالتالي بعد التعديل سيصبح:



         @FXML
            private TableColumn<User, Integer> tableId;

وهكذا.. علمًا أن حقل التاريخ سيكون نوعه Date.

والآن يجب علينا أن نتعلم شيئًا جديدًا، وهو ال model.. أو ببساطة العناصر. الآن من الواضح أنه سيكون لدينا مستخدمين في التطبيق، ولكل مستخدم معلومات عديدة (الاسم الكنية كلمة السر..الخ) ولهذا السبب يجب إنشاء صنف يُعرِّف المستخدم والمعلومات التي سيحتويها (القالب وليس بيانات فعلية يعني فقط متغير الاسم ومتغير الكنية وهكذا دون إعطائهم قيم - باختصار فهم أسماء الأعمدة في جدول المستخدمين في قاعدة البيانات)، وعندها يمكننا أن نأخذ عنصر من هذا الكائن ونتعامل معه بالشكل الذي نريد.

ألم تفهم شيئًا؟

دعني أشرح لك بضعة حالات لاستخدام عناصر الكائن "المستخدم": عندما أريد عرض المستخدم على الجدول فسأعرضه بكامل معلوماته أو جزء منها، عندما أريد حذف مستخدم من الجدول فيكفي أن أحذفه بناء على رقم الـ id الخاص به، وعندما أريد تعديل بياناته فسيلزمني استدعاء جميع معلوماته لعرضها للمستخدم حتى يعدل ما يشاء.. إذًا مرة أحتاج الـ id فقط، ومرة أحتاج كل المعلومات ومرة جزء منها، لابد إذًا من أن يكون هناك عنصر أستطيع أن آخذ منه أي معلومة أريدها في الوقت الذي أشاء، لذا فإن User (يبدأ بحرف كبير) سيكون هو الصنف وهو عبارة عن قالب يحوي المتغييرات فقط، أسماء المتغييرات، ومنه سآخذ عنصر user (يبدأ بحرف صغير) وأعطيه قيم لتلك المتغيرات.

وبالتطبيق أيضا ستفهم أكثر، لذا قم بالضغط على مجلد model ثم New ثم Java Class وسمه User، ثم اكتب جميع الأعمدة التي يحتويها جدول المستخدمين في قاعدة البيانات، على الشكل التالي:

        private Integer idUser;
        private String Name;
        private String Surname;
        private String Level;
        private String password;
        private LocalDate Certificate_date;

**ملاحظة:** ستحتاج لاستيراد مكتبة LocalDate. ودائمًا عند ظهور خطأ باللون الأحمر يمكنك وضع مؤشر الفأرة عنده ليقوم محرر الكود بإعطاء اقتراح لحله، وفي مثل هذا الحال سيظهر زر يقترح استيراد المكتبة، فقط انقر عليه وسيضيف لك المحرر السطر المناسب تلقائيًا.


والآن لإنشاء setters و getters وهم الدالات التي تقوم بإعطاء قيم لهذه المتغيرات أو عرضها عند الحاجة، حيث لايمكن مشاهدة أو ضبط قيم هذه المتغيرات مباشرة كونهم من نوع private أي خاص. وهكذا يجب أن تسير الأمور في لغة جافا.

الآن لإنشاء تلك الدالات اضغط من الأعلى بجانب file على القائمة code ثم Generate ثم Getter and Setter ثم اختر جميع المتغيرات من القائمة واضغط ok.

أخيرا يجب أن نضيف باني أو أكثر لهذا الصنف، والباني أو Consturctor هي دالة تحمل نفس اسم الصنف ويتم استخدامها تلقائيًا عند إنشاء عنصر من ذلك الصنف، فعند إنشاء عنصر من صنف ما وإعطاء بارامترين عند الإنشاء، هذا يعني أن هناك باني في ذلك الصنف يتطلب بارامترين وسيتم استدعاءه تلقائيا في تلك الحالة، وهكذا.

(أنصح بمراجعة فقرة "مفهوم الكونستركتور في جافا" في الصفحة [هذه](https://harmash.com/java/java-class-and-object/) من موقع "هرماش")

لإتمام الصنف هذا ووفقا لمشروعنا هنا فسأقوم بإنشاء باني يتطلب جميع معلومات المستخدم عدا الـ id وآخر مع الـ id:

```java

public User(String name, String nachname, String level, String password, LocalDate zertifikat_datum) {
        Name = name;
        Nachname = nachname;
        Level = level;
        this.password = password;
        Zertifikat_datum = zertifikat_datum;
    }
    public User(Integer id_User, String name, String nachname, String level, LocalDate zertifikat_datum, String password) {
        idUser = id_User;
        Name = name;
        Nachname = nachname;
        Level = level;
        this.password = password;
        Zertifikat_datum = zertifikat_datum;
    }
```

لنذهب الآن لملف (صنف) UserController، وسنقوم في بدايته بإضافة الأسطر التالية لاستخدام صنف User وغيره في هذا الصنف:


        import sample.Database.DatabaseHandler;
        import sample.animations.Shaker;
        import sample.model.User;


ثم قبل السطرين التاليين:

        @FXML
            void initialize() {

سنضيف التالي (كالعادة لإنشاء عنصر من صنق قاعدة البيانات وعنصر من صنف تغيير النافذة):

        DatabaseHandler databaseHandler;
        private SceneController sceneController;

ولكننا سنضيف التالي أيضا لحفظ النتائج القادمة من قاعدة البيانات لها (ضمن قائمة) سميناها oblist اختصارا:

        ObservableList<User> oblist = FXCollections.observableArrayList();

وستحتاج لإضافة المكتبتين التالييتين في بداية ملف UserController للتعرف على السطر السابق:

        import javafx.collections.FXCollections;
        import javafx.collections.ObservableList;


## عرض المستخدمين

لعرض المستخدمين في الجدول لدينا يجب في البداية كتابة الدالة في صنف DatabaseHandler والتي تستخرج جميع المستخدمين وبياناتهم من جدول المستخدمين في قاعدة البيانات، لذا سنضيف الدالة التالية لصنف DatabaseHandler:

```java

public ResultSet getTable(String table){    // لاحظ أن الدالة تأخذ بارامتر واحد وهو اسم الجدول وبالتالي يمكن استخدامها لإعطاء بيانات أي جدول نريده وذلك فقط بتغيير الاسم في البرامتر عند الاستدعاء
        ResultSet resultset = null;
        String query = "SELECT * FROM mydb." + table;
        try {
            resultset = getDbConnection().createStatement().executeQuery(query);

        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return  resultset;  // تقوم الدالة بالتالي بإرجاع معلومات الجدول كاملة أي كل الأسطر التي يحتويها أو ستكون خالية إذا كان الجدول فارغا
    }
```


بعد ذلك في صنف UserController وخارج دالة initialize سنقوم بإضافة الدالة التي تعرض محتويات الجدول عند عرض النافذة، ولاحظ إضافة جميع محتويات الجدول القادم من قاعدة البيانات للقائمة oblist وفي آخر سطر نقوم بضبط محتوى الجدول في النافذة هنا على محتويات القائمة oblist:


```java


 public void tableView(){
        databaseHandler = new DatabaseHandler();
        try{
            ResultSet rs = databaseHandler.getTable("Users");


            while (rs.next()) { // أي بينما يوجد سطر آخر في النتائج القادمة من قاعدة البيانات
            // أسماء الحقول أدناه من Name و Nachname يجب أن تطابق أسماء المتغيرات في صنف User
                oblist.add(new User(rs.getInt("idUser"),rs.getString("Name"), rs.getString("Nachname")
                        , rs.getString("Level"),rs.getDate("Zertifikat_datum").toLocalDate(), rs.getString("password")));   // إنشاء عنصر من المستخدم وإضافة كافة معلومات السطر له ثم إضافتها للقائمة
            } } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

        tableId.setCellValueFactory(new PropertyValueFactory<>("idUser"));  
        //الحقل أعلاه idUser وما يوازيه أدناه يجب أن يطابق اسم العمود في قاعدة البيانات
        table_name.setCellValueFactory(new PropertyValueFactory<>("Name")); 
        table_surname.setCellValueFactory(new PropertyValueFactory<>("Nachname"));
        table_level.setCellValueFactory(new PropertyValueFactory<>("Level"));
        table_date.setCellValueFactory(new PropertyValueFactory<>("Zertifikat_datum"));
        table_pass.setCellValueFactory(new PropertyValueFactory<>("password"));
        table.setItems(oblist); // ضبط عناصر الجدول وفق عناصر القائمة
    }

```




حيث يتم استدعاء هذه الدالة مباشرة عند الضغط على زر "المستخدمين" في النافذة الرئيسية، أي في صنف MainController (وضمن دالة initialize):

```java
 mainUsers.setOnAction(event -> {
            mainUsers.getScene().getWindow().hide();
            try {
                FXMLLoader loader = new FXMLLoader(getClass().getResource("/sample/view/users.fxml"));
                Parent root = (Parent) loader.load();
                UserController userController = loader.getController();
                userController.tableView(); // استدعاء دالة عرض الجدول
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
            }catch  (IOException e){
                e.printStackTrace();
            }       });

```

لاحظ أننا لم نستخدم دالة changeScene من صنف SceneController هنا، وذلك بسبب حاجتنا لاستدعاء بيانات من قاعدة البيانات واستدعاء دالة من صنف النافذة الجديدة أثناء تغيير النافذة. 

الآن قم بتشغيل التطبيق، ويجب أن ترى عند الذهاب لنافذة المستخدمين المستخدم admin في الجدول.

## حذف مستخدم

لحذف المستخدم يتوجب علينا إضافة دالة لقاعدة البيانات تقوم بحذف المستخدم المطلوب من قاعدة البيانات، وكذلك يجب إضافة دالة في صنف UserController لضبط زر الحذف بالشكل الصحيح والتي ستستدعي أيضا دالة tableView لتحديث الجدول المعروض في النافذة.

لنقم أولا بإضافة دالة الحذف للصنف DatabaseHandler:

```java

  public boolean deleteUser(User user) {
        String delete = "DELETE FROM Users " + " Where idUser" + " = ?";
        try {
            PreparedStatement preparedStatement = getDbConnection().prepareStatement(delete);
            preparedStatement.setInt(1, user.getId());
            preparedStatement.execute();
            return true;
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
            return false;
        }
    }

```

ثم في صنف UserController وضمن دالة initialize سنضيف التالي:

```java

        sceneController = new SceneController();

        mainLogout.setOnAction(event -> {       // زر تسجيل الخروج
            sceneController.changeScene(mainLogout, "login.fxml");
        });
        table_back.setOnAction(event -> {       // زر العودة للخلف
            sceneController.changeScene(table_back, "main.fxml");
        });

         user_delete.setOnAction(event ->{      زر حذف مستخدم
            User user = table.getSelectionModel().getSelectedItem();    // إنشاء عنصر من المستخدم والذي سيكون العنصر الذي تم تحديده في الجدول
            if (!table.getSelectionModel().isEmpty()){  // إذا قام المستخدم بتحديد عنصر من الجدول
                boolean check = databaseHandler.deleteUser(user);   // إرسال المستخدم لدالة الحذف في صنف قاعدة البيانات
                if (check){     // جيث ترجع تلك الدالة صح إذا تم الحذف بشكل صحيح
                    radiographer_label.setText("User deleted Successfully!");
                    oblist.clear(); // إفراغ القائمة ليتم بناؤها من جديد في السطر الذي يليه وبالتالي لا يتم عرض محتوى الجدول مرتين
                    tableView();    // استدعاء دالة عرض الجدول التي تقوم بدورها بملء القائمة وفقا للبيانات الحالية في قواعد البيانات
                    FadeTransition fadeTransition = new FadeTransition(Duration.millis(5000),radiographer_label);
                    fadeTransition.setFromValue(1f);
                    fadeTransition.setToValue(0f);
                    fadeTransition.setCycleCount(1);
                    fadeTransition.play();
                }
                else{
                    radiographer_label.setText("User couldn't be deleted!");
                }
            }else{
                radiographer_label.setText("You should select an Item");
            }
        });
```

**ملاحظة:** في الشرط أعلاه (if (check تعني 

          if (check == true)

## إضافة مستخدم

بنفس الطريقة سنضيف دالة إضافة مستخدم لقاعدة البيانات في صنف DatabaseHandler:

```java

public boolean addUser(User user) {
            String insert = "INSERT INTO Users " + " (Name, Nachname, Level, Zertifikat_datum, password) VALUES (?,?,?,?,?);";
            try {
                PreparedStatement preparedStatement = getDbConnection().prepareStatement(insert);
                preparedStatement.setString(1, user.getName());
                preparedStatement.setString(2, user.getNachname());
                preparedStatement.setString(3, user.getLevel());
                preparedStatement.setDate(4, Date.valueOf(user.getZertifikat_datum()));
                preparedStatement.setString(5, user.getPassword());
                preparedStatement.executeUpdate();
                return true;
            } catch (SQLException | ClassNotFoundException e) {
                e.printStackTrace();
                return false;
            }
        }
```

والآن سنحتاج لإنشاء نافذة جديدة مع controller جديد، حيث أن زر إضافة مستخدم سيقوم بالتحويل لنافذة إضافة مستخدم حيث يتم إدخال البيانات، وعند الضغط هناك على زر إضافة يتم استدعاء الدالة أعلاه لإضافة تلك البيانات لجدول المستخدمين في قاعدة البيانات، النافذة الخاصة بإضافة مستخدمين لدي ستكون على الشكل التالي (addUser.fxml):

![نافذة إضافة مستخدم في تطبيق جافا إف إكس](https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-add-user-window.png)

وفي صنف AddUserController سيكون زر إضافة المستخدم مبرمج في الشكل التالي (ضمن دالة initialize):

         addButton.setOnAction(event -> {
                    createUser();
               });


حيث دالة createUser (خارج دالة initialize):

```java

    private void createUser(){
        DatabaseHandler databaseHandler = new DatabaseHandler();
        String Name = addName.getText();
        String Nachname = addSurname.getText();
        String Level = addLevel.getText();
        LocalDate date = addDate.getValue();
        String pass = addPassword.getText();
        boolean check = false;
            User user = new User(Name,Nachname,Level,pass,date);
            check = databaseHandler.addUser(user);

        if (check){
            addName.setText("Name");
            addSurname.setText("Surname");
            addLevel.setText("Level");
            addDate.getEditor().clear();
            addPassword.setText("Password");
            addLabel.setText("User has been added Successfully!");
            FadeTransition fadeTransition = new FadeTransition(Duration.millis(5000),addLabel);
            fadeTransition.setFromValue(1f);
            fadeTransition.setToValue(0f);
            fadeTransition.setCycleCount(1);
            fadeTransition.play();
        } else{
            addLabel.setText("User Couldn't be added!");
        }
    }

```

لاحظ أنني هنا في زر الرجوع لنافذة المستخدمين أيضا لن أستخدم دالة changeScene بسبب حاجتي لاستدعاء دالة tableView، لذا سيكون زر الرجوع هنا بالشكل التالي:

```java

 table_back.setOnAction(event -> {
            table_back.getScene().getWindow().hide();
            try {
                FXMLLoader loader = new FXMLLoader(getClass().getResource("/sample/view/users.fxml"));
                Parent root = (Parent) loader.load();
                UserController userController = loader.getController();
                userController.tableView();
                Stage stage = new Stage();
                stage.setScene(new Scene(root));
                stage.show();
            }catch  (IOException e){
                e.printStackTrace();
            }       });
    }

```

في صنف UserController لاننسى ربط زر الإضافة بدالة تغيير النوافذ للذهاب للنافذة الجديدة:


         addUser.addEventHandler(MouseEvent.MOUSE_CLICKED, event -> {

                    sceneController.changeSceneImage(addUser, "addUser.fxml");
                        }

                        );

قم بتشغيل البرنامج الآن وجرب إضافة مستخدم ثم حذفه للتأكد من أن كل شيئ تم بالشكل الصحيح.

**ملاحظة**: جميع حقول إضافة المستخدم إجبارية ويجب ألا تكون فارغة وإلا سينتج خطأ في البرنامج بسبب تمرير عبارات فارغة في SQL.

يمكنك معاينة الكود في الوضع الحالي من [هنا](https://github.com/Mulham/Java-Project/tree/addUser)

الآن لإمكانية تعديل بيانات مستخدم يتوجب علينا إرسال بياناته لنافذة التعديل حتى يتم عرضها ونتمكن من تعديلها، ولكن كيف يمكن لنا إرسال بيانات ومعلومات المستخدم من نافذة ﻷخرى؟ تابع الصفحة القادمة للتعرف على ذلك.

****


**التالي:** [إرسال بيانات من نافذة ﻷخرى](/javafx-transfer-data-between-scenes)




