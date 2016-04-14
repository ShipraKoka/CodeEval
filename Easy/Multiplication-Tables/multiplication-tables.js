function multiply(num){
	var line = "";
	var number;
	var space;
	for (i = 1; i <= 12; i++){
		number = (num * i).toString();
		if (number[2]){
			space = " ";
		}
		else if (number[1]){
			space = "  ";
		}
		else {
			space = "   ";
		}
		line = line + space + number.toString();
	}
	console.log(line);
}

for (n = 1; n <= 12; n++){
	multiply(n);
}