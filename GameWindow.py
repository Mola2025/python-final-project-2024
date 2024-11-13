import sys
import pygame
from tetris import Tetris, draw_score, draw_game_over, display_top_scores
from database import save_score
from config import WIDTH, HEIGHT, GRID_SIZE, BLACK, WHITE, RED


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
    fall_time = 0
    fall_speed = 400  # Adjust the falling speed
    move_time = 0
    move_speed = 100  # Interval for moving pieces when key is held down

    while True:
        screen.fill(BLACK)

        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and game.game_over:
                # Pedir nombre y guardar puntuación
                name = input("Insert Your Name: ")
                save_score(name, game.score)
                game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.valid_move(game.current_piece, 0, 0, 1):
                    game.current_piece.rotation += 1
                if event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1
                    game.lock_piece(game.current_piece)

        keys = pygame.key.get_pressed()
        move_time += clock.get_time()
        if keys[pygame.K_LEFT] and move_time >= move_speed and game.valid_move(game.current_piece, -1, 0, 0):
            game.current_piece.x -= 1
            move_time = 0
        if keys[pygame.K_RIGHT] and move_time >= move_speed and game.valid_move(game.current_piece, 1, 0, 0):
            game.current_piece.x += 1
            move_time = 0
        if keys[pygame.K_DOWN] and game.valid_move(game.current_piece, 0, 1, 0):
            game.current_piece.y += 1

        fall_time += clock.get_time()
        if fall_time >= fall_speed:
            game.update()
            fall_time = 0

        draw_score(screen, game.score, 10, 10)
        game.draw(screen)
        if game.game_over:
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)
            display_top_scores(screen, 100, 100)

        pygame.display.flip()
        clock.tick(60)  # Control de frames por segundo


if __name__ == "__main__":
    main()
