#!/usr/bin/node

const request = require('request-promise');

async function fetchCompletedTasks(apiUrl) {
  try {
    const body = await request(apiUrl);
    const todos = JSON.parse(body);

    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        completed[todo.userId] = (completed[todo.userId] || 0) + 1;
      }
    });

    const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

    console.log(Object.keys(completed).length > 2 ? output : completed);
  } catch (error) {
    if (error.statusCode) {
      console.error(`Error: API request failed with status code ${error.statusCode}`);
    } else {
      console.error('Error:', error.message);
    }
  }
}

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

fetchCompletedTasks(apiUrl);

