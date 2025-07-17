const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json({ limit: '10mb' }));

const API_KEY = 'YOUR_GOOGLE_CLOUD_VISION_API_KEY'; // <-- Replace with your real key

app.post('/api/vision', async (req, res) => {
  const { image } = req.body;
  try {
    const response = await fetch(
      `https://vision.googleapis.com/v1/images:annotate?key=${API_KEY}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          requests: [
            {
              image: { content: image.replace(/^data:image\/(png|jpeg);base64,/, '') },
              features: [{ type: 'DOCUMENT_TEXT_DETECTION' }]
            }
          ]
        })
      }
    );
    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Vision API request failed.' });
  }
});

app.listen(5001, () => console.log('Vision proxy running on port 5001')); 