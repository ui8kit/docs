# Components API Reference

Complete reference for all UI8Kit components with usage examples and prop types.

## 🧱 Basic Primitives

### Block

Polymorphic semantic container with full styling capabilities.

```tsx
import { Block } from '@ui8kit/core'

<Block component="section" py="xl" bg="background" rounded="lg">
  Content
</Block>
```

**Пропы:**
```tsx
interface BlockProps extends
  React.HTMLAttributes<HTMLElement>,
  VariantSpacingProps,
  ColorProps,
  Pick<VariantLayoutProps, 'w' | 'h' | 'minH' | 'position'>,
  RoundedProps,
  ShadowProps,
  BorderProps {
  children: ReactNode
  component?: ElementType  // section, main, nav, article, etc.
  variant?: 'section' | 'main' | 'nav' | 'article' | 'header' | 'footer' | 'aside' | 'div'
}
```

### Box

Flexible primitive with full variant support. Can render as any HTML element.

```tsx
import { Box } from '@ui8kit/core'

// As input
<Box component="input" type="text" w="full" p="md" rounded="md" border="default" />

// As textarea
<Box component="textarea" rows={4} w="full" p="md" rounded="md" border="default" />

// As div with flex
<Box display="flex" gap="md" align="center">
  Content
</Box>
```

**Пропы:**
```tsx
interface BoxProps extends
  VariantSpacingProps,
  RoundedProps,
  ShadowProps,
  ColorProps,
  VariantLayoutProps,
  BorderProps,
  VariantFlexProps,
  AspectRatioProps {
  component?: ElementType
  className?: string
  children?: ReactNode
  [key: string]: any  // For additional props
}
```

## 🎨 UI Components

### Button

Interactive button with style and state variants.

```tsx
import { Button } from '@ui8kit/core'

<Button variant="primary" size="lg" loading={isLoading}>
  Click me
</Button>

<Button variant="outline" leftSection={<Icon />}>
  With icon
</Button>
```

**Варианты:**
- `variant`: `default`, `primary`, `destructive`, `outline`, `secondary`, `ghost`, `link`
- `size`: `xs`, `sm`, `default`, `md`, `lg`, `xl`, `icon`

**Пропы:**
```tsx
interface ButtonProps extends
  React.ButtonHTMLAttributes<HTMLButtonElement>,
  Pick<VariantSpacingProps, 'm' | 'mx' | 'my' | 'mr'>,
  RoundedProps,
  ShadowProps,
  Pick<VariantLayoutProps, 'w'>,
  ButtonSizeProps,
  ButtonStyleProps,
  ButtonContentAlignProps {
  children: ReactNode
  leftSection?: ReactNode
  rightSection?: ReactNode
  loading?: boolean
  disabled?: boolean
}
```

### Badge

Small status indicators.

```tsx
import { Badge } from '@ui8kit/core'

<Badge variant="success">Active</Badge>
<Badge variant="destructive" dot>Offline</Badge>
<Badge leftSection={<Icon />} rightSection={<Icon />}>
  With icons
</Badge>
```

**Варианты:**
- `variant`: `default`, `secondary`, `destructive`, `outline`, `success`, `warning`
- `size`: `xs`, `sm`, `default`, `lg`

**Пропы:**
```tsx
interface BadgeProps extends
  React.HTMLAttributes<HTMLDivElement>,
  BadgeSizeProps,
  BadgeStyleProps,
  RoundedProps,
  ShadowProps,
  Pick<VariantSpacingProps, 'm' | 'mx' | 'my' | 'mr'> {
  children?: ReactNode
  leftSection?: ReactNode
  rightSection?: ReactNode
  dot?: boolean
}
```

### Card

Card with compound structure.

```tsx
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@ui8kit/core'

<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
  </CardHeader>
  <CardContent>
    Content
  </CardContent>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>
```

**Components:**
- `Card` - main container
- `CardHeader` - card header
- `CardTitle` - title
- `CardDescription` - description
- `CardContent` - main content
- `CardFooter` - footer with actions

### Title

Semantic headings with typography.

```tsx
import { Title } from '@ui8kit/core'

<Title order={1} size="4xl" fw="bold" ta="center">
  Main Heading
</Title>

<Title order={2} size="2xl" c="muted">
  Subheading
</Title>
```

**Пропы:**
```tsx
interface TitleProps extends
  React.HTMLAttributes<HTMLHeadingElement>,
  TextSizeProps,
  FontWeightProps,
  TextAlignProps,
  LeadingProps,
  TypographyModifierProps,
  ColorProps,
  VariantSpacingProps {
  order?: 1 | 2 | 3 | 4 | 5 | 6  // h1, h2, etc.
}
```

### Text

Text elements with full typography control.

```tsx
import { Text } from '@ui8kit/core'

<Text size="lg" fw="medium" c="foreground">
  Regular text
</Text>

<Text size="sm" c="muted" truncate>
  Long text that will be truncated...
</Text>
```

**Пропы:**
```tsx
interface TextProps extends
  React.HTMLAttributes<HTMLParagraphElement>,
  TextSizeProps,
  FontWeightProps,
  TextAlignProps,
  LeadingProps,
  TypographyModifierProps,
  ColorProps,
  VariantSpacingProps {
  truncate?: boolean
}
```

### Image

Enhanced image component.

