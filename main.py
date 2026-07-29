import time
import sys

# Clever fallback wrapper: provides lightweight stubs so static analysis
# and non-microcontroller environments won't error when inspecting the file.
try:
    import board  # type: ignore[import]
    import busio  # type: ignore[import]
    from kmk.kmk_keyboard import KMKKeyboard  # type: ignore[import]
    from kmk.keys import KC  # type: ignore[import]
    from kmk.scanners.keypad import KeysScanner  # type: ignore[import]
    from kmk.modules.macros import Macros, Press, Release, Tap  # type: ignore[import]
    from kmk.extensions import Extension  # type: ignore[import]
    from kmk.extensions.peg_oled import Oled, OledDisplayMode, OledReactionType  # type: ignore[import]
except Exception:
    # Fallback stubs for text editor / IDE static analysis only.
    class _BoardStub:
        D0 = D1 = D2 = D3 = D4 = D5 = D6 = D7 = D8 = D9 = D10 = None
    board = _BoardStub()

    class busio:
        class I2C:
            def __init__(self, _a, _b):
                pass

    class KMKKeyboard:
        def __init__(self):
            self.extensions = []
            self.modules = []
            self.keymap = []
            self.events = type("E", (), {"on_runtime_start": (lambda f: f)})
        def go(self):
            pass

    class KC:
        @staticmethod
        def LCTL(x):
            return x
        @staticmethod
        def LSFT(x):
            return x
        @staticmethod
        def LGUI(x):
            return x
        @staticmethod
        def R(x):
            return x
        ESC = "ESC"
        E = "E"
        ENTER = "ENTER"
        VOLU = "VOLU"
        VOLD = "VOLD"
        class MACRO:
            def __init__(self, *_a, **_k):
                pass
        class NO:
            @staticmethod
            def clone():
                return KC.NO()
            def on_press(self, *_a, **_k):
                pass

    class KeysScanner:
        def __init__(self, _pins, _value_when_pressed=False):
            pass

    class Macros:
        pass

    def Press(_k):
        return _k
    def Release(_k):
        return _k
    def Tap(_k):
        return _k

    class Extension:
        pass

    class Oled:
        def __init__(self, _i2c, _device_address=0x3C, _display_mode=None, _reaction_type=None):
            self.oled = type("_O", (), {
                "fill": lambda *_, **__: None,
                "text": lambda *_, **__: None,
                "show": lambda *_, **__: None,
                "pixel": lambda *_, **__: None,
            })()

    class OledDisplayMode:
        TXT = 0

    class OledReactionType:
        NONE = 0

keyboard = KMKKeyboard()

# --------------------------------------------------------------------------
# 1. HARDWARE DIRECT-PIN CONFIGURATION (Matches your XIAO PCB Traces)
# --------------------------------------------------------------------------
keyboard.matrix = KeysScanner(
    pins=[
        board.D0, board.D1, board.D2,  # Bottom row: SW1, SW2, SW3
        board.D3, board.D6, board.D7,  # Middle row: SW4, SW5, SW6
        board.D8, board.D9, board.D10, # Top row:    SW7, SW8, SW9
    ],
    value_when_pressed=False, # Active-low logic for switches to ground
)

# --------------------------------------------------------------------------
# 2. KEY OVERRIDES & HACK CLUB SHORTCUT MACROS
# --------------------------------------------------------------------------
macros = Macros()
keyboard.modules.append(macros)

TASK_MANAGER = KC.LCTL(KC.LSFT(KC.ESC))
FILE_EXPLORER = KC.LGUI(KC.E)

GO_SLACK = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), 0.08, "https://slack.com", Tap(KC.ENTER))
GO_KICAD = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), 0.08, "https://kicad.org", Tap(KC.ENTER))
GO_TINKERCAD = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), 0.08, "https://tinkercad.com", Tap(KC.ENTER))
GO_SPOTIFY = KC.MACRO(Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI), 0.08, "https://spotify.com", Tap(KC.ENTER))

# --------------------------------------------------------------------------
# 3. THE ANIMATED CAT OLEDBYTEMAP DATA
# --------------------------------------------------------------------------
CAT_FRAME_1 = bytes([
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x1c, 0x3c, 0x38, 0x70, 0x60, 0x60, 0xe0, 0xc0, 0xc0, 0xc0, 0xc0,
    0xc0, 0xc0, 0xc0, 0xc0, 0xe0, 0x60, 0x60, 0x70, 0x38, 0x3c, 0x1c, 0x0c, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x1c, 0x7f, 0xe3, 0xc1, 0x80, 0x00, 0x00, 0x00, 0x0c, 0x0c, 0x00, 0x00, 0x03, 0x03, 0x00,
    0x00, 0x0c, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x80, 0xc1, 0xe3, 0x7f, 0x1c, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x07, 0x1c, 0x30, 0x60, 0x40, 0xc0, 0x80, 0x81, 0x81, 0x81, 0x80, 0x80, 0x80,
    0x80, 0x80, 0x80, 0x81, 0x81, 0x81, 0x80, 0xc0, 0x40, 0x60, 0x30, 0x1c, 0x07, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])

