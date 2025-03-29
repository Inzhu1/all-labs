import pygame  # Импорт библиотеки Pygame

pygame.init()  # Инициализация Pygame

# Задаем размеры окна
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно для рисования
clock = pygame.time.Clock()  # Создаем объект для управления частотой кадров

# Определяем цвета в формате RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLUE  # Устанавливаем начальный цвет

radius = 5  # Радиус кисти
mode = "pen"  # Режим рисования (по умолчанию — карандаш)
start_pos = None  # Начальная позиция для рисования фигур
is_drawing = False  # Флаг для отслеживания нажатия кнопки мыши
points = []  # Список точек для режима "карандаш"

# Заливаем фон черным цветом
screen.fill(BLACK)
pygame.display.flip()  # Обновляем экран

running = True  # Основной цикл программы
while running:
    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Закрытие окна
            running = False
        
        if event.type == pygame.KEYDOWN:  # Обработка нажатий клавиш
            if event.key == pygame.K_r:  # Красный цвет
                current_color = RED
            elif event.key == pygame.K_g:  # Зеленый цвет
                current_color = GREEN
            elif event.key == pygame.K_b:  # Синий цвет
                current_color = BLUE
            elif event.key == pygame.K_e:  # Режим ластика
                mode = "eraser"
            elif event.key == pygame.K_p:  # Режим карандаша
                mode = "pen"
            elif event.key == pygame.K_c:  # Режим круга
                mode = "circle"
            elif event.key == pygame.K_t:  # Режим прямоугольника
                mode = "rect"
            elif event.key == pygame.K_EQUALS:  # Увеличение радиуса кисти
                radius = min(50, radius + 1)
            elif event.key == pygame.K_MINUS:  # Уменьшение радиуса кисти
                radius = max(1, radius - 1)
            elif event.key == pygame.K_ESCAPE:  # Очистка экрана
                screen.fill(BLACK)
                pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:  # Нажатие кнопки мыши
            start_pos = event.pos  # Запоминаем начальную позицию
            is_drawing = True  # Включаем режим рисования
            if mode == "pen":  # Если включен карандаш, добавляем точку
                points.append(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP:  # Отпускание кнопки мыши
            end_pos = event.pos  # Запоминаем конечную позицию
            is_drawing = False  # Отключаем режим рисования
            if mode == "rect":  # Если выбран режим прямоугольника
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, 2)  # Рисуем прямоугольник
            elif mode == "circle":  # Если выбран режим круга
                center = start_pos
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, current_color, center, radius, 2)  # Рисуем круг
            pygame.display.flip()  # Обновляем экран

        if event.type == pygame.MOUSEMOTION and is_drawing:  # Движение мыши с зажатой кнопкой
            if mode == "pen":  # Если включен карандаш
                pygame.draw.line(screen, current_color, points[-1], event.pos, radius)  # Рисуем линию
                points.append(event.pos)  # Добавляем точку в список
            elif mode == "eraser":  # Если включен ластик
                pygame.draw.circle(screen, BLACK, event.pos, radius)  # Стираем область
            pygame.display.flip()  # Обновляем экран

    clock.tick(60)  # Ограничение FPS до 60 кадров в секунду

pygame.quit()  # Завершаем работу Pygame
     
               
