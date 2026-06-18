import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# catch_the_fruit_full.py
# Requires: pygame
# Save this file in a folder where you can create users.json (same folder).
# Run: python catch_the_fruit_full.py

import pygame
import random
import sys
import json
import os

pygame.init()

# ------------------------ Config ------------------------
WIDTH, HEIGHT = 800, 800
FPS = 60
USER_DB_FILE = "users.json"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflex Rumble - Start Playing and Learning✍")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
BUTTON_COLOR = (255, 105, 180)
GRAY = (220, 220, 220)
RED = (180, 0, 0)
BLUE = (0, 100, 200)
DARK = (40, 40, 40)
BG_MENU = (135, 206, 235)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)
big_font = pygame.font.SysFont("Arial", 36)

# Game parameters
basket_width = 120
basket_height = 22
basket_speed = 9
fruit_radius = 22

# GK Questions (question, [options], index_of_correct)
GK_QUESTIONS = [
    ("Who is the father of Computers?", ["Charles Babbage", "Einstein", "Newton", "Tesla"], 0),
    ("Capital of Japan?", ["Seoul", "Tokyo", "Bangkok", "Beijing"], 1),
    ("Largest ocean?", ["Atlantic", "Indian", "Pacific", "Arctic"], 2),
    ("Who wrote Ramayana?", ["Valmiki", "Tulsidas", "Kalidasa", "Ved Vyas"], 0),
    ("Fastest land animal?", ["Lion", "Cheetah", "Horse", "Tiger"], 1),
    ("What is H2O?", ["Oxygen", "Hydrogen", "Water", "Salt"], 2),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1),
    ("Father of Indian Constitution?", ["Gandhi", "Nehru", "B R Ambedkar", "Rajendra Prasad"], 2),
    ("National animal of India?", ["Elephant", "Lion", "Tiger", "Leopard"], 2),
    ("SI unit of electric current?", ["Volt", "Ampere", "Ohm", "Watt"], 1),
    ("Currency of Japan?", ["Yen", "Won", "Dollar", "Ruble"], 0),
    ("Largest planet in solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], 2),
    ("Who discovered gravity?", ["Einstein", "Newton", "Galileo", "Kepler"], 1),
    ("National bird of India?", ["Peacock", "Eagle", "Parrot", "Sparrow"], 0),
    ("Chemical symbol of Gold?", ["Ag", "Au", "Gd", "Go"], 1),
    ("Which gas is essential for respiration?", ["Carbon dioxide", "Nitrogen", "Oxygen", "Helium"], 2),
    ("How many continents are there?", ["5", "6", "7", "8"], 2),
    ("Smallest bone in human body?", ["Stapes", "Femur", "Ulna", "Radius"], 0),
    ("Capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], 2),
    ("Who wrote Indian National Anthem?", ["Tagore", "Bankim", "Gandhi", "Nehru"], 0),
    ("Largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippo"], 1),
    ("Instrument to measure earthquakes?", ["Barometer", "Thermometer", "Seismograph", "Anemometer"], 2),
    ("Hardest natural substance?", ["Iron", "Diamond", "Quartz", "Gold"], 1),
    ("National flower of India?", ["Rose", "Lotus", "Lily", "Tulip"], 1),
    ("Which organ purifies blood?", ["Heart", "Lungs", "Kidney", "Liver"], 2),
    ("Which planet is closest to Sun?", ["Earth", "Venus", "Mercury", "Mars"], 2),
    ("Boiling point of water?", ["90°C", "95°C", "100°C", "110°C"], 2),
    ("Who invented telephone?", ["Edison", "Bell", "Tesla", "Newton"], 1),
    ("Largest desert in the world?", ["Sahara", "Gobi", "Antarctica", "Thar"], 2),
    ("Currency of UK?", ["Euro", "Dollar", "Pound", "Franc"], 2),
    ("How many players in a cricket team?", ["9", "10", "11", "12"], 2),
    ("Brain of computer?", ["RAM", "CPU", "Hard Disk", "Monitor"], 1),
    ("Which gas is used in fire extinguisher?", ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], 2),
    ("Tallest mountain in the world?", ["K2", "Everest", "Kangchenjunga", "Makalu"], 1),
    ("National sport of India (commonly believed)?", ["Cricket", "Hockey", "Football", "Kabaddi"], 1),
    ("Which metal is liquid at room temperature?", ["Iron", "Mercury", "Aluminium", "Copper"], 1),
    ("Who painted Mona Lisa?", ["Picasso", "Van Gogh", "Leonardo da Vinci", "Michelangelo"], 2),
    ("Which vitamin is formed in sunlight?", ["A", "B", "C", "D"], 3),
    ("Longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], 1),
    ("Which country gifted Statue of Liberty?", ["Germany", "France", "Italy", "Spain"], 1),
    ("Largest continent?", ["Africa", "Asia", "Europe", "Australia"], 1),
    ("Which organ controls nervous system?", ["Heart", "Brain", "Liver", "Lungs"], 1),
    ("Which state has longest coastline in India?", ["Tamil Nadu", "Andhra Pradesh", "Gujarat", "Maharashtra"], 2),
    ("Unit of force?", ["Joule", "Newton", "Watt", "Pascal"], 1),
    ("Which ocean is smallest?", ["Indian", "Atlantic", "Pacific", "Arctic"], 3),
    ("First President of India?", ["Nehru", "Rajendra Prasad", "Radhakrishnan", "Zakir Husain"], 1)
]

