import axios from 'axios';

const SYS_URL_PROFIX = 'http://127.0.0.1:5000/api';

export function fetchData(params, callback) {
    const url = `${SYS_URL_PROFIX}/getfile`;
    axios.post(url, params)
    .then(response => {
        callback(response);
    }, error => {
        console.log(error);
    })
}

export function queryImg(params, callback) {
    const url = `${SYS_URL_PROFIX}/getImg/`;
    axios.post(url, params)
    .then(response => {
        console.log(response);
        callback(response);
    }, error => {
        console.log(error);
    })
}