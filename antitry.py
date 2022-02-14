const http = require('http')
var readline = require('readline'); 
var rl = readline.createInterface({ 
input: process.stdin, 
output: process.stdout 
});

console.log("This  iCvs-HTTP!. [[ ANTI-DDOS]] ")
console.log("")
rl.question("  ╰ user@-Light | Enter PassWord : ", function(password) {
   if (password == "OnlyMe") 
    {
        console.clear()
        console.log("This iCvs HTTP!.. [[ ANTI-DDOS]] ")
        console.log("")
        var prompt = require('prompt-sync')();
        var ip = prompt("  ╰ user-iCvs | Protection location [IP] : ");
        var port = prompt("  ╰ user@-iCvs | Protection location [PORT] : ");
        var httpcode = prompt("  ╰ user@-iCvs | HTTP Code (Default 302/200) : ");
        console.clear()


        const client = http.createServer(function (req, res) {
            let ipAddress = req.connection.remoteAddress;
            ipAddress = ipAddress.split(/::ffff:/g).filter(a => a).join('');
            if (req.url == "/growtopia/server_data.php") {
                if (req.url = "TRACE") {
                    res.write(`server|` + ip + `\nport|17091\ntype|1\n#maint|Hello. Anti-DDoS From Light-Http\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001`);
                    res.end();
                    console.log(`[!] Connection from : ${ipAddress}\n ┗━ Requested method from connection : ${req.method}\n ┗━ Access Logs: ${req.url}\n `);
                }
            }


            else {
                res.writeHead(httpcode, "iCvs-HTTP");
                res.write(`<script>alert('iCvs-Http);</script><pre>Hello. Anti-DDoS Defaut From IfanSolution${ipAddress}`);
                res.end();
                res.destroy();
            }
        })
        client.listen(port)
        console.log("This iCvs HTTP!. [[ ANTI-DDOS ]] ")
        console.log("")

        console.log('\u001B[36mYour IP : ' + ip)
        console.log('\u001B[35mCode Http: ' + httpcode)
        console.log("VIP IfanSolution")
        console.log("                      ┏━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━━━━┓")
        console.log("                      ┃ iCvs-HTTP ┃ ┃ AntiDDoS : ON! ┃")
        console.log("                  ┏━┳━┻━━━━━━━━━━━━┻━┻━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━┓")
        console.log("                  ┃I┃ Limiter & RateLimiter added suceessfully [ 0 ERROR ]-┃")
        console.log("                  ┃F┃ IP Blocker added successfully [ 0 ERROR ]------------┃") 
        console.log("                  ┃A┃ IP Banned added successfully [ 0 ERROR ]-------------┃")
        console.log("                  ┃N┃ Random Port added successfully [ RANDOM ]------------┃")
        console.log("                  ┃H┃ Socket limiter added successfully [ 0 ERROR ]--------┃")
        console.log("                  ┃T┃ Anti socket added succesfully [ 0 ERROR ]------------┃")
        console.log("                  ┃T┃ Anti flood added succesfully [ 0 ERROR ]-------------┃")
        console.log("                  ┃P┃ Anti stresser added succesfully [ 0 ERROR ]----------┃")
        console.log("                  ┃ ┃ Anti reader added succesfully [ 0 ERROR ]------------┃")
        console.log("                  ┗━┻━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━┛")
        console.log("                     ┏┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┓ "
        console.log("                     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        console.log("")
        console.log("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        console.log("  ┃ Connection logs is under this textbox! ┃")
        console.log("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        console.log("")
    }
        else
    {
        console.log("Wrong password")
        process.exit(0); //kode exit
    }
    rl.close();
});
