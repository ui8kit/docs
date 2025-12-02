# Layout Components API

Комплексное руководство по компонентам лейаута UI8Kit - Container, Stack, Group, Grid и их использованию.

## 📦 Container

Адаптивный контейнер с предустановленными максимальными ширинами.

### Использование

```tsx
import { Container } from '@ui8kit/core'

<Container size="lg" centered px="md">
  <Block py="xl">
    Ваш контент здесь
  </Block>
</Container>
```

### Пропы

```tsx
interface ContainerProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps {
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  centered?: boolean
}
```

### Размеры контейнера

| Size | Max Width | Breakpoint |
|------|-----------|------------|
| `xs` | 640px  | - |
| `sm` | 768px  | `@media (min-width: 640px)` |
| `md` | 1024px | `@media (min-width: 768px)` |
| `lg` | 1280px | `@media (min-width: 1024px)` |
| `xl` | 1536px | `@media (min-width: 1280px)` |

### Примеры

#### Базовый контейнер
```tsx
<Container>
  <Text>Контент ограничен максимальной шириной</Text>
</Container>
```

#### Контейнер с центрированием
```tsx
<Container centered>
  <Card w="full" maxW="md">
    <Text>Этот контент центрирован по горизонтали</Text>
  </Card>
</Container>
```

#### Адаптивный контейнер
```tsx
<Container size="lg" px={{ base: "md", md: "lg" }}>
  <Grid cols="1-2-3" gap="lg">
    <Card>Колонка 1</Card>
    <Card>Колонка 2</Card>
    <Card>Колонка 3</Card>
  </Grid>
</Container>
```

## 📚 Stack

Вертикальный стек элементов с контролем промежутков.

### Использование

```tsx
import { Stack } from '@ui8kit/core'

<Stack gap="lg" align="center" p="md">
  <Title>Заголовок</Title>
  <Text>Описание</Text>
  <Button>Действие</Button>
</Stack>
```

### Пропы

```tsx
interface StackProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  Pick<VariantFlexProps, 'gap' | 'align'> {
  // Наследует spacing и flex пропы
}
```

### Примеры

#### Базовый стек
```tsx
<Stack gap="md">
  <Title size="lg">Заголовок секции</Title>
  <Text>Описание секции с некоторым текстом</Text>
  <Group gap="sm">
    <Button variant="outline">Отмена</Button>
    <Button>Сохранить</Button>
  </Group>
</Stack>
```

#### Стек с выравниванием
```tsx
<Stack gap="xl" align="center" ta="center">
  <Icon lucideIcon={CheckCircle} size="xl" c="success" />
  <Title>Успешно!</Title>
  <Text c="muted">Операция завершена</Text>
  <Button size="lg">Продолжить</Button>
</Stack>
```

#### Стек с разделителями
```tsx
<Stack gap="lg">
  <Block>
    <Title size="md">Секция 1</Title>
    <Text>Контент первой секции</Text>
  </Block>

  <Block borderTop="default" pt="lg">
    <Title size="md">Секция 2</Title>
    <Text>Контент второй секции</Text>
  </Block>
</Stack>
```

## 🎯 Group

Горизонтальный стек с выравниванием и контролем обертывания.

### Использование

```tsx
import { Group } from '@ui8kit/core'

<Group gap="md" align="center" justify="between">
  <Button variant="outline">Отмена</Button>
  <Button>Сохранить</Button>
</Group>
```

### Пропы

```tsx
interface GroupProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  Pick<VariantFlexProps, 'gap' | 'align' | 'justify' | 'wrap'> {
  // Наследует spacing и flex пропы
}
```

### Примеры

#### Кнопки действий
```tsx
<Group gap="sm" justify="end">
  <Button variant="outline">Отмена</Button>
  <Button variant="destructive">Удалить</Button>
  <Button>Сохранить</Button>
</Group>
```

#### Навигация с иконками
```tsx
<Group gap="lg" align="center">
  <Icon lucideIcon={Home} />
  <Text fw="medium">Главная</Text>
  <Icon lucideIcon={ChevronRight} size="sm" />
  <Text c="muted">Текущая страница</Text>
</Group>
```

#### Адаптивная группа
```tsx
<Group gap="md" wrap="wrap" justify="center">
  <Badge>React</Badge>
  <Badge>TypeScript</Badge>
  <Badge>Tailwind</Badge>
  <Badge>UI8Kit</Badge>
</Group>
```

