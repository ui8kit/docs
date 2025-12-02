# Troubleshooting Guide

Руководство по решению распространенных проблем при работе с UI8Kit. Найдите ответы на самые частые вопросы и проблемы.

## 🚨 Быстрая диагностика

### Проверьте базовую настройку

```bash
# 1. Версии пакетов
npm list @ui8kit/core react react-dom typescript

# 2. TypeScript компиляция
npm run type-check

# 3. Линтинг
npm run lint

# 4. Сборка
npm run build
```

### Компоненты не стилизуются?

```tsx
// Проверьте порядок импортов
import './index.css'          // Сначала CSS
import { ThemeProvider } from '@/providers/theme'
import App from './App'

ReactDOM.render(
  <ThemeProvider theme={defaultTheme}>
    <App />
  </ThemeProvider>,
  document.getElementById('root')
)
```

## 🛠️ Распространенные проблемы

### 1. Компоненты не рендерятся / пустой экран

**Симптомы:**
- Компоненты UI8Kit не отображаются
- Стили не применяются
- Консоль ошибок нет

**Решения:**

#### Проверьте ThemeProvider
```tsx
// ✅ Правильно
import { ThemeProvider } from '@/providers/theme'
import { defaultTheme } from '@/themes'

ReactDOM.render(
  <ThemeProvider theme={defaultTheme}>
    <App />
  </ThemeProvider>,
  document.getElementById('root')
)
```

#### Проверьте CSS переменные
```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    /* ... остальные переменные */
  }
}
```

#### Проверьте Tailwind конфигурацию
```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    // ✅ Обязательно для UI8Kit
    "./node_modules/@ui8kit/core/dist/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        // ... остальные цвета
      }
    }
  }
}
```

### 2. TypeScript ошибки

**Симптомы:**
- `Cannot find module '@ui8kit/core'`
- `Property 'variant' does not exist`
- Красные подчеркивания в IDE

**Решения:**

#### Проверьте установку пакета
```bash
# Переустановите зависимости
rm -rf node_modules package-lock.json
npm install
```

#### Проверьте TypeScript конфигурацию
```json
// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "bundler",  // Для Vite
    "allowImportingTsExtensions": true,
    "skipLibCheck": true
  }
}
```

#### Проверьте версии
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

### 3. Стили конфликтуют с Tailwind

**Симптомы:**
- Неправильные цвета или spacing
- Стили не перезаписываются
- Конфликты с существующими стилями

**Решения:**

#### Проверьте порядок CSS
```css
/* Правильный порядок */
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Ваши кастомные стили после */
.my-custom-class {
  /* ... */
}
```

#### Используйте Tailwind merge
```tsx
import { cn } from '@ui8kit/core/lib/utils'

<div className={cn(
  "bg-red-500 text-white",  // Tailwind классы
  "hover:bg-red-600"        // Модификаторы
)}>
```

#### Проверьте content paths
```js
// tailwind.config.js
export default {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,html}",
    "./node_modules/@ui8kit/core/dist/**/*.{js,ts,jsx,tsx}"
  ]
}
```

### 4. Dark mode не работает

**Симптомы:**
- Тема не переключается
- Цвета не меняются
- localStorage не сохраняется

**Решения:**

#### Проверьте ThemeProvider
```tsx
const { toggleDarkMode, isDarkMode } = useTheme()

// Правильное использование
<button onClick={toggleDarkMode}>
  {isDarkMode ? '☀️ Light' : '🌙 Dark'}
</button>
```

#### Проверьте CSS переменные для dark mode
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

#### Проверьте JavaScript
```tsx
useEffect(() => {
  const root = document.documentElement
  root.classList.toggle('dark', isDarkMode)
  root.style.colorScheme = isDarkMode ? 'dark' : 'light'

  localStorage.setItem('ui:dark', isDarkMode ? '1' : '0')
}, [isDarkMode])
```

### 5. Производительность проблем

**Симптомы:**
- Медленная загрузка
- Лаги при взаимодействии
- Высокое использование CPU

