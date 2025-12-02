# Development Guide

Комплексное руководство для разработчиков, работающих с UI8Kit. Здесь вы найдете все необходимое для эффективной разработки.

## 📋 Содержание

- [Basic Workflow](basic-workflow.md) - Пошаговое руководство по началу работы
- [Best Practices](best-practices.md) - Рекомендации и паттерны
- [Dark Mode](dark-mode.md) - Реализация поддержки тем
- [Component Development](component-development.md) - Создание собственных компонентов
- [Theme Customization](theme-customization.md) - Кастомизация тем
- [Testing](testing.md) - Тестирование компонентов
- [Performance](performance.md) - Оптимизация производительности

## 🎯 Ключевые концепции

### Utility-First Architecture

UI8Kit построен на принципах utility-first дизайна, где каждый визуальный аспект доступен через пропы:

```tsx
// Вместо CSS классов
<div className="p-4 bg-blue-500 text-white rounded-md">

// Используйте пропы
<Block p="md" bg="primary" c="primary-foreground" rounded="md" />
```

### Полиморфные компоненты

Все компоненты могут рендериться как любой HTML элемент:

```tsx
// Семантическая разметка
<Block component="section">
  <Block component="h1">Title</Block>
</Block>

// Доступность
<Button component="a" href="/dashboard">
  Go to Dashboard
</Button>
```

### Система вариантов (CVA)

Типобезопасные варианты через Class Variance Authority:

```tsx
// Варианты автоматически типизируются
<Button variant="primary" size="lg" />

// TypeScript знает все возможные значения
type ButtonProps = {
  variant?: "default" | "primary" | "destructive" | ...
  size?: "xs" | "sm" | "default" | "lg" | "xl" | "icon"
}
```

## 🏗️ Архитектура проекта

### Рекомендуемая структура

```
src/
├── components/          # Переиспользуемые компоненты
│   ├── ui/             # Базовые UI компоненты
│   ├── forms/          # Формы и поля ввода
│   ├── layout/         # Layout компоненты
│   └── feedback/       # Уведомления, модалы
├── hooks/              # Кастомные хуки
├── lib/                # Утилиты и helpers
├── providers/          # Context providers (theme, auth, etc.)
├── styles/             # Глобальные стили
├── types/              # TypeScript типы
├── constants/          # Константы приложения
└── utils/              # Вспомогательные функции
```

### Организация компонентов

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

## 🎨 Работа с темами

### Базовая настройка

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

### Кастомные темы

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

## 🔧 Инструменты разработки

### TypeScript конфигурация

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

### ESLint конфигурация

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

### Prettier конфигурация

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

## 🧪 Тестирование

### Настройка тестовой среды

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

### Примеры тестов

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

## 🚀 Оптимизация производительности

### React DevTools

Используйте React DevTools для профилирования:

1. Установите расширение браузера
2. Включите "Highlight updates when components render"
3. Используйте Profiler для анализа производительности

### Bundle анализ

```bash
# Анализ размера бандла
npm install -D vite-bundle-analyzer
npm run build
npx vite-bundle-analyzer dist
```

### Оптимизации

```tsx
// Мемоизация компонентов
const MemoizedComponent = memo(function Component({ data }) {
  return <div>{data}</div>
})

// Мемоизация вычислений
const filteredData = useMemo(() =>
  data.filter(item => item.active),
  [data]
)

// Стабильные коллбеки
const handleClick = useCallback(() => {
  setCount(c => c + 1)
}, [])
```

## ♿ Доступность (Accessibility)

### ARIA атрибуты

```tsx
// Правильное использование ARIA
<Button
  aria-expanded={isOpen}
  aria-controls="menu"
  aria-haspopup="menu"
>
  Menu
</Button>

// Screen reader контент
<Text className="sr-only">
  Screen reader only text
</Text>
```

### Keyboard navigation

```tsx
// Правильный focus management
const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    handleSelect()
  }
}
```

### Color contrast

```tsx
// Используйте семантические цвета
<Text c="foreground">High contrast text</Text>
<Text c="muted">Lower contrast text</Text>

// Не используйте жестко заданные цвета
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
# Установите husky
npm install -D husky
npx husky install

# Добавьте хуки
echo 'npm run type-check' > .husky/pre-commit
echo 'npm run lint' > .husky/pre-commit
echo 'npm run test' > .husky/pre-commit
```

## 📚 Ресурсы

### Официальная документация

- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Testing Library](https://testing-library.com/docs/)

### Инструменты

- [React DevTools](https://react.dev/learn/react-developer-tools)
- [Vite Bundle Analyzer](https://github.com/btd/vite-bundle-analyzer)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [axe-core](https://github.com/dequelabs/axe-core) - Accessibility testing

### Сообщество

- [React Discord](https://discord.gg/react)
- [TypeScript Community](https://discord.gg/typescript)
- [Tailwind CSS Discord](https://tailwindcss.com/discord)

## 🆘 Troubleshooting

### Распространенные проблемы

1. **TypeScript ошибки**
   - Проверьте `tsconfig.json`
   - Убедитесь в правильности импортов

2. **Стили не применяются**
   - Проверьте Tailwind конфигурацию
   - Убедитесь, что content paths корректны

3. **Компоненты не рендерятся**
   - Проверьте ThemeProvider
   - Убедитесь в правильности CSS переменных

4. **Производительность**
   - Используйте React DevTools Profiler
   - Проверьте bundle analyzer

### Debug режим

```tsx
// Добавьте debug helpers в development
if (process.env.NODE_ENV === 'development') {
  console.log('Component props:', props)
  console.log('Theme context:', useTheme())
}
```

## 🎯 Следующие шаги

Теперь, когда вы ознакомились с основами:

1. **Начните с [Basic Workflow](basic-workflow.md)**
2. **Изучите [Best Practices](best-practices.md)**
3. **Настройте [Dark Mode](dark-mode.md)**
4. **Создайте свои компоненты**
5. **Напишите тесты**
6. **Оптимизируйте производительность**

Присоединяйтесь к сообществу и делитесь своими компонентами! 🚀