```tsx
import { Image } from '@ui8kit/core'

<Image
  src="/image.jpg"
  alt="Description"
  aspect="video"
  fit="cover"
  rounded="lg"
/>
```

**Пропы:**
```tsx
interface ImageProps extends
  React.ImgHTMLAttributes<HTMLImageElement>,
  ImageFitProps,
  ImagePositionProps,
  AspectRatioProps,
  RoundedProps,
  ShadowProps,
  VariantLayoutProps {
  // Standard img props plus variant features
}
```

### Icon

Icon wrapper with size and color control.

```tsx
import { Icon } from '@ui8kit/core'
import { ChevronDown } from 'lucide-react'

<Icon lucideIcon={ChevronDown} size="lg" c="primary" />
```

**Пропы:**
```tsx
interface IconProps extends
  React.HTMLAttributes<SVGElement>,
  ColorProps,
  Pick<VariantLayoutProps, 'w' | 'h'> {
  lucideIcon: LucideIcon
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
}
```

## 📐 Layout Components

### Container

Responsive container with preset sizes.

```tsx
import { Container } from '@ui8kit/core'

<Container size="lg" centered>
  <Block py="xl">
    Content
  </Block>
</Container>
```

**Sizes:**
- `xs`: 640px
- `sm`: 768px
- `md`: 1024px
- `lg`: 1280px
- `xl`: 1536px

**Пропы:**
```tsx
interface ContainerProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps {
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  centered?: boolean
}
```

### Stack

Vertical stack with gap control.

```tsx
import { Stack } from '@ui8kit/core'

<Stack gap="lg" align="center" p="md">
  <Title>Heading</Title>
  <Text>Description</Text>
  <Button>Action</Button>
</Stack>
```

**Пропы:**
```tsx
interface StackProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  Pick<VariantFlexProps, 'gap' | 'align'> {
  // Inherits spacing and flex props       
}
```

### Group

Horizontal stack with alignment.

```tsx
import { Group } from '@ui8kit/core'

<Group gap="md" align="center" justify="between">
  <Button variant="outline">Cancel</Button>
  <Button>Save</Button>
</Group>
```

**Пропы:**
```tsx
interface GroupProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  Pick<VariantFlexProps, 'gap' | 'align' | 'justify' | 'wrap'> {
  // Inherits spacing and flex props
}
```

### Grid

CSS Grid with responsive presets.

```tsx
import { Grid, GridCol } from '@ui8kit/core'

<Grid cols="1-2-3" gap="lg">
  <GridCol span={2}>Wide column</GridCol>
  <GridCol>Narrow column</GridCol>
  <GridCol>Narrow column</GridCol>
</Grid>
```

**Column Presets:**
- `1`: 1 column
- `1-2`: 1 on mobile, 2 on large screens
- `1-2-3`: 1 → 2 → 3 columns
- `1-2-3-4`: 1 → 2 → 3 → 4 columns

**Пропы:**
```tsx
interface GridProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  VariantGridProps {
  cols?: string  // '1-2-3' format
}

interface GridColProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps {
  span?: number
  start?: number
  end?: number
}
```

## 🎭 Composite Components

### Sheet

Modal overlay with animations.

```tsx
import { Sheet, SheetTrigger, SheetContent, SheetHeader, SheetTitle } from '@ui8kit/core'

<Sheet>
  <SheetTrigger asChild>
    <Button>Open Sheet</Button>
  </SheetTrigger>
  <SheetContent>
    <SheetHeader>
      <SheetTitle>Title</SheetTitle>
    </SheetHeader>
    Content
  </SheetContent>
</Sheet>
```

**Components:**
- `Sheet` - root component
- `SheetTrigger` - open trigger
- `SheetContent` - content
- `SheetHeader` - header
- `SheetTitle` - title
- `SheetDescription` - description

### Accordion

Expandable content.

```tsx
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@ui8kit/core'

<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>Item 1</AccordionTrigger>
    <AccordionContent>Content 1</AccordionContent>
  </AccordionItem>
  <AccordionItem value="item-2">
    <AccordionTrigger>Item 2</AccordionTrigger>
    <AccordionContent>Content 2</AccordionContent>
  </AccordionItem>
</Accordion>
```

**Пропы:**
```tsx
interface AccordionProps extends
  React.HTMLAttributes<HTMLDivElement> {
  type?: 'single' | 'multiple'
  value?: string | string[]
  defaultValue?: string | string[]
  onValueChange?: (value: string | string[]) => void
  collapsible?: boolean
}
```

## 🎨 Universal Props

All components support these universal props:

### Spacing
```tsx
p="md" px="lg" py="sm" pt="xl" pr="md" pb="sm" pl="lg"  // Padding
m="md" mx="lg" my="sm" mt="xl" mr="md" mb="sm" ml="lg"  // Margin
```

### Colors
```tsx
bg="primary" c="foreground" borderColor="border"
```

### Layout
```tsx
w="full" h="auto" minH="screen" position="relative" display="flex"
```

### Visual
```tsx
rounded="md" shadow="lg" border="default"
```

### Flex (for layout components)
```tsx
direction="column" align="center" justify="between" wrap="wrap" gap="md"
```

## 🔧 Data Attributes

All components have semantic `data-class` attributes for testing and styling:

```tsx
// In DOM will appear:
<button data-class="button">...</button>
<div data-class="card">
  <div data-class="card-header">...</div>
</div>
```
