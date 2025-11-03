# Core Components API

## Overview

Core Components are the foundational primitives of UI8Kit/Core. They provide basic HTML element wrappers with TypeScript support and prop forwarding.

## Components List

This section documents all core primitive components:

- **Box** - Generic container element
- **Block** - Block-level container
- **Grid** - Grid layout system
- **Stack** - Flexbox stacking container
- **Button** - Button primitive

## Component Documentation

Each core component includes:

1. **Overview** - Purpose and use cases
2. **Props Interface** - TypeScript interface
3. **Props Table** - Detailed prop documentation
4. **forwardRef Support** - Ref typing
5. **HTML Attributes** - Native HTML prop support
6. **Examples** - Practical usage examples

## Box Component

### Overview
Generic container element for flexible layouts.

### Props Interface
```typescript
interface BoxProps extends React.HTMLAttributes<HTMLDivElement> {
  // Inherits all standard HTML div attributes
}
```

### Usage
```typescript
import { Box } from 'ui8kit-core';

<Box>
  Content
</Box>
```

## Block Component

### Overview
Block-level container with semantic meaning.

### Props Interface
```typescript
interface BlockProps extends React.HTMLAttributes<HTMLDivElement> {
  // Inherits all standard HTML div attributes
}
```

### Usage
```typescript
import { Block } from 'ui8kit-core';

<Block>
  Block-level content
</Block>
```

## Grid Component

### Overview
Grid layout system for arranging components.

### Props Interface
```typescript
interface GridProps extends React.HTMLAttributes<HTMLDivElement> {
  cols?: number | string;
  gap?: string;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `cols` | `number \| string` | `1` | Number of columns |
| `gap` | `string` | `0` | Gap between items |
| `...rest` | `HTMLAttributes` | - | All HTML div attributes |

### Usage
```typescript
import { Grid } from 'ui8kit-core';

<Grid cols={3} gap="md">
  <Box>Item 1</Box>
  <Box>Item 2</Box>
  <Box>Item 3</Box>
</Grid>
```

## Stack Component

### Overview
Flexbox container for stacking components.

### Props Interface
```typescript
interface StackProps extends React.HTMLAttributes<HTMLDivElement> {
  direction?: 'row' | 'col';
  gap?: string;
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `'row' \| 'col'` | `'col'` | Stack direction |
| `gap` | `string` | `0` | Gap between items |
| `...rest` | `HTMLAttributes` | - | All HTML div attributes |

### Usage
```typescript
import { Stack } from 'ui8kit-core';

<Stack direction="row" gap="md">
  <Box>Item 1</Box>
  <Box>Item 2</Box>
</Stack>
```

## Button Component

### Overview
Button primitive for user interactions.

### Props Interface
```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  // Inherits all standard HTML button attributes
}
```

### Props Table

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `'button' \| 'submit' \| 'reset'` | `'button'` | Button type |
| `disabled` | `boolean` | `false` | Disable button |
| `onClick` | `(e: React.MouseEvent) => void` | - | Click handler |
| `...rest` | `HTMLAttributes` | - | All HTML button attributes |

### Usage
```typescript
import { Button } from 'ui8kit-core';

<Button type="submit">
  Submit
</Button>
```

## ForwardRef and Refs

All core components support `forwardRef` for direct DOM access:

```typescript
import { useRef } from 'react';
import { Button } from 'ui8kit-core';

function MyComponent() {
  const buttonRef = useRef<HTMLButtonElement>(null);
  
  return (
    <Button 
      ref={buttonRef}
      onClick={() => {
        if (buttonRef.current) {
          console.log('Button clicked!');
        }
      }}
    >
      Click me
    </Button>
  );
}
```

## HTML Attribute Support

All core components accept standard HTML attributes:

```typescript
<Box 
  id="my-box"
  className="custom-class"
  data-test-id="box"
  role="region"
  aria-label="Main content"
>
  Content
</Box>
```

## Display Names

Components have displayName set for debugging:

```typescript
Box.displayName = 'Box';
Block.displayName = 'Block';
Button.displayName = 'Button';
```

## Next Steps

- [UI Components](../ui-components/README.md) - Learn about composite components
- [Variant System](../../03-architecture/variant-system/README.md) - Add styling with variants
- [Architecture](../../03-architecture/core-components/README.md) - Understand core concepts
