# Alche API

This is the backend service for the Alche platform. It exposes the API used by the web and mobile clients and handles authentication, business logic, and data access.

## Overview

The API is built with Node.js and TypeScript, using Express as the HTTP layer and Prisma for database access. It is designed to support a modular backend architecture with separate routes, controllers, middleware, and services.

## Tech Stack

- Node.js
- TypeScript
- Express
- Prisma
- PostgreSQL
- JWT authentication
- Vitest

## Project Structure

```text
api/
├── src/
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── routes/
│   ├── services/
│   └── index.ts
├── prisma/
├── .env.example
├── package.json
├── tsconfig.json
├── README.md
└── ...
```

## Prerequisites

Before starting the API, make sure you have:

- Node.js 18 or newer
- npm or yarn
- PostgreSQL running locally or in a remote environment
- A configured `.env` file with required environment values

## Installation

From the `api` directory, install dependencies:

```bash
npm install
```

## Environment Variables

Create a `.env` file in the `api` directory and add all required values. Example:

```env
PORT=3000
DATABASE_URL=postgresql://user:password@localhost:5432/alche
JWT_SECRET=your_super_secret_key
```

You may also include any other service-specific configuration used by the project.

## Running the API

### Development

```bash
npm run dev
```

This starts the server with watch mode enabled for local development.

### Production Build

```bash
npm run build
npm start
```

## Available Scripts

```bash
npm run dev      # start the server in development mode
npm run build    # compile TypeScript to the dist folder
npm run start    # run the compiled server
npm run lint     # lint the codebase
npm test         # run tests
```

## Database Setup

If Prisma is configured for the project, initialize the database client and apply migrations:

```bash
npx prisma generate
npx prisma migrate dev
```

If the project uses a different database workflow, follow the corresponding setup instructions for that environment.

## API Conventions

- Keep endpoints organized by resource or feature
- Use consistent RESTful patterns
- Validate request payloads before processing
- Return predictable JSON responses
- Centralize business logic in service files
- Protect sensitive routes with middleware and authentication checks

## Security Notes

- Never commit secrets or production credentials
- Keep environment variables in a secure local or hosted secret store
- Validate and sanitize all incoming data
- Use guarded authentication flow for private endpoints

## Deployment

Deploy the API in a Node.js-compatible environment, configure the required environment variables, and ensure your database and infrastructure settings are set correctly for the target deployment.

## License

This project is licensed under the repository's applicable license terms.
