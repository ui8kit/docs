# Package Structure

UI8Kit is organized into a modular package structure where each package has a clear responsibility. This ensures ease of maintenance, testing, and extension.

## 📦 General Structure

```
packages/@ui8kit/
├── core/                    # Main component library
│   ├── src/
│   │   ├── components/      # React componentы
│   │   │   ├── ui/          # Basic UI componentы
│   │   │   └── *.tsx        # Композитные componentы
│   │   ├── variants/        # Система variantов
│   │   ├── lib/             # Утилиты и хелперы
│   │   └── index.ts         # Главная точка входа
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── docs/                    # Документация
├── create-app/              # CLI инструмент для создания приложений
└── workspace/               # Корневой пакет с общими скриптами
```

## 🔍 Detailed Core Package Structure

### components/

```
components/
├── ui/                      # Basic UI components
│   ├── Block.tsx           # Polymorphic semantic container
│   ├── Box.tsx             # Flexible primitive with full variant support
│   ├── Button.tsx          # Interactive button
│   ├── Badge.tsx           # Status indicators
│   ├── Card.tsx            # Card with compound structure
│   ├── Container.tsx       # Responsive container
│   ├── Group.tsx           # Horizontal stack
│   ├── Stack.tsx           # Vertical stack
│   ├── Grid.tsx            # CSS Grid component
│   ├── Title.tsx           # Semantic headings
│   ├── Text.tsx            # Text elements
│   ├── Image.tsx           # Enhanced image
│   └── Icon.tsx            # Icon wrapper
├── Grid.tsx                # Composite Grid (uses ui/Grid)
├── Sheet.tsx               # Modal overlay
├── Accordion.tsx           # Expandable content
└── index.ts                # Exports all components
```

#### Component Classification

**ui/** - Basic components:
- Apply variants to primitives
- Have minimal API
- Focus on one aspect of UI

**Root components/** - Composite components:
- Combine multiple ui components
- Have complex logic
- Provide high-level API

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
└── index.ts                # Export all variants
```

### lib/

```
lib/
├── utils.ts                # Core utilities (cn, etc.)
└── ...
```

## 📋 Component File Structure

### Example UI Component (Button.tsx)

```tsx
// 1. Imports
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

// 2. Props interface
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    // Inherited props
    Pick<VariantSpacingProps, 'm' | 'mx' | 'my' | 'mr'>,
    RoundedProps,
    ShadowProps,
    // Own props
    ButtonSizeProps,
    ButtonStyleProps {
  children: ReactNode
  leftSection?: ReactNode
  rightSection?: ReactNode
  loading?: boolean
}

// 3. Helper components
const ButtonSpinner = () => (
  <span className="mr-2 h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
)

// 4. Main component
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

### Example Composite Component (Card.tsx)

```tsx
// components/ui/Card.tsx
import { forwardRef } from "react"
import { cn } from "../../lib/utils"
import { Block } from "./Block"
import {
  cardVariants,
  type CardProps
} from "../../variants"

// Compound parts
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

// Main component
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

// Export compound parts
export { CardHeader, CardTitle, CardContent, CardFooter, CardDescription }
```

## 🔧 Build system

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

## 📊 Organization Principles

### 1. **Single Responsibility**
Each file/folder has one clear purpose.

### 2. **Hierarchical Export**
```
index.ts → components → ui components → variants
```

### 3. **Type Safety**
All exports are typed, including internal utilities.

### 4. **Tree Shaking**
Unused code is automatically excluded from bundle.

### 5. **Semantic Versioning**
- PATCH: bug fixes
- MINOR: new features (backward compatible)
- MAJOR: breaking changes