CAT_FRAME_2 = bytes([
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x1c, 0x3c, 0x38, 0x70, 0x60, 0x60, 0xe0, 0xc0, 0xc0, 0xc0, 0xc0,
    0xc0, 0xc0, 0xc0, 0xc0, 0xe0, 0x60, 0x60, 0x70, 0x38, 0x3c, 0x1c, 0x0c, 0x06, 0x0f, 0x0f, 0x06,
    0x00, 0x1c, 0x7f, 0xe3, 0xc1, 0x80, 0x00, 0x00, 0x00, 0x0c, 0x0c, 0x00, 0x00, 0x03, 0x03, 0x00,
    0x00, 0x0c, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x80, 0xc1, 0xe3, 0x7f, 0x1c, 0x30, 0xf0, 0xf0, 0x30,
    0x00, 0x00, 0x00, 0x07, 0x1c, 0x30, 0x60, 0x40, 0xc0, 0x80, 0x81, 0x81, 0x81, 0x80, 0x80, 0x80,
    0x80, 0x80, 0x80, 0x81, 0x81, 0x81, 0x80, 0xc0, 0x40, 0x60, 0x30, 0x1c, 0x07, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x01, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
])

# --------------------------------------------------------------------------
# 4. CUSTOM ANIMATION EXTENSION (Replaces QMK oled_task_user)
# --------------------------------------------------------------------------
class CatWaveAnimation(Extension):
    def __init__(self):
        self.show_animation = False
        self.animation_start_time = 0
        self.last_frame_time = 0
        self.current_frame = 0
        self.oled = None

    def on_runtime_start(self, keyboard):
        for ext in keyboard.extensions:
            if isinstance(ext, Oled):
                self.oled = ext.oled
                break

    def trigger_wave(self):
        self.show_animation = True
        self.animation_start_time = time.monotonic()
        if self.oled:
            self.oled.fill(0)

    def before_matrix_scan(self, keyboard):
        if not self.show_animation or not self.oled:
            return

        now = time.monotonic()
        
        # 10 second timeout condition (ANIMATION_DURATION)
        if now - self.animation_start_time > 10.0:
            self.show_animation = False
            self.oled.fill(0)
            self.oled.text("hackropad", 0, 0, 1)
            self.oled.show()
            return

        # 300ms Frame Flip sequence
        if now - self.last_frame_time > 0.3:
            self.last_frame_time = now
            self.current_frame = 1 - self.current_frame
            
            self.oled.fill(0)
            frame_data = CAT_FRAME_1 if self.current_frame == 0 else CAT_FRAME_2
            
            # Rendering 32x32 bounding box mapping block onto screen
            for y in range(4):
                for x in range(32):
                    byte_val = frame_data[y * 32 + x]
                    for bit in range(8):
                        pixel = (byte_val >> bit) & 1
                        self.oled.pixel(x, y * 8 + bit, pixel)
            self.oled.show()

cat_animation = CatWaveAnimation()
keyboard.extensions.append(cat_animation)

def trigger_cat_wave(key, keyboard, *args, **kwargs):
    cat_animation.trigger_wave()

CAT_WAVE = KC.NO.clone()
CAT_WAVE.on_press = trigger_cat_wave

# --------------------------------------------------------------------------
# 5. HARDWARE DISPLAY CONFIGURATION (XIAO Hardware I2C Pins)
# --------------------------------------------------------------------------
# Ensuring i2c_bus isn't called during editor static environment parses
if board.D5 is not None:
    i2c_bus = busio.I2C(board.D5, board.D4) # SCL, SDA
else:
    i2c_bus = None

oled_ext = Oled(
    i2c_bus,
    device_address=0x3C,
    display_mode=OledDisplayMode.TXT,
    reaction_type=OledReactionType.NONE,
)
keyboard.extensions.append(oled_ext)

# --------------------------------------------------------------------------
# 6. ORTHO 3X3 KEYMAP DEF (Matches physical row layouts from top to bottom)
# --------------------------------------------------------------------------
keyboard.keymap = [
    [
        # Top Row (SW7, SW8, SW9)
        GO_SLACK,            GO_KICAD,      GO_TINKERCAD,
        
        # Middle Row (SW4, SW5, SW6)
        KC.VOLU,             KC.VOLD,       GO_SPOTIFY,
        
        # Bottom Row (SW1, SW2, SW3)
        TASK_MANAGER,        FILE_EXPLORER, CAT_WAVE
    ]
]

@keyboard.events.on_runtime_start
def initial_screen():
    if oled_ext.oled:
        oled_ext.oled.fill(0)
        oled_ext.oled.text("hackropad", 0, 0, 1)
        oled_ext.oled.show()

if __name__ == '__main__':
    keyboard.go()
