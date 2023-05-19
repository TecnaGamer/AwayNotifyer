const express = require('express');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(express.json());

app.post('/settings', (req, res) => {
  const { respond_enabled, response_text } = req.body;

  const updatedSettings = {
    respond_enabled,
    response_text
  };

  // Write the updated settings to settings.json
  fs.writeFile('settings.json', JSON.stringify(updatedSettings, null, 2), 'utf8', (err) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Internal Server Error');
    }

    res.status(200).send('Settings updated successfully');
  });
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
