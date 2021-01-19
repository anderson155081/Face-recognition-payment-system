const { BrowserWindow } = require('electron')
const { ipcMain } = require('electron')
const path = require('path')
const pyshell=  require('python-shell');
const mysql = require('mysql');

let window

function createWindow(){

    // await pyshell.PythonShell.run('/Users/chi-an/Desktop/code/project/softnet/order/src/Senior-Project/main.py', null, (err, results) => {
    //   if  (err)  throw err;
    //   console.log('hello.py finished.');
    //   console.log('results', results);
    // });

    window = new BrowserWindow({
        width:800,
        height:700,
        webPreferences:{
            nodeIntegration: true
        }
    })
    window.loadFile('src/index.html')
}

ipcMain.on('send_name_totalprice', (event, arg) => {
    
    pyshell.PythonShell.run('/Users/chi-an/Desktop/code/project/softnet/order/src/Senior-Project/main.py', { pythonOptions: ['-u'] }, (err, results) => {
        if  (err)  throw err
        console.log('finished.');
        
        //send sql

        var send_sql = new pyshell.PythonShell('/Users/chi-an/Desktop/code/project/softnet/order/src/payDB.py');
        send_sql.send(results);
        send_sql.send(arg);

        send_sql.on('message', function(message){
            console.log(message);
        });

        send_sql.end(function(err){
            if(err){
                throw err;
            };
            console.log('sql_finish');
        });
        
        
        console.log(results)
        console.log(arg)
    })

    event.reply('getpython', '貓咪肚子餓')
})

ipcMain.on('take-cat-home-message', (event, arg,yes) => {
    pyshell.PythonShell.run('/Users/chi-an/Desktop/code/project/softnet/order/src/Senior-Project/main.py', { pythonOptions: ['-u'] }, (err, results) => {
        if  (err)  throw err
        console.log('finished.'); 
        var send_sql = new pyshell.PythonShell('/Users/chi-an/Desktop/code/project/softnet/order/src/depositDB.py');
        send_sql.send(results);
        send_sql.send(arg);

        send_sql.on('message', function(message){
            console.log(message);
        });

        send_sql.end(function(err){
            if(err){
                throw err;
            };
            console.log('sql_finish');
        });
        
        
        console.log(results)
        console.log(arg)
    })
})

module.exports = { createWindow }