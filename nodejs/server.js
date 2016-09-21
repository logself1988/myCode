var http = require('http');
http.createServer(function(request,response){
	response.writeHead(200,{'content-type':'text/plain'});
	response.end("Hello Node.js!");
}).listen(8888);

console.log("Server is listening on port 8888!!!");
