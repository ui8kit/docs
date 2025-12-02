# Variant System

UI8Kit's variant system is the heart of the library. It ensures style consistency, type safety, and flexibility throughout the entire codebase.

## 🎯 What are variants?

Variants are predefined sets of CSS classes organized by categories. They allow you to apply styles through component props instead of manually writing classes.

```tsx
// Instead of this:
<div className="p-4 bg-primary text-primary-foreground rounded-md">

// Use this:
<Block p="md" bg="primary" c="primary-foreground" rounded="md" />
```

## 🏗️ Variant Architecture

### Class Variance Authority (CVA)

UI8Kit uses [CVA](https://cva.style/) to create type-safe variants:

```tsx
import { cva } from 'class-variance-authority'

export const buttonVariants = cva(
  "inline-flex items-center justify-center", // base styles
  {
    variants: {
      variant: {
        primary: "bg-primary text-primary-foreground hover:bg-primary/90",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80"
      },
      size: {
        sm: "h-9 px-3 text-sm",
        lg: "h-11 px-8 text-base"
      }
    },
    defaultVariants: {
      variant: "primary",
      size: "sm"
    }
  }
)
```

### Variant Types

```tsx
// Automatically generated types
type ButtonVariants = VariantProps<typeof buttonVariants>
// = {
//   variant?: "primary" | "secondary"
//   size?: "sm" | "lg"
// }
```

## 📂 Variant Structure

### Basic Categories

#### 1. Spacing (`spacing.ts`)
```tsx
export const spacingVariants = cva("", {
  variants: {
    // Margin
    m: { xs: "m-1", sm: "m-2", md: "m-4", lg: "m-6", xl: "m-8", "2xl": "m-12", auto: "m-auto" },
    mx: { /* similar */ },
    my: { /* similar */ },
    mt: { /* similar */ },
    mb: { /* similar */ },
    ml: { /* similar */ },
    mr: { /* similar */ },

    // Padding
    p: { none: "p-0", xs: "p-1", sm: "p-2", md: "p-4", lg: "p-6", xl: "p-8", "2xl": "p-12" },
    px: { /* similar */ },
    py: { /* similar */ },
    pt: { /* similar */ },
    pb: { /* similar */ },
    pl: { /* similar */ },
    pr: { /* similar */ },

    // Space between children
    spaceX: { none: "space-x-0", xs: "space-x-1", sm: "space-x-2", md: "space-x-4" },
    spaceY: { none: "space-y-0", xs: "space-y-1", sm: "space-y-2", md: "space-y-4" }
  }
})
```

#### 2. Colors (`colors.ts`)
```tsx
export const colorVariants = cva("", {
  variants: {
    // Background
    bg: {
      transparent: "bg-transparent",
      primary: "bg-primary",
      secondary: "bg-secondary",
      // ... all semantic colors
    },

    // Text color
    c: {
      foreground: "text-foreground",
      primary: "text-primary",
      muted: "text-muted-foreground",
      // ...
    },

    // Border color
    borderColor: {
      border: "border-border",
      primary: "border-primary",
      // ...
    }
  }
})
```

#### 3. Layout (`layout.ts`)
```tsx
export const layoutVariants = cva("", {
  variants: {
    // Dimensions
    w: { auto: "w-auto", full: "w-full", screen: "w-screen", fit: "w-fit" },
    h: { auto: "h-auto", full: "h-full", screen: "h-screen", fit: "h-fit" },
    minH: { none: "min-h-0", full: "min-h-full", screen: "min-h-screen" },

    // Position
    position: { static: "static", relative: "relative", absolute: "absolute", fixed: "fixed" },

    // Display
    display: { block: "block", inline: "inline", flex: "flex", grid: "grid", none: "none" },

    // Overflow
    overflow: { auto: "overflow-auto", hidden: "overflow-hidden", visible: "overflow-visible" }
  }
})
```

#### 4. Visual (`rounded.ts`, `shadow.ts`, `border.ts`)
```tsx
// rounded.ts
export const roundedVariants = cva("", {
  variants: {
    rounded: {
      none: "rounded-none",
      sm: "rounded-sm",
      md: "rounded-md",
      lg: "rounded-lg",
      xl: "rounded-xl",
      "2xl": "rounded-2xl",
      "3xl": "rounded-3xl",
      full: "rounded-full"
    }
  }
})

// shadow.ts
export const shadowVariants = cva("", {
  variants: {
    shadow: {
      none: "shadow-none",
      sm: "shadow-sm",
      md: "shadow-md",
      lg: "shadow-lg",
      xl: "shadow-xl"
    }
  }
})
```

### Component-specific variants

#### Button (`button.ts`)
```tsx
export const buttonStyleVariants = cva("", {
  variants: {
    variant: {
      default: "bg-primary text-primary-foreground hover:bg-primary/90",
      destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
      outline: "border border-input bg-background hover:bg-accent",
      secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
      ghost: "hover:bg-accent hover:text-accent-foreground",
      link: "text-primary underline-offset-4 hover:underline"
    }
  },
  defaultVariants: {
    variant: "default"
  }
})

export const buttonSizeVariants = cva("", {
  variants: {
    size: {
      xs: "h-6 px-2 text-xs",
      sm: "h-9 px-3 text-sm",
      default: "h-10 px-4 py-2",
      lg: "h-11 px-8",
      xl: "h-12 px-10 text-base",
      icon: "h-10 w-10"
    }
  },
  defaultVariants: {
    size: "default"
  }
})
```

## 🔧 How to use variants

### In components

```tsx
import { buttonVariants, spacingVariants } from '../variants'

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant, size, p, className, ...props }, ref) => (
    <button
      ref={ref}
      className={cn(
        buttonVariants({ variant, size }),
        spacingVariants({ p }),
        className
      )}
      {...props}
    />
  )
)
```

### Variant composition

```tsx
// Combine multiple variants
const combinedClasses = cn(
  buttonVariants({ variant: "primary", size: "lg" }),
  spacingVariants({ p: "md", m: "sm" }),
  colorVariants({ bg: "primary" })
)
// Result: "bg-primary text-primary-foreground hover:bg-primary/90 h-11 px-8 p-4 m-2 bg-primary"
```

### Tailwind Merge

UI8Kit uses `tailwind-merge` to resolve conflicts:

```tsx
import { twMerge } from 'tailwind-merge'

twMerge('px-2 py-1 bg-red-500', 'px-4 bg-blue-500')
// → 'py-1 px-4 bg-blue-500'
```

## 🎨 Variant theming

Variants can be themed via CSS variables or a JavaScript theme.

### CSS variables
```css
:root {
  --primary: 221.2 83.2% 53.3%;
  --background: 0 0% 100%;
}

.dark {
  --primary: 217.2 91.2% 59.8%;
  --background: 222.2 84% 4.9%;
}
```

### JavaScript theme
```tsx
const theme = {
  rounded: { default: "lg", button: "xl" },
  buttonSize: { default: "md" }
}

// Application in component
const rounded = theme.rounded[variant] || theme.rounded.default
```

## 🚀 Creating new variants

### 1. Create a variant file
```tsx
// variants/newFeature.ts
import { cva, type VariantProps } from "class-variance-authority"

export const newFeatureVariants = cva("", {
  variants: {
    variant: {
      primary: "bg-primary text-primary-foreground",
      secondary: "bg-secondary text-secondary-foreground"
    },
    size: {
      sm: "text-sm",
      lg: "text-lg"
    }
  },
  defaultVariants: {
    variant: "primary",
    size: "sm"
  }
})

export type NewFeatureProps = VariantProps<typeof newFeatureVariants>
```

### 2. Export in index.ts
```tsx
// variants/index.ts
export * from './newFeature'
```

### 3. Use in component
```tsx
// components/ui/NewComponent.tsx
import { newFeatureVariants, type NewFeatureProps } from '../../variants'

interface ComponentProps extends NewFeatureProps {
  // other props
}

export const NewComponent = forwardRef<Element, ComponentProps>(
  ({ variant, size, className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(newFeatureVariants({ variant, size }), className)}
      {...props}
    />
  )
)
```

## 📊 Performance

- **Zero runtime** - All variants are compiled into CSS
- **Tree shaking** - Unused variants are excluded
- **Class merging** - Conflicts are resolved automatically
- **Type safety** - Full typing without runtime checks
