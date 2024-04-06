// app.js
const express = require('express');
const multer  = require('multer');
const fs = require('fs');

const app = express();
const port = 8080;

app.use(express.static('public'));

// Set up multer for file upload
const upload = multer({ dest: 'uploads/' });

// POST endpoint for file upload
app.post('/upload', upload.single('file'), (req, res) => {
    const fileName = req.file.originalname;
    const fileContent = fs.readFileSync(req.file.path);

    fs.writeFileSync(`public/${fileName}`, fileContent);

    res.send('File uploaded successfully');
});

app.get('/', (req, res) => {
    res.send('Hello 2100031358')
})

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
