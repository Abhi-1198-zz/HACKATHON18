 <?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "teamgnc";
// define variables and set to empty values
$EID = $FNAME = $LNAME =$DOB = $DOJ = $PHONE =$EMAIL ="";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $EID = test_input($_POST["EID"]);
  $FNAME = test_input($_POST["FNAME"]);
  $LNAME = test_input($_POST["LNAME"]);
  $DOB = test_input($_POST["DOB"]);
  $DOJ = test_input($_POST["DOJ"]);
  $PHONE = test_input($_POST["PHONE"]);
  $EMAIL = test_input($_POST["EMAIL"]);
  $DOBM = date("Y-m-d H:i:s",strtotime($DOB));
  $DOJM = date("Y-m-d H:i:s",strtotime($DOJ));
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO EMPGNC(FNAME,LNAME,GENDER,DOB,DOJ,PHONE,EMAIL,ADDRESS) VALUES ('$FNAME','$LNAME','$DOBM','$DOJM','$PHONE','$EMAIL')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?> 