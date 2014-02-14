<?php

//Connect to Cloud SQL
$conn = mysql_connect(":/cloudsql/<appid>:<dbinstance>","root","Ove52SWE");
if(!$conn){
	die('Connect Error(' . mysql_error());
}

$db_selected = mysql_select_db('bigstars', $conn);
if(!$db_selected){
	die('can\'t use db (' . mysql_error());
}

$result = mysql_query("Select * from stars");

echo "<h3>Result from Google Cloud SQL</h3>";
echo "<table>";
echo "<th>name</th>";
echo "<th>size</th>";

while($row = mysql_fetch_assoc($result)){
	echo "<tr>";
	echo "<td>" . $row['name'] . "</td>";
	echo "<td>" . $row['size'] . "</td>";
	echo "</tr>";
}
echo "</table>";
?>


