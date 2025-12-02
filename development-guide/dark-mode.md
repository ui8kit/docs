# Dark Mode Implementation

Complete guide to implementing dark mode in UI8Kit applications with system preferences support and manual switching.

## 🎯 Overview

UI8Kit provides a ready-made theme system with dark mode support through:

- CSS variables for colors
- ThemeProvider context
- Automatic system preferences detection
- Smooth transitions between themes

## 🛠️ CSS Variables Setup

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

## 🎨 ThemeProvider

Create theme provider in `src/providers/theme.tsx`:

```tsx
import { createContext, useContext, useEffect, useMemo, useState, ReactNode } from 'react'

export type ThemeBase = {
  name: string
  rounded: Record<string, any> & { default: any }
  buttonSize: Record<string, any> & { default: any }
  isNavFixed?: boolean
}

interface ThemeContextValue<T extends ThemeBase = ThemeBase> {
  theme: T
  rounded: T['rounded']
  buttonSize: T['buttonSize']
  isDarkMode: boolean
  isNavFixed?: T['isNavFixed']
  prefersReducedMotion: boolean
  toggleDarkMode: () => void
  setDarkMode: (value: boolean) => void
}

const ThemeContext = createContext<ThemeContextValue<ThemeBase> | null>(null)

export function ThemeProvider({ children, theme }: { children: ReactNode; theme: ThemeBase }) {
  const baseTheme = theme

  const [isDarkMode, setIsDarkMode] = useState<boolean>(() => {
    const stored = typeof window !== 'undefined' ? window.localStorage.getItem('ui:dark') : null
    if (stored !== null) return stored === '1'
    if (typeof window !== 'undefined' && window.matchMedia) {
      return window.matchMedia('(prefers-color-scheme: dark)').matches
    }
    return false
  })

  useEffect(() => {
    if (typeof document === 'undefined') return
    document.documentElement.classList.toggle('dark', isDarkMode)
    document.documentElement.style.colorScheme = isDarkMode ? 'dark' : 'light'
    try {
      window.localStorage.setItem('ui:dark', isDarkMode ? '1' : '0')
    } catch {}
  }, [isDarkMode])

  const [prefersReducedMotion, setPrefersReducedMotion] = useState<boolean>(() => {
    if (typeof window === 'undefined' || !window.matchMedia) return false
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches
  })

  useEffect(() => {
    if (typeof window === 'undefined' || !window.matchMedia) return
    const mql = window.matchMedia('(prefers-reduced-motion: reduce)')
    const handler = (e: MediaQueryListEvent | MediaQueryList) => {
      const matches = 'matches' in e ? e.matches : (e as MediaQueryList).matches
      setPrefersReducedMotion(matches)
    }
    handler(mql as unknown as MediaQueryList)
    if (mql.addEventListener) {
      mql.addEventListener('change', handler as EventListener)
      return () => mql.removeEventListener('change', handler as EventListener)
    } else if (mql.addListener) {
      mql.addListener(handler)
      return () => mql.removeListener(handler)
    }
  }, [])

  const value = useMemo<ThemeContextValue>(
    () => ({
      theme: baseTheme,
      rounded: baseTheme.rounded,
      buttonSize: baseTheme.buttonSize,
      isDarkMode,
      isNavFixed: baseTheme.isNavFixed,
      prefersReducedMotion,
      toggleDarkMode: () => setIsDarkMode((v) => !v),
      setDarkMode: setIsDarkMode,
    }),
    [baseTheme, isDarkMode, prefersReducedMotion]
  )

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useTheme<T extends ThemeBase = ThemeBase>(): ThemeContextValue<T> {
  const ctx = useContext(ThemeContext)
  if (!ctx) {
    throw new Error('useTheme must be used within ThemeProvider')
  }
  return ctx as ThemeContextValue<T>
}
```

## 🎭 Theme Definition

Create theme configuration:

