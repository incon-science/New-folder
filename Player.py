from Character import *

class Player(Character):
    def __init__(self):
        super().__init__()

        # Initialize joystick support for this player (use first joystick if available)
        try:
            pygame.joystick.init()
            if pygame.joystick.get_count() > 0:
                self.joystick = pygame.joystick.Joystick(0)
                self.joystick.init()
            else:
                self.joystick = None
        except Exception:
            self.joystick = None

        # deadzone for analog sticks
        self.joystick_deadzone = 0.25

    def controls(self, event):
        # Allow quitting with usual events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                self.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.cancel_jump()

        # Mouse attack mapping (existing behavior)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.stopattacking:
                self.attacking = True
                self.stopattacking = False
        if event.type == pygame.MOUSEBUTTONUP:
            self.stopattacking = True

        # Joystick button events (if a joystick is present)
        if event.type == pygame.JOYBUTTONDOWN and self.joystick is not None:
            # Common mapping: button 0 = A (jump), button 1 = B (attack), button 4/5 = shoulder (run)
            try:
                if event.button == 0:
                    self.jump()
                elif event.button == 1:
                    if self.stopattacking:
                        self.attacking = True
                        self.stopattacking = False
                elif event.button in (4, 5):
                    self.running = True
            except Exception:
                pass

        if event.type == pygame.JOYBUTTONUP and self.joystick is not None:
            try:
                if event.button == 0:
                    self.cancel_jump()
                elif event.button in (4, 5):
                    self.running = False
                elif event.button == 1:
                    self.stopattacking = True
            except Exception:
                pass

    def movements(self):
        # Default keyboard handling
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LSHIFT]:
            self.running = True
        else:
            # if controller run button will override later
            self.running = False

        # Horizontal movement from keyboard
        if pressed_keys[K_q]:
            self.moved_left = True
            self.no_move = False
        elif pressed_keys[K_d]:
            self.moved_left = False
            self.no_move = False
        else:
            self.no_move = True

        # If joystick present, poll axes/buttons for movement
        if getattr(self, 'joystick', None) is not None:
            try:
                # Horizontal axis (axis 0): negative = left, positive = right
                axis_x = self.joystick.get_axis(0)
                if abs(axis_x) > self.joystick_deadzone:
                    self.no_move = False
                    # prefer axis over keyboard
                    if axis_x < 0:
                        self.moved_left = True
                    else:
                        self.moved_left = False
                else:
                    # if no keyboard input either, mark no_move
                    if not (pressed_keys[K_q] or pressed_keys[K_d]):
                        self.no_move = True

                # Run: check shoulder buttons or triggers (common indexes 4/5 or 6/7)
                run_pressed = False
                for btn_idx in (4, 5, 6, 7):
                    try:
                        if self.joystick.get_numbuttons() > btn_idx and self.joystick.get_button(btn_idx):
                            run_pressed = True
                            break
                    except Exception:
                        continue
                self.running = run_pressed or self.running
            except Exception:
                pass
 
