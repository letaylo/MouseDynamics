<?php session_start();
//Place this part in the login page
session_regenerate_id();

?>
<!DOCTYPE html>
<html lang="en">

    <head>
    
        <meta charset="utf-8">
        
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		
        <!--<script id="text/javascript" src="mouse_log.js"></script>
		<!--<script src="jquery-3.2.1.min.js"></script> -->
		
        <title>Account Forum</title>
        
        <style type="text/css">
        		
        		 .container {
        		 		margin-top: 60px;
        		 		width: 800px;
        		 }      
        		 
        		 #lock-img {
					  height: 120px;    
					  float:left; 
					  margin: 0 auto;
        		 }
        		 
				
				/* Customize the label (the container) */
				.checkbox-container {
				  display: block;
				  position: relative;
				  padding-left: 35px;
				  margin-bottom: 12px;
				  cursor: pointer;
				  -webkit-user-select: none;
				  -moz-user-select: none;
				  -ms-user-select: none;
				  user-select: none;
				}
				
				/* Hide the browser's default radio button */
				.checkbox-container input {
				  position: absolute;
				  opacity: 0;
				}
				
				/* Create a custom radio button */
				.checkmark {
				  position: absolute;
				  top: 15px;
				  left: 7px;;
				  height: 13.5px;
				  width: 13.5px;
				  background-color: #eee;
				  border-radius: 50%;
				  margin-left: 5px;
				}
				
				/* On mouse-over, add a grey background color */
				.checkbox-container:hover input ~ .checkmark {
				  background-color: #ccc;
				}
				
				/* When the radio button is checked, add a blue background */
				.checkbox-container input:checked ~ .checkmark {
				  background-color: #2196F3;
				}
				
				/* Create the indicator (the dot/circle - hidden when not checked) */
				.checkmark:after {
				  content: "";
				  position: absolute;
				  display: none;
				}
				
				/* Show the indicator (dot/circle) when checked */
				.checkbox-container input:checked ~ .checkmark:after {
				  display: block;
				}
				
				/* Style the indicator (dot/circle) */
				.checkbox-container .checkmark:after {
				  top: 4.5px;
				  left: 5px;
				  width: 4px;
				  height: 4px;
				  border-radius: 50%;
				  background: white;
				}
				
				.card-img {
					margin-top: 8px;
					height: 32px;
					width: auto;
				}
				
				select {
					margin-left: 10px;
					border-radius: 5px;		
					background-color: rgb(237, 237, 237);
				}
				
				#sec-code {
					width: 75px;
					margin-right: 10px;
					margin-left: 15px;
				}
        
        </style>
        
    </head>
    
    <body>
	
		<!-- Hidden Form for mouse data collection -->
		<form name="mouse_data" id="mouse_data" method="post">
		<input type="hidden" name="xpos" id="xpos">
		<input type="hidden" name="ypos" id="ypos">
		<input type="hidden" name="timestamp" id="timestamp">
		<input type="hidden" name="events" id="events">

		</form>

        <div class="container">

			  <div class="row">
	   	
			    	<img src="lock.png" alt="Lock-Image" id="lock-img">
					    
				    <div class="col-10">
					  
					 <h5 id="title"><strong>Secure Payment Info</strong></h5>
					    
				    <hr>
				    
				    <form method="post" action="export_table.php">
						    
						 <div class="row" id="card-selection">
						
							<div class="c-card" id="mastercard">
							
								<label class="checkbox-container">									
											
										<img class="card-img" src="mastercard.png" alt="MasterCard">
									  
										<input type="radio" checked="checked" name="card-type">
		
										<span class="checkmark"></span>
									 
								</label>	

							</div>
								
							<div class="c-card" id="visa">
							
								<label class="checkbox-container">									
											
										<img class="card-img" src="visa.png" alt="Visa">
									  
										<input type="radio" name="card-type">
		
										<span class="checkmark"></span>
									 
								</label>
						
							</div>
								
							<div class="c-card" id="amex">
							
								<label class="checkbox-container">									
											
										<img class="card-img" src="AmericanExpress.svg" alt="Amex">
									  
										<input type="radio" name="card-type">
		
										<span class="checkmark"></span>
									 
								</label>
								
							</div>
						
							<div class="c-card" id="discover">
							
								<label class="checkbox-container">									
											
										<img class="card-img" src="discover.jpg" alt="Amex">
									  
										<input type="radio" name="card-type">
		
										<span class="checkmark"></span>
									 
								</label>	 
								
							</div>
							
							<div class="c-card" id="payPal">
					         	
			          		<label class="checkbox-container">
			          			
			          			  <img class="card-img" src="paypal.png" alt="PayPal">
								
		                       <input type="radio" name="card-type">
	
									  <span class="checkmark"></span>
	
								</label>
								
							</div>
															
						</div>
						
						<br>
		             
		            <div class="form-group" id="name-area">
		            
		                <label for="input-name">Name (as it appears on your card)</label>
		              
		                <input class="form-control" placeholder="John Doe etc. " id="name">
		         				             
		            </div>
				             
		            <div class="form-group" id="card-num-area">
		               
		                <label for="input-card-num">Card Number (no dashes or spaces)</label>
		            
		                <input type="text" id="card-num" class="form-control">
		              
		            </div>
				             
		            <div class="form-group" id="expiration-date-area">
		              
	              		<label for="input-name">Expiration date</label>
						      
					      <div class="row">

				            <div>							              

				              <div style="width:15%;margin-left:5px;">

								    <select id="month">

									    <option value=''>--Select Month--</option>

									    <option selected value='January'>01 - January</option>

									    <option value='February'>01 - February</option>

									    <option value='March'>03 - March</option>

									    <option value='April'>04 - April</option>

									    <option value='May'>05 - May</option>

									    <option value='June'>06 - June</option>

									    <option value='June'>07 - July</option>

									    <option value='August'>08 - August</option>

									    <option value='September'>09 - September</option>

									    <option value='October'>10 - October</option>

									    <option value='November'>11 - November</option>

									    <option value='December'>12 - December</option>

								    </select> 
								   
								  </div>
								
								</div>  


			              <div style="width:15%;margin-left:5px;">

							    <select id="year"></select>

							  </div>

							</div>  
								
		             </div> 
				             
		             <div class="form-group" id="sec-code-area">
		                   
		                   <label class="control-label">Security code (3 on back, Amex: 4 on front)</label>
		                   
		                   <div class="row">		                   

			                   <input class="form-control" id="sec-code" name="Security Code">

			                   <img src="sec-code.png" alt="Security Code" class="card-img">

		                   </div>	

		             </div>
		             <hr>
		             <div class="form-group" id="shipping-options">
		               
		               <label class="control-label">Delivery Options</label><br>
							
								  <div class="shipping-option" id="2-day-shipping"><input type="radio"  name="delivery-option" value="male"> <i>FREE Two-Day Shipping</i><br></div>
								  <div class="shipping-option" id="no-rush-shipping"><input type="radio" name="delivery-option" value="female"> <i>FREE No-Rush Shipping</i><br></div>								  
								  <div class="shipping-option" id="1-day-shipping"><input type="radio" name="delivery-option" value="other"> <i>One-Day Shipping</i><br></div>								  
								  <div class="shipping-option" id="same-day-shipping"><input type="radio" name="delivery-option" value="female"> <i>Same-Day Delivery</i><br></div>
								  <div class="shipping-option" id="standard-shipping"><input type="radio" name="delivery-option" value="female"> <i>Standard Shipping (4-5 business days)</i><br></div>							
							
							
						</div>
		             
		             <div class="form-group" id="street-addr-area">
		                   <label class="control-label">Street Address</label>
		                   <input class="form-control" id="street-address">
		             </div>
		              
		             <div class="form-group" id="zip-code-area">
		                    <label class="control-label">Zip Code</label>
		                    <input class="form-control" id="zip-code">
		             </div>
		            
		             <div class="form-group" id="city-area">
		                    <label class="control-label">City</label>
		                    <input class="form-control" id="city">
		             </div> 

		             <div class="form-group" id="state-area">
		                    <label class="control-label">State</label>
		                    <input class="form-control" id="state">
		             </div>
		            				             
		             <div class="form-group" id="	country-area">
		                    <label class="control-label">Country</label>
		                    <input class="form-control" id="country">
		             </div>
		          
		             <button type="submit" class="btn btn-primary" id="submit" >Submit</button>
		          
				 	</form>
			  
			    </div>
	
			 </div>
   
        </div>
        
        <br><br>
     
     
        <script src = "jquery.min.js"></script>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js" integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4" crossorigin="anonymous"></script>

        <script type="text/javascript">
        				
				var log = "";
						
            $(function () {
                $('[data-toggle="popover"]').popover()
            });

            $(function () {
                $('[data-toggle="tooltip"]').tooltip()
            });

				
				var focused = false;
				$("select, .form-control").on("focusin", function(){
					 if(!focused){
                	console.log( $(this).attr("id") + ' focused in at ' + new Date());
                	log += ( $(this).attr("id") + ' focused in at ' + new Date() + '\n');
                	focused = true;      
                }
            });
            $("select, .shipping-option").on("click", function(){
                //alert("value clicked");
                console.log($(this).attr("id") + ' ' + $(this).attr("id").val() + ' clicked at ' + new Date());
                log += ($(this).attr("id") + ' ' + $(this).attr("id").val() + ' clicked at ' + new Date() + '\n');
            });
            $("select, .form-control").on("focusout", function(){
                focused = false;
                console.log($(this).attr("id") + ' focused out at ' + new Date());
                log += ($(this).attr("id") + ' focused out at ' + new Date() + '\n')
            });
				
            var c_date;
            $(".c-card, #lock-img, .form-group").hover(function(){
                c_date = new Date();
            }, function(){
                console.log($(this).attr("id") + " hovered for "+(new Date()-c_date)/1000.0 + " seconds");
                log += ($(this).attr("id") + " hovered for "+(new Date()-c_date)/1000.0 + " seconds" + '\n');
                c_date = new Date();
            });
            
				var c_date2;
            $(".shipping-option").hover(function(){
                c_date2 = new Date();
            }, function(){
                console.log($(this).attr("id") + " hovered for "+(new Date()-c_date2)/1000.0 + " seconds");
                log += ($(this).attr("id") + " hovered for "+(new Date()-c_date2)/1000.0 + " seconds" + '\n');
                c_date2 = new Date();
            });
                        
            
            var first = true;// quick fix for double click event firing
            $(".c-card").click( function() {
            	if(first){
            		console.log($(this).attr("id") + ' clicked at ' + new Date());
            		log += ($(this).attr("id") + ' clicked at ' + new Date() + '\n');
            		first = false;
            	}
            	else{
            		first = true;            	
            	}     
            });
            
            $(document).keypress(function(event){
                console.log(String.fromCharCode(event.which) + ' entered in ' + $(event.target).attr("id"));
                log += (String.fromCharCode(event.which) + ' entered in ' + $(event.target).attr("id") + '\n');
            });        
        
            
            $("form").submit(function (e){
            	var filename = "log.txt";
            	download(filename, log);        	
          	});

				function download(filename, text) {
				  var element = document.createElement('a');
				  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
				  element.setAttribute('download', filename);
				
				  element.style.display = 'none';
				  document.body.appendChild(element);
				
				  element.click();
				
				  document.body.removeChild(element);
				}


				// Creating date range for expiration date
			   var start = new Date().getFullYear();
			   var end = start + 20;
				var options = "";
				for(var year = start ; year <=end; year++){
				   options += "<option>"+ year +"</option>";
				}
				document.getElementById("year").innerHTML = options;
        
        </script>
        <script type="text/javascript">
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
			document.getElementById("events").value = $event_type;
			
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
</script>
    </body>
    
</html>