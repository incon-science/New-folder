from head import *
import math

import random

class Tentacule(pygame.sprite.Sprite):
    def __init__(self, pos, direction="east"):
        pygame.sprite.Sprite.__init__(self)
        self.pos = vec(pos)
        self.base_pos = vec(pos)
        self.initial_x = pos[0]  # Position initiale x pour le mouvement de translation
        self.time = random.uniform(0, 10.0)  # Temps initial aléatoire
        self.time_offset = random.uniform(0, math.pi * 2)  # Décalage de phase aléatoire
        self.movement_offset = random.uniform(0, math.pi * 2)  # Décalage pour le mouvement latéral
        self.segments = []
        self.length = 30  # Segments un peu plus longs
        self.num_segments = 20  # Beaucoup plus de segments pour une tentacule plus longue
        self.direction = direction  # "east" pour droite, "west" pour gauche
        
        # Paramètres d'ondulation
        self.wave_speeds = [1.2, 1.0, 0.8]  # Vitesses doublées
        self.wave_amplitudes = [30, 20, 15]  # Différentes amplitudes
        self.phase_shifts = [0, math.pi/4, math.pi/2]  # Décalages de phase
        
        # Initialiser la chaîne de segments horizontalement
        prev_pos = self.pos
        for i in range(self.num_segments):
            self.segments.append({
                "pos": vec(prev_pos),
                "angle": 0,
                "phase_offset": i * 0.2  # Décalage progressif pour l'effet d'onde
            })
            # Ajuster la direction du segment
            if self.direction == "east":
                prev_pos.x += self.length  # Vers la droite
            else:
                prev_pos.x -= self.length  # Vers la gauche
    
    def move(self):
        # Mettre à jour le temps avec une vitesse plus rapide
        self.time += 0.04
        
        # Mouvement de translation horizontal lent
        translation_x = math.sin(self.time * 0.3 + self.movement_offset) * 100
        self.base_pos.x = self.initial_x + translation_x
        
        # Pour chaque segment
        for i, segment in enumerate(self.segments):
            # Position de base horizontale selon la direction
            if self.direction == "east":
                base_x = self.base_pos.x + i * self.length  # Vers la droite
            else:
                base_x = self.base_pos.x - i * self.length  # Vers la gauche
            base_y = self.base_pos.y
            
            # Facteur d'amplitude qui diminue vers la pointe
            amplitude_factor = (self.num_segments - i) / self.num_segments
            
            # Combiner plusieurs ondes sinusoïdales avec des fréquences différentes
            wave_x = 0
            wave_y = 0
            
            for j in range(len(self.wave_speeds)):
                # Onde verticale (principale) avec décalage temporel
                wave_y += math.sin(
                    (self.time + self.time_offset) * self.wave_speeds[j] + 
                    segment["phase_offset"] + 
                    self.phase_shifts[j]
                ) * self.wave_amplitudes[j] * amplitude_factor
                
                # Onde horizontale (plus subtile, pour la tension)
                wave_x += math.cos(
                    self.time * self.wave_speeds[j] * 0.7 + 
                    segment["phase_offset"] * 1.5 + 
                    self.phase_shifts[j]
                ) * (self.wave_amplitudes[j] * 0.1) * amplitude_factor
            
            # Position cible pour ce segment
            target_pos = vec(base_x + wave_x, base_y + wave_y)
            
            # Mouvement fluide vers la position cible
            if i == 0:
                # Le premier segment suit directement le mouvement
                segment["pos"] = segment["pos"].lerp(target_pos, 0.1)
            else:
                # Les segments suivants suivent avec un effet de chaîne
                prev_segment = self.segments[i-1]
                dir_to_prev = prev_segment["pos"] - segment["pos"]
                
                if dir_to_prev.length() > 0:
                    # Garder une distance constante avec le segment précédent
                    ideal_pos = prev_segment["pos"] - dir_to_prev.normalize() * self.length
                    # Mélanger la position idéale avec la position ondulante
                    target_pos = target_pos.lerp(ideal_pos, 0.5)
                    # Mouvement fluide
                    segment["pos"] = segment["pos"].lerp(target_pos, 0.15)
                    
            # Calculer l'angle pour l'orientation
            if i < len(self.segments) - 1:
                next_pos = self.segments[i+1]["pos"]
                dir_to_next = next_pos - segment["pos"]
                segment["angle"] = math.atan2(dir_to_next.y, dir_to_next.x)

    def display(self, surface, camera):
        # Dessiner chaque segment
        for i in range(len(self.segments)):
            # Position à l'écran du segment actuel
            curr_pos = self.segments[i]["pos"] - camera.pos
            
            # Dessiner le segment
            if i < len(self.segments) - 1:
                next_pos = self.segments[i + 1]["pos"] - camera.pos
                
                # Épaisseur qui diminue de façon exponentielle vers la pointe
                progress = i / (len(self.segments) - 1)  # 0 au début, 1 à la fin
                # Utilisation d'une fonction de puissance pour une diminution plus douce
                thickness = max(25 * pow(1 - progress, 1.8), 1)  # Diminution plus progressive et pointe moins fine
                
                # Couleurs blanc et noir
                white = (255, 255, 255)  # Couleur principale blanche
                black = (0, 0, 0)        # Contour noir
                
                # Dessiner d'abord le contour noir
                pygame.draw.line(surface, black, curr_pos, next_pos, int(thickness + 2))
                # Puis le segment blanc par-dessus
                pygame.draw.line(surface, white, curr_pos, next_pos, int(thickness))