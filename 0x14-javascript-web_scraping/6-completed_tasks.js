#!/usr/bin/node
const request = require('request');
const link = process.argv[2];
request(link, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};
    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId.toString();
        if (completedTasks[userId]) {
          completedTasks[userId] += 1;
        } else {
          completedTasks[userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
