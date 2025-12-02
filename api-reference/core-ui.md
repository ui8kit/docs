# Core UI API Reference

Reference for variant system, utilities, and low-level primitives of UI8Kit.

## 🎨 Система variantов

### Spacing Variants

```tsx
import { spacingVariants } from '@ui8kit/core'

// Margin
m="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"
mx="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"  // left + right
my="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"  // top + bottom
mt="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"  // top
mb="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"  // bottom
ml="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"  // left
mr="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl" | "auto"  // right

// Padding
p="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
px="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
py="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
pt="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
pb="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
pl="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
pr="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"

// Space between children
spaceX="none" | "xs" | "sm" | "md" | "lg" | "xl"
spaceY="none" | "xs" | "sm" | "md" | "lg" | "xl"
```

**Usage Examples:**
```tsx
<Block p="md" mx="auto" spaceY="lg">
  <Text>Item 1</Text>
  <Text>Item 2</Text>
</Block>
```

### Color Variants

```tsx
import { colorVariants } from '@ui8kit/core'

// Background colors
bg="transparent" | "background" | "foreground" | "primary" | "primary-foreground" |
   "secondary" | "secondary-foreground" | "muted" | "muted-foreground" |
   "accent" | "accent-foreground" | "destructive" | "destructive-foreground" |
   "border" | "input" | "ring" | "card" | "popover"

// Text colors
c="foreground" | "primary" | "primary-foreground" | "secondary" | "secondary-foreground" |
  "muted" | "muted-foreground" | "accent" | "accent-foreground" |
  "destructive" | "destructive-foreground"

// Border colors
borderColor="transparent" | "current" | "border" | "input" | "ring" | "foreground" |
            "primary" | "secondary" | "destructive" | "muted" | "accent"

// Accent color
accentColor="auto" | "inherit" | "current"

// Placeholder color
placeholder="foreground" | "muted"

// Caret color
caret="primary" | "secondary" | "accent" | "foreground" | "current" | "transparent"

// Selection colors (global styles)
selectionBg="primary" | "secondary" | "accent"
selectionText="foreground" | "primary"
```

**Usage Examples:**
```tsx
<Button bg="primary" c="primary-foreground">
  Primary Button
</Button>

<Block bg="card" c="card-foreground" borderColor="border">
  Card content
</Block>
```

### Layout Variants

```tsx
import { layoutVariants } from '@ui8kit/core'

// Dimensions
w="auto" | "full" | "screen" | "fit" | "min" | "max" | "1/2" | "1/3" | "2/3" | "1/4" | "3/4"
h="auto" | "full" | "screen" | "fit" | "min" | "max"
minH="none" | "full" | "screen" | "fit" | "0" | "xs" | "sm" | "md" | "lg" | "xl"

// Position
position="static" | "relative" | "absolute" | "fixed" | "sticky"

// Display
display="block" | "inline" | "inline-block" | "flex" | "inline-flex" | "grid" | "inline-grid" | "none"

// Overflow
overflow="auto" | "hidden" | "visible" | "scroll"
overflowX="auto" | "hidden" | "visible" | "scroll"
overflowY="auto" | "hidden" | "visible" | "scroll"

// Z-index
z="auto" | "0" | "10" | "20" | "30" | "40" | "50"
```

**Usage Examples:**
```tsx
<Container w="full" minH="screen" position="relative">
  <Block w="1/2" h="full" overflow="auto">
    Content
  </Block>
</Container>
```

### Visual Variants

#### Rounded
```tsx
rounded="none" | "sm" | "md" | "lg" | "xl" | "2xl" | "3xl" | "full"
```

#### Shadow
```tsx
shadow="none" | "sm" | "md" | "lg" | "xl" | "2xl" | "inner"
```

#### Border
```tsx
border="none" | "default" | "2" | "4" | "8"
borderTop="none" | "default" | "2" | "4" | "8"
borderBottom="none" | "default" | "2" | "4" | "8"
borderLeft="none" | "default" | "2" | "4" | "8"
borderRight="none" | "default" | "2" | "4" | "8"
```

**Usage Examples:**
```tsx
<Card rounded="xl" shadow="lg" border="default">
  Card content
</Card>
```

### Flex Variants

```tsx
import { flexVariants } from '@ui8kit/core'

// Direction
direction="row" | "column" | "row-reverse" | "column-reverse"

// Alignment
align="stretch" | "start" | "center" | "end" | "baseline"
justify="start" | "center" | "end" | "between" | "around" | "evenly"

// Wrap
wrap="nowrap" | "wrap" | "wrap-reverse"

// Gap
gap="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"

// Flex item props
flex="none" | "auto" | "initial" | "1" | "grow" | "shrink"
shrink="0" | "1"
grow="0" | "1"
basis="auto" | "full" | "1/2" | "1/3" | "1/4"
```

