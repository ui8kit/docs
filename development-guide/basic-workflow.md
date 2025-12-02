# Basic Development Workflow

Step-by-step guide to developing with UI8Kit - from installation to deployment. Follow this workflow for efficient work.

## 🚀 Quick Start

### 1. Creating a new project

```bash
# Use create-ui8kit-app (if available)
npx create-ui8kit-app my-app
cd my-app

# Or set up manually
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install @ui8kit/core
```

### 2. Basic Setup

Create `src/providers/theme.tsx`:

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
  const [isDarkMode, setIsDarkMode] = useState(false)
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false)

  const value = useMemo<ThemeContextValue>(() => ({
    theme,
    rounded: theme.rounded,
    buttonSize: theme.buttonSize,
    isDarkMode,
    isNavFixed: theme.isNavFixed,
    prefersReducedMotion,
    toggleDarkMode: () => setIsDarkMode(v => !v),
    setDarkMode,
  }), [theme, isDarkMode, prefersReducedMotion])

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useTheme<T extends ThemeBase = ThemeBase>(): ThemeContextValue<T> {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useTheme must be used within ThemeProvider')
  return ctx as ThemeContextValue<T>
}
```

### 3. Theme Setup

Create `src/themes/index.ts`:

```tsx
export const defaultTheme = {
  name: "Default",
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
```

### 4. CSS Setup

Update `src/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
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
}
```

### 5. Tailwind Setup

Update `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./node_modules/@ui8kit/core/dist/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
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
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))"
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))"
        }
      }
    }
  },
  plugins: []
}
```

### 6. Creating Your First Component

Update `src/App.tsx`:

```tsx
import { Block, Container, Button, Title, Text, Stack } from '@ui8kit/core'
import { ThemeProvider, useTheme } from '@/providers/theme'
import { defaultTheme } from '@/themes'

function AppContent() {
  const { toggleDarkMode, isDarkMode } = useTheme()

  return (
    <Block minH="screen" bg="background" c="foreground">
      <Container py="xl">
        <Stack gap="lg" align="center" ta="center">
          <Title size="4xl">Welcome to UI8Kit</Title>
          <Text size="lg" c="muted">
            Create beautiful web applications with ease
          </Text>
          <Button variant="primary" size="lg" onClick={toggleDarkMode}>
            {isDarkMode ? '☀️ Light Mode' : '🌙 Dark Mode'}
          </Button>
        </Stack>
      </Container>
    </Block>
  )
}

function App() {
  return (
    <ThemeProvider theme={defaultTheme}>
      <AppContent />
    </ThemeProvider>
  )
}

export default App
```

## 🛠️ Daily Workflow

### Component Development

1. **Create Component**
```tsx
// src/components/MyComponent.tsx
import { Block, Button } from '@ui8kit/core'

export function MyComponent() {
  return (
    <Block p="md" bg="card" rounded="md">
      <Button variant="primary">Click me</Button>
    </Block>
  )
}
```

2. **Add to Barrel Export**
```tsx
// src/components/index.ts
export { MyComponent } from './MyComponent'
```

3. **Use in Application**
```tsx
import { MyComponent } from '@/components'

function App() {
  return <MyComponent />
}
```

### Working with Forms

```tsx
import { Block, Box, Button, Group } from '@ui8kit/core'
import { useState } from 'react'

export function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('Form submitted:', formData)
  }

  const handleChange = (field: string) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData(prev => ({ ...prev, [field]: e.target.value }))
  }

  return (
    <Block
      component="form"
      onSubmit={handleSubmit}
      w="full"
      maxW="md"
      p="lg"
      bg="card"
      rounded="lg"
      shadow="md"
    >
      <Stack gap="md">
        <Block>
          <Box
            component="label"
            display="block"
            c="foreground"
            fw="medium"
            mb="sm"
          >
            Name
          </Box>
          <Box
            component="input"
            type="text"
            value={formData.name}
            onChange={handleChange('name')}
            w="full"
            p="md"
            rounded="md"
            border="default"
            bg="input"
            required
          />
        </Block>

        <Block>
          <Box
            component="label"
            display="block"
            c="foreground"
            fw="medium"
            mb="sm"
          >
            Email
          </Box>
          <Box
            component="input"
            type="email"
            value={formData.email}
            onChange={handleChange('email')}
            w="full"
            p="md"
            rounded="md"
            border="default"
            bg="input"
            required
          />
        </Block>

        <Block>
          <Box
            component="label"
            display="block"
            c="foreground"
            fw="medium"
            mb="sm"
          >
            Message
          </Box>
          <Box
            component="textarea"
            value={formData.message}
            onChange={handleChange('message')}
            w="full"
            p="md"
            rounded="md"
            border="default"
            bg="input"
            rows={4}
            required
          />
        </Block>

        <Group justify="end" gap="sm">
          <Button type="button" variant="outline">
            Cancel
          </Button>
          <Button type="submit" variant="primary">
            Send
          </Button>
        </Group>
      </Stack>
    </Block>
  )
}
```

### Working with Grids

```tsx
import { Grid, Card, Title, Text } from '@ui8kit/core'

const products = [
  { id: 1, name: 'Product 1', price: '$29.99' },
  { id: 2, name: 'Product 2', price: '$39.99' },
  { id: 3, name: 'Product 3', price: '$49.99' },
]