## 🔲 Grid

CSS Grid с адаптивными пресетами колонок.

### Использование

```tsx
import { Grid, GridCol } from '@ui8kit/core'

<Grid cols="1-2-3" gap="lg">
  <GridCol span={2}>Широкая колонка</GridCol>
  <GridCol>Обычная колонка</GridCol>
  <GridCol>Обычная колонка</GridCol>
</Grid>
```

### Пропы Grid

```tsx
interface GridProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps,
  VariantGridProps {
  cols?: string  // Формат: "1-2-3" (моб-табл-десктоп)
}
```

### Пропы GridCol

```tsx
interface GridColProps extends
  React.HTMLAttributes<HTMLDivElement>,
  VariantSpacingProps {
  span?: number    // Сколько колонок занимает
  start?: number   // Начальная линия
  end?: number     // Конечная линия
}
```

### Пресеты колонок

| Preset | Мобильный | Планшет | Десктоп |
|--------|-----------|---------|---------|
| `"1"` | 1 колонка | 1 колонка | 1 колонка |
| `"1-2"` | 1 | 2 | 2 |
| `"1-2-3"` | 1 | 2 | 3 |
| `"1-2-4"` | 1 | 2 | 4 |
| `"1-3-6"` | 1 | 3 | 6 |

### Примеры

#### Простая сетка
```tsx
<Grid cols="1-2-3" gap="md">
  <Card>Элемент 1</Card>
  <Card>Элемент 2</Card>
  <Card>Элемент 3</Card>
</Grid>
```

#### Сетка с разными размерами колонок
```tsx
<Grid cols="3" gap="lg">
  <GridCol span={2}>
    <Card p="lg">
      <Title>Широкий контент</Title>
      <Text>Эта колонка занимает 2/3 ширины</Text>
    </Card>
  </GridCol>
  <GridCol>
    <Card p="lg">
      <Title>Боковая панель</Title>
      <Text>Узкая колонка</Text>
    </Card>
  </GridCol>
</Grid>
```

#### Асимметричная сетка
```tsx
<Grid cols="4" gap="md">
  <GridCol span={1} start={1}>1</GridCol>
  <GridCol span={2} start={2}>2-3</GridCol>
  <GridCol span={1} start={4}>4</GridCol>
</Grid>
```

#### Карточная сетка
```tsx
<Grid cols="1-2-3-4" gap="lg" p="lg">
  {items.map((item) => (
    <Card key={item.id} p="md" rounded="lg" shadow="md">
      <Image src={item.image} aspect="video" rounded="md" />
      <Stack gap="sm" mt="md">
        <Title size="lg">{item.title}</Title>
        <Text c="muted">{item.description}</Text>
        <Group justify="between" mt="sm">
          <Text fw="bold">{item.price}</Text>
          <Button size="sm">Купить</Button>
        </Group>
      </Stack>
    </Card>
  ))}
</Grid>
```

## 🏗️ Расширенные паттерны

### Holy Grail Layout

```tsx
<Container minH="screen">
  <Stack gap="0">
    {/* Header */}
    <Block bg="primary" c="primary-foreground" p="md">
      <Group justify="between" align="center">
        <Title>Логотип</Title>
        <Group gap="lg">
          <Button variant="ghost">Главная</Button>
          <Button variant="ghost">О нас</Button>
          <Button variant="ghost">Контакты</Button>
        </Group>
      </Group>
    </Block>

    {/* Main Content */}
    <Grid cols="1-4" gap="lg" p="lg" flex="grow">
      {/* Sidebar */}
      <GridCol span={1}>
        <Stack gap="md">
          <Card p="md">
            <Title size="md">Навигация</Title>
            {/* Навигационные ссылки */}
          </Card>
          <Card p="md">
            <Title size="md">Фильтры</Title>
            {/* Фильтры */}
          </Card>
        </Stack>
      </GridCol>

      {/* Content */}
      <GridCol span={3}>
        <Stack gap="lg">
          <Title>Основной контент</Title>
          <Grid cols="1-2-3" gap="md">
            {/* Карточки контента */}
          </Grid>
        </Stack>
      </GridCol>
    </Grid>

    {/* Footer */}
    <Block bg="muted" c="muted-foreground" p="md" mt="auto">
      <Group justify="between" align="center">
        <Text>© 2024 UI8Kit</Text>
        <Group gap="md">
          <Button variant="link" size="sm">Политика</Button>
          <Button variant="link" size="sm">Условия</Button>
        </Group>
      </Group>
    </Block>
  </Stack>
</Container>
```

