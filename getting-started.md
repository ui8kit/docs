# Getting Started with UI8Kit

This guide will help you quickly get started with UI8Kit - a modern React UI library.

## 📦 Installation

### npm
```bash
npm install @ui8kit/core
```

### yarn
```bash
yarn add @ui8kit/core
```

### bun
```bash
bun add @ui8kit/core
```

## ⚡ Requirements

- **React**: `^18.0.0 || ^19.0.0`
- **TypeScript**: `^5.0.0` (recommended)
- **Tailwind CSS**: `^3.3.0`

## 🛠️ Setup

### 1. Configure Tailwind CSS

Add UI8Kit to your `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx}',
    './node_modules/@ui8kit/core/dist/**/*.{js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      // UI8Kit uses standard Tailwind colors
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))"
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))"
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))"
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))"
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))"
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))"
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))"
        }
      }
    }
  },
  plugins: []
}
```

### 2. CSS Variables

Add CSS variables to your `globals.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96%;
    --secondary-foreground: 222.2 84% 4.9%;
    --muted: 210 40% 96%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96%;
    --accent-foreground: 222.2 84% 4.9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 221.2 83.2% 53.3%;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;
    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;
    --primary: 217.2 91.2% 59.8%;
    --primary-foreground: 222.2 84% 4.9%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 224.3 76.3% 94.1%;
  }
}
```

## 🚀 Your First Component

Import and use components:

```tsx
import { Button, Block, Container } from '@ui8kit/core'

function App() {
  return (
    <Container>
      <Block py="xl" ta="center">
        <Button variant="primary" size="lg">
          Hello UI8Kit!
        </Button>
      </Block>
    </Container>
  )
}

export default App
```

## 🎨 Theming (Optional)

If you want to use a custom theme:

```tsx
import { ThemeProvider } from './providers/theme'

const customTheme = {
  name: "MyTheme",
  rounded: {
    default: "md",
    button: "lg"
  },
  buttonSize: {
    default: "sm"
  },
  isNavFixed: true
}

function App() {
  return (
    <ThemeProvider theme={customTheme}>
      {/* Your app */}
    </ThemeProvider>
  )
}
```

## 📁 Project Structure

Recommended structure:

```
src/
├── components/
│   └── ui/           # Your custom components
├── providers/
│   └── theme.tsx     # Theme provider
├── App.tsx
└── main.tsx
```

## 🔧 TypeScript

UI8Kit is fully typed. For best types:

```tsx
import type { ButtonProps } from '@ui8kit/core'

// Now you have full IntelliSense
function CustomButton(props: ButtonProps) {
  return <Button {...props} />
}
```

## 🎯 Next Steps

- [API Reference](./api-reference/components.md) - Learn all components
- [Development Guide](./development-guide/) - Best development practices
- [Examples](../apps/web/) - See usage examples
