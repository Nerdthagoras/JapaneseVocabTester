import Constants
import Functions
import Settings
import datetime
import pygame
import random
from tkinter import filedialog

class MenuState:
    def __init__(self):
        self.done = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #KEYDOWN
            if event.type == pygame.KEYDOWN:
                #Space Key
                if event.key == pygame.K_SPACE:
                    if Settings.file_path != "":
                        if Settings.Max_answers > len(Settings.all_questions):
                            Settings.reducedanswers = True
                            Settings.original_Max_answers = Settings.Max_answers
                            Settings.Max_answers = len(Settings.all_questions)
                        self.done = True
            #MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                #start
                if Settings.file_path != "":
                    if self.start_button.collidepoint(event.pos):
                        if Settings.Max_answers > len(Settings.all_questions):
                            Settings.reducedanswers = True
                            Settings.original_Max_answers = Settings.Max_answers                            
                            Settings.Max_answers = len(Settings.all_questions)
                        self.done = True
                #load
                if self.load_button.collidepoint(event.pos):
                    Settings.file_path = filedialog.askopenfilename()
                #sound
                if self.sound_toggle.collidepoint(event.pos):
                    if Settings.Sound:
                        Settings.Sound = False
                    else:
                        Settings.Sound = True
                #display
                if self.display_toggle.collidepoint(event.pos):
                    if Settings.Display:
                        Settings.Display = False
                    else:
                        Settings.Display = True
                #number of answers
                if self.answer_number.collidepoint(event.pos):
                    if Settings.Max_answers >= 9:
                        Settings.Max_answers = 2
                    else:
                        Settings.Max_answers += 1
                #test type
                if self.test_type.collidepoint(event.pos):
                    if Settings.Test >= 3:
                        Settings.Test = 1
                    else:
                        Settings.Test += 1
                #endless
                if self.Endless_button.collidepoint(event.pos):
                    if Settings.Endless == 1:
                        Settings.Endless = 0
                    else:
                        Settings.Endless = 1

    def update(self):
        gameover_state.done = False        
        file_name = Settings.file_path
        if file_name:
            Settings.all_questions = Functions.read_csv(file_name)

    def draw(self, screen):
        screen.fill(Constants.WHITE)

        # Load Button
        self.load_button_location = (10, 10, 200, 40)        
        self.load_button = pygame.Rect(self.load_button_location)
        load_text = Constants.small_font.render('Load', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.load_button, 2)
        screen.blit(load_text, (self.load_button_location[0]+10, self.load_button_location[1]+10))

        # Sound Button
        self.sound_toggle_location = (10, 50, 200, 40)
        self.sound_toggle = pygame.Rect(self.sound_toggle_location)
        sound_toggle_text = Constants.small_font.render('Sound', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.sound_toggle, 2)
        screen.blit(sound_toggle_text, (self.sound_toggle_location[0]+10, self.sound_toggle_location[1]+10))
        if Settings.Sound:
            sound_state = Constants.small_font.render('On', True, Constants.BLACK)
            screen.blit(sound_state, (75, 60))
        else:
            sound_state = Constants.small_font.render('Off', True, Constants.BLACK)
            screen.blit(sound_state, (75, 60))

        # Display Button
        self.display_toggle_location = (10, 90, 200, 40)
        self.display_toggle = pygame.Rect(self.display_toggle_location)
        display_toggle_text = Constants.small_font.render('Display', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.display_toggle, 2)
        screen.blit(display_toggle_text, (self.display_toggle_location[0]+10, self.display_toggle_location[1]+10))
        if Settings.Display:
            display_state = Constants.small_font.render('On', True, Constants.BLACK)
            screen.blit(display_state, (100, 100))
        else:
            display_state = Constants.small_font.render('Off', True, Constants.BLACK)
            screen.blit(display_state, (100, 100))

        # Answer Number Button
        self.answer_number_location = (10, 130, 200, 40)
        self.answer_number = pygame.Rect(self.answer_number_location)
        answer_number_text = Constants.small_font.render('Answers:', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.answer_number, 2)
        screen.blit(answer_number_text, (self.answer_number_location[0]+10,self.answer_number_location[1]+10))
        num_text = Constants.small_font.render(str(Settings.Max_answers), True, Constants.BLACK)
        screen.blit(num_text,(120, 140))

        # Test Type Button
        test_type_location = (10, 170, 200, 40)
        self.test_type = pygame.Rect(test_type_location)
        if Settings.Test == 1:
            test_type_text = Constants.small_font.render('Kanji -> English', True, Constants.BLACK)
        elif Settings.Test == 2:
            test_type_text = Constants.small_font.render('English -> Kanji', True, Constants.BLACK)
        elif Settings.Test == 3:
            test_type_text = Constants.small_font.render('Kanji -> Kana', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.test_type, 2)
        screen.blit(test_type_text, (test_type_location[0]+10,test_type_location[1]+10))

        # Endless Button
        Endless_location = (10, 210, 200, 40)
        self.Endless_button = pygame.Rect(Endless_location)
        if Settings.Endless == 1:
            Endless_text = Constants.small_font.render('Endless Mode ON', True, Constants.BLACK)
        else:
            Endless_text = Constants.small_font.render('Endless Mode OFF', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.Endless_button, 2)
        screen.blit(Endless_text, (Endless_location[0]+10,Endless_location[1]+10)) 

        # Start Button
        if Settings.file_path != "":
            self.start_button_location = (Constants.WIDTH // 2-75, Constants.HEIGHT //2-80, 150, 70)
            self.start_button = pygame.Rect(self.start_button_location)
            self.start_text = Constants.question_font.render('START', True, Constants.BLACK)
            pygame.draw.rect(screen, Constants.BLACK, self.start_button, 2)
            screen.blit(self.start_text, (self.start_button_location[0]+10, self.start_button_location[1]+10))                      

        font = pygame.font.Font(None, 36)
        if Settings.file_path == "":
            text = font.render("Please Load a file", True, Constants.BLACK)
        else:
            text = font.render("Press SPACE to start", True, Constants.BLACK)
        text_rect = text.get_rect(center=(Constants.WIDTH // 2, 160))
        screen.blit(text, text_rect)

        chosen_file = font.render(((Settings.file_path).split("/")[-1]).replace(".csv",""), True, Constants.BLACK)
        chosen_file_rect = chosen_file.get_rect(center=(Constants.WIDTH // 2, 200))
        screen.blit(chosen_file,chosen_file_rect)

    def sound(self):
        pass

class GameState:
    def __init__(self):
        self.done = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.collidepoint(event.pos):
                    self.question_end_time = datetime.datetime.now()
                    time_diff = self.question_end_time - self.question_start_time
                    Settings.time_to_answer += time_diff.seconds
                    Settings.shuff = True
                    self.done = True
                for i, option in enumerate(question.answers):
                    button = pygame.Rect(100, 150+i*Constants.answer_spacing, 500, Constants.answer_spacing)
                    if button.collidepoint(event.pos):
                        question.check_answer(option,Constants.screen)
                        self.question_end_time = datetime.datetime.now()
                        time_diff = self.question_end_time - self.question_start_time
                        Settings.time_to_answer += time_diff.seconds
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
                if event.key == pygame.K_r:
                    Settings.play_audio = True
                for i, option in enumerate(question.answers):
                    selected_option_index = event.key - pygame.K_0 - 1
                    if selected_option_index == i:
                        question.check_answer(option,Constants.screen)
                        self.question_end_time = datetime.datetime.now()
                        time_diff = self.question_end_time - self.question_start_time
                        Settings.time_to_answer += time_diff.seconds

    def update(self):
        question.generate_question()
        self.question_start_time = datetime.datetime.now()
        self.question_text = Constants.question_font.render(question.question, True, Constants.WHITE)
        self.helper_text = Constants.small_font.render(question.helper, True, Constants.WHITE)
        self.answer_texts = [Constants.medium_font.render(option, True, Constants.WHITE) for option in question.answers]

    def draw(self, screen):
        screen.fill(Constants.GRAY)
        if Settings.Display:
            Constants.screen.blit(self.question_text, ((Constants.WIDTH - self.question_text.get_width()) // 2, 50))
            Constants.screen.blit(self.helper_text, ((Constants.WIDTH - self.helper_text.get_width()) // 2, 110))

        for i, option_text in enumerate(self.answer_texts):
            button = pygame.Rect(100, 150+i*Constants.answer_spacing, 500, Constants.answer_spacing)
            ans_num_text = Constants.small_font.render(str(i+1), True, Constants.WHITE)
            pygame.draw.rect(screen, Constants.BLACK, button, 2)
            screen.blit(option_text, (110, 155+i*Constants.answer_spacing))
            screen.blit(ans_num_text, (button[2]+80,120+(i+1)*Constants.answer_spacing))

        # Define the quit button
        self.quit_button_location = (Constants.WIDTH - 95, Constants.HEIGHT - 45, 90, 40)
        self.quit_button = pygame.Rect(self.quit_button_location)
        quit_text = Constants.small_font.render('Quit', True, Constants.WHITE)
        pygame.draw.rect(screen, Constants.BLACK, self.quit_button, 2)
        screen.blit(quit_text, (self.quit_button_location[0]+10, self.quit_button_location[1]+10))

        if Settings.Endless == 0:
            score_text = Constants.small_font.render(f"Score: {Settings.score}/{len(Settings.all_questions)}", True, Constants.WHITE)
            screen.blit(score_text, (10,10,90,40))
        else:
            Endlessmode_text = Constants.small_font.render(f"Endless Mode", True, Constants.WHITE)
            screen.blit(Endlessmode_text, (10,10,90,40))

    def sound(self):
        if Settings.Sound:
            if Settings.play_audio:
                Functions.playaudio(question.helper,question.helper_lang)
                Settings.play_audio = False

class GameOverState:
    def __init__(self):
        self.done = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.collidepoint(event.pos):
                    self.done = True     
                if self.menu_button.collidepoint(event.pos):
                    Settings.all_questions = []
                    Settings.score = 0
                    Settings.question_num = 0
                    Settings.time_to_answer = 0
                    game_state.done = False
                    menu_state.done = False
                    self.done = True

    def update(self):
        Settings.play_audio = True
        if Settings.reducedanswers == True:
            Settings.Max_answers = Settings.original_Max_answers

    def draw(self, screen):
        screen.fill(Constants.WHITE)
        # Show Score
        score_text = Constants.question_font.render(f"You Scored {Settings.score} Points", True, Constants.BLACK)
        screen.blit(score_text, ((Constants.WIDTH - score_text.get_width()) // 2, 50))
        outof_text = Constants.question_font.render(f"Out of {len(Settings.all_questions)} Questions", True, Constants.BLACK)
        screen.blit(outof_text, ((Constants.WIDTH - outof_text.get_width()) // 2, 90))

        # Show total time
        timer_text = Constants.question_font.render(f"Total time to answer: {Settings.time_to_answer}s", True, Constants.BLACK)
        screen.blit(timer_text, ((Constants.WIDTH - timer_text.get_width()) // 2, 160))

        # Create end score based on Time an Points
        if Settings.score != 0:
            end_score = int(Settings.time_to_answer / Settings.score)
        else: 
            end_score = 0
        
        end_score_text = Constants.large_font.render(f"Quickness Score: {end_score}", True, Constants.BLACK)
        screen.blit(end_score_text, ((Constants.WIDTH - end_score_text.get_width()) // 2, 240))

        # Define the quit button
        self.quit_button_location = (Constants.WIDTH - 95, Constants.HEIGHT - 45, 90, 40)
        self.quit_button = pygame.Rect(self.quit_button_location)
        quit_text = Constants.small_font.render('Quit', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.quit_button, 2)
        screen.blit(quit_text, (self.quit_button_location[0]+10, self.quit_button_location[1]+10))

        # Define the menu button
        self.menu_button_location = (10, Constants.HEIGHT - 45, 90, 40)
        self.menu_button = pygame.Rect(self.menu_button_location)
        menu_text = Constants.small_font.render('Menu', True, Constants.BLACK)
        pygame.draw.rect(screen, Constants.BLACK, self.menu_button, 2)
        screen.blit(menu_text, (self.menu_button_location[0]+10, self.menu_button_location[1]+10))  

    def sound(self):
        pass

class Question:
    def __init__(self):
        pass
    
    def generate_question(self):
        self.kanji, self.kana, self.english = Settings.all_questions[Settings.question_num]
        if Settings.shuff:
            if Settings.Test == 1:
                self.question = self.kanji
                self.question_language = "ja"
                self.answers = [self.english]
                self.real_answer = self.english
                self.answer_lang = "en"
                self.helper = self.kana
                self.helper_lang = "ja"
                col = 2
            elif Settings.Test == 2:
                self.question = self.english
                self.question_language = "en"
                self.answers = [self.kanji]
                self.real_answer = self.kanji
                self.answer_lang = "ja"
                self.helper = self.kana
                self.helper_lang = "ja"
                col = 0
            elif Settings.Test == 3:
                self.question = self.kanji
                self.question_language = "ja"
                self.answers = [self.kana]
                self.real_answer = self.kana
                self.answer_lang = "ja"
                self.helper = self.english
                self.helper_lang = "en"                
                col = 1

            while len(self.answers) < Settings.Max_answers:
                random_answer = random.choice(Settings.all_questions)[col]
                if random_answer not in self.answers:
                    self.answers.append(random_answer)
                Settings.shuff = False
            random.shuffle(self.answers)

    def check_answer(self, selected_answer,screen):
        if selected_answer == self.real_answer:
            screen.fill(Constants.GREEN)
            # Correct answer 
            correct_text = Constants.question_font.render(selected_answer, True, Constants.WHITE)
            correct_text_rect = correct_text.get_rect()
            correct_text_rect.center = (Constants.WIDTH // 2, 100)
            screen.blit(correct_text, correct_text_rect)
            # Helper
            correct_text = Constants.question_font.render("("+self.helper+")", True, Constants.WHITE)
            correct_text_rect = correct_text.get_rect()
            correct_text_rect.center = (Constants.WIDTH // 2, 150)
            screen.blit(correct_text, correct_text_rect)
            # "Is Correct"
            correct_text = Constants.question_font.render("is Correct!", True, Constants.WHITE)
            correct_text_rect = correct_text.get_rect()
            correct_text_rect.center = (Constants.WIDTH // 2, 200)
            screen.blit(correct_text, correct_text_rect)
            # Update Screen and Play Audio
            pygame.display.update()
            Functions.playaudio(selected_answer, self.answer_lang)
            Functions.playaudio(self.helper,self.helper_lang)
            Functions.playaudio("is Correct","en")
            Settings.score += 1
        else:
            screen.fill(Constants.RED)
            # Your answer
            incorrect_text = Constants.question_font.render(selected_answer, True, Constants.WHITE)
            incorrect_text_rect = incorrect_text.get_rect()
            incorrect_text_rect.center = (Constants.WIDTH // 2, 100)
            screen.blit(incorrect_text, incorrect_text_rect)
            # "Is Wrong"
            incorrect_text = Constants.question_font.render("is Wrong :(", True, Constants.WHITE)
            incorrect_text_rect = incorrect_text.get_rect()
            incorrect_text_rect.center = (Constants.WIDTH // 2, 150)
            screen.blit(incorrect_text, incorrect_text_rect)
            # "The Correct Answer Is"
            incorrect_text = Constants.question_font.render("The Correct Answer is", True, Constants.WHITE)
            incorrect_text_rect = incorrect_text.get_rect()
            incorrect_text_rect.center = (Constants.WIDTH // 2, 200)
            screen.blit(incorrect_text, incorrect_text_rect)
            # The Question
            question_text = Constants.question_font.render(self.question, True, Constants.WHITE)
            question_text_rect = question_text.get_rect()
            question_text_rect.center = (Constants.WIDTH // 2, 300)
            screen.blit(question_text, question_text_rect)
            # The Correct Answer
            correct_text = Constants.question_font.render(self.real_answer, True, Constants.WHITE)
            correct_text_rect = correct_text.get_rect()
            correct_text_rect.center = (Constants.WIDTH // 2, 350)
            screen.blit(correct_text, correct_text_rect)
            # Helper Answer
            correct_text = Constants.question_font.render("("+self.helper+")", True, Constants.WHITE)
            correct_text_rect = correct_text.get_rect()
            correct_text_rect.center = (Constants.WIDTH // 2, 400)
            screen.blit(correct_text, correct_text_rect)
            # Update Screen and Play Audio            
            pygame.display.update()
            Functions.playaudio(selected_answer, self.answer_lang)
            Functions.playaudio("is wrong","en")
            Functions.playaudio("The correct answer is","en")
            Functions.playaudio(self.real_answer,self.answer_lang)
            Functions.playaudio(self.helper,self.helper_lang)
        if Settings.Endless == 1:
            Settings.question_num = random.randint(0,len(Settings.all_questions)-1)
        else:
            Settings.question_num += 1
        Settings.shuff = True
        Settings.play_audio = True
        if Settings.question_num >= len(Settings.all_questions):
            current_state.done = True

# Instantiate Classes
menu_state = MenuState()
game_state = GameState()
gameover_state = GameOverState()
question = Question()

# Set current state
current_state = menu_state