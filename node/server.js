var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
	const uptimeSECONDS = os.uptime();
	const uptimeDAY = Math.floor(uptimeSECONDS / 86400);
	const uptimeHOURS = Math.floor((uptimeSECONDS % 86400) / 3600);
	const uptimeMINUTES = Math.floor((uptimeSECONDS % 3600) / 60);
	const uptimeREMAININGSEC = Math.floor(uptimeSECONDS % 60);

	const totalMemory = os.totalmem();
	const totalMemoryMB = Math.round(totalMemory / 1024 / 1024);
	const openMemory = os.freemem();
	const openMemoryMB = Math.round(openMemory / 1024 / 1024);

	const CPUs = os.cpus().length;
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${uptimeDAY}, Hours: ${uptimeHOURS}, Minutes: ${uptimeMINUTES}, Seconds: ${uptimeREMAININGSEC}</p>
            <p>Total Memory: ${totalMemoryMB} MB</p>
            <p>Free Memory: ${openMemoryMB} MB</p>
            <p>Number of CPUs: ${CPUs}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");