**Решения:**

#### Code splitting
```tsx
// Динамические импорты
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

// Стабильные коллбеки
const handleClick = useCallback(() => {
    setCount(c => c + 1)
  }, [])
```

#### Bundle анализ
```bash
# Установите analyzer
npm install -D vite-bundle-analyzer

# Проанализируйте
npm run build
npx vite-bundle-analyzer dist
```

### 6. Формы не работают

**Симптомы:**
- onSubmit не вызывается
- Поля не обновляются
- Валидация не срабатывает

**Решения:**

#### Правильная структура формы
```tsx
function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()  // ✅ Предотвратить перезагрузку
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

### 7. Адаптивность не работает

**Симптомы:**
- Компоненты не перестраиваются на мобильных
- Grid не адаптируется
- Брейкпоинты игнорируются

**Решения:**

#### Проверьте responsive props
```tsx
// ✅ Responsive spacing
<Block p={{ base: "md", md: "lg", xl: "xl" }}>
  Content
</Block>

// ✅ Responsive grid
<Grid cols="1-2-3-4">
  {/* 1 колонка на моб, 4 на xl */}
</Grid>
```

#### Проверьте Tailwind breakpoints
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

### 8. Accessibility проблемы

**Симптомы:**
- Screen readers не работают
- Keyboard navigation не работает
- Color contrast проблемы

**Решения:**

#### ARIA атрибуты
```tsx
// Правильная семантика
<Block component="nav" aria-label="Main navigation">
  <Group component="ul" role="menubar">
    <Block component="li" role="none">
      <Button component="a" href="/">Home</Button>
    </Block>
  </Group>
</Block>

// Screen reader контент
<Text className="sr-only">Loading...</Text>
```

#### Focus management
```tsx
// Правильный focus flow
const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    handleAction()
  }
}
```

## 🧪 Тестирование проблем

### Тесты падают

```tsx
// Проверьте test setup
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

### Mock window APIs

```tsx
// Для localStorage, matchMedia
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

## 🚀 Продвинутые решения

### Custom webpack конфигурация

```js
// Для сложных случаев
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

### Monorepo setup

```json
// Для работы с локальными пакетами
// package.json
{
  "workspaces": [
    "packages/*",
    "apps/*"
  ]
}
```

## 📞 Получение помощи

### Debug информация

```tsx
// Добавьте в development
if (process.env.NODE_ENV === 'development') {
  console.log('UI8Kit Debug:', {
    theme: useTheme(),
    classes: document.documentElement.className,
    cssVariables: getComputedStyle(document.documentElement)
  })
}
```

### Сообщество

- **GitHub Issues**: Для баг репортов
- **GitHub Discussions**: Для вопросов
- **Discord**: Для быстрой помощи

### Необходимая информация для баг репортов

```
## Описание проблемы
- Что ожидалось
- Что произошло
- Шаги для воспроизведения

## Environment
- UI8Kit version: x.x.x
- React version: x.x.x
- TypeScript version: x.x.x
- Browser: Chrome/Firefox/Safari
- OS: Windows/macOS/Linux

## Code example
```tsx
// Минимальный пример для воспроизведения
```

## Logs
```
Console errors or warnings
```
```

## 🎯 Профилактика

### Регулярные проверки

1. **Обновляйте зависимости**
```bash
npm update @ui8kit/core
```

2. **Проверяйте TypeScript**
```bash
npm run type-check
```

3. **Анализируйте bundle**
```bash
npm run build && npm run analyze
```

4. **Тестируйте accessibility**
```bash
npx axe-core your-app-url
```

### Best practices

- Всегда используйте ThemeProvider
- Проверяйте компоненты в обеих темах
- Тестируйте на мобильных устройствах
- Мониторьте performance metrics
- Следите за обновлениями библиотеки

Следуя этому руководству, вы сможете решить большинство проблем с UI8Kit. Если проблема persists, не стесняйтесь обращаться в сообщество! 🚀
