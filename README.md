# Part 1: Front-End Prompt

- Design a table front-end component that takes row based data and displays it in an interactive table. (think Wikipedia Tables, Google Sheets, etc)
- Should be able to handle numerical and text data

- Do some styling, but save polishing for the end to make sure you can get basic functionality
- Add 1-2 features for interactability, ideas are but not limited to:
    - Row-based Sorting
    - Row-based Filtering
    - Cell Editing
    - Column Resorting
    - Sub-table support
    - Pagination
    - Infinite Scroll
    - Additional Data types (like gracefully displaying a 3-Dimensional Vector or Quaternion)
    - Cell Selection / Maniupulation

- Use one of the following frameworks: React, Lit, Vue
- Included is a starter kit for React, but feel free to use your own boiler plate, or project root.
- Allowed npm packages:
    - Utility Libraries: Lodash, underscore, etc
    - Build Libraries: Webpack, Rollup, etc
    - State Libraries: Immutable, Redux, etc
    - Language Mods: Typescript, SASS, etc
    - Date libraries
- Disallowed Npm Packages: 
    - CSS Libraries like bootstrap or tailwind
    - Whole React Components like `react-table`
- Styling and interaction should be all your code.

- You can use the included data jsons, or use your own mock or real data that demonstrates your features the best
- Example input data:

```javascript
let planets = [
    {
        name: "mars",
        radius: 1e6,
        mass: 3e20,
        distance: 23
    },
    {
        name: "jupiter",
        radius: 1e8,
        mass: 3e23,
        distance: 46
    },
    ...
];
```

```javascript
let trajectory = [
    {
        time: 0,
        position: [0, 0, 0],
        velocity: [0, 0, 0],
        status: "ready",
        fuel: 3000
    },
    {
        time: 100,
        position: [0, 0, 0],
        velocity: [10, 0, 0],
        status: "in_transit",
        fuel: 2900
    }
    ...
];

Contained in this folder is a project starting point, that uses uses create-react-app.
You can use this boiler plate or use your own if you prefer Vue, or a different framework.

```
# Part 2: Back-End Prompt
Create a light server that will read data from a CSV and serve it to the front end to show on the table
You can use Flask or Django. A template is started for flask, make sure to run `pip install flask flask-cors`

# Part 3: Extras
If time permits, you can implement more features after you have the basics implemented.

1. Backend features: 
    - Data Interpolation (Fetch data on a different time frequency other than is in the data)
    - Live Data (Feed New Data that is streamed to front end)
    - Editing functionality

2. Frontend features
    - Add extra polish and niceness to the UI 
    - Add an extra front end feature from the list

When done, zip up your project folder (omit node_modules!) and notify your proctor
Don't hesitate to reach out for any questions.

# Running the app:
```
npm install
npm run start
```

In a separate terminal or in background:
```
python server.py
```


