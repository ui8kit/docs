# Troubleshooting Guide

Guide to solving common problems when working with UI8Kit. Find answers to the most frequent questions and issues.

## 🚨 Quick Diagnostics

### Check basic setup

```bash
# 1. Package versions
npm list @ui8kit/core react react-dom typescript

# 2. TypeScript compilation
npm run type-check

# 3. Linting
npm run lint

# 4. Build
npm run build
```

### Components not styling?

```tsx
// Check import order
import './index.css'          // CSS first
import { ThemeProvider } from '@/providers/theme'
import App from './App'

ReactDOM.render(
  <ThemeProvider theme={defaultTheme}>
    <App />
  </ThemeProvider>,
  document.getElementById('root')
)
```

## 🛠️ Common Problems

### 1. Components not rendering / blank screen

**Symptoms:**
- UI8Kit components don't display
- Styles not applied
- No console errors

**Solutions:**

#### Check ThemeProvider
```tsx
// ✅ Correct
import { ThemeProvider } from '@/providers/theme'
import { defaultTheme } from '@/themes'

ReactDOM.render(
  <ThemeProvider theme={defaultTheme}>
    <App />
  </ThemeProvider>,
  document.getElementById('root')
)
```

#### Check CSS Variables
```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    /* ... other variables */
  }
}
```

#### Check Tailwind Configuration
```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    // ✅ Required for UI8Kit
    "./node_modules/@ui8kit/core/dist/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        // ... other colors
      }
    }
  }
}
```

### 2. TypeScript Errors

**Symptoms:**
- `Cannot find module '@ui8kit/core'`
- `Property 'variant' does not exist`
- Red underlines in IDE

**Solutions:**

#### Check Package Installation
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

#### Check TypeScript Configuration
```json
// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "bundler",  // For Vite
    "allowImportingTsExtensions": true,
    "skipLibCheck": true
  }
}
```

#### Check Versions
```json
// package.json
{
  "dependencies": {
    "@ui8kit/core": "^0.1.8",
    "typescript": "^5.0.0",
    "react": "^18.0.0 || ^19.0.0"
  }
}
```

### 3. Styles Conflict with Tailwind

**Symptoms:**
- Incorrect colors or spacing
- Styles not being overridden
- Conflicts with existing styles

**Solutions:**

#### Check CSS Order
```css
/* Correct order */
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Your custom styles after */
.my-custom-class {
  /* ... */
}
```

#### Use Tailwind Merge
```tsx
import { cn } from '@ui8kit/core/lib/utils'

<div className={cn(
  "bg-red-500 text-white",  // Tailwind classes
  "hover:bg-red-600"        // Modifiers
)}>
```

#### Check Content Paths
```js
// tailwind.config.js
export default {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,html}",
    "./node_modules/@ui8kit/core/dist/**/*.{js,ts,jsx,tsx}"
  ]
}
```

### 4. Dark Mode Not Working

**Symptoms:**
- Theme doesn't switch
- Colors don't change
- localStorage doesn't save

**Solutions:**

#### Check ThemeProvider
```tsx
const { toggleDarkMode, isDarkMode } = useTheme()

// Correct usage
<button onClick={toggleDarkMode}>
  {isDarkMode ? '☀️ Light' : '🌙 Dark'}
</button>
```

#### Check CSS Variables for Dark Mode
```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
  }
}
```

#### Check JavaScript
```tsx
useEffect(() => {
  const root = document.documentElement
  root.classList.toggle('dark', isDarkMode)
  root.style.colorScheme = isDarkMode ? 'dark' : 'light'

  localStorage.setItem('ui:dark', isDarkMode ? '1' : '0')
}, [isDarkMode])
```

### 5. Performance Issues

**Symptoms:**
- Slow loading
- Lag during interaction
- High CPU usage

**Solutions:**

#### Code Splitting
```tsx
// Dynamic imports
const Modal = lazy(() => import('./Modal'))

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Modal />
    </Suspense>
  )
}
```

#### Memoization
```tsx
const MemoizedComponent = memo(function Component({ data }) {
  return <div>{data}</div>
})

// Stable callbacks
const handleClick = useCallback(() => {
    setCount(c => c + 1)
  }, [])
```

