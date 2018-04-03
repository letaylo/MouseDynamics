//CHANGES MUST BE UPLOADED TO INDEX YA DOOF

$(document).ready(function() {
	//var $date = new Date();
	
	
	$(document).mousemove(function(event) {
		//var $dateNew = new Date();
		//var $dateCompare = $date.getTime() + 100;
		
		//if ($dateCompare <= $dateNew.getTime()) {
			
			//saves important data
			var $xpos = event.pageX;
			var $ypos = event.pageY;
			var $timestamp = event.timeStamp;
			var $event_type = "mm";
			
			
			//updates form
			/*document.getElementById("xpos").value = $xpos;
			document.getElementById("ypos").value = $ypos;
			document.getElementById("timestamp").value = $timestamp;
			document.getElementById("l_down").value = $l_down;
			document.getElementById("r_down").value = $r_down;
			document.getElementById("m_down").value = $m_down;
			document.getElementById("l_up").value = $l_up;
			document.getElementById("r_up").value = $r_up;
			document.getElementById("m_up").value = $l_up;
			//document.getElementById("click").value = $click;
			//document.getElementById("enter").value = $enter;*/
			//document.getElementById("events").value = $event_type;
			
			//sends data to php for processing
			$.ajax( {
				type: "POST",
				url: 'mouse_handling.php',
				processData: true,
				data: {xpos : $xpos, ypos : $ypos, timestamp : $timestamp, events : $event_type},
				success: function(data) {
					//alert("success");
				},
				error: function(data) {
					alert("Error!");
				},
			});		
			

			//$date = $dateNew;
					
		//}
	}); 	
	
	$(document).mousedown(function(event) {
		//var $dateNew = new Date();
		//var $dateCompare = $date.getTime() + 100;
		
		//if ($dateCompare <= $dateNew.getTime()) {
			
			//saves important data
			var $xpos = event.pageX;
			var $ypos = event.pageY;
			var $timestamp = event.timeStamp;
			var $event_type;
			
			if (event.button == 0) {
				$event_type = "ld";
			}else if (event.button == 1) {
				$event_type = "rd";
			}else {
				$event_type = "md";
			}
			
			//updates form
			/*document.getElementById("xpos").value = $xpos;
			document.getElementById("ypos").value = $ypos;
			document.getElementById("timestamp").value = $timestamp;
			document.getElementById("l_down").value = $l_down;
			document.getElementById("r_down").value = $r_down;
			document.getElementById("m_down").value = $m_down;
			document.getElementById("l_up").value = $l_up;
			document.getElementById("r_up").value = $r_up;
			document.getElementById("m_up").value = $l_up;
			//document.getElementById("click").value = $click;
			//document.getElementById("enter").value = $enter;*/

			
			//sends data to php for processing
			$.ajax( {
				type: "POST",
				url: 'mouse_handling.php',
				processData: true,
				data: {xpos : $xpos, ypos : $ypos, timestamp : $timestamp, events : $event_type},
				success: function(data) {
					//alert("success");
				},
				error: function(data) {
					alert("Error!");
				},
			});		
			

			//$date = $dateNew;
					
		//}
	});
	
	$(document).mouseup(function(event) {
		//var $dateNew = new Date();
		//var $dateCompare = $date.getTime() + 100;
		
		//if ($dateCompare <= $dateNew.getTime()) {
			
			//saves important data
			var $xpos = event.pageX;
			var $ypos = event.pageY;
			var $timestamp = event.timeStamp;
			var $event_type;
			
			if (event.button == 0) {
				$event_type = "lu";
			}else if (event.button == 1) {
				$event_type = "ru";
			}else {
				$event_type = "mu";
			}
			
			//updates form
			/*document.getElementById("xpos").value = $xpos;
			document.getElementById("ypos").value = $ypos;
			document.getElementById("timestamp").value = $timestamp;
			document.getElementById("l_down").value = $l_down;
			document.getElementById("r_down").value = $r_down;
			document.getElementById("m_down").value = $m_down;
			document.getElementById("l_up").value = $l_up;
			document.getElementById("r_up").value = $r_up;
			document.getElementById("m_up").value = $l_up;
			//document.getElementById("click").value = $click;
			//document.getElementById("enter").value = $enter; */

			
			//sends data to php for processing
			$.ajax( {
				type: "POST",
				url: 'mouse_handling.php',
				processData: true,
				data: {xpos : $xpos, ypos : $ypos, timestamp : $timestamp, events : $event_type},
				success: function(data) {
					//alert("success");
				},
				error: function(data) {
					alert("Uh-Oh!");
				},
			});		
			

			$date = $dateNew;
					
		//}
	});
	
});