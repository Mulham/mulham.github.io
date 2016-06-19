---
layout: post
title: "سكريبت php بسيط لرفع ملف"
date: 2016-06-19
---

نقدم لكم سكريبت بسيط بلغة php لرفع ملف .


يستخدم هذا السكريبت لرفع صور أو ملفات من نوع آخر لسيرفرك ،<!--more--> حيث يحتوي على نموذج بلغة `HTML` فيه حقل لرفع ملف ، و كود `php` والذي يتأكد من نوع الملف (لاحقته) ، حجم الملف ، العرض والطول بالنسبة للصور ، ويقوم برفع الملف اذا لم يكن هناك أخطاء .


يمكنك في السكريبت تحديد نوع الملفات المسموحة (عبر اللاحقة )، الحجم الأعظمي المسموح للملف و الطول والعرض الأعظميين المسومح بهما للصور.


يتم حفظ الملف في مجلد `upload` (أو المجلد الذي تحدده في متغير `uploadpath$` )  ، هذا المجلد يجب إنشاؤه في نفس المكان الذي يوضع فيه ملف الـ `php` الحاوي على هذا السكريبت . يجب أن تكون php لديها صلاحيات الكتابة في هذا المجلد `( chmod 0755 / 0777 )` حتى تتمكن من حفظ الملف .


بعد رفع الملف بنجاح سيقوم السكريبت بعرض عنوان الملف على السيرفر .


الكود :

{% highlight php %}

<?php
// Simple PHP Upload Script:  http://coursesweb.net/php-mysql/

$uploadpath = 'upload/';      // directory to store the uploaded files
$max_size = 2000;          // maximum file size, in KiloBytes
$alwidth = 900;            // maximum allowed width, in pixels
$alheight = 800;           // maximum allowed height, in pixels
$allowtype = array('bmp', 'gif', 'jpg', 'jpe', 'png');        // allowed extensions

if(isset($_FILES['fileup']) && strlen($_FILES['fileup']['name']) > 1) {
  $uploadpath = $uploadpath . basename( $_FILES['fileup']['name']);       // gets the file name
  $sepext = explode('.', strtolower($_FILES['fileup']['name']));
  $type = end($sepext);       // gets extension
  list($width, $height) = getimagesize($_FILES['fileup']['tmp_name']);     // gets image width and height
  $err = '';         // to store the errors

  // Checks if the file has allowed type, size, width and height (for images)
  if(!in_array($type, $allowtype)) $err .= 'The file: <b>'. $_FILES['fileup']['name']. '</b> not has the allowed extension type.';
  if($_FILES['fileup']['size'] > $max_size*1000) $err .= '<br/>Maximum file size must be: '. $max_size. ' KB.';
  if(isset($width) && isset($height) && ($width >= $alwidth || $height >= $alheight)) $err .= '<br/>The maximum Width x Height must be: '. $alwidth. ' x '. $alheight;

  // If no errors, upload the image, else, output the errors
  if($err == '') {
    if(move_uploaded_file($_FILES['fileup']['tmp_name'], $uploadpath)) { 
      echo 'File: <b>'. basename( $_FILES['fileup']['name']). '</b> successfully uploaded:';
      echo '<br/>File type: <b>'. $_FILES['fileup']['type'] .'</b>';
      echo '<br />Size: <b>'. number_format($_FILES['fileup']['size']/1024, 3, '.', '') .'</b> KB';
      if(isset($width) && isset($height)) echo '<br/>Image Width x Height: '. $width. ' x '. $height;
      echo '<br/><br/>Image address: <b>http://'.$_SERVER['HTTP_HOST'].rtrim(dirname($_SERVER['REQUEST_URI']), '\\/').'/'.$uploadpath.'</b>';
    }
    else echo '<b>Unable to upload the file.</b>';
  }
  else echo $err;
}
?> 
<div style="margin:1em auto; width:333px; text-align:center;">
 <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data"> 
  Upload File: <input type="file" name="fileup" /><br/>
  <input type="submit" name='submit' value="Upload" /> 
 </form>
</div>

{% endhighlight %}

إذا تم رفع الملف بنجاح ، سيقوم السكريبت بتقديم معلومات كما في المثال التالي


		File: image.jpg successfully uploaded:

		File type: image/jpeg

		Size: 16.545 KB

		Image Width x Height: 300 x 200


		Image address: http://domain/upload/image.jpg
