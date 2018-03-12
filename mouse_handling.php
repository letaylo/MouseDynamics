<?php session_start();
//Place this part in the login page
//session_regenerate_id();
$_SESSION['sessionid'] = session_id();


$id = $_SESSION['sessionid'];
//echo $id; //for testing, remove this
//echo $_POST['xpos'];
/*if (!isset($_SESSION['user'])){
	header('Location: index.php');
}*/

if ( isset($_POST['events']) && isset($_POST['xpos']) && isset($_POST['ypos']) && isset($_POST['timestamp'])){ //Check if the form was submitted
	$failed=0; //Set default end code
	echo "test";
	$mysqli=new mysqli("localhost", "admin", "weblogger", "mouse_log");	//Connect to database
	if ($mysqli->connect_errno) {
		echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error . " ";
		$failed=1;
	} else {
		$mysqli->set_charset('utf8');		
		//Insert into database		
		/*
		$fetch = "SELECT session_id,timestamp,rel_time,xpos,ypos,vs FROM mouse_data WHERE entry_id=(SELECT max(entry_id) FROM mouse_data)";
		$result = $mysqli->query($fetch);
		$followingdata = $result->fetch_assoc();
		$xpos = $followingdata['xpos'];
		$ypos = $followingdata['ypos'];
		$rel_time = $followingdata['rel_time'];
		$session = $followingdata['session_id'];
		$speed = $followingdata['vs'];
		$timestamp = $followingdata['timestamp'];
		if ($_POST['timestamp'] != $timestamp || mysqli_num_rows($result) == 0 ) {
			$vx = 0;
			$vy = 0;
			$vs = 0;
			$dt = 0;
			$a = 0;
			$angle = 0;
		} else if ( $_POST['rel_time'] > ($rel_time + 150) ) {
			$dx = $_POST['xpos'] - $xpos;
			$dy = $_POST['ypos'] - $ypos;
			$vx = 0;
			$vy = 0;
			$vs = 0;
			$dt = ( $_POST['rel_time'] - $rel_time ) / 1000;
			$a = 0;
			$angle = atan($dy/$dx); 
		} else {
			$dt = ( $_POST['rel_time'] - $rel_time ) / 1000;
			$dx = $_POST['xpos'] - $xpos;
			$dy = $_POST['ypos'] - $ypos;
			$vx = $dx / $dt;
			$vy = $dy / $dt;
			$vs = sqrt( ($vx**2) + ($vy**2) );
			$a = abs( $vs - $speed ) / $dt;
			$angle = atan($dy/$dx);
			$dt = 0;
		}*/
		//$stmt = $mysqli->prepare("INSERT INTO mouse_data(session_id,timestamp,xpos,ypos,l_mousedown,l_mouseup,r_mousedown,r_mouseup,m_mousedown,m_mouseup) VALUES $id,$_POST['timestamp'],$_POST['xpos'],$_POST['ypos'],$_POST['l_down'],$_POST['l_up'],$_POST['r_down'],$_POST['r_up'],$_POST['m_down'],$_POST['m_up']");
		//$stmt->execute();
		if (!($stmt = $mysqli->prepare("INSERT INTO mouse_data(event,session_id,timestamp,xpos,ypos) VALUES (?,?,?,?,?)"))) {
			echo "Prepare failed: (" . $mysqli->errno . ") " . $mysqli->error . " ";
			$failed=5;
		} else {
			if (!$stmt->bind_param("sssss",$_POST['events'],$id,$_POST['timestamp'],$_POST['xpos'],$_POST['ypos'])) {
				echo "Binding parameters failed: (" . $stmt->errno . ") " . $stmt->error . " ";
				$failed=6;
			} else {
				if (!$stmt->execute()) {
					echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error . " ";
					$failed=7;
				}
			}
		}
	}
	//echo $xpos;
	//echo $ypos;
	unset($mysqli);
	switch ($failed){
		case 0:
			echo "Data entered successfully.";
			break;
		case 1:
			echo "Data entry failed.";
			break;
		case 2:
			echo "Data entry failed: Error 2";
			break;
		case 3:
			echo "Data entry failed: Error 3";
			break;
		case 4:
			echo "Data entry failed: Error 4";
			break;
		case 5:
			echo "Data entry failed: Error 5";
			break;
		case 6:
			echo "Data entry failed: Error 6";
			break;
		case 7:
			echo "Data entry failed: Error 7";
			break;
		default:
			echo "Data entry failed.";
	}
}
?>

<!DOCTYPE HTML>
<head>
	<title>Handling</title>
	<meta charset="UTF-8">
	<script src = "jquery.min.js"></script>
	<!--<script src="jquery-3.2.1.min.js"></script> -->
	<script src="mouse_log.js"></script>
</head>

<body>

<form name="mouse_data" id="mouse_data" method="post">
<input type="hidden" name="xpos" id="xpos">
<input type="hidden" name="ypos" id="ypos">
<input type="hidden" name="timestamp" id="timestamp">
<input type="hidden" name="events" id="events">


</form>


</body>