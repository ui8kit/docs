# Best Practices

Рекомендации и паттерны для эффективной разработки с UI8Kit. Следуйте этим практикам для создания поддерживаемого и масштабируемого кода.

## 🎯 Общие принципы

### 1. Используйте семантические пропы

```tsx
// ✅ Хорошо - семантические пропы
<Block bg="primary" c="primary-foreground" p="md">
  Primary section
</Block>

// ❌ Плохо - жестко заданные классы
<div className="bg-blue-500 text-white p-4">
  Primary section
</div>
```

### 2. Следуйте дизайн-системе

```tsx
// ✅ Хорошо - используйте дизайн токены
<Button variant="primary" size="lg" rounded="md">
  Primary Action
</Button>

// ❌ Плохо - кастомные стили
<Button className="bg-blue-500 text-white px-6 py-3 rounded-lg">
  Primary Action
</Button>
```

### 3. Будьте последовательны в API

```tsx
// ✅ Хорошо - последовательное использование
<Stack gap="lg">
  <Title size="xl">Header</Title>
  <Text>Content</Text>
  <Group gap="md">
    <Button>Cancel</Button>
    <Button variant="primary">Save</Button>
  </Group>
</Stack>

// ❌ Плохо - смешивание подходов
<div className="space-y-6">
  <h1 className="text-3xl">Header</h1>
  <p>Content</p>
  <div className="flex gap-4">
    <Button>Cancel</Button>
    <button className="bg-blue-500">Save</button>
  </div>
</div>
```

## 🧩 Компонентные паттерны

### Полиморфные компоненты

Используйте `component` проп для семантической разметки:

```tsx
// ✅ Хорошо - семантическая разметка
<Block component="section" py="xl">
  <Block component="h1">Title</Block>
  <Text component="p">Content</Text>
</Block>

// ✅ Хорошо - доступность
<Button component="a" href="/dashboard">
  Go to Dashboard
</Button>

// ❌ Плохо - неправильная семантика
<div>
  <div>Page Title</div>
  <span>Content</span>
</div>
```

### Составные компоненты

Используйте compound components для сложных UI:

```tsx
// ✅ Хорошо - compound pattern
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card description</CardDescription>
  </CardHeader>
  <CardContent>
    Main content
  </CardContent>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>

// ❌ Плохо - плоская структура
<div className="card">
  <div className="card-header">
    <h3>Card Title</h3>
    <p>Card description</p>
  </div>
  <div className="card-content">
    Main content
  </div>
  <div className="card-footer">
    <button>Action</button>
  </div>
</div>
```

## 🎨 Стилизация

### Spacing система

```tsx
// ✅ Хорошо - используйте spacing scale
<Stack gap="lg">
  <Block p="md">Content</Block>
  <Block py="xl">Large padding</Block>
</Stack>

// ❌ Плохо - магические числа
<Stack style={{ gap: '24px' }}>
  <Block style={{ padding: '12px' }}>Content</Block>
  <Block style={{ paddingTop: '48px', paddingBottom: '48px' }}>Large padding</Block>
</Stack>
```

### Цветовая система

```tsx
// ✅ Хорошо - семантические цвета
<Button variant="primary">Primary</Button>
<Button variant="destructive">Delete</Button>
<Text c="muted">Muted text</Text>

// ❌ Плохо - жестко заданные цвета
<Button className="bg-blue-500">Primary</Button>
<Button className="bg-red-500">Delete</Button>
<Text className="text-gray-500">Muted text</Text>
```

### Responsive дизайн

```tsx
// ✅ Хорошо - mobile-first
<Grid cols="1-2-3" gap="md">
  <Card>Responsive content</Card>
</Grid>

// ✅ Хорошо - responsive spacing
<Block p={{ base: "md", md: "lg", xl: "xl" }}>
  Responsive padding
</Block>

// ❌ Плохо - множественные условия
{isMobile ? (
  <div className="p-4">Mobile</div>
) : (
  <div className="p-8">Desktop</div>
)}
```

## 🔧 Производительность

### Избегайте ненужных ре-рендеров

```tsx
// ✅ Хорошо - мемоизированные коллбеки
const handleClick = useCallback(() => {
  // handle click
}, [])

// ✅ Хорошо - стабильные ссылки
const theme = useMemo(() => ({ /* theme */ }), [])

// ❌ Плохо - новые объекты при каждом рендере
<Button onClick={() => setCount(c => c + 1)}>
  Click
</Button>
```

