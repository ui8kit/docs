# Architecture

## Overview

UI8Kit/Core follows a three-layered architecture that mirrors atomic design principles. Each layer builds upon the previous one, creating a scalable and maintainable component system.

## The Three Layers

### Layer 1: Core Components (Atoms)
Located in `src/core/ui/`, these are the foundational primitives:
- **Box** - Basic container for layout
- **Block** - Block-level layout component
- **Grid** - Grid layout system
- **Stack** - Flexbox-based stacking
- **Button** - Base button primitive

These components provide basic styling, prop forwarding, and TypeScript support.

[Learn more about Core Components →](./core-components/README.md)

### Layer 2: UI Components (Molecules)
Located in `src/components/ui/`, these are composite components built from core components:
- **Card** - Complex container with header, content, footer
- **Input** - Enhanced input with variants
- **Select** - Dropdown selection component
- **Modal** - Dialog/modal component
- **Alert** - Notification component

These components add higher-level functionality and include the prop forwarding API.

[Learn more about UI Components →](./ui-components/README.md)

### Layer 3: Layouts (Organisms)
Located in `src/layouts/`, these are complex page layout systems:
- **DashLayout** - Dashboard layout with sidebar
- **SplitBlock** - Split/two-column layout
- **LayoutBlock** - Flexible layout container
- **Grid** - Advanced grid layout
- **Flex** - Flexible layout components

These components compose multiple layers to create complete page layouts.

[Learn more about Layouts →](./layouts/README.md)

## Key Architectural Concepts

### CVA-Based Variant System
The variant system is centralized in `src/core/variants/` using Class Variance Authority (CVA). This provides:
- Composable, reusable styling units
- Reduced class duplication
- Type-safe variant props
- Consistent design across components

[Deep dive into Variant System →](./variant-system/README.md)

### Prop Forwarding API
Components support extending base components with additional variant props:
```typescript
<Button 
  variant="primary"           // Core prop
  padding="lg"                // Variant prop
  bgColor="blue"              // Variant prop
>
  Click me
</Button>
```

This pattern enables unlimited customization within the design system.

[Learn about UI Components →](./ui-components/README.md)

### Data-Class Attributes
All components use `data-class` attributes for identification:
```html
<div data-class="card-header">Content</div>
<div data-class="button-primary">Button</div>
```

This enables easy DOM targeting, testing, and component tracking.

## Directory Structure

```
src/
├── core/
│   ├── ui/              # Core primitives
│   ├── variants/        # CVA variant system
│   └── types/           # Shared TypeScript types
├── components/
│   ├── ui/              # Composite UI components
│   ├── README.md        # Usage examples
│   └── GUIDE_CREATE_FORM.md  # Custom form guide
├── layouts/             # Layout components
├── themes/
│   └── providers/       # Theme management
└── styles/              # Global styles
```

## Package Configuration

The library supports multiple distribution formats through `package.json` configuration:
- Main entry point for CommonJS
- ES module exports
- TypeScript definitions
- Per-component exports

[Learn about Package Structure →](./package-structure/README.md)

## Build System

The library uses TypeScript for compilation and supports:
- Automated builds for distribution
- Type definition generation
- Multiple output formats

[Learn about Build System →](./build-system/README.md)

## Component Registry

A `registry.json` file provides component metadata for tooling support:
- Component descriptions
- Available props
- Usage examples
- Installation information

[Learn about Component Registry →](./component-registry/README.md)

## TypeScript Configuration

Full TypeScript support includes:
- Strict type checking
- Path aliases for imports
- Generated type definitions
- Comprehensive type safety

[Learn about TypeScript Configuration →](./typescript-configuration/README.md)

## Design Philosophy

**Minimalism First**: The architecture is designed around a principle of minimal components for maximum flexibility. Just 15 composite components and 12 reusable variants cover approximately 80% of typical design scenarios.

This means:
- Learning curve is reduced
- Maintenance is simplified
- Customization remains unlimited
- Performance is optimized

## Next Steps

- [Core Components](./core-components/README.md) - Start with the primitives
- [Variant System](./variant-system/README.md) - Understand styling approach
- [UI Components](./ui-components/README.md) - Explore composite components