QUESTION_BANK = {
    "General Knowledge": GK_QUESTIONS,
    "Science": [
        ("What is H2O?", ["Oxygen", "Hydrogen", "Water", "Salt"], 2),
        ("SI unit of electric current?", ["Volt", "Ampere", "Ohm", "Watt"], 1),
        ("Chemical symbol of Gold?", ["Ag", "Au", "Gd", "Go"], 1),
        ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1)
    ],
    "Maths": [
        ("What is 12 x 8?", ["96", "84", "72", "108"], 0),
        ("Square root of 144?", ["10", "11", "12", "13"], 2),
        ("Value of pi (approx)?", ["2.14", "3.14", "4.14", "5.14"], 1)
    ],
    "Computer Science": [
        ("Brain of computer?", ["RAM", "CPU", "Hard Disk", "Monitor"], 1),
        ("Python is a?", ["Language", "Browser", "OS", "Database"], 0),
        ("CPU stands for?", ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Control Processing Unit"], 0)
    ]
}

# ---------------------- Utilities -----------------------
def load_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    try:
        with open(USER_DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(users):
    try:
        with open(USER_DB_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)
    except Exception as e:
        print("Error saving users:", e)

def draw_button(surface, text, x, y, w, h, color=BUTTON_COLOR, text_color=WHITE):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, rect, border_radius=10)
    label = font.render(text, True, text_color)
    surface.blit(label, (x + w//2 - label.get_width()//2, y + h//2 - label.get_height()//2))
    return rect

def get_fruit_color(speed):
    if speed < 6:
        return (255, 0, 0)
    elif speed < 8:
        return (255, 140, 0)
    elif speed < 10:
        return (255, 255, 0)
    else:
        return (255, 0, 255)

# ---------------------- Game State ----------------------
def reset_game():
    return {
        "basket_x": WIDTH // 2 - basket_width // 2,
        "basket_y": HEIGHT - 80,
        "fruit_x": random.randint(fruit_radius, WIDTH - fruit_radius),
        "fruit_y": -fruit_radius,
        "fruit_speed": 5,
        "score": 0,
        "correct_q": 0,
        "wrong_q": 0,
        # wrong_details is a dict question_text -> correct_answer_text (no duplicates)
        "wrong_details": {}
    }

# --------------------- GK Question UI -------------------
def ask_gk_question(state, selected_category):
    """
    Single-question loop with 30s timer.
    - Correct: increments correct_q and returns "OK"
    - Wrong: increments wrong_q, adds unique wrong_details entry, shows feedback, then picks new question
    - Timeout: shows 'Time's up' briefly and picks new question
    - If user quits from question screen, returns "QUIT"
    """
    last_question = None
    while True:
        # pick different from last_question where possible
        question_pool = QUESTION_BANK[selected_category]
        choices = [q for q in question_pool if q is not last_question] if len(question_pool) > 1 else question_pool
        q, opts, ans = random.choice(choices)
        last_question = (q, opts, ans)

        # option rectangles
        option_rects = []
        opt_w, opt_h = 520, 68
        left_x = (WIDTH - opt_w) // 2
        for i in range(len(opts)):
            option_rects.append(pygame.Rect(left_x, 260 + i * (opt_h + 12), opt_w, opt_h))

        question_start = pygame.time.get_ticks()
        answered = False

        while not answered:
            elapsed_ms = pygame.time.get_ticks() - question_start
            remaining_ms = max(0, 30000 - elapsed_ms)
            remaining_s = remaining_ms // 1000

            # draw
            screen.fill(WHITE)
            title = big_font.render("Answer to Continue", True, BLUE)
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 40))

            q_surface = font.render(q if len(q) < 60 else q[:57] + "...", True, BLACK)
            screen.blit(q_surface, (WIDTH//2 - q_surface.get_width()//2, 130))

            timer_text = font.render(f"Time left: {remaining_s}s", True, BLACK)
            screen.blit(timer_text, (WIDTH - 200, 30))

            for i, op in enumerate(opts):
                rect = option_rects[i]
                pygame.draw.rect(screen, GRAY, rect, border_radius=8)
                txt = font.render(op, True, BLACK)
                screen.blit(txt, (rect.x + 18, rect.y + 18))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(option_rects):
                        if rect.collidepoint(event.pos):
                            if i == ans:
                                state["correct_q"] += 1
                                fb = font.render("Correct! Resuming...", True, (0, 140, 0))
                                screen.blit(fb, (WIDTH//2 - fb.get_width()//2, HEIGHT - 110))
                                pygame.display.update()
                                pygame.time.delay(700)
                                return "OK"
                            else:
                                state["wrong_q"] += 1
                                if q not in state["wrong_details"]:
                                    state["wrong_details"][q] = opts[ans]
                                fb = font.render(f"Wrong! Correct: {opts[ans]}", True, RED)
                                screen.blit(fb, (WIDTH//2 - fb.get_width()//2, HEIGHT - 110))
                                pygame.display.update()
                                pygame.time.delay(900)
                                answered = True
                                break

            if remaining_ms <= 0:
                msg = font.render("Time's up! Next question...", True, RED)
                screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT - 110))
                pygame.display.update()
                pygame.time.delay(700)
                answered = True
                break

            clock.tick(30)

# -------------------- Pause Menu -----------------------
def show_pause_menu(state, current_user, users):
    paused = True

    scroll_offset = 0
    LINE_HEIGHT = 70
    VISIBLE_LINES = 5

    wrong_items = list(state["wrong_details"].items())

    while paused:
        screen.fill((245, 245, 245))
        title = big_font.render("Paused", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 40))

        score_t = font.render(f"Your Score: {state['score']}", True, BLACK)
        screen.blit(score_t, (80, 120))

        high = users.get(current_user, {}).get("high_score", 0)
        high_t = font.render(f"Your Best Score: {high}", True, BLACK)
        screen.blit(high_t, (80, 160))

        corr_t = font.render(f"Number of Correct Answers: {state['correct_q']}", True, BLACK)
        screen.blit(corr_t, (80, 200))

        wrong_t = font.render(f"Number of Incorrect Answers: {state['wrong_q']}", True, BLACK)
        screen.blit(wrong_t, (80, 240))

        y = 300
        if wrong_items:
            sub = font.render("Questions you need to work on (scroll ↓):", True, BLACK)
            screen.blit(sub, (80, y))
            y += 40

            visible = wrong_items[
                scroll_offset : scroll_offset + VISIBLE_LINES
            ]

            for q_text, correct_ans in visible:
                q_line = font.render(
                    q_text if len(q_text) < 60 else q_text[:57] + "...",
                    True,
                    DARK
                )
                ans_line = font.render(f"Correct: {correct_ans}", True, RED)

                screen.blit(q_line, (80, y))
                screen.blit(ans_line, (80, y + 28))
                y += LINE_HEIGHT
        else:
            none_t = font.render("No wrong questions yet. Nice!", True, DARK)
            screen.blit(none_t, (80, 300))

        resume_btn = draw_button(
            screen, "Resume",
            WIDTH//2 - 120, HEIGHT - 110,
            240, 60
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # scroll up
                    scroll_offset = max(0, scroll_offset - 1)

                if event.button == 5:  # scroll down
                    max_scroll = max(0, len(wrong_items) - VISIBLE_LINES)
                    scroll_offset = min(max_scroll, scroll_offset + 1)

                if resume_btn.collidepoint(event.pos):
                    paused = False

        clock.tick(30)

    return "OK"


# ------------------ Sign In / Sign Up / Delete UI ----------------
def input_box_loop(prompt, hidden=False):
    text = ""
    while True:
        screen.fill(WHITE)
        prompt_surf = font.render(prompt, True, BLACK)
        screen.blit(prompt_surf, (WIDTH//2 - prompt_surf.get_width()//2, 200))

        box = pygame.Rect(WIDTH//2 - 200, 260, 400, 50)
        pygame.draw.rect(screen, GRAY, box, border_radius=8)
        disp = ("*" * len(text)) if hidden else text
        txt_surf = font.render(disp, True, BLACK)
        screen.blit(txt_surf, (box.x + 12, box.y + 12))

        inst = font.render("Press Enter to Continue | Esc to go back.", True, DARK)
        screen.blit(inst, (WIDTH//2 - inst.get_width()//2, box.y + 70))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if len(text) < 32 and event.unicode.isprintable():
                        text += event.unicode
        clock.tick(30)

def username_slider_draw(usernames, index):
    box_w, box_h = 320, 48
    x = WIDTH//2 - box_w//2
    y = 580

    # arrows
    left_rect = pygame.Rect(x - 50, y, 40, box_h)
    right_rect = pygame.Rect(x + box_w + 10, y, 40, box_h)

    pygame.draw.rect(screen, GRAY, left_rect, border_radius=6)
    pygame.draw.rect(screen, GRAY, right_rect, border_radius=6)

    screen.blit(font.render("<", True, BLACK),
                (left_rect.centerx - 8, left_rect.centery - 14))
    screen.blit(font.render(">", True, BLACK),
                (right_rect.centerx - 8, right_rect.centery - 14))

    # username box
    mid_rect = pygame.Rect(x, y, box_w, box_h)
    pygame.draw.rect(screen, WHITE, mid_rect, border_radius=8)

    name = usernames[index] if usernames else "No users"
    txt = font.render(name, True, BLACK)
    screen.blit(txt, (mid_rect.centerx - txt.get_width()//2,
                      mid_rect.centery - txt.get_height()//2))

    return left_rect, right_rect, mid_rect


# Dropdown UI for delete: Option B
def username_dropdown_draw(users, selected, open_dropdown):
    # draws a compact dropdown at center; returns rects for items if open
    base_w, base_h = 360, 48
    base_x = WIDTH//2 - base_w//2
    base_y = 340
    base_rect = pygame.Rect(base_x, base_y, base_w, base_h)
    pygame.draw.rect(screen, GRAY, base_rect, border_radius=8)
    label = font.render(selected if selected else "Select username...", True, BLACK)
    screen.blit(label, (base_x + 12, base_y + 12))

    arrow = font.render("▼" if not open_dropdown else "▲", True, BLACK)
    screen.blit(arrow, (base_x + base_w - 30, base_y + 12))

    item_rects = []
    if open_dropdown:
        max_display = 8
        usernames = list(users.keys())
        display = usernames[:max_display]
        box_h = 44
        for i, u in enumerate(display):
            r = pygame.Rect(base_x, base_y + base_h + 8 + i*(box_h+6), base_w, box_h)
            pygame.draw.rect(screen, WHITE, r, border_radius=6)
            txt = font.render(u, True, BLACK)
            screen.blit(txt, (r.x + 12, r.y + 10))
            item_rects.append((u, r))
    return base_rect, item_rects
def show_warning(message, delay=1200):
    screen.fill(WHITE)
    warn = font.render(message, True, RED)
    screen.blit(
        warn,
        (WIDTH//2 - warn.get_width()//2, HEIGHT//2 - warn.get_height()//2)
    )
    pygame.display.update()
    pygame.time.delay(delay)

def sign_in_up_delete_flow(users):
    usernames = list(users.keys())
    sel_index = 0

    while True:
        screen.fill(BG_MENU)

        # Title
        title = big_font.render("Reflex Rumble", True, BLUE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        info = font.render("Start Playing and Learning.", True, DARK)
        screen.blit(info, (WIDTH//2 - info.get_width()//2, 140))

        # Main buttons
        sign_in_btn = draw_button(screen, "Log In", WIDTH//2 - 260, 220, 200, 60)
        sign_up_btn = draw_button(screen, "Sign Up", WIDTH//2 + 60, 220, 200, 60)
        start_btn = draw_button(screen, "Start (As Guest)", WIDTH//2 - 120, 300, 240, 60)

        # ---- DELETE SECTION (BOTTOM) ----
        del_title = font.render("Delete Account", True, BLACK)
        screen.blit(del_title, (WIDTH//2 - del_title.get_width()//2, 540))

        left_btn, right_btn, mid_box = username_slider_draw(usernames, sel_index)

        del_btn = draw_button(
            screen,
            "Delete Selected",
            WIDTH//2 - 120,
            650,
            240,
            55,
            color=(200, 60, 60)
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if sign_in_btn.collidepoint(pos):
                    u = input_box_loop("Enter your Username:")
                    if u is None:
                        continue

                    if u not in users:
                        show_warning("Username does not exist! Please Sign Up!")
                        continue

                    p = input_box_loop("Enter your Password:", hidden=True)
                    if users[u]["password"] == p:
                        return u
                    else:
                        show_warning("Incorrect password.")


                elif sign_up_btn.collidepoint(pos):
                    while True:
                        u = input_box_loop("Choose a Username:")
                        if u is None:   # Esc pressed
                            break

                        if u in users:
                            show_warning("Username already exists! Choose another!")
                            continue

                        if not u.strip():
                            show_warning("Username cannot be empty!")
                            continue

                        p = input_box_loop("Choose a Password:", hidden=True)
                        if p is None:
                            break

                        users[u] = {"password": p, "high_score": 0}
                        save_users(users)
                        return u



                elif start_btn.collidepoint(pos):
                    guest = f"guest_{random.randint(1000,9999)}"
                    users.setdefault(guest, {"password": "", "high_score": 0})
                    save_users(users)
                    return guest

                elif left_btn.collidepoint(pos) and usernames:
                    sel_index = (sel_index - 1) % len(usernames)

                elif right_btn.collidepoint(pos) and usernames:
                    sel_index = (sel_index + 1) % len(usernames)

                elif del_btn.collidepoint(pos) and usernames:
                    uname = usernames[sel_index]
                    pwd = input_box_loop(f"Password for '{uname}':", hidden=True)
                    if pwd == users[uname]["password"]:
                        del users[uname]
                        save_users(users)
                        usernames = list(users.keys())
                        sel_index = 0

        clock.tick(30)



def select_quiz_category():
    categories = list(QUESTION_BANK.keys())

    while True:
        screen.fill(BG_MENU)

        title = big_font.render("Select Quiz Category", True, BLUE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        buttons = []

        for i, category in enumerate(categories):
            btn = draw_button(
                screen,
                category,
                WIDTH//2 - 180,
                220 + i * 90,
                360,
                60
            )
            buttons.append((btn, category))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn, category in buttons:
                    if btn.collidepoint(event.pos):
                        return category

        clock.tick(30)


# ----------------------- Main Flow & Game Loop ----------------------
def main():
    users = load_users()
    current_user = sign_in_up_delete_flow(users)
    if current_user is None:
        pygame.quit()
        sys.exit()

    # Start screen
    while True:
        screen.fill(BG_MENU)
        title = big_font.render("Reflex Rumble", True, DARK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        login_info = font.render(f"Signed in as: {current_user}", True, BLACK)
        screen.blit(login_info, (WIDTH//2 - login_info.get_width()//2, 150))

        high = users.get(current_user, {}).get("high_score", 0)
        best_info = font.render(f"Your Highest Score: {high}", True, BLACK)
        screen.blit(best_info, (WIDTH//2 - best_info.get_width()//2, 190))

        start_btn = draw_button(screen, "Start Game", WIDTH//2 - 140, 300, 280, 70)
        logout_btn = draw_button(screen, "Log Out", WIDTH//2 - 80, 400, 160, 60)
        quit_btn = draw_button(screen, "Quit", WIDTH//2 - 80, 480, 160, 60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_users(users)
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    selected_category = select_quiz_category()
                    if selected_category:
                        run_game_loop(users, current_user, selected_category)
                if logout_btn.collidepoint(event.pos):
                    # go back to sign in screen
                    current_user = sign_in_up_delete_flow(users)
                    if current_user is None:
                        save_users(users)
                        pygame.quit(); sys.exit()
                if quit_btn.collidepoint(event.pos):
                    save_users(users)
                    pygame.quit(); sys.exit()
        clock.tick(30)

def run_game_loop(users, current_user, selected_category):
    state = reset_game()
    user_record = users.get(current_user, {"password": "", "high_score": 0})
    running = True

    while running:
        # draw background
        screen.fill(BG_MENU)

        # Buttons
        exit_button = draw_button(screen, "Exit", 20, 20, 120, 50)
        pause_button = draw_button(screen, "Pause", WIDTH - 170, 20, 150, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if state["score"] > user_record.get("high_score", 0):
                    users[current_user]["high_score"] = state["score"]
                    save_users(users)
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.collidepoint(event.pos):
                    res = show_pause_menu(state, current_user, users)
                    if res == "QUIT":
                        running = False
                        break
                if exit_button.collidepoint(event.pos):
                    if state["score"] > user_record.get("high_score", 0):
                        users[current_user]["high_score"] = state["score"]
                        save_users(users)
                    running = False
                    break

        if not running:
            break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and state["basket_x"] > 0:
            state["basket_x"] -= basket_speed
        if keys[pygame.K_RIGHT] and state["basket_x"] < WIDTH - basket_width:
            state["basket_x"] += basket_speed

        state["fruit_y"] += state["fruit_speed"]

        if state["fruit_y"] > HEIGHT:
            # reset fruit then require correct answer to continue
            state["fruit_y"] = -fruit_radius
            state["fruit_x"] = random.randint(fruit_radius, WIDTH - fruit_radius)
            result = ask_gk_question(state, selected_category)
            if result == "QUIT":
                if state["score"] > user_record.get("high_score", 0):
                    users[current_user]["high_score"] = state["score"]
                    save_users(users)
                running = False
                break

        # Catch detection
        if (state["basket_y"] < state["fruit_y"] + fruit_radius < state["basket_y"] + basket_height and
            state["basket_x"] < state["fruit_x"] < state["basket_x"] + basket_width):
            state["score"] += 1
            state["fruit_y"] = -fruit_radius
            state["fruit_x"] = random.randint(fruit_radius, WIDTH - fruit_radius)
            state["fruit_speed"] += 0.2

            # update high score live
            if state["score"] > user_record.get("high_score", 0):
                users[current_user]["high_score"] = state["score"]
                save_users(users)
                user_record = users.get(current_user)

        # draw basket & fruit & HUD
        pygame.draw.rect(screen, GREEN, (state["basket_x"], state["basket_y"], basket_width, basket_height))
        fruit_color = get_fruit_color(state["fruit_speed"])
        pygame.draw.circle(screen, fruit_color, (state["fruit_x"], int(state["fruit_y"])), fruit_radius)

        score_text = font.render(f"Score: {state['score']}", True, BLACK)
        screen.blit(score_text, (10, HEIGHT - 40))

        cur_best = users.get(current_user, {}).get("high_score", 0)
        best_text = font.render(f"Best: {cur_best}", True, DARK)
        screen.blit(best_text, (10, HEIGHT - 75))

        pygame.display.update()
        clock.tick(FPS)

    return

if __name__ == "__main__":
    main()