### Tree Shaking

```tsx
// ✅ Хорошо - импортируйте только нужное
import { Button, Card } from '@ui8kit/core'

// ❌ Плохо - импортируйте все
import * as UI from '@ui8kit/core'
```

### Bundle анализ

Регулярно анализируйте размер бандла:

```bash
# Используйте bundle analyzer
npm run build
npx vite-bundle-analyzer dist
```

## ♿ Accessibility

### Семантическая разметка

```tsx
// ✅ Хорошо - правильная семантика
<Block component="main">
  <Block component="nav" aria-label="Main navigation">
    <Group component="ul" role="menubar">
      <Block component="li" role="none">
        <Button component="a" href="/">Home</Button>
      </Block>
    </Group>
  </Block>
  <Block component="section" aria-labelledby="main-heading">
    <Title id="main-heading">Main Content</Title>
  </Block>
</Block>

// ❌ Плохо - неправильная семантика
<div>
  <div>
    <div>
      <button>Home</button>
    </div>
  </div>
  <div>
    <h1>Main Content</h1>
  </div>
</div>
```

### Focus management

```tsx
// ✅ Хорошо - правильный focus flow
<Modal>
  <ModalContent>
    <ModalHeader>
      <ModalTitle>Modal Title</ModalTitle>
    </ModalHeader>
    <ModalBody>
      <form onSubmit={handleSubmit}>
        <input autoFocus />
        {/* form fields */}
        <Button type="submit">Submit</Button>
      </form>
    </ModalBody>
  </ModalContent>
</Modal>
```

### ARIA атрибуты

```tsx
// ✅ Хорошо - ARIA для сложных компонентов
<Button
  aria-expanded={isOpen}
  aria-controls="menu"
  aria-haspopup="menu"
>
  Menu
</Button>

// ✅ Хорошо - screen reader контент
<Text className="sr-only">
  Screen reader description
</Text>
```

## 🧪 Тестирование

### Unit тесты компонентов

```tsx
// ✅ Хорошо - тестируйте поведение
describe('Button', () => {
  it('calls onClick when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    fireEvent.click(screen.getByRole('button'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('shows loading spinner when loading', () => {
    render(<Button loading>Loading</Button>)

    expect(screen.getByRole('button')).toBeDisabled()
    expect(screen.getByClass('animate-spin')).toBeInTheDocument()
  })
})
```

### Visual regression тесты

```tsx
// ✅ Хорошо - visual snapshots
describe('Button variants', () => {
  it('renders primary variant correctly', () => {
    const { container } = render(<Button variant="primary">Primary</Button>)
    expect(container.firstChild).toMatchSnapshot()
  })
})
```

### E2E тесты

```tsx
// ✅ Хорошо - end-to-end flows
it('completes user registration', () => {
  cy.visit('/register')
  cy.findByLabelText('Email').type('user@example.com')
  cy.findByLabelText('Password').type('password123')
  cy.findByRole('button', { name: 'Register' }).click()
  cy.url().should('include', '/dashboard')
})
```

## 📁 Структура проекта

### Организация файлов

```
src/
├── components/          # Переиспользуемые компоненты
│   ├── ui/             # Базовые UI компоненты
│   ├── forms/          # Формы
│   └── layout/         # Layout компоненты
├── hooks/              # Кастомные хуки
├── lib/                # Утилиты
├── providers/          # Context providers
├── styles/             # Глобальные стили
└── types/              # TypeScript типы
```

### Именование компонентов

```tsx
// ✅ Хорошо - PascalCase, описательные имена
export function UserProfileCard() { /* ... */ }
export function DataTable() { /* ... */ }
export function ThemeToggle() { /* ... */ }

// ❌ Плохо - неясные имена
export function Card() { /* ... */ }      // Слишком общее
export function Btn() { /* ... */ }       // Сокращения
export function component1() { /* ... */ } // Низкоуровневое
```

### Barrel exports

