<?php
	$id = $_POST['id'];
	$name = $_POST['name'];
	$gender = $_POST['gender'];
	$age = $_POST['age'];
	$number = $_POST['number'];
	$db = $_POST['date of birth'];
	$address=$_POST['address'];
	$Qualification$_POST['Qualification']

	// Database connection
	$conn = new mysqli('localhost','root','','test');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("insert into registration(id, name, gender, age, number, db, address, Qualification) values(?, ?, ?, ?, ?, ?, ?, ?)");
		$stmt->bind_param("sssssi", $id, $name, $gender, $age, $number, $db, $address, $Qualification);
		$execval = $stmt->execute();
		echo $execval;
		echo "Registration successfully...";
		$stmt->close();
		$conn->close();
	}
?>
