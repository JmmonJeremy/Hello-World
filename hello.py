# import colorama to allow different colors for the hello text
import colorama
# import the functions to be used from colorama
from colorama import Fore, Back, Style
# import pygame to be able to display a flashing hello
import pygame
# import pygame as pg to be able to stop the program
import pygame as pg

# create the main function to run the program
def main():
    # set the display screen size
    screen = pygame.display.set_mode((550, 130))
    # set the font to the default and set font size
    FONT = pygame.font.SysFont(None, 100)
    # create variables holding the text and its colors
    text = FONT.render(" Hello ", False, pygame.Color("red"))
    text2 = FONT.render("World ", False, pygame.Color("blue"))
    text3 = FONT.render("!!! ", False, pygame.Color("purple"))
    
    # use variables to set the box around the text and create new variables
    surf = pygame.Surface(text.get_rect().size)
    surf2 = pygame.Surface(text2.get_rect().size)
    surf3 = pygame.Surface(text3.get_rect().size)
    # use variable to set the color key enabling for transparency
    surf.set_colorkey((1, 1, 1))
    surf2.set_colorkey((1, 1, 1))
    surf3.set_colorkey((1, 1, 1))
    # use variable to fill the box with yellow color
    surf.fill((255, 255, 0))
    surf2.fill((255, 255, 0))
    surf3.fill((255, 255, 0))
    # use variables to display the text
    surf.blit(text, (0, 5))
    surf2.blit(text2, (0, 5))
    surf3.blit(text3, (0, 5))
    # create a variable for the clock
    clock = pygame.time.Clock()
    # set the alpha to zero
    alpha = 0
    # run the program until exited
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # set alpha for the text to fade it out
        alpha = (alpha + 1) % 256
        surf.set_alpha(alpha)
        surf2.set_alpha(alpha)
        surf3.set_alpha(alpha)
        
        # set background color for the pygame screen
        screen.fill(pygame.Color("black"))
        # set placement of the text being displayed
        screen.blit(surf, (20, 30))
        screen.blit(surf2, (233, 30))
        screen.blit(surf3, (445, 30))
        # set the time for the program to run
        clock.tick(120)
        # the example I learned from diplayed the alpha in the terminal with print(alpha), I didn't so I could instead display my python hello
       
        # diplay the changes to the pygame screen
        pygame.display.update()

# run the Hello Word through pygame in the main function
if __name__ == '__main__':
    pygame.init()
    # print Hello World with different colors and use the join fuction to use the unicode character \u0332 for underline to underline Hello
    print(Style.BRIGHT + Fore.RED + Back.YELLOW + "\u0332".join(" Hello ") + Fore.CYAN + "World" + Fore.MAGENTA + " !!! " + Style.RESET_ALL)
    main()


# stop the process when exited
if __name__ == '__main__':   
    pg.quit()