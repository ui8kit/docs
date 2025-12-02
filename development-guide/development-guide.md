# Development Guide

Comprehensive guide for developers working with UI8Kit. Here you'll find everything you need for efficient development.

## 📋 Contents

- [Basic Workflow](basic-workflow.md) - Step-by-step getting started guide
- [Best Practices](best-practices.md) - Recommendations and patterns
- [Dark Mode](dark-mode.md) - Theme support implementation
- [Component Development](component-development.md) - Creating custom components
- [Theme Customization](theme-customization.md) - Theme customization
- [Testing](testing.md) - Component testing
- [Performance](performance.md) - Performance optimization

## 🎯 Key Concepts

### Utility-First Architecture

UI8Kit is built on utility-first design principles, where every visual aspect is accessible through props:

```tsx
// Instead of CSS classes
<div className="p-4 bg-blue-500 text-white rounded-md">

// Use props
<Block p="md" bg="primary" c="primary-foreground" rounded="md" />
```

### Polymorphic Components

All components can render as any HTML element:

```tsx
// Semantic markup
<Block component="section">
  <Block component="h1">Title</Block>
</Block>

// Accessibility
<Button component="a" href="/dashboard">
  Go to Dashboard
</Button>
```

### Variant System (CVA)

Type-safe variants through Class Variance Authority:

```tsx
// Variants are automatically typed
<Button variant="primary" size="lg" />

// TypeScript knows all possible values
type ButtonProps = {
  variant?: "default" | "primary" | "destructive" | ...
  size?: "xs" | "sm" | "default" | "lg" | "xl" | "icon"
}
```

## 🏗️ Project Architecture

### Recommended Structure

```
src/
├── components/          # Reusable components
│   ├── ui/             # Basic UI components
│   ├── forms/          # Forms and input fields
│   ├── layout/         # Layout components
│   └── feedback/       # Notifications, modals
├── hooks/              # Custom hooks
├── lib/                # Utilities and helpers
├── providers/          # Context providers (theme, auth, etc.)
├── styles/             # Global styles
├── types/              # TypeScript types
├── constants/          # Application constants
└── utils/              # Helper functions
```

### Component Organization

```tsx
// components/index.ts - Barrel exports
export { Button } from './ui/Button'
export { Card } from './ui/Card'
export { Input } from './forms/Input'
export { Modal } from './feedback/Modal'

// components/ui/Button/index.ts
export { Button } from './Button'
export type { ButtonProps } from './Button'

// components/ui/Button/Button.tsx
export interface ButtonProps extends /* ... */ {
  // Props
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (props, ref) => {
    // Implementation
  }
)

Button.displayName = 'Button'
```

## 🎨 Working with Themes

### Basic Setup

```tsx
// providers/theme.tsx
import { createContext, useContext, ReactNode } from 'react'

export type ThemeBase = {
  name: string
  rounded: Record<string, any> & { default: any }
  buttonSize: Record<string, any> & { default: any }
  isNavFixed?: boolean
}

export function ThemeProvider({ children, theme }: {
  children: ReactNode
  theme: ThemeBase
}) {
  // Implementation
}

export function useTheme<T extends ThemeBase = ThemeBase>() {
  // Implementation
}
```

### Custom Themes

```tsx
// themes/index.ts
export const lightTheme = {
  name: "Light",
  rounded: {
    default: "md" as const,
    button: "lg" as const,
    card: "xl" as const
  },
  buttonSize: {
    default: "sm" as const,
    icon: "md" as const
  },
  isNavFixed: true
}

export const darkTheme = {
  // Dark theme configuration
}
```

## 🔧 Development Tools

### TypeScript Configuration

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### ESLint Configuration

```js
// eslint.config.js
import js from '@eslint/js'
import ts from 'typescript-eslint'
import react from 'eslint-plugin-react'
import reactHooks from 'eslint-plugin-react-hooks'

export default [
  js.configs.recommended,
  ...ts.configs.recommended,
  react.configs.flat.recommended,
  reactHooks.configs.recommended,
  {
    rules: {
      // Custom rules
      'react/react-in-jsx-scope': 'off',
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }]
    }
  }
]
```

### Prettier Configuration

