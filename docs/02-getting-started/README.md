# Getting Started

## Installation

### NPM Installation

```bash
npm install ui8kit-core
```

### Yarn Installation

```bash
yarn add ui8kit-core
```

### Bun Installation

```bash
bun add ui8kit-core
```

## Basic Setup

### 1. Tailwind CSS Configuration

UI8Kit/Core requires Tailwind CSS to be set up in your project. If you haven't already, follow the [Tailwind CSS installation guide](https://tailwindcss.com/docs/installation).

Ensure your `tailwind.config.js` includes:

```javascript
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./node_modules/ui8kit-core/dist/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### 2. Import Components

In your React application:

```typescript
import { Button, Card } from 'ui8kit-core';

export default function App() {
  return (
    <Card>
      <Card.Header>Welcome</Card.Header>
      <Card.Content>
        <Button variant="primary">Click me</Button>
      </Card.Content>
    </Card>
  );
}
```

## Setup for Different Project Types

### Next.js

Add to your `next.config.js`:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Your existing config...
};

module.exports = nextConfig;
```

### Vite

No additional configuration needed. Just ensure Tailwind CSS is installed and configured.

### Create React App

No additional configuration needed beyond standard CRA setup with Tailwind CSS.

## Verification

To verify the installation was successful:

1. Import a component
2. Use it in your JSX
3. Check that styles are applied correctly

If styles aren't showing up, ensure:
- Tailwind CSS is properly configured
- The content path in `tailwind.config.js` includes UI8Kit/Core
- Your CSS file imports Tailwind directives

## Next Steps

- [Architecture](../03-architecture/README.md) - Understand how components are organized
- [API Reference](../04-api-reference/README.md) - Explore available components
- [Development Guide](../05-development-guide/README.md) - Learn usage patterns