export function ProductGrid() {
  return (
    <Grid cols="1-2-3-4" gap="lg">
      {products.map(product => (
        <Card key={product.id} p="md">
          <Stack gap="sm">
            <Title size="lg">{product.name}</Title>
            <Text c="muted">Product description</Text>
            <Text fw="bold" c="primary">{product.price}</Text>
            <Button variant="primary" w="full">
              Add to Cart
            </Button>
          </Stack>
        </Card>
      ))}
    </Grid>
  )
}
```

## 🧪 Testing

### Test Setup

```bash
npm install -D @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

### Creating Tests

```tsx
// src/components/__tests__/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from '@ui8kit/core'

describe('Button', () => {
  it('renders children correctly', () => {
    render(<Button>Hello World</Button>)
    expect(screen.getByText('Hello World')).toBeInTheDocument()
  })

  it('calls onClick when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    fireEvent.click(screen.getByRole('button'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('applies correct variant classes', () => {
    const { container } = render(<Button variant="primary">Button</Button>)
    expect(container.firstChild).toHaveClass('bg-primary')
  })
})
```

### Test Environment Setup

```tsx
// src/test-utils.tsx
import { render, RenderOptions } from '@testing-library/react'
import { ThemeProvider } from '@/providers/theme'
import { defaultTheme } from '@/themes'

const AllTheProviders = ({ children }: { children: React.ReactNode }) => {
  return (
    <ThemeProvider theme={defaultTheme}>
      {children}
    </ThemeProvider>
  )
}

const customRender = (
  ui: React.ReactElement,
  options?: Omit<RenderOptions, 'wrapper'>,
) => render(ui, { wrapper: AllTheProviders, ...options })

export * from '@testing-library/react'
export { customRender as render }
```

## 🚀 Deployment

### Production Build

```bash
npm run build
```

### Pre-deployment Checks

```bash
# Type checking
npm run type-check

# Linting
npm run lint

# Tests
npm run test

# Build
npm run build
```

### Deploy to Vercel

1. Create an account on [Vercel](https://vercel.com)
2. Connect your GitHub repository
3. Configure build settings:
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

### Deploy to Netlify

1. Create an account on [Netlify](https://netlify.com)
2. Drag the `dist` folder to the drag & drop area
3. Or connect GitHub and configure:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`

## 🔧 Extending UI8Kit

### Creating Custom Components

```tsx
// src/components/ui/CustomCard.tsx
import { forwardRef } from 'react'
import { Block } from '@ui8kit/core'
import { cn } from '@/lib/utils'

export interface CustomCardProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'featured'
}

export const CustomCard = forwardRef<HTMLDivElement, CustomCardProps>(
  ({ className, variant = 'default', ...props }, ref) => {
    return (
      <Block
        ref={ref}
        bg="card"
        rounded="lg"
        shadow={variant === 'featured' ? 'lg' : 'md'}
        border={variant === 'featured' ? 'default' : undefined}
        p="lg"
        className={cn(
          variant === 'featured' && 'ring-2 ring-primary/20',
          className
        )}
        {...props}
      />
    )
  }
)

CustomCard.displayName = 'CustomCard'
```

### Adding Custom Variants

```tsx
// src/lib/variants.ts
import { cva } from 'class-variance-authority'

export const statusVariants = cva('', {
  variants: {
    status: {
      success: 'bg-green-100 text-green-800 border-green-200',
      warning: 'bg-yellow-100 text-yellow-800 border-yellow-200',
      error: 'bg-red-100 text-red-800 border-red-200'
    }
  }
})
```

## 📊 Monitoring and Optimization

### Bundle Analysis

```bash
# Install analyzer
npm install -D vite-bundle-analyzer

# Add to package.json
{
  "scripts": {
    "analyze": "vite-bundle-analyzer dist"
  }
}

# Run analysis
npm run build && npm run analyze
```

### Performance monitoring

```tsx
// src/hooks/usePerformance.ts
import { useEffect } from 'react'

export function usePerformance() {
  useEffect(() => {
    if (process.env.NODE_ENV === 'development') {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          console.log('Performance:', entry.name, entry.duration)
        }
      })

      observer.observe({ entryTypes: ['measure'] })

      return () => observer.disconnect()
    }
  }, [])
}
```

## 🎯 Troubleshooting

### Common Issues

1. **Components Not Styling**
   - Check that Tailwind is configured correctly
   - Ensure content paths include UI8Kit

2. **TypeScript Errors**
   - Check TypeScript version (^5.0.0)
   - Ensure types are imported correctly

3. **Theme Not Applied**
   - Check that ThemeProvider wraps the application
   - Ensure CSS variables are defined

4. **Build Failing**
   - Check node_modules
   - Try `rm -rf node_modules && npm install`

### Useful Commands

```bash
# Clean and reinstall
rm -rf node_modules package-lock.json
npm install

# Type checking
npx tsc --noEmit

# Linting
npx eslint src --ext .ts,.tsx

# Formatting
npx prettier --write src
```

## 📚 Next Steps

- [API Reference](../api-reference/) - Learn all components
- [Best Practices](best-practices.md) - Learn best practices
- [Dark Mode](dark-mode.md) - Set up theme support
- [Troubleshooting](../../troubleshooting.md) - Troubleshooting guide
