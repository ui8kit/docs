# UI8Kit Overview

**UI8Kit** is a modern React UI library built on utility-first design principles with semantic classes. The library combines the flexibility of Tailwind CSS with the convenience of ready-made components.

## 🎯 Key Features

- **TypeScript-first**: Full type safety with autocompletion
- **Utility-first**: All visual properties available as props
- **Polymorphic components**: One component can render as any HTML element
- **Variant system**: Consistent styling system through CVA
- **Minimalist API**: Clean, predictable interfaces

## 🏗️ Architecture

```
USER LEVEL               COMPOSITE LEVEL           PRIMITIVE LEVEL
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ <Button         │────▶│ components/ui/Button │────▶│ core/ui/Button    │
│   variant="primary"│     │ + buttonVariants   │     │ (no styles)     │
│   size="lg"     │     │ + spacingVariants │     │                 │
│   rounded="md"  │     │ = Beautiful API  │     │                 │
│ />              │     │                  │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## 📦 What's Included

### Basic Primitives
- **Block** - Semantic container with full style control
- **Box** - Flexible primitive with support for all variants

### Layout Components
- **Container** - Responsive container with preset sizes
- **Stack** - Vertical stack with gap control
- **Group** - Horizontal stack with alignment
- **Grid** - CSS Grid with responsive presets

### UI Components
- **Button** - Interactive button with variants and states
- **Badge** - Small status indicators
- **Title** - Semantic headings with typography
- **Text** - Text elements with full control
- **Image** - Enhanced image component
- **Icon** - Icon wrapper with size and color control
- **Card** - Card with compound structure

### Composite Components
- **Sheet** - Modal overlay with animations
- **Accordion** - Expandable content

## 🎨 Styling System

### Universal Props
All components support universal visual props:

```tsx
<Block
  p="lg"           // padding
  m="md"           // margin
  bg="primary"     // background
  c="foreground"   // text color
  rounded="md"     // border radius
  shadow="lg"      // box shadow
  border="default" // border width
/>
```

### Color System
The library uses a semantic color system:
- `primary` / `secondary` - primary colors
- `muted` / `accent` - secondary colors
- `destructive` - error colors
- `foreground` / `background` - base text and background colors

### Theming
Simple theme system with dark mode support:

```tsx
const theme = {
  name: "MyTheme",
  rounded: { default: "md", button: "lg" },
  buttonSize: { default: "sm" },
  isNavFixed: true
}
```

## 🚀 Quick Start

```bash
npm install @ui8kit/core
```

```tsx
import { Button, Block, Container } from '@ui8kit/core'

function App() {
  return (
    <Container>
      <Block py="xl" ta="center">
        <Button variant="primary" size="lg">
          Get Started
        </Button>
      </Block>
    </Container>
  )
}
```

## 📚 Documentation

- [Getting Started](./getting-started.md) - Installation and setup
- [API Reference](./api-reference/) - Component reference
- [Architecture](./architecture/) - Library architecture
- [Development Guide](./development-guide/) - Developer guide
