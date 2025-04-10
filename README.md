# AI CyberWardrobe

An intelligent wardrobe management system powered by AI, helping users organize their clothes and get personalized fashion recommendations.

## 🚀 Features

- Personal Profile & Style Preferences Management
- Smart Clothing Recognition & Management
- AI Outfit Recommendation Engine
- Smart Shopping & Style Matching
- AI Virtual Try-on & Outfit Preview
- Personalized Growth System & Virtual Stylist

## 🛠 Technical Stack

### Frontend
- Next.js 14 (React framework)
- TypeScript
- Tailwind CSS
- Shadcn/ui (UI components)
- React Query (Data fetching)
- Zustand (State management)

### Backend
- Python FastAPI
- PostgreSQL (Database)
- Redis (Caching)
- Celery (Task queue)

### AI/ML Components
- PyTorch
- OpenCV
- Stable Diffusion (for virtual try-on)
- Hugging Face Transformers
- TensorFlow

### Cloud Services
- AWS S3 (Image storage)
- AWS Rekognition (Image analysis)
- AWS Lambda (Serverless functions)

## 📁 Project Structure

```
ai-cyberwardrobe/
├── frontend/                 # Next.js frontend application
│   ├── src/
│   │   ├── app/             # Next.js app router
│   │   ├── components/      # Reusable UI components
│   │   ├── features/        # Feature-specific components
│   │   ├── hooks/           # Custom React hooks
│   │   ├── lib/             # Utility functions
│   │   ├── store/           # State management
│   │   └── types/           # TypeScript types
│   └── public/              # Static assets
│
├── backend/                  # FastAPI backend
│   ├── app/
│   │   ├── api/             # API endpoints
│   │   ├── core/            # Core functionality
│   │   ├── models/          # Database models
│   │   ├── schemas/         # Pydantic schemas
│   │   └── services/        # Business logic
│   └── tests/               # Backend tests
│
├── ai/                       # AI/ML components
│   ├── clothing_recognition/ # Clothing detection & classification
│   ├── virtual_tryon/       # Virtual try-on models
│   ├── style_recommendation/# Style recommendation engine
│   └── body_scanning/       # Body scanning & modeling
│
├── docker/                   # Docker configuration
├── docs/                     # Documentation
└── scripts/                  # Utility scripts
```

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd backend
   pip install -r requirements.txt
   ```

3. Set up environment variables
4. Start the development servers:
   ```bash
   # Frontend
   npm run dev

   # Backend
   uvicorn app.main:app --reload
   ```

## 📝 Development Guidelines

- Follow TypeScript best practices
- Write unit tests for critical functionality
- Use conventional commits
- Document API endpoints
- Follow the design system guidelines

## 🤝 Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details