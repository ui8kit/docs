# UI Components

## Overview

UI Components are composite components built from core primitives, located in `src/components/ui/`. They represent the "molecules" in atomic design, adding higher-level functionality while maintaining type safety and prop forwarding.

## Key Characteristics

- **Composite structure** - Built from core components
- **Variant integration** - Import and use variant props
- **Prop forwarding API** - Extend with additional variant props
- **Data-class attributes** - Consistent DOM identification
- **Compound pattern** - Components like Card with subcomponents

## Core Principles

### 1. Composition Over Duplication
UI Components compose core components rather than duplicating code:

```typescript
import { Box, Block } from '@core/ui';
import { spacing, colors } from '@core/variants';

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ padding = 'md', bgColor = 'white', ...props }, ref) => {
    const classes = cx(
      spacing({ padding }),
      colors({ bgColor })
    );
    return <Box ref={ref} className={classes} {...props} />;
  }
);
```

### 2. Prop Forwarding API
UI Components accept variant props from the core system:

```typescript
<Button 
  variant="primary"    // Component prop
  padding="lg"         // Variant prop from spacing
  bgColor="blue"       // Variant prop from colors
  rounded="md"         // Variant prop from effects
>
  Click me
</Button>
```

### 3. Compound Components
Complex components use the compound pattern for flexible composition:

```typescript
<Card>
  <Card.Header data-class="card-header">
    Header Content
  </Card.Header>
  <Card.Content data-class="card-content">
    Main Content
  </Card.Content>
  <Card.Footer data-class="card-footer">
    Footer Content
  </Card.Footer>
</Card>
```

### 4. Data-Class Identification
All UI Components include `data-class` attributes for DOM targeting:

```typescript
// Components render with data-class for identification
<div data-class="card">
  <div data-class="card-header">...</div>
  <div data-class="card-content">...</div>
  <div data-class="card-footer">...</div>
</div>
```

## TypeScript Integration

### Props Interfaces
UI Components have comprehensive TypeScript interfaces:

```typescript
interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  padding?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  bgColor?: 'white' | 'gray' | 'blue';
  shadow?: 'none' | 'sm' | 'md' | 'lg';
}
```

### Ref Forwarding
All UI Components properly forward refs:

```typescript
const cardRef = useRef<HTMLDivElement>(null);
<Card ref={cardRef} />  // Full type safety
```

## Common Patterns

### Pattern 1: Basic Props Extension
```typescript
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ size = 'md', variant = 'primary', ...props }, ref) => {
    const classes = cx(
      'inline-flex items-center justify-center',
      sizes[size],
      variants[variant]
    );
    return <button ref={ref} className={classes} {...props} />;
  }
);
```

### Pattern 2: Compound Components
```typescript
export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ ...props }, ref) => (
    <div ref={ref} data-class="card" {...props} />
  )
);

Card.Header = forwardRef<HTMLDivElement, CardHeaderProps>(
  (props, ref) => <div ref={ref} data-class="card-header" {...props} />
);

Card.Content = forwardRef<HTMLDivElement, CardContentProps>(
  (props, ref) => <div ref={ref} data-class="card-content" {...props} />
);
```

### Pattern 3: Controlled Components
```typescript
export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ value, onChange, ...props }, ref) => {
    return (
      <input 
        ref={ref} 
        value={value} 
        onChange={onChange}
        data-class="input"
        {...props} 
      />
    );
  }
);
```

## Variant Integration

UI Components import and use variants from the core system:

```typescript
import { spacing, colors, effects, layout } from '@core/variants';

const cardClasses = cx(
  spacing({ padding: props.padding }),      // From spacing variant
  colors({ bgColor: props.bgColor }),       // From colors variant
  effects({ shadow: props.shadow }),        // From effects variant
  layout({ width: 'full' })                 // From layout variant
);
```

## Best Practices

### 1. Keep Interfaces Simple
```typescript
// ✓ Good - focused interface
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
}

// ✗ Avoid - too many custom props
interface ButtonProps {
  variant, size, color, shadow, padding, margin, ...
}
```

### 2. Use Data-Class Consistently
```typescript
// ✓ Good
<div data-class="card-header">...</div>

// ✗ Avoid inconsistent naming
<div data-class="cardHeader">...</div>
<div data-class="card_header">...</div>
```

### 3. Leverage Compound Components
```typescript
// ✓ Good - explicit structure
<Card>
  <Card.Header />
  <Card.Content />
  <Card.Footer />
</Card>

// ✗ Avoid - generic children
<Card header={...} content={...} footer={...} />
```

## Next Steps

- [Variant System](../variant-system/README.md) - Understand how variants work
- [Layouts](../layouts/README.md) - See how UI components are used in layouts
- [API Reference - UI Components](../../04-api-reference/ui-components/README.md) - Complete component documentation
