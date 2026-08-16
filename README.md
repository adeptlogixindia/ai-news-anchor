## 🎙️ AI News Anchor – Automated News Video Generator

AI News Anchor is a fully autonomous system that fetches real-time news based on a user-given topic, generates human-like anchor scripts, converts them to realistic voiceovers, and produces complete news videos featuring a talking AI avatar with relevant B-roll visuals. This project showcases the power of generative AI in media automation and the future of AI-driven journalism.

---

## 🌟 Features

- 🔍 Fetches latest news headlines using SerpAPI
- 🧠 Generates professional news scripts using a Large Language Model (LLM)
- 🎤 Converts scripts to natural-sounding voice using text-to-speech
- 🧑‍💻 Animates a digital avatar to lip-sync with the generated voice
- 🎬 Merges avatar speech with real-world video clips (B-roll)
- ✅ Fully automated pipeline from topic input to final news video


---

## 🚀 How It Works

1. **User Enters a Topic**  
   e.g., "earthquake in Delhi"

2. **News Retrieval**  
   Fetches top 5 news articles from the web using SerpAPI

3. **Script Generation**  
   A local LLM (e.g., Mistral) summarizes the headlines into a spoken news script

4. **Voice Synthesis**  
   Uses `gTTS` to convert text to realistic anchor-style voice

5. **Avatar Generation**  
   Uses Wav2Lip to animate a static face image to speak the script

6. **Video Merging**  
   Merges avatar and B-roll clips into a final, polished news video

---

## ⚙️ Setup

1. **Install Python dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Install external tools**
   - [ffmpeg](https://ffmpeg.org/download.html) (must be on PATH)
   - [Ollama](https://ollama.com) with the Mistral model: `ollama pull mistral`
   - [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) — clone it next to this project and place the `wav2lip_gan.pth` checkpoint in `Wav2Lip/checkpoints/`

3. **Add your API keys** — replace the `"Enter key"` placeholders for `SERPAPI_KEY` (SerpAPI) and `DID_API_KEY` (D-ID, only needed for `generate_voice.py`) in the scripts.

4. **Add the avatar face image** at `input/face.jpg`.

5. **Run**
   ```
   streamlit run app.py
   ```

---

## 🖼️ Demo Screenshot

<p align="center">
  <img src="assets/Screenshot 2025-07-03 132825.png"/>
</p>

---

## 🎬 Demo Video

📂 The full demo video is available here:  
[▶️ Watch or Download AI News Anchor Demo](assets/final_news_video.mp4)

_(Click the link to play it in the browser or download it)_

---

## ✅ Impact of AI News Anchor

- 📺 1. 24/7 Automated News Broadcasting
Eliminate the need for human anchors by enabling real-time, non-stop video-based news generation. Perfect for small media houses, startups, or regions lacking broadcasting infrastructure.

- 🌍 2. Hyper-Local & Multilingual News Distribution
Auto-generate region-specific news videos in local languages using LLMs + TTS, expanding access to news for rural, remote, or low-literacy populations.

- 🎓 3. AI-Powered EdTech Simulations
Simulate current events for educational institutions, helping students understand breaking news through personalized, visualized summaries in an engaging format.

- 🧠 4. AI Journalism Demonstration
Showcases how generative AI can automate every stage of digital journalism: research, writing, voiceover, and on-screen delivery — all without human involvement.

- 💼 5. Corporate & Internal News Video Generator
Corporates can use it to auto-generate daily/weekly updates in video form for employee communications — no manual editing or narration needed.

---

## 🌟 Real-World Impact

- Bridging Information Gaps in areas with limited access to professional journalism.

- Reducing costs for media content creation through automation.

- Democratizing content creation by empowering non-technical users to generate professional videos.

- Future-proofing journalism by demonstrating how AI can support — not replace — human anchors with scalable tools.

---

## 🛑 Disclaimer

This project is intended for research and educational purposes only. The generated content is based on available online information and does not represent verified journalism.



