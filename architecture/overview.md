# Architecture Overview

UI8Kit построен на принципах модульной архитектуры, где каждый слой имеет четкую ответственность. Библиотека сочетает гибкость utility-first подхода с удобством готовых компонентов.

## 🏗️ Архитектурные принципы

### 1. **Utility-First с семантикой**
- Все визуальные свойства доступны как пропы компонентов
- Семантические имена пропов (`bg`, `c`, `p`, `m`)
- Консистентная система значений через всю библиотеку

### 2. **Полиморфные компоненты**
- Компоненты могут рендериться как любой HTML элемент через `component` проп
- Полная типизация для всех возможных элементов
- Гибкость в семантической разметке

### 3. **Система вариантов (CVA)**
- Class Variance Authority для типобезопасных вариантов
- Композиция вариантов без конфликтов
- Автоматическое объединение классов через `tailwind-merge`

### 4. **TypeScript-First**
- Полная типизация всех пропов
- Автодополнение в IDE
- Строгая типобезопасность

## 📦 Структура пакетов

```
packages/@ui8kit/
├── core/                    # Основная библиотека
│   ├── src/
│   │   ├── components/      # React компоненты
│   │   │   ├── ui/          # Базовые UI компоненты
│   │   │   └── *.tsx        # Композитные компоненты
│   │   ├── variants/        # Система вариантов (CVA)
│   │   ├── lib/             # Утилиты
│   │   └── index.ts         # Главный экспорт
│   ├── package.json
│   └── tsconfig.json
├── docs/                    # Документация
└── create-app/              # CLI инструмент
```

## 🔧 Ключевые технологии

### Class Variance Authority (CVA)
```tsx
import { cva } from 'class-variance-authority'

const buttonVariants = cva(
  "inline-flex items-center justify-center", // base styles
  {
    variants: {
      variant: {
        primary: "bg-primary text-primary-foreground",
        secondary: "bg-secondary text-secondary-foreground"
      },
      size: {
        sm: "h-9 px-3",
        lg: "h-11 px-8"
      }
    }
  }
)
```

### Полиморфные компоненты
```tsx
interface BlockProps extends React.HTMLAttributes<HTMLElement> {
  component?: ElementType
}

// Использование
<Block component="section" py="lg">Content</Block>
<Block component="form" onSubmit={handleSubmit}>Form</Block>
```

### Tailwind Merge
```tsx
import { twMerge } from 'tailwind-merge'

// Автоматическое разрешение конфликтов классов
twMerge('px-2 py-1', 'px-4') // → 'py-1 px-4'
```

## 🧩 Слои архитектуры

### 1. **Variants Layer** (variants/)
Определяет все возможные визуальные варианты:

- **spacing.ts** - margin, padding, gaps
- **colors.ts** - background, text, border colors
- **layout.ts** - width, height, position, display
- **typography.ts** - font size, weight, alignment
- **button.ts** - button-specific variants

### 2. **Primitives Layer** (core/ui/)
Базовые компоненты без стилей:

```tsx
// Просто forwardRef без классов
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ children, ...props }, ref) => (
    <button ref={ref} {...props}>
      {children}
    </button>
  )
)
```

### 3. **Components Layer** (components/ui/)
Применяет варианты к примитивам:

```tsx
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'default', size = 'default', className, ...props }, ref) => (
    <button
      ref={ref}
      className={cn(
        buttonVariants({ variant, size }),
        className
      )}
      {...props}
    />
  )
)
```

### 4. **Composition Layer** (components/)
Композитные компоненты из базовых:

```tsx
export function Card({ children, ...props }: CardProps) {
  return (
    <Block bg="card" rounded="lg" shadow="md" {...props}>
      {children}
    </Block>
  )
}
```

## 🎨 Система тем

### Простая структура темы
```tsx
interface Theme {
  name: string
  rounded: Record<string, any> & { default: any }
  buttonSize: Record<string, any> & { default: any }
  isNavFixed?: boolean
}
```

### CSS переменные
Библиотека использует CSS переменные для цветов:
```css
:root {
  --primary: 221.2 83.2% 53.3%;
  --background: 0 0% 100%;
}
```

## 🔄 Data Flow

```
Props → Variants → Classes → Tailwind → CSS
     ↓
Component → forwardRef → Element → DOM
```

## 📊 Принципы производительности

1. **Tree Shaking** - Только используемые компоненты попадают в бандл
2. **CSS-in-JS без рантайма** - Все стили компилируются в CSS
3. **Minimal re-renders** - Стабильные ссылки через useMemo
4. **Small bundle size** - Зависимости: clsx, tailwind-merge, cva

## 🚀 Расширение библиотеки

### Добавление нового варианта
```tsx
// variants/new-feature.ts
export const newFeatureVariants = cva("", {
  variants: {
    variant: {
      primary: "bg-primary",
      secondary: "bg-secondary"
    }
  }
})
```

### Создание нового компонента
```tsx
// components/ui/NewComponent.tsx
export const NewComponent = forwardRef<Element, NewComponentProps>(
  ({ className, ...props }, ref) => (
    <Box
      ref={ref}
      className={cn(newFeatureVariants({ variant }), className)}
      {...props}
    />
  )
)
```
