const atomus = require('atomus');
var request = require("request");

request("http://www.inscripciones.uni.edu.pe/", function (error, response, body) {
    if (!error) {
        atomus().html(body)
        .ready(function(errors, window) {
            var $ = this.$; // jQuery
          $('#link').on('click', function() {
            console.log('link clicked');
          });
          this.clicked($('#link'));
        });
    } else {
        console.log("error");
        console.log(error);
    }
});