#### Bundle Analysis
```bash
# Install analyzer
npm install -D vite-bundle-analyzer

# Analyze
npm run build
npx vite-bundle-analyzer dist
```

### 6. Forms Not Working

**Symptoms:**
- onSubmit not called
- Fields don't update
- Validation doesn't trigger

**Solutions:**

#### Correct Form Structure
```tsx
function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()  // ✅ Prevent reload
    console.log(formData)
  }

  const handleChange = (field: string) => (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({ ...prev, [field]: e.target.value }))
  }

  return (
    <Block component="form" onSubmit={handleSubmit}>
      <Box component="input" value={formData.name} onChange={handleChange('name')} />
      <Button type="submit">Send</Button>
    </Block>
  )
}
```

#### Controlled inputs
```tsx
// ✅ Controlled
const [value, setValue] = useState('')
<Box component="input" value={value} onChange={e => setValue(e.target.value)} />

// ❌ Uncontrolled
<Box component="input" defaultValue="value" />
```

### 7. Responsiveness Not Working

**Symptoms:**
- Components don't rearrange on mobile
- Grid doesn't adapt
- Breakpoints ignored

**Solutions:**

#### Check Responsive Props
```tsx
// ✅ Responsive spacing
<Block p={{ base: "md", md: "lg", xl: "xl" }}>
  Content
</Block>

// ✅ Responsive grid
<Grid cols="1-2-3-4">
  {/* 1 column on mobile, 4 on xl */}
</Grid>
```

#### Check Tailwind Breakpoints
```js
// tailwind.config.js
export default {
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px'
    }
  }
}
```

### 8. Accessibility Issues

**Symptoms:**
- Screen readers don't work
- Keyboard navigation doesn't work
- Color contrast issues

**Solutions:**

#### ARIA Attributes
```tsx
// Correct semantics
<Block component="nav" aria-label="Main navigation">
  <Group component="ul" role="menubar">
    <Block component="li" role="none">
      <Button component="a" href="/">Home</Button>
    </Block>
  </Group>
</Block>

// Screen reader content
<Text className="sr-only">Loading...</Text>
```

#### Focus Management
```tsx
// Correct focus flow
const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    handleAction()
  }
}
```

## 🧪 Testing Issues

### Tests Failing

```tsx
// Check test setup
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

### Mock Window APIs

```tsx
// For localStorage, matchMedia
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn()
  }))
})
```

## 🚀 Advanced Solutions

### Custom Webpack Configuration

```js
// For complex cases
// webpack.config.js
module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@ui8kit/core': path.resolve(__dirname, 'node_modules/@ui8kit/core/dist')
    }
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }
    ]
  }
}
```

### Monorepo Setup

```json
// For working with local packages
// package.json
{
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

## 📞 Getting Help

### Debug Information

```tsx
// Add in development
if (process.env.NODE_ENV === 'development') {
  console.log('UI8Kit Debug:', {
    theme: useTheme(),
    classes: document.documentElement.className,
    cssVariables: getComputedStyle(document.documentElement)
  })
}
```

### Community

- **GitHub Issues**: For bug reports
- **GitHub Discussions**: For questions
- **Discord**: For quick help

### Required Information for Bug Reports

```
## Problem Description
- What was expected
- What happened
- Steps to reproduce

## Environment
- UI8Kit version: x.x.x
- React version: x.x.x
- TypeScript version: x.x.x
- Browser: Chrome/Firefox/Safari
- OS: Windows/macOS/Linux

## Code Example
```tsx
// Minimal example to reproduce
```

## Logs
```
Console errors or warnings
```
```

## 🎯 Prevention

### Regular Checks

1. **Update Dependencies**
```bash
npm update @ui8kit/core
```

2. **Check TypeScript**
```bash
npm run type-check
```

3. **Analyze Bundle**
```bash
npm run build && npm run analyze
```

4. **Test Accessibility**
```bash
npx axe-core your-app-url
```

### Best Practices

- Always use ThemeProvider
- Test components in both themes
- Test on mobile devices
- Monitor performance metrics
- Follow library updates

Following this guide, you'll be able to solve most UI8Kit issues. If the problem persists, don't hesitate to reach out to the community! 🚀