```tsx
// src/themes/index.ts
export const lightTheme = {
  name: "Light",
  rounded: {
    default: "md" as const,
    button: "lg" as const,
    badge: "xl" as const
  },
  buttonSize: {
    default: "sm" as const,
    badge: "sm" as const
  },
  isNavFixed: true
} as const

export const darkTheme = {
  name: "Dark",
  rounded: {
    default: "sm" as const,
    button: "md" as const,
    badge: "2xl" as const
  },
  buttonSize: {
    default: "md" as const,
    badge: "md" as const
  },
  isNavFixed: true
} as const

export const lesseUITheme = {
  name: "LesseUI",
  rounded: {
    default: "sm" as const,
    button: "md" as const,
    badge: "xl" as const
  },
  buttonSize: {
    default: "sm" as const,
    badge: "sm" as const
  },
  isNavFixed: true
} as const
```

## 🚀 Usage in Application

### Basic Setup

```tsx
// src/main.tsx
import { ThemeProvider } from '@/providers/theme'
import { lesseUITheme } from '@/themes'
import App from './App'

ReactDOM.render(
  <ThemeProvider theme={lesseUITheme}>
    <App />
  </ThemeProvider>,
  document.getElementById('root')
)
```

### Theme Toggle Component

```tsx
// src/components/ThemeToggle.tsx
import { Button } from '@ui8kit/core'
import { useTheme } from '@/providers/theme'

export function ThemeToggle() {
  const { toggleDarkMode, isDarkMode } = useTheme()

  return (
    <Button
      variant={isDarkMode ? 'primary' : 'secondary'}
      onClick={toggleDarkMode}
    >
      {!isDarkMode ? '🌙 Dark Mode' : '☀️ Light Mode'}
    </Button>
  )
}
```

### App component

```tsx
// src/App.tsx
import { Block, Container, Title, Text, Stack } from '@ui8kit/core'
import { useTheme } from '@/providers/theme'
import { ThemeToggle } from '@/components/ThemeToggle'

function AppContent() {
  const { isDarkMode } = useTheme()

  return (
    <Block py="xl">
      <Container>
        <Stack gap="lg" align="center" ta="center">
          <Title size="4xl">Welcome to UI8Kit</Title>
          <Text>
            Create beautiful web applications with ease using our UI components
          </Text>
          <ThemeToggle />
          <Text size="sm" c="muted">
            Current theme: {isDarkMode ? 'Dark' : 'Light'}
          </Text>
        </Stack>
      </Container>
    </Block>
  )
}

export default function App() {
  return <AppContent />
}
```

## 🎨 Custom Colors for Dark Mode

### Adding Custom Colors

```css
@layer base {
  :root {
    --custom-primary: 220 70% 50%;
    --custom-secondary: 160 60% 50%;
  }

  .dark {
    --custom-primary: 220 70% 60%;
    --custom-secondary: 160 60% 60%;
  }
}
```

### Usage in Tailwind Config

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        custom: {
          primary: 'hsl(var(--custom-primary))',
          secondary: 'hsl(var(--custom-secondary))'
        }
      }
    }
  }
}
```

## 🔧 Advanced Patterns

### Themes with Context

```tsx
// src/contexts/ThemeContext.tsx
import { createContext, useContext, useState } from 'react'
import { ThemeProvider, useTheme, type ThemeBase } from '@/providers/theme'
import { lightTheme, darkTheme } from '@/themes'

type ThemeMode = 'light' | 'dark' | 'system'

interface ExtendedThemeContext {
  mode: ThemeMode
  setMode: (mode: ThemeMode) => void
  actualTheme: ThemeBase
}

const ExtendedThemeContext = createContext<ExtendedThemeContext | null>(null)

