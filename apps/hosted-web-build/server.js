const express = require('express');
const server = new express();
const fs = require('fs');
const https = require('https');

// Load the key and crt paths from environment variables.
key_path = `${process.env.SECRET_MNT_PATH}/${process.env.CNE_CONNECT_KEY}`;
crt_path = `${process.env.SECRET_MNT_PATH}/${process.env.CNE_CONNECT_CRT}`;

console.log(`key_path: ${key_path}`)
console.log(`crt_path: ${crt_path}`)

// Read the key and crt files into variables.
const key_data = fs.readFileSync(key_path);
const crt_data = fs.readFileSync(crt_path);

console.log(`key_data length:\n ${key_data.length}`);
console.log(`crt_data length:\n ${crt_data.length}`);

const options =  {
    key: key_data,
    cert: crt_data
};

// Reference files in the public folder e.g. index.html.
server.use(express.static('public'));
// Respond to a GET request with index.html site.
server.get('/', (req, res) => {
    res.sendFile(`${__dirname}/public/index.html`);
});

// Declare the web app port number.
const port = 8080;
// Start receiving https requests.
https.createServer(options, server).listen(port, function () {
    console.log('Server listening on port ', port)
});
