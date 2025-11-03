# Component Registry

## Overview

The Component Registry is a `registry.json` file that contains metadata about all components in UI8Kit/Core. This enables tooling support, component discovery, and programmatic access to component information.

## Registry Purpose

The registry serves multiple purposes:

1. **Component Discovery** - List all available components
2. **Tooling Support** - Enable CLI tools like `npx buildy-ui add`
3. **Documentation Generation** - Auto-generate component docs
4. **IDE Integration** - IntelliSense and autocomplete support
5. **Component Metadata** - Props, types, and usage information

## Registry Structure

### Basic Format

```json
{
  "version": "3.0.0",
  "components": [
    {
      "name": "Button",
      "type": "component",
      "category": "inputs",
      "path": "src/components/ui/button",
      "exports": ["Button"],
      "description": "Primary button component",
      "props": {
        "variant": {
          "type": "string",
          "values": ["primary", "secondary"],
          "default": "primary"
        },
        "size": {
          "type": "string",
          "values": ["sm", "md", "lg"],
          "default": "md"
        }
      }
    }
  ]
}
```

## Component Entry

Each component in the registry includes:

### Basic Information

```json
{
  "name": "Button",
  "type": "component",
  "category": "inputs",
  "path": "src/components/ui/button"
}
```

- **name** - Component display name
- **type** - Type (component, layout, primitive)
- **category** - Category grouping (inputs, containers, layouts)
- **path** - Source file path

### Exports

```json
{
  "exports": ["Button", "ButtonGroup", "ButtonIcon"],
  "defaultExport": "Button"
}
```

Lists all exports from the component module.

### Description

```json
{
  "description": "Primary button component with multiple variants",
  "longDescription": "A versatile button component that supports various sizes, variants, and states. Includes prop forwarding for extended customization."
}
```

Short and long descriptions for documentation.

### Props

```json
{
  "props": {
    "variant": {
      "type": "string",
      "enum": ["primary", "secondary", "danger"],
      "default": "primary",
      "description": "Button visual variant"
    },
    "size": {
      "type": "string",
      "enum": ["sm", "md", "lg"],
      "default": "md",
      "description": "Button size"
    },
    "disabled": {
      "type": "boolean",
      "default": false,
      "description": "Disable the button"
    }
  }
}
```

Detailed prop information for each component.

### Installation

```json
{
  "installation": {
    "npm": "npm install ui8kit-core",
    "cli": "npx buildy-ui add button",
    "import": "import { Button } from 'ui8kit-core';"
  }
}
```

Installation methods and import statements.

### Usage Example

```json
{
  "examples": [
    {
      "title": "Basic Button",
      "code": "<Button>Click me</Button>"
    },
    {
      "title": "Primary Variant",
      "code": "<Button variant=\"primary\">Submit</Button>"
    }
  ]
}
```

Usage examples for developers.

## Registry Organization

### By Category

Group components logically:

```json
{
  "categories": {
    "inputs": ["Button", "Input", "Select", "Checkbox"],
    "containers": ["Card", "Box", "Block"],
    "layouts": ["DashLayout", "SplitBlock", "Grid"],
    "typography": ["Heading", "Text", "Code"]
  }
}
```

### By Layer

Organize by architectural layer:

```json
{
  "layers": {
    "core": ["Box", "Block", "Grid", "Stack"],
    "components": ["Card", "Button", "Input"],
    "layouts": ["DashLayout", "SplitBlock"]
  }
}
```

### By Type

Group by component type:

```json
{
  "types": {
    "primitive": ["Box", "Block", "Grid"],
    "composite": ["Card", "Button", "Input"],
    "layout": ["DashLayout", "SplitBlock"],
    "compound": ["Card.Header", "Card.Content"]
  }
}
```

## Complete Registry Example

```json
{
  "version": "3.0.0",
  "title": "UI8Kit/Core",
  "description": "Three-layered React UI component library",
  "repository": "https://github.com/org/ui8kit-core",
  "license": "MIT",
  "components": [
    {
      "id": "button",
      "name": "Button",
      "type": "component",
      "layer": "components",
      "category": "inputs",
      "path": "src/components/ui/button",
      "exports": ["Button"],
      "description": "Versatile button component with multiple variants",
      "props": {
        "variant": {
          "type": "string",
          "enum": ["primary", "secondary"],
          "default": "primary"
        },
        "size": {
          "type": "string",
          "enum": ["sm", "md", "lg"],
          "default": "md"
        },
        "disabled": {
          "type": "boolean",
          "default": false
        }
      },
      "installation": {
        "npm": "npm install ui8kit-core",
        "cli": "npx buildy-ui add button",
        "import": "import { Button } from 'ui8kit-core';"
      },
      "examples": [
        {
          "title": "Basic",
          "code": "<Button>Click me</Button>"
        },
        {
          "title": "Primary",
          "code": "<Button variant=\"primary\">Submit</Button>"
        }
      ]
    },
    {
      "id": "card",
      "name": "Card",
      "type": "component",
      "layer": "components",
      "category": "containers",
      "path": "src/components/ui/card",
      "exports": ["Card"],
      "compound": ["Card.Header", "Card.Content", "Card.Footer"],
      "description": "Container component with header, content, and footer"
    }
  ]
}
```

## Using the Registry

### For Tooling

CLI tools can query the registry:

```javascript
// buildy-ui install tool
const registry = require('ui8kit-core/registry.json');
const button = registry.components.find(c => c.id === 'button');
console.log(button.installation.cli);
```

### For Documentation

Auto-generate documentation:

```javascript
// Generate component page
const component = registry.components[0];
const docs = `
# ${component.name}

${component.description}

## Props
${Object.entries(component.props).map(([name, prop]) => 
  `- **${name}** (${prop.type}): ${prop.description}`
).join('\n')}
`;
```

### For IDE Integration

Provide autocomplete support:

```typescript
// TypeScript definitions from registry
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
}
```

## Registry Maintenance

### Updating the Registry

When adding new components:

1. Create component source files
2. Export from module
3. Add entry to registry.json
4. Update categories if needed
5. Add usage examples
6. Commit and publish

### Validation

Validate registry structure:

```bash
npm run validate:registry
```

Check for:
- Valid JSON syntax
- Required fields present
- Unique component IDs
- Correct paths
- Valid prop types

## Best Practices

### 1. Keep Registry Synchronized
```json
{
  "components": [
    {
      "name": "Button",
      "path": "src/components/ui/button"
    }
  ]
}
```

Update registry when components change.

### 2. Include Complete Metadata
```json
{
  "description": "Clear description",
  "props": { /* comprehensive */ },
  "examples": [ /* practical examples */ ]
}
```

### 3. Use Consistent IDs
```json
{
  "id": "button",
  "name": "Button"
}
```

IDs in kebab-case, names in PascalCase.

### 4. Document All Props
```json
{
  "props": {
    "variant": {
      "type": "string",
      "enum": [...],
      "description": "..."
    }
  }
}
```

## Next Steps

- [Package Structure](../package-structure/README.md) - Understand package configuration
- [Build System](../build-system/README.md) - Learn about the build process
- [TypeScript Configuration](../typescript-configuration/README.md) - Type support details
