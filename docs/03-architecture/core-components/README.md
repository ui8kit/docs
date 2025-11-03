# Core Components

## Overview

Core Components are the foundational primitives of UI8Kit/Core, located in `src/core/ui/`. They represent the "atoms" in atomic design, providing basic building blocks with essential styling and TypeScript support.

## Key Characteristics

- **Minimal functionality** - Focus on single responsibilities
- **forwardRef support** - Full ref forwarding for DOM access
- **HTML attributes** - Native HTML prop support
- **TypeScript types** - Full type safety
- **No variant props** - Keep primitives lean

## Fundamental Concepts

### Props and Interfaces

Core components accept standard React props plus HTML attributes:

```typescript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  // Component-specific props
}
```

### ForwardRef Implementation

All core components implement `forwardRef` for direct DOM access:

```typescript
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (props, ref) => {
    return <button ref={ref} {...props} />;
  }
);
```

### Element Naming

Components are named after their primary HTML element:
- `<Button>` renders `<button>`
- `<Box>` renders `<div>` with semantic styling
- `<Grid>` renders `<div>` with grid layout

### Display Configurations

Components handle various display scenarios:
- Block-level vs. inline elements
- Flexbox vs. grid layouts
- Semantic HTML tags

## Common Patterns

### HTML Attribute Forwarding

All HTML attributes are forwarded to the underlying element:

```typescript
<Button 
  type="submit" 
  disabled 
  aria-label="Submit form"
>
  Submit
</Button>
```

### Styling Approach

Core components use Tailwind utility classes directly:

```typescript
className="px-4 py-2 bg-blue-600 text-white rounded-md"
```

## Next Steps

- [Variant System](../variant-system/README.md) - Learn how to extend with styling variants
- [UI Components](../ui-components/README.md) - See how core components are composed
- [API Reference - Core Components](../../04-api-reference/core-components/README.md) - Complete component documentation
