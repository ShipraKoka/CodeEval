var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        
        var numbers = line.split(";");
        var digits = "";
        
        for (i = 0; i < numbers.length; i++){
            switch (numbers[i].substr(0, 2)){
                case "ze":
                    digits += "0";
                    break;
                case "on":
                    digits += "1";
                    break;
                case "tw":
                    digits += "2";
                    break;
                case "th":
                    digits += "3";
                    break;
                case "fo":
                    digits += "4";
                    break;
                case "fi":
                    digits += "5";
                    break;
                case "si":
                    digits += "6";
                    break;
                case "se":
                    digits += "7";
                    break;
                case "ei":
                    digits += "8";
                    break;
                case "ni":
                    digits += "9";
                    break;
            }
        }
        
        console.log(digits);
    }
});
