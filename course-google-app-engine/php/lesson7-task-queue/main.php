<?php
require_once 'google/appengine/api/taskqueue/PushTask.php';
use google\appengine\api\taskqueue\PushTask;

echo 'Hello World';
$task = new PushTask('/task.php');
$task_name = $task->add();
?>