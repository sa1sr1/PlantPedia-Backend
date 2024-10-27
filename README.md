# PlantPedia 🌱  
An AR Plant Doctor built for Snap AR's Spectacles platform, that leverages Plantnet, a plant identification API, Wikipedia, Google's Gemini LLM, custom neural networks, and custom logistic models to curate plant growth guidelines and ensure your plants are thriving.

---

![PlantPedia](https://github.com/user-attachments/assets/3abd9ee5-6d1b-4b6c-a72e-70b991ee256c)

### **Source Code**  
[GitHub Repository](https://github.com/Serrindipity/PlantPedia)

### **Demo Video**  
[View Demo on Common Houseplants](https://github.com/user-attachments/assets/d4ad335c-69ce-419f-becb-67b9b6b45c77)

---

## 📋 Project Overview
**PlantPedia** is an AR Plant Doctor designed to help users understand and care for their plants using augmented reality and cutting-edge machine learning. Powered by a suite of advanced APIs and custom algorithms, PlantPedia identifies plants, offers growth guidelines, and provides real-time health assessments to ensure plants thrive.

---

## 🌿 What PlantPedia Does
PlantPedia is a seamless blend of AR and AI that offers:
- **Plant Identification**: Leverages PlantNet API to identify plants from captured frames.
- **Personalized Growth Guidelines**: Curates plant care advice by analyzing information from Wikipedia and prompting Google’s Gemini LLM.
- **Real-time Health Insights**: Utilizes custom neural networks and logistic models to deliver insights on plant health.

With PlantPedia, users have a virtual plant specialist right on their Snap AR Spectacles, making plant care engaging and accessible.

---

## 🔧 How We Built PlantPedia
**Tech Stack**:  
- **Frontend**: Snap AR’s Spectacles with Interaction Kit & Script Component integration for user-friendly AR experiences.
- **Backend**: A custom API processes plant images, conducts health analysis, and compiles care guidelines.
- **APIs & Libraries**: 
  - **PlantNet API**: Identifies plant species from images.
  - **Wikipedia**: Extracts essential plant information.
  - **Google's Gemini LLM**: Curates growth recommendations.
  - **Custom Neural Networks & Logistic Models**: Evaluates plant health based on various indicators.

The captured frame is analyzed to identify the plant type, retrieve relevant information, and prompt Google’s Gemini for plant care tips. Results are displayed within world-anchored containers on the Snap AR Spectacles, giving users an immersive, hands-free plant care experience.

---

## 🛠️ Getting Started

### Prerequisites
- Snap AR Spectacles with the Interaction Kit installed.
- Python 3.8+ (for backend setup).

### Set Up the Backend
(Optional) Set up a virtual environment

macOS:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

### Install the required Python packages:

pip install -r requirements.txt
