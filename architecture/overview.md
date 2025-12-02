# Architecture Overview

UI8Kit is built on modular architecture principles where each layer has a clear responsibility. The library combines the flexibility of utility-first approach with the convenience of ready-made components.

## 🏗️ Architectural Principles

### 1. **Utility-First with Semantics**
- All visual properties available as component props
- Semantic prop names (`bg`, `c`, `p`, `m`)
- Consistent value system throughout the library

### 2. **Polymorphic Components**
- Components can render as any HTML element via `component` prop
- Full typing for all possible elements
- Flexibility in semantic markup

### 3. **Variants System (CVA)**
- Class Variance Authority for type-safe variants
- Variant composition without conflicts
- Automatic class merging through `tailwind-merge`

### 4. **TypeScript-First**
- Full typing of all props
- IDE autocompletion
- Strict type safety

## 📦 Package Structure

```
packages/@ui8kit/
├── core/                    # Main library
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── ui/          # Base UI components
│   │   │   └── *.tsx        # Composite components
│   │   ├── variants/        # Variants system (CVA)
│   │   ├── lib/             # Utilities
│   │   └── index.ts         # Main export
│   ├── package.json
│   └── tsconfig.json
├── docs/                    # Documentation
└── create-app/              # CLI tool
```

## 🔧 Key Technologies

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

### Polymorphic Components
```tsx
interface BlockProps extends React.HTMLAttributes<HTMLElement> {
  component?: ElementType
}

// Usage
<Block component="section" py="lg">Content</Block>
<Block component="form" onSubmit={handleSubmit}>Form</Block>
```

### Tailwind Merge
```tsx
import { twMerge } from 'tailwind-merge'

// Automatic class conflict resolution
twMerge('px-2 py-1', 'px-4') // → 'py-1 px-4'
```

## 🧩 Architecture Layers

### 1. **Variants Layer** (variants/)
Defines all possible visual variants:

- **spacing.ts** - margin, padding, gaps
- **colors.ts** - background, text, border colors
- **layout.ts** - width, height, position, display
- **typography.ts** - font size, weight, alignment
- **button.ts** - button-specific variants

### 2. **Primitives Layer** (core/ui/)
Base components without styles:

```tsx
// Just forwardRef without classes
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ children, ...props }, ref) => (
    <button ref={ref} {...props}>
      {children}
    </button>
  )
)
```

### 3. **Components Layer** (components/ui/)
Applies variants to primitives:

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
Composite components from base ones:

```tsx
export function Card({ children, ...props }: CardProps) {
  return (
    <Block bg="card" rounded="lg" shadow="md" {...props}>
      {children}
    </Block>
  )
}
```

## 🎨 Theme System

### Simple theme structure
```tsx
interface Theme {
  name: string
  rounded: Record<string, any> & { default: any }
  buttonSize: Record<string, any> & { default: any }
  isNavFixed?: boolean
}
```

### CSS Variables
The library uses CSS variables for colors:
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

## 📊 Performance Principles

1. **Tree Shaking** - Only used components end up in the bundle
2. **Runtime-free CSS-in-JS** - All styles compiled to CSS
3. **Minimal re-renders** - Stable references through useMemo
4. **Small bundle size** - Dependencies: clsx, tailwind-merge, cva

## 🚀 Library Extension

### Adding a new variant
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

### Creating a new component
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
