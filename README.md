# WearMind - AI智能时尚助手

WearMind是一个结合AI技术的智能时尚助手应用，帮助用户管理衣橱、获取穿搭建议、虚拟试穿服装和智能购物。

## 功能特点

- **我的衣橱**: 数字化管理您的所有服装物品
- **AI造型师**: 根据场合、天气和个人喜好获取个性化搭配建议
- **虚拟试衣间**: 使用AI技术虚拟试穿任何服装
- **智能购物**: 发现并购买符合您风格的新服装

## 技术栈

### 前端
- Vue.js 3 (Composition API)
- Vite
- Tailwind CSS
- Vue Router

### 后端
- Python
- FastAPI
- PyTorch (用于AI模型)
- OpenCV (图像处理)

## 安装和运行

### 前提条件
- Node.js 16+
- Python 3.8+
- npm 或 yarn

### 安装依赖

```bash
# 安装前端依赖
cd frontend
npm install

# 安装后端依赖
cd backend
pip install -r requirements.txt
```

### 运行开发服务器

```bash
# 运行前端开发服务器
cd frontend
npm run dev

# 运行后端开发服务器
cd backend
python -m uvicorn main:app --reload
```

## 项目结构

```
wearmind/
├── frontend/              # 前端Vue.js应用
│   ├── public/            # 静态资源
│   ├── src/               # 源代码
│   │   ├── assets/        # 资源文件(CSS, 图片等)
│   │   ├── components/    # Vue组件
│   │   ├── pages/         # 页面组件
│   │   ├── router/        # Vue Router配置
│   │   ├── App.vue        # 主应用组件
│   │   └── main.js        # 应用入口
│   ├── index.html         # HTML入口
│   └── vite.config.js     # Vite配置
├── backend/               # 后端Python应用
│   ├── main.py            # FastAPI应用入口
│   ├── ai/                # AI模型和服务
│   │   ├── clothing_recognition/  # 服装识别服务
│   │   ├── style_recommendation/  # 风格推荐服务
│   │   └── virtual_tryon/         # 虚拟试穿服务
└── README.md              # 项目文档
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