import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import JobInfo from './App';
//import reportWebVitals from './reportWebVitals';

const cont = document.querySelector("#jobinfo");
ReactDOM.render(<JobInfo />, cont);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
