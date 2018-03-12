<!-- This Code is executed upon form submit -->
<?php session_start();
//$id = $_SESSION['sessionid'] . ".csv";
//echo $id;
$mysqli=new mysqli("localhost", "admin", "weblogger", "mouse_log");

if ($mysqli->connect_error) {
    echo "Connection failed: " . $mysqli->connect_error;
}
//Inserts data into file
$retrieve_stmt = $mysqli->stmt_init();
if($retrieve_stmt->prepare("SELECT * INTO OUTFILE 'mouse_log.csv' FROM mouse_data")) {
	//$retrieve_stmt->bind_param('s',$id);
	$retrieve_stmt->execute();
	
	//clears out database and resets auto increment
	//$clean_stmt = $mysqli->stmt_init();
	if($mysqli->query("TRUNCATE TABLE mouse_data;")) {
		//$clean_stmt->execute();
	}else {
		echo "failed";
	}
}else {
	echo "Failed";
}

?>
