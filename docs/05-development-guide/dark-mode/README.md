# Dark Mode

## Overview

Dark mode implementation in UI8Kit/Core using the Theme Provider for configuration, toggling, and persistence.

## Theme Configuration

### Setup ThemeProvider

Wrap your application with ThemeProvider:

```typescript
import { ThemeProvider } from 'ui8kit-core/themes';
import { App } from './App';

export function Root() {
  return (
    <ThemeProvider>
      <App />
    </ThemeProvider>
  );
}
```

## Using Dark Mode Hook

Access theme state using `useTheme` hook:

```typescript
import { useTheme } from 'ui8kit-core/themes';

function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();

  return (
    <button onClick={toggleTheme}>
      Current theme: {theme}
    </button>
  );
}
```

### Hook API

```typescript
interface UseThemeReturn {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
  setTheme: (theme: 'light' | 'dark') => void;
  isDark: boolean;
  isLight: boolean;
}

const { 
  theme,      // Current theme value
  toggleTheme,  // Toggle between light/dark
  setTheme,   // Set specific theme
  isDark,     // Boolean check for dark mode
  isLight     // Boolean check for light mode
} = useTheme();
```

## Theme Toggle Component

### Basic Toggle

```typescript
import { useTheme } from 'ui8kit-core/themes';
import { Button } from 'ui8kit-core';

function DarkModeToggle() {
  const { isDark, toggleTheme } = useTheme();

  return (
    <Button 
      onClick={toggleTheme}
      variant={isDark ? 'primary' : 'secondary'}
    >
      {isDark ? '🌙 Dark' : '☀️ Light'}
    </Button>
  );
}
```

### Toggle in Header

```typescript
import { DashLayout, Flex, Button } from 'ui8kit-core';
import { useTheme } from 'ui8kit-core/themes';

function Header() {
  const { isDark, toggleTheme } = useTheme();

  return (
    <Flex 
      justify="between" 
      align="center" 
      padding="md"
    >
      <h1>My App</h1>
      <Flex gap="md">
        <Button>Settings</Button>
        <Button onClick={toggleTheme}>
          {isDark ? '🌙' : '☀️'}
        </Button>
      </Flex>
    </Flex>
  );
}
```

### Toggle with Icon

```typescript
import { useTheme } from 'ui8kit-core/themes';
import { Button } from 'ui8kit-core';

function ThemeToggleIcon() {
  const { isDark, toggleTheme } = useTheme();

  return (
    <Button
      onClick={toggleTheme}
      variant="ghost"
      size="sm"
      aria-label={`Switch to ${isDark ? 'light' : 'dark'} mode`}
    >
      {isDark ? (
        <svg className="w-5 h-5">
          {/* Sun icon */}
        </svg>
      ) : (
        <svg className="w-5 h-5">
          {/* Moon icon */}
        </svg>
      )}
    </Button>
  );
}
```

## Conditional Styling

### Using Theme in Components

```typescript
import { useTheme } from 'ui8kit-core/themes';
import { Card } from 'ui8kit-core';

function ThemedCard() {
  const { isDark } = useTheme();

  return (
    <Card
      bgColor={isDark ? 'dark-gray' : 'white'}
      className={isDark ? 'border-gray-700' : 'border-gray-200'}
    >
      Content
    </Card>
  );
}
```

### Dark Mode Classes

Use Tailwind's dark mode classes:

```typescript
<div className="bg-white dark:bg-gray-900 text-black dark:text-white">
  Content that changes with dark mode
</div>
```

## Persistence

### LocalStorage Persistence

Theme preference is automatically saved to localStorage:

```typescript
// Automatically persisted
const { theme, toggleTheme } = useTheme();

// On page reload, the saved theme is restored
```

### System Preference Detection

ThemeProvider respects system dark mode preference:

```typescript
// If no saved preference, checks:
// prefers-color-scheme: dark/light
```

### Manual Persistence

Override auto-save if needed:

```typescript
import { useTheme } from 'ui8kit-core/themes';
import { useEffect } from 'react';

function MyComponent() {
  const { theme, setTheme } = useTheme();

  useEffect(() => {
    // Save to custom location
    localStorage.setItem('my-app-theme', theme);
  }, [theme]);

  return null;
}
```

## CSS Variables

### Available Theme Variables

Dark mode uses CSS variables for theming:

```css
:root {
  /* Light mode */
  --color-bg: #ffffff;
  --color-text: #000000;
  --color-border: #e5e5e5;
}

:root.dark {
  /* Dark mode */
  --color-bg: #1f2937;
  --color-text: #f3f4f6;
  --color-border: #374151;
}
```

### Using CSS Variables

```typescript
<div className="bg-[var(--color-bg)] text-[var(--color-text)]">
  Uses theme colors
</div>
```

## Complete Theme Setup

### Full Application Example

```typescript
import { ThemeProvider } from 'ui8kit-core/themes';
import { DashLayout, Flex, Button } from 'ui8kit-core';
import { useTheme } from 'ui8kit-core/themes';

function Header() {
  const { isDark, toggleTheme } = useTheme();

  return (
    <Flex justify="between" align="center" padding="md">
      <h1>App Title</h1>
      <Button onClick={toggleTheme}>
        {isDark ? '🌙 Dark' : '☀️ Light'}
      </Button>
    </Flex>
  );
}

function Content() {
  const { isDark } = useTheme();

  return (
    <div className={isDark ? 'bg-gray-900' : 'bg-white'}>
      Main content
    </div>
  );
}

function App() {
  return (
    <DashLayout header={<Header />}>
      <DashLayout.Content>
        <Content />
      </DashLayout.Content>
    </DashLayout>
  );
}

export function Root() {
  return (
    <ThemeProvider defaultTheme="light">
      <App />
    </ThemeProvider>
  );
}
```

## Theme Provider Props

```typescript
interface ThemeProviderProps {
  children: React.ReactNode;
  defaultTheme?: 'light' | 'dark';
  storageKey?: string;
  attribute?: 'class' | 'data-theme';
}

<ThemeProvider
  defaultTheme="light"
  storageKey="my-app-theme"
  attribute="class"
>
  <App />
</ThemeProvider>
```

## Best Practices

### 1. Centralize Theme Toggle
```typescript
// Good - accessible in header
<Header>
  <ThemeToggle />
</Header>

// Less ideal - buried in settings
<Settings>
  <ThemeToggle />
</Settings>
```

### 2. Respect User Preference
```typescript
// Good - respects system preference
<ThemeProvider>
  <App />
</ThemeProvider>

// Less ideal - forces theme
<ThemeProvider defaultTheme="light">
  <App />
</ThemeProvider>
```

### 3. Consistent Colors
```typescript
// Good - use CSS variables
className="bg-[var(--color-bg)]"

// Less consistent - hardcoded
className={isDark ? 'bg-gray-900' : 'bg-white'}
```

## Troubleshooting

### Theme Not Persisting

Check:
1. `ThemeProvider` wraps entire app
2. Browser storage is enabled
3. No conflicting localStorage keys

### Flash of Wrong Theme

Prevent by loading theme early:

```typescript
// Add to head tag
<script>
  const theme = localStorage.getItem('theme') || 'light';
  document.documentElement.classList.add(theme);
</script>
```

### Tailwind Dark Mode Not Working

Ensure Tailwind config includes dark mode:

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  // ... rest of config
};
```

## Next Steps

- [Best Practices](../best-practices/README.md) - General guidelines
- [Development Guide](../README.md) - Back to overview
- [Architecture](../../03-architecture/README.md) - System overview