```js
// prettier.config.js
export default {
  semi: false,
  singleQuote: true,
  tabWidth: 2,
  trailingComma: 'none',
  printWidth: 100
}
```

## 🧪 Testing

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

### Test Examples

```tsx
// components/__tests__/Button.test.tsx
import { render, screen, fireEvent } from '@/test-utils'
import { Button } from '../Button'

describe('Button', () => {
  it('renders children correctly', () => {
    render(<Button>Hello World</Button>)
    expect(screen.getByText('Hello World')).toBeInTheDocument()
  })

  it('handles click events', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    fireEvent.click(screen.getByRole('button'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('applies correct styles', () => {
    const { container } = render(<Button variant="primary">Button</Button>)
    expect(container.firstChild).toHaveClass('bg-primary')
  })
})
```

## 🚀 Performance Optimization

### React DevTools

Use React DevTools for profiling:

1. Install browser extension
2. Enable "Highlight updates when components render"
3. Use Profiler for performance analysis

### Bundle Analysis

```bash
# Analyze bundle size
npm install -D vite-bundle-analyzer
npm run build
npx vite-bundle-analyzer dist
```

### Optimizations

```tsx
// Component memoization
const MemoizedComponent = memo(function Component({ data }) {
  return <div>{data}</div>
})

// Computation memoization
const filteredData = useMemo(() =>
  data.filter(item => item.active),
  [data]
)

// Stable callbacks
const handleClick = useCallback(() => {
  setCount(c => c + 1)
}, [])
```

## ♿ Accessibility

### ARIA Attributes

```tsx
// Correct ARIA usage
<Button
  aria-expanded={isOpen}
  aria-controls="menu"
  aria-haspopup="menu"
>
  Menu
</Button>

// Screen reader content
<Text className="sr-only">
  Screen reader only text
</Text>
```

### Keyboard navigation

```tsx
// Correct focus management
const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    handleSelect()
  }
}
```

### Color contrast

```tsx
// Use semantic colors
<Text c="foreground">High contrast text</Text>
<Text c="muted">Lower contrast text</Text>

// Don't use hardcoded colors
<Text className="text-gray-600">Bad contrast</Text>
```

## 🔄 CI/CD

### GitHub Actions workflow

```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - run: npm ci
      - run: npm run type-check
      - run: npm run lint
      - run: npm run test
      - run: npm run build
```

### Pre-commit hooks

```bash
# Install husky
npm install -D husky
npx husky install

# Add hooks
echo 'npm run type-check' > .husky/pre-commit
echo 'npm run lint' >> .husky/pre-commit
echo 'npm run test' >> .husky/pre-commit
```

## 📚 Resources

### Official Documentation

- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Testing Library](https://testing-library.com/docs/)

### Tools

- [React DevTools](https://react.dev/learn/react-developer-tools)
- [Vite Bundle Analyzer](https://github.com/btd/vite-bundle-analyzer)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [axe-core](https://github.com/dequelabs/axe-core) - Accessibility testing

### Community

- [React Discord](https://discord.gg/react)
- [TypeScript Community](https://discord.gg/typescript)
- [Tailwind CSS Discord](https://tailwindcss.com/discord)

## 🆘 Troubleshooting

### Common Issues

1. **TypeScript Errors**
   - Check `tsconfig.json`
   - Ensure imports are correct

2. **Styles Not Applied**
   - Check Tailwind configuration
   - Ensure content paths are correct

3. **Components Not Rendering**
   - Check ThemeProvider
   - Ensure CSS variables are correct

4. **Performance**
   - Use React DevTools Profiler
   - Check bundle analyzer

### Debug Mode

```tsx
// Add debug helpers in development
if (process.env.NODE_ENV === 'development') {
  console.log('Component props:', props)
  console.log('Theme context:', useTheme())
}
```

## 🎯 Next Steps

Now that you're familiar with the basics:

1. **Start with [Basic Workflow](basic-workflow.md)**
2. **Learn [Best Practices](best-practices.md)**
3. **Set up [Dark Mode](dark-mode.md)**
4. **Create your components**
5. **Write tests**
6. **Optimize performance**

Join the community and share your components! 🚀
