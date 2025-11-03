# API Reference

## Overview

Complete API documentation for all UI8Kit/Core components, organized by architectural layer.

## Three Sections

### 1. Core Components API
Basic primitives and foundational components with minimal functionality.

[View Core Components API →](./core-components/README.md)

Components:
- Box
- Block
- Grid
- Stack
- Button
- And more...

### 2. UI Components API
Composite components built from core primitives with extended functionality.

[View UI Components API →](./ui-components/README.md)

Components:
- Card (with Header, Content, Footer)
- Button (enhanced)
- Input
- Select
- Modal
- Alert
- And more...

### 3. Layout Components API
Complex page layout systems for common scenarios.

[View Layout Components API →](./layout-components/README.md)

Components:
- DashLayout
- SplitBlock
- LayoutBlock
- Grid (advanced)
- Flex
- And more...

## Component Documentation Format

Each component is documented with:

### Overview
Brief description and use cases

### Props Interface
Complete TypeScript interface with all properties:

```typescript
interface ComponentProps extends React.HTMLAttributes<HTMLElement> {
  // Custom props
}
```

### Props Table
Detailed table of all props with types and defaults

### Variants
Available variant props from the core variant system

### Type Safety
TypeScript type information and ref types

### Usage Examples
Practical code examples demonstrating typical usage

### Best Practices
Recommendations for optimal usage

## Navigation

- [Core Components](./core-components/README.md) - Basic building blocks
- [UI Components](./ui-components/README.md) - Ready-made components
- [Layout Components](./layout-components/README.md) - Page layouts

## TypeScript Support

All components are fully typed:

```typescript
import { Button, Card } from 'ui8kit-core';

const ref = useRef<HTMLButtonElement>(null);

<Button 
  ref={ref}
  variant="primary"
  size="lg"
>
  Click me
</Button>
```

## Variants

Components use variants from the core system:

```typescript
import { Button } from 'ui8kit-core';

<Button
  padding="lg"           // Spacing variant
  bgColor="blue"         // Color variant
  shadow="md"            // Effect variant
  rounded="md"           // Effect variant
>
  Customized Button
</Button>
```

## Data-Class Attributes

All components include `data-class` attributes:

```typescript
<Button data-class="button-primary" />
// Renders: <button data-class="button-primary" />
```

Use for:
- DOM testing and targeting
- Component identification
- Analytics tracking
- Debug inspection

## Integration

### NPM Import
```typescript
import { Button, Card } from 'ui8kit-core';
```

### Per-Component Import
```typescript
import { Button } from 'ui8kit-core/button';
import { Card } from 'ui8kit-core/card';
```

### Direct Source
```typescript
import { Button } from 'ui8kit-core/src/components/ui/button';
```

## TypeScript Version

Requires TypeScript 4.5 or higher for full type support.

## Next Steps

- [Core Components](./core-components/README.md) - Learn the primitives
- [UI Components](./ui-components/README.md) - Explore ready-made components
- [Layout Components](./layout-components/README.md) - Build page layouts
