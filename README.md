# Markify - AI-Based Smart Attendance System

An intelligent attendance management system using face recognition and voice identification.

## Features
- 🎯 AI-powered face recognition attendance
- 🎤 Voice-based attendance marking
- 🔐 Two-factor authentication (Face + PIN)
- 👨‍🏫 Teacher dashboard for managing subjects
- 👨‍🎓 Student portal for tracking attendance
- 📊 Real-time attendance analytics
- 📱 QR code subject enrollment

## Tech Stack
- **Frontend**: Streamlit
- **AI/ML**: dlib, scikit-learn, resemblyzer
- **Database**: Supabase
- **Security**: bcrypt, PIN verification

## Setup Instructions

### Prerequisites
- Python 3.8+
- Supabase account
- Camera access (for face recognition)

### Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd AI_Pro
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure Supabase
   - Create a `.streamlit/secrets.toml` file
   - Add your Supabase credentials:
```toml
[supabase]
url = "your-supabase-url"
key = "your-supabase-key"
```

4. Run the application
```bash
streamlit run app.py
```

## Database Schema

### Tables Required:
- `teachers` - Teacher accounts
- `students` - Student profiles with face/voice embeddings
- `subjects` - Course information
- `subject_students` - Enrollment records
- `attendance_logs` - Attendance history

## Deployment

### Streamlit Cloud
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Add secrets in Streamlit Cloud dashboard
4. Deploy!

### Important Notes
- Ensure HTTPS for camera access
- Add Supabase credentials to secrets
- Camera permissions required for face recognition

## License
MIT License
