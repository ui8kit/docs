# Overview

## Introduction to UI8Kit/Core

**UI8Kit/Core** is a three-layered React UI component library built with utility-first classes and clean HTML5 semantic tag approach. The architecture aligns with atomic design philosophy, providing a structured and scalable system for building modern web interfaces.

## Core Philosophy: Minimalism

The fundamental motivation behind UI8Kit/Core is **minimalism**. Complex interfaces can be built using just **15 composite components** and **12 reusable variants** that cover approximately 80% of design scenarios. This approach delivers:

- **Minimal code footprint** - Only what you need, nothing more
- **Eliminated redundant classes** - Centralized variant system prevents duplication
- **Unlimited design flexibility** - Tailwind utility-first approach enables any layout

## Architecture at a Glance

UI8Kit/Core follows a three-layered architectural model:

```
┌─────────────────────────────────────────────┐
│  Layouts (Templates)                        │
│  DashLayout, SplitBlock, Grid, Flex         │
└─────────────────────────────────────────────┘
                     ↑
┌─────────────────────────────────────────────┐
│  UI Components (Composite)                  │
│  Card, Button, Input, Select, etc.          │
│  With prop forwarding and variants          │
└─────────────────────────────────────────────┘
                     ↑
┌─────────────────────────────────────────────┐
│  Core Components (Primitives)               │
│  Box, Block, Grid, Stack, Button, etc.      │
│  Basic building blocks                      │
└─────────────────────────────────────────────┘
```

This structure mirrors atomic design:
- **Atoms** → Core Components (basic primitives)
- **Molecules** → UI Components (composite components)
- **Organisms** → Layouts (complex page layouts)

## Key Features

### 1. CVA-Based Variant System
The component styling logic is centralized using Class Variance Authority (CVA). All variants are composable and reusable across components:
- Spacing (margin/padding)
- Colors (backgrounds/text)
- Layout (width/height)
- Shadows, borders, rounded corners
- Typography properties
- Flexbox and grid properties

### 2. Prop Forwarding API
Extended components use a consistent prop forwarding pattern that allows composing base components with additional variant props from the core system. This enables unlimited customization without leaving the design system.

### 3. Compound Components Pattern
Components use the compound pattern (e.g., `Card.Header`, `Card.Content`, `Card.Footer`) for flexible composition while maintaining type safety.

### 4. Data-Class Attributes
All components use consistent `data-class` attributes for identification and DOM targeting, enabling:
- Easy testing and debugging
- Programmatic DOM manipulation
- Component tracking and analytics

### 5. TypeScript-First
Full TypeScript support with strict type checking, path aliases, and generated type definitions.

## Integration Formats

UI8Kit/Core supports multiple integration scenarios:

1. **NPM Installation** - Standard `npm install ui8kit-core`
2. **Per-Component Installation** - Via `npx buildy-ui add [component]`
3. **JSON Registry** - Programmatic access to component metadata
4. **Git Submodule** - For monorepo architectures
5. **Direct Source Integration** - For custom builds

## What You'll Learn

This documentation covers:
- **Architecture** - Deep dive into the three-layer system
- **API Reference** - Complete documentation for all components
- **Development Guide** - Practical workflows and patterns
- **Best Practices** - Recommendations for optimal usage
- **Dark Mode** - Theme implementation and configuration

## Next Steps

- [Getting Started](../02-getting-started/README.md) - Set up the library in your project
- [Architecture](../03-architecture/README.md) - Understand the system structure
- [API Reference](../04-api-reference/README.md) - Explore available components
