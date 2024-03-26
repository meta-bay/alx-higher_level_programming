#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
    if(err){
        console.error(err);
    }
    const completedUserTask = {};
    todos = JSON.parse(body)
    todos.forEach(todo => {
        if(todo.completed){
            if(completedUserTask[todo.userId]){
                completedUserTask[todo.userId]++;
            } else {
                completedUserTask[todo.userId] = 1;
            }
        }
    });
    console.log(completedUserTask);
});