# Alche API

A backend API service for the Alche platform.

## Overview

This project provides the REST API used by the application. It handles authentication, user management, business logic, and persistence for the platform.

## Tech Stack

- Node.js
- Express
- TypeScript
- PostgreSQL / Prisma (if used in the project)
- JWT-based auth

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn
- A configured database connection
- Environment variables set in a `.env` file

### Installation

```bash
npm install
```

### Environment Variables

Create a `.env` file in the `api` directory and add the required variables. Example:

```env
PORT=3000
DATABASE_URL=postgresql://user:password@localhost:5432/alche
JWT_SECRET=your_jwt_secret
```

### Run the API

Development mode:

```bash
npm run dev
```

Production mode:

```bash
npm run build
npm start
```

## Project Structure

```text
api/
├── src/
│   ├── controllers/
│   ├── routes/
│   ├── services/
│   ├── middleware/
│   ├── config/
│   └── index.ts
├── .env.example
├── package.json
├── tsconfig.json
└── README.md
```

## Available Scripts

```bash
npm run dev      # start development server
npm run build    # compile TypeScript
npm run start    # run built server
npm run lint     # lint the codebase
npm test         # run tests
```

## API Conventions

- Use RESTful routes
- Validate request payloads
- Return consistent JSON responses
- Protect sensitive routes with authentication middleware
- Centralize business logic in services

## Deployment

Deploy this service behind a reverse proxy or API gateway and configure environment variables in your hosting platform.

## License

This project is licensed under the terms in the repository.
