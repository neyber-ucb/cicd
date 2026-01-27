# ToDo List Frontend

React + TypeScript + Vite frontend application for the ToDo List API with JWT authentication.

## Features

- ✅ User authentication (Login/Register)
- ✅ JWT token management with auto-refresh
- ✅ Protected routes
- ✅ Full CRUD operations for tasks
- ✅ Modern, responsive UI with TailwindCSS
- ✅ Real-time task updates
- ✅ Task completion tracking
- ✅ Beautiful icons with Lucide React

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **TailwindCSS** - Utility-first CSS framework
- **Axios** - HTTP client
- **Lucide React** - Icon library
- **JWT Decode** - Token decoding

## Prerequisites

- Node.js 18+ and npm
- Backend API running on http://localhost:8000

## Setup

### 1. Install dependencies

```bash
npm install
```

### 2. Run the development server

```bash
npm run dev
```

The application will be available at http://localhost:5173

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   └── ProtectedRoute.tsx    # Route protection component
│   ├── context/
│   │   └── AuthContext.tsx       # Authentication context
│   ├── pages/
│   │   ├── Login.tsx             # Login page
│   │   ├── Register.tsx          # Registration page
│   │   └── Dashboard.tsx         # Main dashboard with tasks
│   ├── services/
│   │   └── api.ts                # API client and endpoints
│   ├── types/
│   │   └── index.ts              # TypeScript type definitions
│   ├── App.tsx                   # Main app with routing
│   ├── main.tsx                  # App entry point
│   └── index.css                 # TailwindCSS imports
├── tailwind.config.js            # TailwindCSS configuration
├── tsconfig.json                 # TypeScript configuration
└── vite.config.ts                # Vite configuration
```

## Usage

### 1. Register a new account

Navigate to http://localhost:5173/register and create a new account.

### 2. Login

After registration, you'll be automatically logged in. Otherwise, go to http://localhost:5173/login

### 3. Manage tasks

On the dashboard, you can:
- **Create** new tasks with title and description
- **Read** all your tasks
- **Update** task details or mark as complete
- **Delete** tasks you no longer need

### 4. Logout

Click the logout button in the navigation bar to end your session.

## Building for Production

```bash
npm run build
```

The production-ready files will be in the `dist/` directory.