```tsx
// ✅ Хорошо - barrel exports для удобного импорта
// components/index.ts
export { Button } from './ui/Button'
export { Card } from './ui/Card'
export { Input } from './forms/Input'

// Использование
import { Button, Card, Input } from '@/components'

// ❌ Плохо - глубокие импорты
import Button from '@/components/ui/Button/Button'
import Card from '@/components/ui/Card/Card'
```

## 🔄 Работа с темами

### Темизация компонентов

```tsx
// ✅ Хорошо - используйте theme context
function ThemedButton({ variant, ...props }) {
  const { rounded } = useTheme()

  return (
    <Button
      variant={variant}
      rounded={rounded.button}
      {...props}
    />
  )
}

// ❌ Плохо - жестко заданные значения
function ThemedButton({ variant, ...props }) {
  return (
    <Button
      variant={variant}
      rounded="md"
      {...props}
    />
  )
}
```

### Кастомные темы

```tsx
// ✅ Хорошо - расширяйте базовую тему
const customTheme = {
  ...baseTheme,
  colors: {
    ...baseTheme.colors,
    brand: '#ff6b6b'
  }
}

// ❌ Плохо - перезаписывайте все
const badTheme = {
  primary: '#ff6b6b',
  // отсутствуют другие необходимые свойства
}
```

## 🚀 Оптимизация

### Code splitting

```tsx
// ✅ Хорошо - lazy loading модальных окон
const Modal = lazy(() => import('./Modal'))

function App() {
  const [showModal, setShowModal] = useState(false)

  return (
    <div>
      <Button onClick={() => setShowModal(true)}>Open Modal</Button>
      {showModal && (
        <Suspense fallback={<div>Loading...</div>}>
          <Modal onClose={() => setShowModal(false)} />
        </Suspense>
      )}
    </div>
  )
}
```

### Memoization

```tsx
// ✅ Хорошо - мемоизируйте тяжелые вычисления
const filteredItems = useMemo(() =>
  items.filter(item => item.status === 'active'),
  [items]
)

// ✅ Хорошо - мемоизируйте компоненты
const UserCard = memo(function UserCard({ user }) {
  return (
    <Card>
      <Text>{user.name}</Text>
      <Text c="muted">{user.email}</Text>
    </Card>
  )
})
```

## 📝 Документирование

### Компонентная документация

```tsx
// ✅ Хорошо - документируйте API
interface ButtonProps extends
  React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** Button style variant */
  variant?: 'default' | 'primary' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link'
  /** Button size */
  size?: 'xs' | 'sm' | 'default' | 'md' | 'lg' | 'xl' | 'icon'
  /** Loading state */
  loading?: boolean
  /** Left section content */
  leftSection?: ReactNode
  /** Right section content */
  rightSection?: ReactNode
}

export function Button({ variant = 'default', size = 'default', ...props }: ButtonProps) {
  // implementation
}
```

### README файлы

```markdown
# Component Name

Brief description of what this component does.

## Usage

```tsx
import { ComponentName } from './ComponentName'

// Basic usage
<ComponentName prop="value" />

// Advanced usage
<ComponentName
  prop="value"
  onChange={handleChange}
>
  Children
</ComponentName>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| prop | string | - | Description of prop |
```

## 🔍 Отладка

### Development tools

```tsx
// ✅ Хорошо - development helpers
if (process.env.NODE_ENV === 'development') {
  // Debug logging
  console.log('Component state:', state)

  // Visual indicators
  return (
    <div data-debug="component-name">
      {/* component content */}
    </div>
  )
}
```

### Error boundaries

```tsx
// ✅ Хорошо - error boundaries для компонентов
class ErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo) {
    console.error('Component error:', error, errorInfo)
  }

  render() {
    if (this.state.hasError) {
      return <Text c="destructive">Something went wrong</Text>
    }

    return this.props.children
  }
}
```

## 🎯 Итоговые рекомендации

1. **Следуйте дизайн-системе** - используйте семантические пропы вместо кастомных классов
2. **Пишите доступный код** - правильная семантика и ARIA атрибуты
3. **Тестируйте thoroughly** - unit, integration и e2e тесты
4. **Оптимизируйте производительность** - memoization и code splitting
5. **Документируйте API** - JSDoc и README для компонентов
6. **Используйте TypeScript** - строгая типизация для надежности
7. **Будьте последовательны** - единый стиль кода и паттерны
8. **Планируйте масштабируемость** - модульная архитектура