**Usage Examples:**
```tsx
<Group direction="row" align="center" justify="between" gap="md">
  <Button>Left</Button>
  <Button>Right</Button>
</Group>
```

### Typography Variants

#### Text Size
```tsx
size="xs" | "sm" | "base" | "lg" | "xl" | "2xl" | "3xl" | "4xl" | "5xl" | "6xl" | "7xl" | "8xl" | "9xl"
```

#### Font Weight
```tsx
fw="thin" | "extralight" | "light" | "normal" | "medium" | "semibold" | "bold" | "extrabold" | "black"
```

#### Text Align
```tsx
ta="left" | "center" | "right" | "justify" | "start" | "end"
```

#### Leading (Line Height)
```tsx
leading="none" | "tight" | "snug" | "normal" | "relaxed" | "loose"
```

#### Typography Modifiers
```tsx
// Transform
transform="none" | "capitalize" | "uppercase" | "lowercase"

// Whitespace
whitespace="normal" | "nowrap" | "pre" | "pre-line" | "pre-wrap"

// Word break
break="normal" | "words" | "all"

// Hyphens
hyphens="none" | "manual" | "auto"

// Decoration
underline="none" | "underline" | "line-through" | "overline"
decoration="solid" | "double" | "dotted" | "dashed" | "wavy"
decorationColor="current" | "foreground" | "primary" | ...
```

**Usage Examples:**
```tsx
<Title size="4xl" fw="bold" ta="center" c="primary">
  Main Heading
</Title>

<Text size="lg" leading="relaxed" c="muted" transform="capitalize">
  Description text
</Text>
```

## 🎯 Component-Specific Variants

### Button Variants

```tsx
// Style variants
variant="default" | "primary" | "destructive" | "outline" | "secondary" | "ghost" | "link"

// Size variants
size="xs" | "sm" | "default" | "md" | "lg" | "xl" | "icon"

// Content alignment
contentAlign="start" | "center" | "end" | "between"
```

### Badge Variants

```tsx
// Style variants
variant="default" | "secondary" | "destructive" | "outline" | "success" | "warning"

// Size variants
size="xs" | "sm" | "default" | "lg"
```

### Image Variants

```tsx
// Object fit
fit="contain" | "cover" | "fill" | "none" | "scale-down"

// Object position
position="center" | "top" | "bottom" | "left" | "right" | "top-left" | "top-right" | "bottom-left" | "bottom-right"

// Aspect ratio
aspect="square" | "video" | "auto" | "1/1" | "4/3" | "16/9" | "21/9"
```

### Grid Variants

```tsx
// Grid template columns
cols="1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" |
     "none" | "subgrid"

// Grid template rows
rows="1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" |
     "none" | "subgrid"

// Gap
gap="none" | "xs" | "sm" | "md" | "lg" | "xl" | "2xl"
```

## 🛠️ Utilities

### cn() - Class Merger

```tsx
import { cn } from '@ui8kit/core/lib/utils'

// Merges classes and resolves conflicts
const classes = cn(
  "px-2 py-1 bg-red-500",
  "px-4 bg-blue-500",  // px-2 
        "text-center"         // will add new class
)
// Result: "py-1 px-4 bg-blue-500 text-center"
```

### Variant Types

All variants export their types:

```tsx
import type {
  VariantSpacingProps,
  ColorProps,
  VariantLayoutProps,
  RoundedProps,
  ShadowProps,
  BorderProps,
  VariantFlexProps,
  TextSizeProps,
  FontWeightProps,
  ButtonSizeProps,
  ButtonStyleProps
} from '@ui8kit/core'
```

## 🎨 Creating Custom Variants

```tsx
import { cva, type VariantProps } from 'class-variance-authority'

export const customVariants = cva(
  "base-classes",
  {
    variants: {
      variant: {
        primary: "bg-primary text-primary-foreground",
        secondary: "bg-secondary text-secondary-foreground"
      },
      size: {
        sm: "text-sm px-2 py-1",
        lg: "text-lg px-4 py-2"
      }
    },
    defaultVariants: {
      variant: "primary",
      size: "sm"
    }
  }
)

export type CustomProps = VariantProps<typeof customVariants>
```

## 🔄 Composition Patterns

### Variant Inheritance

```tsx
interface MyComponentProps extends
  VariantSpacingProps,
  ColorProps,
  RoundedProps {
  customProp?: string
}
```

### Component Composition

```tsx
const CustomButton = ({ variant, size, ...props }) => (
  <Button
    variant={variant || "primary"}
    size={size || "md"}
    rounded="md"
    {...props}
  />
)
```

## 📊 CSS Custom Properties

UI8Kit использует CSS переменные для цветов:

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 221.2 83.2% 53.3%;
  --primary-foreground: 210 40% 98%;
  /* ... */
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 217.2 91.2% 59.8%;
  /* ... */
}
```

Эти переменные используются в Tailwind через `hsl(var(--primary))`.
