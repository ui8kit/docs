# Variant System

## Overview

The Variant System is the styling backbone of UI8Kit/Core, located in `src/core/variants/`. It uses Class Variance Authority (CVA) to centralize and organize Tailwind utility classes into reusable, composable units.

## Why Variants?

In traditional component libraries, styling logic is scattered throughout components, leading to:
- **Duplicated classes** - Same utilities repeated across components
- **Inconsistent design** - Styles drift over time
- **Hard to maintain** - Changes require editing multiple files
- **Difficult to scale** - Adding new components means copying style patterns

**Variants solve this** by centralizing all styling logic in one place.

## Core Principles

### 1. Composability
Variants are built from smaller, reusable units:
```typescript
const spacing = cva('', {
  variants: {
    padding: {
      sm: 'p-2',
      md: 'p-4',
      lg: 'p-6',
    }
  }
});

const colors = cva('', {
  variants: {
    bg: {
      blue: 'bg-blue-600',
      green: 'bg-green-600',
    }
  }
});
```

### 2. Reusability
Variants are shared across all components:
```typescript
// Used in Button, Card, Input, Select, etc.
const buttonClasses = cx(spacing({ padding: 'md' }), colors({ bg: 'blue' }));
```

### 3. Type Safety
Variants are fully typed with TypeScript:
```typescript
// TypeScript catches invalid variant values
<Button padding="lg" />  // ✓ Valid
<Button padding="huge" />  // ✗ TypeScript error
```

## Variant Categories

### Spacing Variants
Control margin and padding:
```typescript
// Properties: margin, padding
// Values: xs, sm, md, lg, xl, 2xl
```

### Color Variants
Manage colors and backgrounds:
```typescript
// Properties: bgColor, textColor
// Values: gray, blue, green, red, etc.
```

### Layout Variants
Handle dimensions and layouts:
```typescript
// Properties: width, height, display
// Values: full, half, 1/3, 1/4, auto, etc.
```

### Effect Variants
Shadow, border, and rounded corners:
```typescript
// Properties: shadow, border, rounded
// Values: none, sm, md, lg, xl
```

### Typography Variants
Font and text styling:
```typescript
// Properties: fontSize, fontWeight, lineHeight
// Values: xs, sm, md, lg, xl, bold, normal, etc.
```

### Flexbox Variants
Flexible layout control:
```typescript
// Properties: flexDirection, justifyContent, alignItems
// Values: row, col, center, between, start, end
```

### Grid Variants
Grid layout control:
```typescript
// Properties: gridCols, gridRows, gridGap
// Values: 1, 2, 3, 4, 6, 12, auto, etc.
```

## CVA Basics

### What is CVA?

Class Variance Authority provides a type-safe way to manage variant combinations:

```typescript
import { cva } from 'class-variance-authority';

const button = cva('px-4 py-2 rounded-md', {
  variants: {
    intent: {
      primary: 'bg-blue-600 text-white',
      secondary: 'bg-gray-200 text-gray-900',
    },
    size: {
      sm: 'text-sm',
      md: 'text-base',
      lg: 'text-lg',
    },
  },
  defaultVariants: {
    intent: 'primary',
    size: 'md',
  },
});
```

### Using CVA Variants

```typescript
button()  // Uses defaults
button({ intent: 'secondary', size: 'lg' })  // Custom values
```

## Variant Composition

Multiple variants compose together without conflicts:

```typescript
const containerClasses = cx(
  spacing({ padding: 'lg' }),      // p-6
  colors({ bgColor: 'white' }),     // bg-white
  effects({ shadow: 'md' }),        // shadow-md
  typography({ fontSize: 'base' })  // text-base
);
```

## Integration with Components

Variants are imported and used in components:

```typescript
import { spacing, colors, layout } from '@core/variants';

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ padding = 'md', bgColor = 'white', ...props }, ref) => {
    const classes = cx(
      spacing({ padding }),
      colors({ bgColor })
    );
    return <div ref={ref} className={classes} {...props} />;
  }
);
```

## Best Practices

### 1. Use Variants, Not ClassName Props
```typescript
// ✓ Good
<Button padding="lg" />

// ✗ Avoid
<Button className="p-4" />
```

### 2. Extend Through Props, Not CSS
```typescript
// ✓ Good
<Button padding="lg" bgColor="blue" />

// ✗ Avoid
<button style={{ padding: '24px', background: 'blue' }} />
```

### 3. Keep Variants Focused
Each variant handles one design concern:
```typescript
// ✓ Good - focused
const spacing = { padding: { ... }, margin: { ... } }

// ✗ Avoid - too broad
const allStyles = { padding: { ... }, margin: { ... }, color: { ... }, ... }
```

## Next Steps

- [Core Components](../core-components/README.md) - See how variants are used
- [UI Components](../ui-components/README.md) - Complex variant composition examples
- [API Reference](../../04-api-reference/README.md) - View all available variants
