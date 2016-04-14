var fs = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
	if (line !== "") {
		var words = [];
		words = line.split(" ");
		var newWords = [];
		
		for (var i = 0; i < words.length; i++) {
			newWords.unshift(words[i]);
		}
		
		answer_line = newWords.toString().split(",").join(" ");
		console.log(answer_line);
	}
});