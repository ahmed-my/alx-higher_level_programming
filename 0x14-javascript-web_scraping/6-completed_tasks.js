#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
      const todos = JSON.parse(body);
      const completedTasksByUser = new Map();
      todos.forEach(todo => {
        if (todo.completed) {
          const userId = todo.userId;
          completedTasksByUser.set(userId, (completedTasksByUser.get(userId) || 0) + 1);
        }
    });
    console.log('Users with completed tasks:');
    completedTasksByUser.forEach((count, userId) => {
      console.log(`User ${userId}: ${count} completed tasks`);
    });
  }
});

