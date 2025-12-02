# UI8Kit Documentation

**UI8Kit** is a modern React UI library with TypeScript-first approach, utility-first styling, and polymorphic components.

## 📚 Documentation

### Quick Start
- **[Overview](overview.md)** - Library overview
- **[Getting Started](getting-started.md)** - Installation and setup

### API Reference
- **[Components](api-reference/components.md)** - Complete component reference
- **[Core UI](api-reference/core-ui.md)** - Variants system and utilities
- **[Layouts](api-reference/layouts.md)** - Layout components (Container, Stack, Grid)

### Architecture
- **[Architecture Overview](architecture/overview.md)** - General architecture
- **[Variant System](architecture/variant-system.md)** - Variants system (CVA)
- **[Package Structure](architecture/package-structure.md)** - Package structure
- **[TypeScript Configuration](architecture/typescript-configuration.md)** - TypeScript setup
- **[Build System](architecture/build-system.md)** - Build system

### Development
- **[Development Guide](development-guide/development-guide.md)** - Main guide
- **[Basic Workflow](development-guide/basic-workflow.md)** - Step-by-step workflow
- **[Best Practices](development-guide/best-practices.md)** - Best practices
- **[Dark Mode](development-guide/dark-mode.md)** - Theme implementation

### Troubleshooting
- **[Troubleshooting](troubleshooting.md)** - Solving common issues

## 🚀 Key Features

- **TypeScript-first**: Full type safety with autocompletion
- **Utility-first**: All styles available as component props
- **Polymorphic components**: Any HTML element via `component` prop
- **Variants system**: Consistent styling through CVA
- **Dark mode**: Built-in theme support
- **Tree shaking**: Automatic unused code removal
- **Accessibility**: ARIA attributes and keyboard navigation

## 📦 Installation

```bash
npm install @ui8kit/core
```

## 🎯 Usage Example

```tsx
import { Button, Block, Container, Stack, Card } from '@ui8kit/core'
import { ThemeProvider } from './providers/theme'

function App() {
  return (
    <ThemeProvider theme={defaultTheme}>
      <Container>
        <Stack gap="lg" align="center">
          <Block py="xl" ta="center">
            <Title size="4xl">Welcome to UI8Kit</Title>
            <Text c="muted">Modern React UI Library</Text>
          </Block>

          <Card p="lg" rounded="xl">
            <Stack gap="md">
              <Text fw="bold">Getting Started</Text>
              <Button variant="primary" size="lg">
                Learn More
              </Button>
            </Stack>
          </Card>
        </Stack>
      </Container>
    </ThemeProvider>
  )
}
```

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

## 📊 Performance

- **Bundle size**: ~15KB gzipped (full core)
- **Tree shaking**: Automatic unused code removal
- **Zero runtime**: Styles compiled to CSS
- **Stable references**: No unnecessary re-renders

## 🤝 Community

- **GitHub**: [github.com/ui8kit/core](https://github.com/ui8kit/core)
- **Issues**: For bug reports and feature requests
- **Discussions**: For questions and discussions

## 📄 License

GPL-3.0

---

**Start developing with [Getting Started](getting-started.md)!** 🚀