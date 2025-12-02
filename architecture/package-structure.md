# Package Structure

UI8Kit организован в модульную структуру пакетов, где каждый пакет имеет четкую ответственность. Это обеспечивает легкость поддержки, тестирования и расширения.

## 📦 Общая структура

```
packages/@ui8kit/
├── core/                    # Основная библиотека компонентов
│   ├── src/
│   │   ├── components/      # React компоненты
│   │   │   ├── ui/          # Базовые UI компоненты
│   │   │   └── *.tsx        # Композитные компоненты
│   │   ├── variants/        # Система вариантов
│   │   ├── lib/             # Утилиты и хелперы
│   │   └── index.ts         # Главная точка входа
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── docs/                    # Документация
├── create-app/              # CLI инструмент для создания приложений
└── workspace/               # Корневой пакет с общими скриптами
```

## 🔍 Детальная структура core пакета

### components/

```
components/
├── ui/                      # Базовые UI компоненты
│   ├── Block.tsx           # Полиморфный семантический контейнер
│   ├── Box.tsx             # Гибкий примитив с полным набором вариантов
│   ├── Button.tsx          # Интерактивная кнопка
│   ├── Badge.tsx           # Статус индикаторы
│   ├── Card.tsx            # Карточка с составной структурой
│   ├── Container.tsx       # Адаптивный контейнер
│   ├── Group.tsx           # Горизонтальный стек
│   ├── Stack.tsx           # Вертикальный стек
│   ├── Grid.tsx            # CSS Grid компонент
│   ├── Title.tsx           # Семантические заголовки
│   ├── Text.tsx            # Текстовые элементы
│   ├── Image.tsx           # Улучшенное изображение
│   └── Icon.tsx            # Обертка иконок
├── Grid.tsx                # Композитный Grid (использует ui/Grid)
├── Sheet.tsx               # Модальный оверлей
├── Accordion.tsx           # Раскрывающийся контент
└── index.ts                # Экспорт всех компонентов
```

#### Классификация компонентов

**ui/** - Базовые компоненты:
- Применяют варианты к примитивам
- Имеют минимальный API
- Фокусируются на одном аспекте UI

**Корень components/** - Композитные компоненты:
- Комбинируют несколько ui компонентов
- Имеют сложную логику
- Предоставляют high-level API

### variants/

```
variants/
├── spacing.ts              # Margin, padding, gaps
├── colors.ts               # Background, text, border colors
├── layout.ts               # Width, height, position, display
├── rounded.ts              # Border radius
├── shadow.ts               # Box shadows
├── border.ts               # Border width, style
├── sizing.ts               # Size utilities
├── flex.ts                 # Flexbox utilities
├── button.ts               # Button-specific variants
├── badge.ts                # Badge variants
├── typography.ts           # Font size, weight, alignment
├── image.ts                # Image utilities
└── index.ts                # Экспорт всех вариантов
```

### lib/

```
lib/
├── utils.ts                # Основные утилиты (cn, etc.)
└── ...
```

## 📋 Файловая структура компонента

### Пример ui компонента (Button.tsx)

```tsx
// 1. Импорты
import type { ReactNode } from "react"
import { forwardRef } from "react"
import { cn } from "../../lib/utils"
import {
  buttonSizeVariants,
  buttonStyleVariants,
  spacingVariants,
  roundedVariants,
  shadowVariants,
  type ButtonSizeProps,
  type ButtonStyleProps,
  type VariantSpacingProps,
  type RoundedProps,
  type ShadowProps
} from "../../variants"

// 2. Интерфейс пропов
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    // Унаследованные пропы
    Pick<VariantSpacingProps, 'm' | 'mx' | 'my' | 'mr'>,
    RoundedProps,
    ShadowProps,
    // Собственные пропы
    ButtonSizeProps,
    ButtonStyleProps {
  children: ReactNode
  leftSection?: ReactNode
  rightSection?: ReactNode
  loading?: boolean
}

// 3. Вспомогательные компоненты
const ButtonSpinner = () => (
  <span className="mr-2 h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
)

// 4. Основной компонент
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({
    children,
    className,
    variant = 'default',
    size = 'default',
    rounded = 'lg',
    shadow,
    loading = false,
    disabled = false,
    m, mx, my, mr,
    leftSection,
    rightSection,
    ...props
  }, ref) => {
    return (
      <button
        ref={ref}
        data-class="button"
        disabled={disabled || loading}
        className={cn(
          // Base styles
          'inline-flex items-center justify-center gap-2',
          'whitespace-nowrap text-sm font-medium',
          'transition-colors disabled:pointer-events-none disabled:opacity-50',
          '[&_svg]:pointer-events-none [&_svg]:shrink-0 shrink-0',
          'outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',

          // Variants
          buttonSizeVariants({ size }),
          buttonStyleVariants({ variant }),
          roundedVariants({ rounded }),
          shadowVariants({ shadow }),
          spacingVariants({ m, mx, my, mr }),
          className
        )}
        {...props}
      >
        {loading && <ButtonSpinner />}
        {!loading && leftSection && (
          <span data-class="button-left-section" className="mr-2">{leftSection}</span>
        )}
        {children}
        {!loading && rightSection && (
          <span data-class="button-right-section" className="ml-2">{rightSection}</span>
        )}
      </button>
    )
  }
)

Button.displayName = "Button"
```

### Пример композитного компонента (Card.tsx)

```tsx
// components/ui/Card.tsx
import { forwardRef } from "react"
import { cn } from "../../lib/utils"
import { Block } from "./Block"
import {
  cardVariants,
  type CardProps
} from "../../variants"

// Составные части
export const CardHeader = forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <Block
      ref={ref}
      data-class="card-header"
      className={cn("flex flex-col space-y-1.5 p-6", className)}
      {...props}
    />
  )
)
CardHeader.displayName = "CardHeader"

export const CardTitle = forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <Block
      ref={ref}
      component="h3"
      data-class="card-title"
      className={cn("text-2xl font-semibold leading-none tracking-tight", className)}
      {...props}
    />
  )
)
CardTitle.displayName = "CardTitle"

// Основной компонент
export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ className, ...props }, ref) => (
    <Block
      ref={ref}
      data-class="card"
      bg="card"
      c="card-foreground"
      rounded="lg"
      border="default"
      shadow="sm"
      className={className}
      {...props}
    />
  )
)
Card.displayName = "Card"

// Экспорт составных частей
export { CardHeader, CardTitle, CardContent, CardFooter, CardDescription }
```

## 🔧 Build система

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
    "noFallthroughCasesInSwitch": true,
    "declaration": true,
    "declarationMap": true,
    "outDir": "dist"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Package.json

```json
{
  "name": "@ui8kit/core",
  "version": "0.1.8",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  },
  "files": ["dist/**/*", "README.md", "LICENSE"],
  "scripts": {
    "build": "tsc -p tsconfig.json",
    "type-check": "tsc --noEmit"
  }
}
```

## 📊 Принципы организации

### 1. **Единая ответственность**
Каждый файл/папка имеет одну четкую цель.

### 2. **Иерархический экспорт**
```
index.ts → компоненты → ui компоненты → варианты
```

### 3. **Типобезопасность**
Все экспорты типизированы, включая внутренние утилиты.

### 4. **Tree Shaking**
Неиспользуемый код автоматически исключается из бандла.

### 5. **Семантическое версионирование**
- PATCH: баг фиксы
- MINOR: новые фичи (backward compatible)
- MAJOR: breaking changes
