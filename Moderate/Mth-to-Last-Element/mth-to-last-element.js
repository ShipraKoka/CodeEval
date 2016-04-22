var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        
        var characters = line.split(" ");
        var index = characters.pop();
		var m = "";
		
		if (index == 1){
			m = characters.pop();
			console.log(m);
		}
		else if (index <= characters.length){
			for (i = 1; i < index; i++){
				characters.pop();
			}
			m = characters.pop();
			console.log(m);
		}
	}
});
