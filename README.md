# Handwriting-to-Text Converter

This project converts handwritten images to text using OCR and can enhance the extracted text using AI models.

## 🚀 Features
- **OCR (Optical Character Recognition):** Extracts text from images using Tesseract.js (works in browser and on Firebase Hosting).
- **AI Text Enhancement (Local Only):** Uses Ollama with the Mistral model to clean up and improve OCR text (available only when running locally).
- **Firebase Integration:** Save, retrieve, and manage extracted/enhanced text files securely in the cloud.
- **Modern React UI:** Responsive, dark mode, and mobile-friendly.

## 🎥 Video Demo
- See the video for a demonstration of AI-enhanced text using Ollama Mistral (local LLM).

## 🖥️ Run Locally with Ollama (for AI Enhancement)
1. **Install [Ollama](https://ollama.com/download)** and pull the Mistral model:
   ```bash
   ollama run mistral
   ```
2. **Start the React app:**
   ```bash
   cd client
   npm install
   npm start
   ```
3. **Use the "Improve with AI" button** to enhance OCR text using your local Ollama server.

## 📦 Code
- [GitHub Repository]()

## ⚠️ Note
- AI enhancement (Ollama Mistral) requires running locally and cannot be provided on public cloud/free hosting due to hardware and deployment limitations.
- The public demo is for OCR and basic text features only.

---

Feel free to try the public demo, watch the video, or clone the repo and run the full version locally!
