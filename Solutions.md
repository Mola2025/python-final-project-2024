# Issue: [Pieces Out Of Screen]

## Problem Description

- What was the unexpected behavior?
  R// The piece went out of the screen but it continues working and when in touches the end of the screen appears in the middle of it, breaking the game
- What should have happened instead?
  R// Dont go out of the screen the piece
- How was this issue discovered?
  R// By playing the game and observing the piece going out of the screen and coming back in the
  middle of it

## Root Cause Analysis

- What was the underlying cause?
  R// The piece was not being checked if it was out of the screen before moving it
- What assumptions were incorrect?
  R// The assumption that the piece would not go out of the screen was incorrect
- What dependencies were involved?
  R// The piece's position and the screen's size were involved

## Resolution

- How was it fixed? (or planned fix if unresolved)

- What changes were made?
  R//

  BEFORE:

  for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
  for j, cell in enumerate(row):
  try:
  if cell == 'O' and (self.grid[piece.y + i + y][piece.x + j + x] != 0):
  return False
  except IndexError:
  return False
  return True

  AFTER:
  for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
  for j, cell in enumerate(row):
  if cell == 'O':
  if (piece.x + j + x < 0 or piece.x + j + x >= self.width or
  piece.y + i + y >= self.height or self.grid[piece.y + i + y][piece.x + j + x] != 0):
  return False
  return True

## Prevention

- What lessons were learned?
  R// Always check the boundaries of the piece before moving it and consider the grid's size and
  the piece's position
- What warning signs should be watched for?
  R// Pieces going out of the screen or colliding with other pieces without any apparent reason

# Issue 2: [Not Reading Holding Key For Piece Movement]

## Problem Description

- What was the unexpected behavior?
  R// The piece was not moving when the holding key was pressed
- What should have happened instead?
  R// The piece should have moved continuously when the holding key was pressed
- How was this issue discovered?
  R// I reported that the piece was not moving when the holding key was pressed

## Root Cause Analysis

- What was the underlying cause?
  R// The game was not reading the holding key for piece movement correctly
- What assumptions were incorrect?
  R// The game assumed that the holding key was being read correctly
- What dependencies were involved?
  R// The game's movement logic and the holding key's functionality

## Resolution

- How was it fixed? (or planned fix if unresolved)
  R// The game now reads the holding key for piece movement correctly by adding inside the for loop of the game the property pygame.key.get_pressed()
- What changes were made?
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
  After the loop of the only two Key.Down
- What alternatives were considered?
  R// The game could have used a different approach to handle piece movement, such as using a separate
  thread or process

## Prevention

- How can similar issues be prevented?
  R// The game should always check the dependencies involved in its logic and ensure that they are
  working correctly
- What lessons were learned?
  R// The game should always test its logic thoroughly to catch any unexpected behavior
- What warning signs should be watched for?
  R// The game should watch for any unexpected behavior or crashes that may indicate a problem with
  its logic
