import pygame
import random


def main():

    pygame.init()

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # Define center and coordinates to draw
    shape_name = random.choice(list(ascii_shapes.keys()))
    rows = ascii_shapes[shape_name]

    spacing = 25
    particle_radius = 10

    ascii_width = max(len(row) for row in rows)
    ascii_height = len(rows)

    shape_width = ascii_width * spacing
    shape_height = ascii_height * spacing

    start_x = SCREEN_WIDTH // 2 - shape_width // 2
    start_y = SCREEN_HEIGHT // 2 - shape_height // 2

    shape_points = []

    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != " ":
                screen_x = start_x + x * spacing
                screen_y = start_y + y * spacing
                shape_points.append((screen_x, screen_y))

    random.shuffle(shape_points)

    visible_count = 0
    particles_per_frame = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        # Draw particles
        for coordinate in shape_points[:visible_count]:
            pygame.draw.circle(screen, "white", coordinate, particle_radius)

        if visible_count < len(shape_points):
            visible_count += particles_per_frame

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# ASCII Art Shapes
ascii_shapes = {
    "cow": [
        r"        \   ^__^",
        r"         \  (oo)\_______",
        r"            (__)\       )\/\\",
        r"                ||----w |",
        r"                ||     ||",
    ],

    "dog": [
        r"  / \__",
        r" (    @\___",
        r" /         O",
        r"/   (_____/",
        r"/_____/   U",
    ],

    "cat": [
        r" /\_/\ ",
        r"( o.o )",
        r" > ^ < ",
    ],

    "fish": [
        r"      /`·.¸",
        r"     /¸...¸`:·",
        r" ¸.·´  ¸   `·.¸.·´)",
        r": © ):´;      ¸  {",
        r" `·.¸ `·  ¸.·´\`·¸)",
        r"     `\\´´\¸.·´",
    ],

    "butterfly": [
        r"  .==-.                   .-==.  ",
        r"   \()8`-._  `.   .'  _.-'8()/   ",
        r"   (88'   ::.  \./  .::   `88)   ",
        r"    \_.'`-::::.(#).::::-'`._/    ",
        r"      `._... .q(_)p. ..._.'      ",
        r"        ''-..-'|=|`-..-''        ",
        r"        .'' .' /|\ `. ''.        ",
        r"       ,':8(o)./|\.(o)8:`.       ",
        r"      (O :8 ::/ \:: 8: O)        ",
        r"       \O `::/   \::' O/         ",
        r"        ''--'     '--''          ",
    ],

    "heart": [
        r"  ***   ***  ",
        r" ***** ***** ",
        r"*************",
        r"*************",
        r" *********** ",
        r"  *********  ",
        r"   *******   ",
        r"    *****    ",
        r"     ***     ",
        r"      *      ",
    ],

    "star": [
        r"      *      ",
        r"     ***     ",
        r"    *****    ",
        r"*************",
        r"  *********  ",
        r"    *****    ",
        r"   **   **   ",
        r"  *       *  ",
    ],

    "tree": [
        r"      *      ",
        r"     ***     ",
        r"    *****    ",
        r"   *******   ",
        r"  *********  ",
        r" *********** ",
        r"     |||     ",
        r"     |||     ",
    ],

    "rocket": [
        r"       /\       ",
        r"      /  \      ",
        r"     /++++\     ",
        r"    /  ()  \    ",
        r"    |      |    ",
        r"    |      |    ",
        r"    |______|    ",
        r"   /|      |\   ",
        r"  /_|______|_\  ",
        r"     /_/\_\     ",
        r"    /_/  \_\    ",
    ],

    "dragon": [
        r"           / \  //\ ",
        r"    |\___/|      /   \//  \\",
        r"    /0  0  \__  /    //  | \ \ ",
        r"   /     /  \/_/    //   |  \  \ ",
        r"   @_^_@'/   \/_   //    |   \   \ ",
        r"   //_^_/     \/_ //     |    \    \ ",
        r"( //) |        \///      |     \     \ ",
        r"( / /) _|_ /   )  //       |      \     _\ ",
        r"( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.",
    ],
}


if __name__ == "__main__":
    main()