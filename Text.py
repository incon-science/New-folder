from head import *

class Text(pygame.sprite.Sprite):
    def __init__(self, txt, color, size, pos, font='Lucida Console', bg_color=None, padding=6, bg_alpha=200):
        """
        txt: string
        color: (r,g,b)
        size: int (font size)
        pos: tuple (x,y) center position on screen
        font: system font name
        bg_color: None or (r,g,b) background color. If None, no background.
        padding: pixels of padding around text when drawing background
        bg_alpha: 0-255 alpha for background when bg_color provided
        """
        super().__init__()

        my_font = pygame.font.SysFont(font, size)
        text_surf = my_font.render(txt, True, color)

        # If background requested, create a surface with padding and alpha
        if bg_color is not None:
            w = text_surf.get_width() + padding * 2
            h = text_surf.get_height() + padding * 2
            surf = pygame.Surface((w, h), pygame.SRCALPHA)
            # Fill background with color+alpha
            r, g, b = bg_color
            surf.fill((r, g, b, bg_alpha))
            # Blit text onto background surface centered with padding
            surf.blit(text_surf, (padding, padding))
            self.surf = surf
        else:
            self.surf = text_surf

        self.rect = self.surf.get_rect(center=pos)

    def display(self, surf):
        surf.blit(self.surf, self.rect)