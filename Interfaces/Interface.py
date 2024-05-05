import pygame
import random

class Carte:
    pygame.init()

    MARGIN = 10
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    GRID_SIZE = 5
    CELL_SIZE = (SCREEN_WIDTH - 2 * MARGIN) // GRID_SIZE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("POKEMON")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    background_images = ["Images/Jardin.jpg", "Images/0003Venusaur.PNG", "Images/0002Ivysaur.PNG"]
    current_background_index = 0

    @classmethod
    def dessiner_grille(cls):
        cls.screen.fill(cls.WHITE)
        background_image = pygame.image.load(cls.background_images[cls.current_background_index])
        background_image = pygame.transform.scale(background_image, (cls.SCREEN_WIDTH, cls.SCREEN_HEIGHT))
        cls.screen.blit(background_image, (0, 0))

        pygame.draw.rect(cls.screen, cls.BLACK,
                         pygame.Rect(cls.MARGIN, cls.MARGIN, cls.SCREEN_WIDTH - 2 * cls.MARGIN,
                                     cls.SCREEN_HEIGHT - 2 * cls.MARGIN), 1)

        for i in range(1, cls.GRID_SIZE):
            pygame.draw.line(cls.screen, cls.BLACK, (cls.MARGIN, cls.MARGIN + i * cls.CELL_SIZE),
                             (cls.SCREEN_WIDTH - cls.MARGIN, cls.MARGIN + i * cls.CELL_SIZE), 1)
            pygame.draw.line(cls.screen, cls.BLACK, (cls.MARGIN + i * cls.CELL_SIZE, cls.MARGIN),
                             (cls.MARGIN + i * cls.CELL_SIZE, cls.SCREEN_HEIGHT - cls.MARGIN), 1)

        pygame.display.flip()

    @classmethod
    def changer_background(cls):
        # Mettre à jour l'index de l'image d'arrière-plan
        cls.current_background_index = (cls.current_background_index + 1) % len(cls.background_images)

class Joueur:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = (255, 0, 0)
        self.bonhomme_image = pygame.image.load("Images/Bulbizarre-RFVF.png")
        self.bonhomme_image = pygame.transform.scale(self.bonhomme_image,
                                                     (int(Carte.CELL_SIZE * 0.8), int(Carte.CELL_SIZE * 0.8)))

    def deplacer(self, direction):
        if direction == "haut" and self.col > 0:
            self.col -= 1
        elif direction == "bas" and self.col < Carte.GRID_SIZE - 1:
            self.col += 1
        elif direction == "gauche" and self.row > 0:
            self.row -= 1
        elif direction == "droite" and self.row < Carte.GRID_SIZE - 1:
            self.row += 1

    def dessiner(self):
        Carte.screen.blit(self.bonhomme_image,
                          (Carte.MARGIN + self.col * Carte.CELL_SIZE, Carte.MARGIN + self.row * Carte.CELL_SIZE))


rows, cols = random.randint(1, Carte.GRID_SIZE)-1, random.randint(1, Carte.GRID_SIZE)-1
joueur = Joueur(rows, cols)

running = True
clock = pygame.time.Clock()  # Créer une horloge pygame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                joueur.deplacer("haut")
            elif event.key == pygame.K_DOWN:
                joueur.deplacer("bas")
            elif event.key == pygame.K_LEFT:
                joueur.deplacer("gauche")
            elif event.key == pygame.K_RIGHT:
                joueur.deplacer("droite")

    Carte.dessiner_grille()
    joueur.dessiner()

    pygame.display.flip()

    clock.tick(0.5)  # Régler la fréquence de changement d'image à 1 image par seconde
    Carte.changer_background()  # Changer l'image d'arrière-plan

pygame.quit()