### Dashboard Layout

```tsx
<Container minH="screen" bg="background">
  <Grid cols="12" minH="screen">
    {/* Sidebar */}
    <GridCol span={2} bg="muted" p="lg">
      <Stack gap="lg">
        <Title size="lg">Dashboard</Title>
        <Stack gap="sm">
          <Button variant="ghost" w="full" justify="start">
            <Icon lucideIcon={Home} mr="sm" />
            Главная
          </Button>
          <Button variant="ghost" w="full" justify="start">
            <Icon lucideIcon={Users} mr="sm" />
            Пользователи
          </Button>
          <Button variant="ghost" w="full" justify="start">
            <Icon lucideIcon={Settings} mr="sm" />
            Настройки
          </Button>
        </Stack>
      </Stack>
    </GridCol>

    {/* Main Content */}
    <GridCol span={10} p="lg">
      <Stack gap="lg">
        {/* Header */}
        <Group justify="between" align="center">
          <Title>Аналитика</Title>
          <Group gap="sm">
            <Button variant="outline">Экспорт</Button>
            <Button>Создать отчет</Button>
          </Group>
        </Group>

        {/* Stats Grid */}
        <Grid cols="1-2-4" gap="md">
          <Card p="md" bg="primary" c="primary-foreground">
            <Title size="2xl">1,234</Title>
            <Text>Пользователи</Text>
          </Card>
          <Card p="md" bg="secondary" c="secondary-foreground">
            <Title size="2xl">567</Title>
            <Text>Заказы</Text>
          </Card>
          <Card p="md" bg="accent" c="accent-foreground">
            <Title size="2xl">$89,012</Title>
            <Text>Доход</Text>
          </Card>
          <Card p="md" bg="muted" c="foreground">
            <Title size="2xl">94.2%</Title>
            <Text>Конверсия</Text>
          </Card>
        </Grid>

        {/* Charts and Tables */}
        <Grid cols="1-2" gap="lg">
          <Card p="lg">
            <Title size="lg" mb="md">График продаж</Title>
            {/* Chart component */}
          </Card>
          <Card p="lg">
            <Title size="lg" mb="md">Последние заказы</Title>
            {/* Table component */}
          </Card>
        </Grid>
      </Stack>
    </GridCol>
  </Grid>
</Container>
```

## 📱 Адаптивные паттерны

### Mobile-First Grid

```tsx
<Grid cols="1-2-3-4" gap="md">
  {/* Автоматически: 1 колонка на моб, 4 на десктопе */}
  {Array.from({ length: 8 }, (_, i) => (
    <Card key={i} p="md">
      Элемент {i + 1}
    </Card>
  ))}
</Grid>
```

### Responsive Stack/Group

```tsx
{/* Stack на мобильном, Group на десктопе */}
<Box display={{ base: "flex", md: "block" }} flexDirection={{ base: "column", md: "row" }} gap="md">
  <Card>Элемент 1</Card>
  <Card>Элемент 2</Card>
  <Card>Элемент 3</Card>
</Box>
```

## 🔧 Кастомизация

### Темизация лейаут компонентов

```tsx
const theme = {
  rounded: {
    container: "xl",
    card: "lg"
  },
  spacing: {
    section: "xl",
    card: "lg"
  }
}

// Использование в компонентах
<Container rounded={theme.rounded.container} p={theme.spacing.section}>
  <Card rounded={theme.rounded.card} p={theme.spacing.card}>
    Content
  </Card>
</Container>
```

### Создание кастомных лейаут компонентов

```tsx
const PageLayout = ({ children, sidebar, header, footer }) => (
  <Container minH="screen">
    <Stack gap="0">
      {header && <Block as="header">{header}</Block>}
      <Group gap="0" flex="grow">
        {sidebar && (
          <Block w="64" minH="screen">
            {sidebar}
          </Block>
        )}
        <Block flex="grow" p="lg">
          {children}
        </Block>
      </Group>
      {footer && <Block as="footer">{footer}</Block>}
    </Stack>
  </Container>
)
```
