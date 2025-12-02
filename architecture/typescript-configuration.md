# TypeScript Configuration

UI8Kit построен с TypeScript-first подходом. Эта документация объясняет, как настроить TypeScript для максимальной эффективности работы с библиотекой.

## 📋 Рекомендуемая конфигурация

### tsconfig.json для приложений

```json
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
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/components": ["src/components"],
      "@/lib/*": ["src/lib/*"],
      "@/hooks/*": ["src/hooks/*"],
      "@/providers/*": ["src/providers/*"],
      "@/types/*": ["src/types/*"],
      "@/utils/*": ["src/utils/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### tsconfig.json для библиотек

```json
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

## 🔧 Ключевые опции

### Target и Lib
```json
{
  "target": "ES2020",
  "lib": ["ES2020", "DOM", "DOM.Iterable"]
}
```
- **ES2020**: Современные возможности JS
- **DOM**: Браузерные API
- **DOM.Iterable**: for...of для DOM коллекций

### Module Resolution
```json
{
  "module": "ESNext",
  "moduleResolution": "bundler"
}
```
- **ESNext**: Современные ES модули
- **bundler**: Для Vite/Rollup/Webpack

### JSX
```json
{
  "jsx": "react-jsx"
}
```
Автоматический импорт React для JSX.

### Strict Mode
```json
{
  "strict": true,
  "noUnusedLocals": true,
  "noUnusedParameters": true,
  "noFallthroughCasesInSwitch": true
}
```
Максимальная строгость для качества кода.

### Path Mapping
```json
{
  "baseUrl": ".",
  "paths": {
    "@/*": ["src/*"],
    "@/components": ["src/components"]
  }
}
```
Короткие импорты для лучшей DX.

## 🎯 UI8Kit TypeScript API

### Типы компонентов

Все компоненты экспортируют свои типы:

```tsx
import type {
  ButtonProps,
  CardProps,
  BlockProps,
  BoxProps
} from '@ui8kit/core'
```

### Универсальные пропы

```tsx
interface UniversalProps extends
  VariantSpacingProps,
  ColorProps,
  RoundedProps,
  ShadowProps,
  BorderProps {}
```

### Темизация

```tsx
import type { ThemeBase } from '@/providers/theme'

interface CustomTheme extends ThemeBase {
  brandColors: {
    primary: string
    secondary: string
  }
}
```

## 🛠️ Расширенные паттерны

### Conditional Types

```tsx
// Тип для полиморфных компонентов
type ComponentProps<T extends ElementType> = {
  component?: T
} & React.ComponentPropsWithoutRef<T>

// Использование
interface ButtonProps<T extends ElementType = 'button'> extends
  ComponentProps<T> {
  variant?: 'primary' | 'secondary'
  loading?: boolean
}
```

### Template Literal Types

```tsx
// Для CSS классов
type SpacingScale = 'xs' | 'sm' | 'md' | 'lg' | 'xl'
type SpacingClass = `p-${SpacingScale}` | `m-${SpacingScale}`

// Результат: "p-xs" | "p-sm" | "p-md" | "p-lg" | "p-xl" | "m-xs" | ...
```

### Utility Types

```tsx
// Обязательные пропы
type RequiredProps<T, K extends keyof T> = T & Required<Pick<T, K>>

// Опциональные пропы
type OptionalProps<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>

// Условные пропы
type ConditionalProps<T, Condition> = Condition extends true
  ? T & { requiredProp: string }
  : T & { optionalProp?: string }
```

## 🔍 Инференция типов

### Auto-completion

```tsx
// Полное автодополнение
<Button
  variant="primary"     // ✅ Автодополнение
  size="lg"            // ✅ Автодополнение
  rounded="md"         // ✅ Автодополнение
  onClick={handleClick} // ✅ Типизированный коллбек
/>

// Ошибки компиляции
<Button
  variant="invalid"    // ❌ Ошибка: не входит в union type
  size="huge"         // ❌ Ошибка: не входит в union type
/>
```

### IntelliSense для тем

```tsx
const theme = useTheme()

// Автодополнение для theme.rounded
<Block rounded={theme.rounded.default} />  // ✅

// Автодополнение для theme.buttonSize
<Button size={theme.buttonSize.icon} />   // ✅
```

## 🧪 Тестирование с TypeScript

### Setup тестов

```tsx
// jest.config.js
export default {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/test-setup.ts'],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1'
  }
}
```

### Typed тесты

```tsx
// components/__tests__/Button.test.tsx
import { render, screen } from '@/test-utils'
import { Button } from '../Button'

describe('Button', () => {
  it('accepts valid props', () => {
    render(
      <Button
        variant="primary"
        size="lg"
        onClick={jest.fn()}
      >
        Test
      </Button>
    )

    expect(screen.getByRole('button')).toBeInTheDocument()
  })

  it('rejects invalid props', () => {
    // @ts-expect-error - invalid variant
    render(<Button variant="invalid">Test</Button>)
  })
})
```

## 🚀 Производительность типов

### Type-checking оптимизации

```json
{
  "skipLibCheck": true,        // Пропустить проверку .d.ts файлов
  "incremental": true,         // Инкрементальная компиляция
  "tsBuildInfoFile": "dist/tsbuildinfo"
}
```

### Selective type checking

```tsx
// types/hot.ts - для быстрой проверки
export type ButtonVariant = 'primary' | 'secondary'
export type ButtonSize = 'sm' | 'md' | 'lg'

// types/cold.ts - для полной проверки
export interface ButtonProps {
  variant: ButtonVariant
  size: ButtonSize
  children: ReactNode
  onClick?: () => void
}
```

## 🐛 Troubleshooting

### Распространенные ошибки

#### 1. Module not found
```
Cannot find module '@ui8kit/core'
```
**Решение:**
- Проверьте установку пакета: `npm install @ui8kit/core`
- Проверьте tsconfig paths

#### 2. Type errors в компонентах
```
Type 'string' is not assignable to type 'RoundedProps'
```
**Решение:**
- Используйте union типы: `rounded: "md" as const`
- Или настройте `strict: false` для конкретных файлов

#### 3. IntelliSense не работает
**Решение:**
- Перезапустите TypeScript language server
- Проверьте, что .d.ts файлы сгенерированы
- Убедитесь в правильности tsconfig.json

### Debug типы

```tsx
// utils/debug.ts
export type DebugType<T> = T extends (...args: any[]) => any
  ? T
  : T extends abstract new (...args: any[]) => any
  ? T
  : {
      [K in keyof T]: T[K]
    }

// Использование
type ButtonDebug = DebugType<ButtonProps>
// Показывает развернутую структуру типа
```

## 📚 Дополнительные ресурсы

### Официальная документация
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)

### Инструменты
- [TypeScript Playground](https://www.typescriptlang.org/play)
- [Type Challenges](https://github.com/type-challenges/type-challenges)
- [Total TypeScript](https://www.totaltypescript.com/)

### Конфигурации
- [Awesome TypeScript](https://github.com/dzharii/awesome-typescript)
- [TypeScript ESLint](https://typescript-eslint.io/)

## 🎯 Лучшие практики

1. **Всегда используйте strict mode**
2. **Настраивайте path mapping** для чистых импортов
3. **Экспортируйте типы** из компонентов
4. **Используйте generic constraints** для гибкости
5. **Документируйте сложные типы** с JSDoc
6. **Регулярно обновляйте** TypeScript до последней версии
7. **Настраивайте IDE** для лучшего автодополнения

При правильной настройке TypeScript станет вашим лучшим союзником в разработке с UI8Kit! 🚀
