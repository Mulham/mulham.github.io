---
date: 2021-03-02
title: تبادل البيانات بين الأصناف في جافا إف إكس
description: كيفية إرسال بيانات ومعلومات من صنف لآخر ومن نافذة لأخرى في جافا وجافا FX
hidden : true
---

> هذه الصفحة جزء من شرح [بناء تطبيق جافا إف إكس من الصفر](/java-project-from-scratch)
{: .prompt-info }

إذًا لإمكانية تعديل بيانات مستخدم يجب علينا أن نرسل بياناته الموجودة والتي نرغب بتعديلها إلى نافذة التعديل.

لنقم أولًا بإضافة الدالة التي تقوم فعليا بتعديل البيانات في قواعد البيانات في صنف DatabaseHandler:


```java
    public boolean editUser(User user) {
        String edit = "update Users " + " set Name = ?, Nachname = ?, Level = ?, Zertifikat_datum = ?, password = ?"
                +" Where idUser" + " = ?";
        try {
            PreparedStatement preparedStatement = getDbConnection().prepareStatement(edit);
            preparedStatement.setString(1, user.getName());
            preparedStatement.setString(2, user.getNachname());
            preparedStatement.setString(3, user.getLevel());
            preparedStatement.setString(4, String.valueOf(user.getZertifikat_datum()));
            preparedStatement.setString(5, user.getPassword());
            preparedStatement.setInt(6, user.getId());
            preparedStatement.executeUpdate();
            return true;
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
            return false;
        }
    }
```

لنقم بإنشاء نافذة editUser.fxml والتي ستكون بنفس محتوى addUser ولكن سيختلف فقط رز Add ويصبح Update، النافذة لدي ستصبح على الشكل التالي:

![نافذة تعديل مستخدم في تطبيق جافا FX](https://raw.githubusercontent.com/Mulham/Java-Project/images/images/gluon-edit-users-window.png)


ثم في صنف EditUserController سأقوم بإنشاء دالة getInfo والتي تأخذ بيانات المستخدم الذي تم تحديده من الجدول وتعرضه في النموذج لدينا (كما دمجت زر تحديث البيانات ضمن الدالة):


```java
 public void getInfo(User user){
       addName.setText(user.getName());
       addSurname.setText(user.getNachname());
       addLevel.setText(user.getLevel());
       addDate.getEditor().setText(String.valueOf(user.getZertifikat_datum()));
       idLabel.setText(String.valueOf(user.getId()));
       updateButton.setOnAction(event -> {
            databaseHandler = new DatabaseHandler();
            User rg = new User( user.getId() , addName.getText(),addSurname.getText(),
                    addLevel.getText(),addDate.getValue(), addPassword.getText() );
            boolean check = databaseHandler.editUser(rg);
            if (check){
                addLabel.setText("User updated successfully!");
                FadeTransition fadeTransition = new FadeTransition(Duration.millis(5000),addLabel);
                fadeTransition.setFromValue(1f);
                fadeTransition.setToValue(0f);
                fadeTransition.setCycleCount(1);
                fadeTransition.play();
            }
            else{
                addLabel.setText("Couldn't update the user!");
            }
       });
    }
```

وأخيرا في صنف UserController لنقم ببرمجة زر التعديل حيث يتم استدعاء دالة getInfo وتمرير المستخدم المحدد في الجدول إليها، وهذه هي طريقة إرسال بيانات من صنف لآخر أي من نافذة ﻷخرى:

```java

user_edit.setOnAction(event -> {
            User user = table.getSelectionModel().getSelectedItem();    // إنشاء عنصر من صنف المستخدم حيث معلوماته تكون من  السطر المحدد في الجدول
            if (!table.getSelectionModel().isEmpty()){  // إذا قام المستخدم بتحديد سطر من الجدول
                user_edit.getScene().getWindow().hide();
                try {
                    FXMLLoader loader = new FXMLLoader(getClass().getResource("/sample/view/editUser.fxml"));
                    Parent root = (Parent) loader.load();
                    EditUserController editUserController = loader.getController();
                    editUserController.getInfo(user);   // إرسال عنصر المستخدم مع كافة بياناته كبارامتر للدالة الموجودة في صنف التعديل
                    Stage stage = new Stage();
                    stage.setScene(new Scene(root));
                    stage.show(); 
                }catch  (IOException e){
                    e.printStackTrace();
                }
            }
            else{
                radiographer_label.setText("You should select an Item");
            }


        });
```


والآن قم بتجربة البرنامج وتجربة وظيفة التعديل الجديدة فيه.


يمكنك معاينة الكود في الوضع الحالي من [هنا](https://github.com/Mulham/Java-Project/tree/editUser)

*****

**التالي:** [النهاية](/javafx-working-process)

