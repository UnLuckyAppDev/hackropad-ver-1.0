#include QMK_KEYBOARD_H

// 1. Give your custom shortcuts descriptive names
enum custom_keycodes {
    LAUNCH_SLACK = SAFE_RANGE,
    OPEN_TINKERCAD,
    OPEN_SPOTIFY
};

// 2. Map your 1-9 physical keys
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        LAUNCH_SLACK,   KC_APP_KICAD,   OPEN_TINKERCAD,
        OPEN_SPOTIFY,   KC_VOLU,        KC_VOLD,
        KC_TASK_MGR,    KC_EXPLORER,    KC_CAT_ANIM
    )
};

// Variables to keep track of the 10-second cat animation timer
uint32_t cat_anim_timer = 0;
bool show_cat_anim = false;

// 3. Define exactly what each macro button does when clicked
bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (record->event.pressed) {
        switch (keycode) {
            case LAUNCH_SLACK:
                // Sends Ctrl+Shift+Alt+Win+S to launch Slack
                SEND_STRING(SS_DOWN(X_LALT) SS_DOWN(X_LCTL) SS_DOWN(X_LSFT) SS_DOWN(X_LGUI) "s" 
                            SS_UP(X_LGUI) SS_UP(X_LSFT) SS_UP(X_LCTL) SS_UP(X_LALT));
                return false;

            case OPEN_TINKERCAD:
                // Opens Windows Run prompt, types URL, and presses Enter
                SEND_STRING(SS_DOWN(X_LGUI) "r" SS_UP(X_LGUI));
                qmk_delay_ms(150);
                SEND_STRING("https://tinkercad.com\n");
                return false;

            case OPEN_SPOTIFY:
                // Opens Windows Run prompt, types URL, and presses Enter
                SEND_STRING(SS_DOWN(X_LGUI) "r" SS_UP(X_LGUI));
                qmk_delay_ms(150);
                SEND_STRING("https://spotify.com\n");
                return false;

            case KC_CAT_ANIM:
                // Start the 10 second timer when Key 9 is pressed
                show_cat_anim = true;
                cat_anim_timer = timer_read32();
                return true;
        }
    }
    return true;
}

// 4. Windows Hotkeys mapped directly
#define KC_APP_KICAD       LWIN(KC_2)         // Assumes KiCad is the 2nd app on your Windows taskbar
#define KC_TASK_MGR        LCTL(LSFT(KC_ESC)) // Ctrl + Shift + Esc opens Task Manager
#define KC_EXPLORER        LWIN(KC_E)         // Win + E opens File Explorer
#define KC_CAT_ANIM        SAFE_RANGE + 3

// 5. OLED Screen Display Logic (Blank while idle, wakes for cat animation)
#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Turn off screen if 10 seconds (10000ms) pass
    if (show_cat_anim && timer_elapsed32(cat_anim_timer) > 10000) {
        show_cat_anim = false;
        oled_off(); 
    }

    if (show_cat_anim) {
        oled_on(); 
        
        // Alternates frames every 250ms to make the cat wave
        if ((timer_read32() / 250) % 2 == 0) {
            oled_write_P(PSTR("  /\\_/\\\n ( o.o )\n > ^ <_ \n"), false); 
        } else {
            oled_write_P(PSTR("  /\\_/\\\n ( o.o )/\n > ^ <  \n"), false); 
        }
    } else {
        oled_off(); // Keeps screen completely dark while idle
    }
    return false;
}
#endif
