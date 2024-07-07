import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        #initialize score keeping attributes
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.stats

        #font settings for score keepign information
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        #prepare the initial score image
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """Tend the score into a rendered image"""

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        #display the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = (self.screen_rect.right - 20)
        self.score_rect.top = 20

    def prep_highscore(self):
        """Trun the highscore into a rendered image"""
        highscore = round(self.stats.highscore, -1)
        highscore_str = "{:,}".format(highscore)
        self.highscore_image = self.font.render(highscore_str, True, self.text_color, self.settings.bg_color)

        #center the score at the top of the screen
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top
    def show_score(self):
        """show score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """check if we have the highest score"""
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()


    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)

        #position the level above the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.top

    def prep_ship(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 * ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)