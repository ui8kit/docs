# Build System

UI8Kit uses a modern build system optimized for performance, tree shaking, and developer experience.

## 🏗️ Build Architecture

### Monorepo Structure

```
packages/
├── @ui8kit/
│   ├── core/           # Main library
│   ├── docs/           # Documentation
│   └── create-app/     # CLI tool
├── apps/
│   └── web/            # Example application
workspace/
├── package.json        # Root dependencies
├── turbo.json          # Build orchestration
└── tsconfig.json       # Base TypeScript config
```

### Turbo - Build Orchestration

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["**/.env.*local"],
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "lint": {},
    "type-check": {},
    "test": {},
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

## 📦 Core Library

### TypeScript + tsc

```json
// packages/@ui8kit/core/package.json
{
  "scripts": {
    "build": "tsc -p tsconfig.json",
    "type-check": "tsc --noEmit",
    "lint": "eslint src --ext .ts,.tsx",
    "lint:fix": "eslint src --ext .ts,.tsx --fix"
  }
}
```

```json
// packages/@ui8kit/core/tsconfig.json
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "outDir": "dist",
    "declaration": true,
    "declarationMap": true,
    "emitDeclarationOnly": false,
    "noEmit": false,
    "isolatedModules": false
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "**/*.test.ts", "**/*.test.tsx", "dist"]
}
```

### ESM + CJS outputs

```json
// package.json exports
{
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  }
}
```

### Bundle Analysis

```bash
# packages/@ui8kit/core/package.json
{
  "scripts": {
    "analyze": "npx vite-bundle-analyzer dist"
  }
}
```

## 🛠️ Development setup

### Vite for Applications

```typescript
// apps/web/vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  server: {
    port: 3000,
    open: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@ui8kit/core']
        }
      }
    }
  }
})
```

### Hot Module Replacement

Vite provides instant HMR:

```tsx
// Automatic reload on changes
if (import.meta.hot) {
  import.meta.hot.accept()
}
```

## 🎨 CSS and Styling

### Tailwind CSS

```js
// apps/web/tailwind.config.js
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
        // ... semantic colors
      }
    }
  },
  plugins: []
}
```

### PostCSS

```js
// apps/web/postcss.config.js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
}
```

## 🔧 Quality Assurance

### ESLint

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
      'react/react-in-jsx-scope': 'off',
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/consistent-type-imports': 'error'
    }
  }
]
```

### Prettier

```js
// prettier.config.js
export default {
  semi: false,
  singleQuote: true,
  tabWidth: 2,
  trailingComma: 'none',
  printWidth: 100,
  plugins: ['prettier-plugin-tailwindcss']
}
```

### Husky + lint-staged

```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{js,json}": ["prettier --write"]
  }
}
```

## 🚀 Deployment

### CI/CD Pipeline

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

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: npm run deploy
```

### Bundle optimization

```typescript
// vite.config.ts
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // Chunk splitting
          vendor: ['react', 'react-dom'],
          ui: ['@ui8kit/core'],
          utils: ['clsx', 'tailwind-merge']
        }
      }
    },
    // Minification
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    }
  }
})
```

## 📊 Performance monitoring

### Bundle analyzer

```bash
# Bundle size analysis
npm install -D vite-bundle-analyzer
npm run build
npx vite-bundle-analyzer dist
```

### Lighthouse CI

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse

on: [pull_request]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install -g @lhci/cli
      - run: lhci autorun
```

## 🧪 Testing Infrastructure

### Jest + Testing Library

```js
// jest.config.js
export default {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/test-setup.ts'],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts'
  ],
  coverageReporters: ['text', 'lcov', 'html']
}
```

### Test setup

```tsx
// src/test-setup.ts
import '@testing-library/jest-dom'

// Mock window.matchMedia
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

## 🔄 Version Management

### Changesets

```json
// .changeset/config.json
{
  "$schema": "https://unpkg.com/@changesets/config@2.3.0/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}
```

### Release workflow

```bash
# Create changeset
npx changeset

# Version bump
npx changeset version

# Publish
npx changeset publish
```

## 📈 Monitoring & Analytics

### Error tracking

```tsx
// src/lib/error-tracking.ts
import * as Sentry from '@sentry/react'

Sentry.init({
  dsn: process.env.REACT_APP_SENTRY_DSN,
  environment: process.env.NODE_ENV
})
```

### Performance monitoring

```tsx
// src/lib/performance.ts
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals'

getCLS(console.log)
getFID(console.log)
getFCP(console.log)
getLCP(console.log)
getTTFB(console.log)
```

## 🎯 Optimization Strategies

### Tree shaking

```typescript
// Ensure exports are tree-shakeable
export { Button } from './Button'
export type { ButtonProps } from './Button'

// Don't use default exports
export { default as Button } from './Button' // ❌
```

### Dynamic imports

```tsx
// Code splitting for routes
const Dashboard = lazy(() => import('./pages/Dashboard'))
const Settings = lazy(() => import('./pages/Settings'))
```

### Image optimization

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import { imagetools } from 'vite-imagetools'

export default defineConfig({
  plugins: [imagetools()]
})
```

## 🔒 Security

### Dependency scanning

```yaml
# .github/workflows/security.yml
name: Security

on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm audit --audit-level=high
      - run: npm run lint:security
```

### CSP headers

```typescript
// For production build
const csp = {
  'default-src': "'self'",
  'style-src': "'self' 'unsafe-inline'",
  'script-src': "'self'"
}
```

## 📚 Resources

### Build tools
- [Vite](https://vitejs.dev/)
- [Turbo](https://turbo.build/)
- [esbuild](https://esbuild.github.io/)

### Quality tools
- [ESLint](https://eslint.org/)
- [Prettier](https://prettier.io/)
- [TypeScript](https://www.typescriptlang.org/)

### Testing
- [Jest](https://jestjs.io/)
- [Testing Library](https://testing-library.com/)

### Deployment
- [Vercel](https://vercel.com/)
- [Netlify](https://netlify.com/)
- [Railway](https://railway.app/)

UI8Kit's modern build system ensures fast development, high performance, and reliability in production! 🚀
