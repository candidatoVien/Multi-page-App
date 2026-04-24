# 🚀 Professional Portfolio Web App
### Vien Adah O. Candidato | BSCS 3rd Year | DEBESMSCAT

"Welcome! This is my personal portfolio—a space I built using Streamlit to share my journey as a Computer Science student at DEBESMSCAT. More than just a collection of code, this site is a reflection of my growth in Python and Web Development, my academic milestones, and the creative side of me that loves to sing, dance, and create. It’s a snapshot of where I am now and where I’m headed in the tech world."

---

## 📋 Features

### 🏠 Home Page
- **Circular Profile Hero:** Uses custom CSS for a centered, professional circular image.
- **Interactive Theme Engine:** Sidebar controls allowing users to adjust the page and sidebar background colors (Wine Red by default) in real-time.
- **Growth Mindset Intro:** A personal introduction detailing my journey as a 20-year-old developer committed to continuous learning.
- **30-Second Rating Prompt:** An interactive feature that prompts the user for a quick rating after 30 seconds of browsing.

### ℹ️ About Me
- **High-Density Personal Info:** Uses custom `.personal-info` CSS for maximum readability of personal details.
- **Academic Milestones:** Detailed history from Polot Elementary and Liceo De Baleno to my current BSCS degree.
- **Family Profile:** Interactive expanders containing background on my siblings.
- **Creative Interests:** Media-rich sections highlighting interests in **Dancing** (Video), **Singing**, and **Crocheting**.

### 👩‍💻 Skills & Certificates
- **Technical Proficiency:** Visual progress bars for Python Development (85%), Networking (60%), and Web Development (90%).
- **Interactive Toolbox:** Metric dashboard for professional tools including GitHub, VS Code, and Streamlit.
- **Awards Gallery:** Visual showcase of academic excellence, including **Dean's List** recognition and various AI/Python certifications.

### 📁 Projects Showcase
- **System Portfolio:** A detailed gallery featuring:
    - **Beach Reservation System:** Python-based automation for guest inputs and outputs.
    - **Asia Novo Hotel System:** A professional database implementation using MS Access.
    - **CPU Simulator:** A technical educational tool visualizing the instruction cycle.
    - **Library Management System:** Handling book logistics via Python.

### 📬 Contact & Inspiration
- **Functional Contact Form:** Built-in validation for name, email, and messages.
- **Daily Inspiration:** An interactive quotes page where users can view random quotes or submit their own.

---

## 🛠️ Technical Stack

- **Framework:** Streamlit (Python 3.x)
- **Styling:** Custom CSS Injection (Glassmorphism, Flexbox, Base64 Encoding)
- **Deployment:** Streamlit Community Cloud
- **Version Control:** GitHub

🛠️ Performance & Optimization
Asset Encoding: Uses Base64 string conversion for the profile hero section to prevent flickering during page reloads.

State Management: Implements st.session_state to ensure the user's custom theme (Wine Red) persists as they navigate between different sub-pages.

Lazy Loading: Images are structured in a local /images directory to optimize load times on the Streamlit Cloud server.

---

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/yourusername/portfolio-app.git](https://github.com/yourusername/portfolio-app.git)

2. Install Requirements
    pip install streamlit

3. Run the Application
    streamlit run Home.py

📁 Project Structure

portfolio_app/
├── Home.py                # Main landing page & theme configuration
├── requirements.txt       # App dependencies (streamlit)
├── images/                # Folder containing profile, project, and pet assets
└── pages/                 
    ├── 1_ℹ️_About.py       # Personal & Academic details
    ├── 2_🛠️_Skills.py      # Skill metrics & technical tools
    ├── 3_📁_Projects.py    # System portfolio gallery
    ├── 4_🏆_Certificates.py# Awards & academic recognition
    ├── 5_🐾_Viens_Pets.py  # Pet showcase (Hikaro, Prism, Caelum, Cosmo)
    ├── 6_📞_Contact.py     # Contact portal & social links
    └── 7_💬_Quotes.py      # Interactive quotes generator

📄 License

This project is part of an academic requirement for Activity 02: Streamlit Multipage App. Feel free to use the structure as a template for your own Streamlit applications.

📞 Support & Contact
Email: candidatovien327@gmail.com

Facebook: Vien Candidato

Instagram: @vi_en_ny