export function ExtendedThemeProvider({ children }: { children: ReactNode }) {
  const [mode, setMode] = useState<ThemeMode>('system')
  const { isDarkMode, setDarkMode } = useTheme()

  const actualTheme = mode === 'system'
    ? (isDarkMode ? darkTheme : lightTheme)
    : mode === 'dark' ? darkTheme : lightTheme

  useEffect(() => {
    if (mode === 'system') {
      setDarkMode(window.matchMedia('(prefers-color-scheme: dark)').matches)
    } else {
      setDarkMode(mode === 'dark')
    }
  }, [mode, setDarkMode])

  return (
    <ThemeProvider theme={actualTheme}>
      <ExtendedThemeContext.Provider value={{ mode, setMode, actualTheme }}>
        {children}
      </ExtendedThemeContext.Provider>
    </ThemeProvider>
  )
}

export function useExtendedTheme() {
  const ctx = useContext(ExtendedThemeContext)
  if (!ctx) throw new Error('useExtendedTheme must be used within ExtendedThemeProvider')
  return ctx
}
```

### Theme Selector Component

```tsx
// src/components/ThemeSelector.tsx
import { Button, Group } from '@ui8kit/core'
import { useExtendedTheme } from '@/contexts/ThemeContext'

const themes = [
  { key: 'light', label: '☀️ Light', value: 'light' },
  { key: 'dark', label: '🌙 Dark', value: 'dark' },
  { key: 'system', label: '💻 System', value: 'system' }
] as const

export function ThemeSelector() {
  const { mode, setMode } = useExtendedTheme()

  return (
    <Group gap="sm">
      {themes.map((theme) => (
        <Button
          key={theme.key}
          variant={mode === theme.value ? 'default' : 'outline'}
          size="sm"
          onClick={() => setMode(theme.value)}
        >
          {theme.label}
        </Button>
      ))}
    </Group>
  )
}
```

## 🎭 Transition Animations

Add smooth transitions between themes:

```css
@layer base {
  * {
    transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease;
  }

  /* Disable animations on reduced motion */
  @media (prefers-reduced-motion: reduce) {
    * {
      transition: none;
    }
  }
}
```

## 🔍 Debugging Dark Mode

### Debug Hook

```tsx
// src/hooks/useThemeDebug.ts
import { useTheme } from '@/providers/theme'
import { useEffect } from 'react'

export function useThemeDebug() {
  const { isDarkMode, prefersReducedMotion } = useTheme()

  useEffect(() => {
    console.log('Theme Debug:', {
      isDarkMode,
      prefersReducedMotion,
      documentClass: document.documentElement.className,
      colorScheme: document.documentElement.style.colorScheme
    })
  }, [isDarkMode, prefersReducedMotion])
}
```

### Visual Theme Indicator

```tsx
// src/components/ThemeIndicator.tsx
import { Badge } from '@ui8kit/core'
import { useTheme } from '@/providers/theme'

export function ThemeIndicator() {
  const { isDarkMode } = useTheme()

  if (process.env.NODE_ENV !== 'development') return null

  return (
    <Badge
      variant={isDarkMode ? 'default' : 'secondary'}
      className="fixed bottom-4 right-4 z-50"
    >
      {isDarkMode ? '🌙 Dark' : '☀️ Light'}
    </Badge>
  )
}
```

## 📱 System Preferences

### Automatic Tracking

ThemeProvider automatically tracks system preference changes:

```tsx
useEffect(() => {
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
  const handler = (e) => setDarkMode(e.matches)

  mediaQuery.addEventListener('change', handler)
  return () => mediaQuery.removeEventListener('change', handler)
}, [])
```

### Testing System Preferences

```js
// In browser console
// Simulate dark theme
window.matchMedia('(prefers-color-scheme: dark)').matches = true
window.dispatchEvent(new Event('change'))

// Simulate light theme
window.matchMedia('(prefers-color-scheme: dark)').matches = false
window.dispatchEvent(new Event('change'))
```

## 🚀 Best Practices

1. **Always use semantic colors** instead of hardcoded ones
2. **Test both themes** - light and dark
3. **Consider contrast** for accessibility
4. **Add smooth transitions** for better UX
5. **Save user preference** in localStorage
6. **Support system preferences** by default
7. **Test with reduced motion** settings
