from tkinter import *
from tkinter import messagebox, scrolledtext, filedialog
from mydb import Database
from myapi import API
import json
from datetime import datetime


class NLPApp:

    def __init__(self):
        # Create db and api objects
        self.dbo = Database()
        self.apio = API()

        # Store current user
        self.current_user = None

        # Main window setup
        self.root = Tk()
        self.root.title('NLPApp - Smart Text Analysis')
        try:
            self.root.iconbitmap('resources/favicon.ico')
        except:
            pass  # Icon file not required
        self.root.geometry('550x750')
        self.root.configure(bg='#2C3E50')
        self.root.resizable(False, False)

        self.login_gui()
        self.root.mainloop()

    def add_footer(self):
        """Add interactive footer"""
        footer = Label(self.root, text='✨ Made by Mahi ✨',
                       bg='#2C3E50', fg='#95A5A6',
                       font=('Arial', 9, 'bold italic'),
                       cursor='hand2')
        footer.place(relx=1.0, rely=1.0, anchor=SE, x=-15, y=-8)

        # Hover effect
        def on_enter(e):
            footer.config(fg='#3498DB', font=('Arial', 10, 'bold italic'))

        def on_leave(e):
            footer.config(fg='#95A5A6', font=('Arial', 9, 'bold italic'))

        footer.bind("<Enter>", on_enter)
        footer.bind("<Leave>", on_leave)

    def create_styled_button(self, parent, text, command, color='#3498DB', width=None):
        """Create modern styled buttons with hover effects"""
        btn = Button(parent, text=text, command=command,
                     bg=color, fg='white',
                     font=('Arial', 11, 'bold'),
                     relief=FLAT,
                     activebackground=self.darken_color(color),
                     activeforeground='white',
                     cursor='hand2',
                     padx=20, pady=10,
                     width=width)

        # Hover effects
        darker = self.darken_color(color)
        btn.bind("<Enter>", lambda e: btn.config(bg=darker))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

        return btn

    def darken_color(self, color):
        """Darken a hex color for hover effect"""
        color_map = {
            '#3498DB': '#2980B9',
            '#27AE60': '#229954',
            '#9B59B6': '#8E44AD',
            '#E74C3C': '#C0392B',
            '#7F8C8D': '#5D6D7E',
            '#E67E22': '#D68910',
            '#1ABC9C': '#17A589'
        }
        return color_map.get(color, color)

    def login_gui(self):
        self.clear()
        self.current_user = None

        # Header Frame
        header_frame = Frame(self.root, bg='#1ABC9C', height=120)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        heading = Label(header_frame, text='🤖 NLPApp',
                        bg='#1ABC9C', fg='white',
                        font=('Arial', 32, 'bold'))
        heading.pack(pady=(20, 5))

        subheading = Label(header_frame, text='Smart Text Analysis Tool',
                           bg='#1ABC9C', fg='white',
                           font=('Arial', 13))
        subheading.pack()

        # Main content frame
        content_frame = Frame(self.root, bg='#34495E', relief=RIDGE, bd=2)
        content_frame.pack(pady=40, padx=50, fill=BOTH, expand=True)

        Label(content_frame, text='📧 Email Address',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(30, 5))

        self.email_input = Entry(content_frame, width=35,
                                 font=('Arial', 12),
                                 relief=SOLID, bd=1)
        self.email_input.pack(pady=5, ipady=10)
        self.email_input.focus()

        Label(content_frame, text='🔒 Password',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(20, 5))

        self.password_input = Entry(content_frame, width=35, show='●',
                                    font=('Arial', 12),
                                    relief=SOLID, bd=1)
        self.password_input.pack(pady=5, ipady=10)

        # Bind Enter key to login
        self.password_input.bind('<Return>', lambda e: self.perform_login())

        login_btn = self.create_styled_button(content_frame,
                                              '🚀 Login',
                                              self.perform_login,
                                              '#27AE60',
                                              width=20)
        login_btn.pack(pady=25)

        # Divider
        Label(content_frame, text='─────────  OR  ─────────',
              bg='#34495E', fg='#7F8C8D',
              font=('Arial', 10)).pack(pady=15)

        Label(content_frame, text='Don\'t have an account?',
              bg='#34495E', fg='#BDC3C7',
              font=('Arial', 10)).pack(pady=5)

        redirect_btn = self.create_styled_button(content_frame,
                                                 '📝 Create New Account',
                                                 self.register_gui,
                                                 '#9B59B6',
                                                 width=20)
        redirect_btn.pack(pady=(10, 30))
        self.add_footer()

    def register_gui(self):
        self.clear()

        # Header Frame
        header_frame = Frame(self.root, bg='#9B59B6', height=120)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        heading = Label(header_frame, text='📝 Create Account',
                        bg='#9B59B6', fg='white',
                        font=('Arial', 28, 'bold'))
        heading.pack(pady=(25, 5))

        subheading = Label(header_frame, text='Join NLPApp Today',
                           bg='#9B59B6', fg='white',
                           font=('Arial', 12))
        subheading.pack()

        # Main content frame
        content_frame = Frame(self.root, bg='#34495E', relief=RIDGE, bd=2)
        content_frame.pack(pady=30, padx=50, fill=BOTH, expand=True)

        Label(content_frame, text='👤 Full Name',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(25, 5))

        self.name_input = Entry(content_frame, width=35,
                                font=('Arial', 12),
                                relief=SOLID, bd=1)
        self.name_input.pack(pady=5, ipady=10)
        self.name_input.focus()

        Label(content_frame, text='📧 Email Address',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(15, 5))

        self.email_input = Entry(content_frame, width=35,
                                 font=('Arial', 12),
                                 relief=SOLID, bd=1)
        self.email_input.pack(pady=5, ipady=10)

        Label(content_frame, text='🔒 Password',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(15, 5))

        self.password_input = Entry(content_frame, width=35, show='●',
                                    font=('Arial', 12),
                                    relief=SOLID, bd=1)
        self.password_input.pack(pady=5, ipady=10)

        # Password hint
        Label(content_frame, text='💡 Use at least 6 characters',
              bg='#34495E', fg='#95A5A6',
              font=('Arial', 9, 'italic')).pack(pady=5)

        # Bind Enter key
        self.password_input.bind('<Return>', lambda e: self.perform_registration())

        register_btn = self.create_styled_button(content_frame,
                                                 '✅ Register',
                                                 self.perform_registration,
                                                 '#27AE60',
                                                 width=20)
        register_btn.pack(pady=25)

        # Divider
        Label(content_frame, text='─────────────────',
              bg='#34495E', fg='#7F8C8D',
              font=('Arial', 10)).pack(pady=10)

        Label(content_frame, text='Already have an account?',
              bg='#34495E', fg='#BDC3C7',
              font=('Arial', 10)).pack(pady=5)

        redirect_btn = self.create_styled_button(content_frame,
                                                 '🔙 Back to Login',
                                                 self.login_gui,
                                                 '#7F8C8D',
                                                 width=20)
        redirect_btn.pack(pady=(10, 25))
        self.add_footer()

    def home_gui(self):
        self.clear()

        # Header with user greeting
        header_frame = Frame(self.root, bg='#1ABC9C', height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        heading = Label(header_frame, text='🤖 NLPApp Dashboard',
                        bg='#1ABC9C', fg='white',
                        font=('Arial', 26, 'bold'))
        heading.pack(pady=(15, 5))

        if self.current_user:
            user_label = Label(header_frame, text=f'Welcome, {self.current_user}!',
                               bg='#1ABC9C', fg='white',
                               font=('Arial', 11))
            user_label.pack()

        # Cards Frame
        cards_frame = Frame(self.root, bg='#2C3E50')
        cards_frame.pack(pady=30, padx=30, fill=BOTH, expand=True)

        Label(cards_frame, text='Choose an Analysis Tool:',
              bg='#2C3E50', fg='white',
              font=('Arial', 13, 'bold')).pack(pady=(0, 15), anchor=W)

        # Feature Cards
        features = [
            ('😊 Sentiment Analysis',
             'Analyze if text is positive, negative, or neutral',
             self.sentiment_gui, '#3498DB'),
            ('🏷️ Named Entity Recognition',
             'Extract names, places, dates, and organizations',
             self.ner_gui, '#E67E22'),
            ('💭 Emotion Prediction',
             'Detect emotions like joy, anger, fear, and more',
             self.emotion_gui, '#9B59B6')
        ]

        for title, desc, command, color in features:
            card = self.create_feature_card(cards_frame, title, desc, command, color)
            card.pack(pady=8, fill=X)

        # Bottom buttons
        button_frame = Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=15)

        history_btn = self.create_styled_button(button_frame,
                                                '📜 View History',
                                                self.show_history,
                                                '#7F8C8D')
        history_btn.pack(side=LEFT, padx=5)

        logout_btn = self.create_styled_button(button_frame,
                                               '🚪 Logout',
                                               self.login_gui,
                                               '#E74C3C')
        logout_btn.pack(side=LEFT, padx=5)
        self.add_footer()

    def create_feature_card(self, parent, title, description, command, color):
        """Create an attractive feature card"""
        card = Frame(parent, bg='#34495E', relief=RAISED, bd=0,
                     highlightbackground=color, highlightthickness=3)

        content_frame = Frame(card, bg='#34495E')
        content_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

        title_label = Label(content_frame, text=title,
                            bg='#34495E', fg='white',
                            font=('Arial', 14, 'bold'))
        title_label.pack(anchor=W)

        desc_label = Label(content_frame, text=description,
                           bg='#34495E', fg='#BDC3C7',
                           font=('Arial', 10),
                           wraplength=400)
        desc_label.pack(anchor=W, pady=(5, 10))

        btn = Button(content_frame, text='Try Now →', command=command,
                     bg=color, fg='white',
                     font=('Arial', 10, 'bold'),
                     relief=FLAT, cursor='hand2',
                     padx=20, pady=8)
        btn.pack(anchor=E)

        darker = self.darken_color(color)
        btn.bind("<Enter>", lambda e: btn.config(bg=darker))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

        # Card hover effect
        def on_enter(e):
            card.config(highlightthickness=4)

        def on_leave(e):
            card.config(highlightthickness=3)

        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)
        for child in card.winfo_children():
            child.bind("<Enter>", on_enter)
            child.bind("<Leave>", on_leave)

        return card

    def sentiment_gui(self):
        self.clear()

        # Header
        header_frame = Frame(self.root, bg='#3498DB', height=90)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        Label(header_frame, text='😊 Sentiment Analysis',
              bg='#3498DB', fg='white',
              font=('Arial', 24, 'bold')).pack(pady=25)

        # Main content
        content_frame = Frame(self.root, bg='#2C3E50')
        content_frame.pack(pady=20, padx=30, fill=BOTH, expand=True)

        Label(content_frame, text='Enter your text below:',
              bg='#2C3E50', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(5, 5), anchor=W)

        # Text input with scrollbar
        text_frame = Frame(content_frame, bg='#2C3E50')
        text_frame.pack(fill=BOTH, expand=True, pady=5)

        self.sentiment_input = scrolledtext.ScrolledText(text_frame,
                                                         width=50, height=6,
                                                         font=('Arial', 11),
                                                         wrap=WORD,
                                                         relief=SOLID, bd=1)
        self.sentiment_input.pack(fill=BOTH, expand=True)
        self.sentiment_input.focus()

        # Character counter
        self.sentiment_counter = Label(content_frame,
                                       text='Words: 0 | Characters: 0',
                                       bg='#2C3E50', fg='#95A5A6',
                                       font=('Arial', 9))
        self.sentiment_counter.pack(pady=5, anchor=E)

        self.sentiment_input.bind('<KeyRelease>',
                                  lambda e: self.update_counter(self.sentiment_input,
                                                                self.sentiment_counter))

        # Example hint
        hint = "💡 Example: 'I absolutely love this amazing app! It's so helpful!'"
        Label(content_frame, text=hint,
              bg='#2C3E50', fg='#95A5A6',
              font=('Arial', 9, 'italic')).pack(pady=5)

        # Buttons
        button_frame = Frame(content_frame, bg='#2C3E50')
        button_frame.pack(pady=15)

        analyze_btn = self.create_styled_button(button_frame,
                                                '🔍 Analyze Sentiment',
                                                self.do_sentiment_analysis,
                                                '#27AE60')
        analyze_btn.pack(side=LEFT, padx=5)

        clear_btn = self.create_styled_button(button_frame,
                                              '🗑️ Clear',
                                              lambda: self.sentiment_input.delete('1.0', END),
                                              '#E67E22')
        clear_btn.pack(side=LEFT, padx=5)

        # Result frame
        result_frame = Frame(content_frame, bg='#34495E',
                             relief=GROOVE, bd=3)
        result_frame.pack(pady=15, fill=BOTH)

        Label(result_frame, text='📊 Analysis Result:',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(15, 5), anchor=W, padx=15)

        self.sentiment_result = Label(result_frame,
                                      text='Your result will appear here...',
                                      bg='#34495E', fg='#BDC3C7',
                                      font=('Arial', 16, 'bold'),
                                      wraplength=450,
                                      justify=LEFT)
        self.sentiment_result.pack(pady=20, padx=20)

        # Export button (initially hidden)
        self.sentiment_export_btn = self.create_styled_button(result_frame,
                                                              '💾 Export Result',
                                                              lambda: self.export_result('sentiment'),
                                                              '#7F8C8D')

        # Back button
        back_btn = self.create_styled_button(content_frame,
                                             '← Back to Home',
                                             self.home_gui,
                                             '#7F8C8D')
        back_btn.pack(pady=10)
        self.add_footer()

    def ner_gui(self):
        self.clear()

        # Header
        header_frame = Frame(self.root, bg='#E67E22', height=90)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        Label(header_frame, text='🏷️ Named Entity Recognition',
              bg='#E67E22', fg='white',
              font=('Arial', 22, 'bold')).pack(pady=25)

        # Main content
        content_frame = Frame(self.root, bg='#2C3E50')
        content_frame.pack(pady=20, padx=30, fill=BOTH, expand=True)

        Label(content_frame, text='Enter your text below:',
              bg='#2C3E50', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(5, 5), anchor=W)

        # Text input
        self.ner_input = scrolledtext.ScrolledText(content_frame,
                                                   width=50, height=6,
                                                   font=('Arial', 11),
                                                   wrap=WORD,
                                                   relief=SOLID, bd=1)
        self.ner_input.pack(pady=5, fill=BOTH, expand=True)
        self.ner_input.focus()

        # Character counter
        self.ner_counter = Label(content_frame,
                                 text='Words: 0 | Characters: 0',
                                 bg='#2C3E50', fg='#95A5A6',
                                 font=('Arial', 9))
        self.ner_counter.pack(pady=5, anchor=E)

        self.ner_input.bind('<KeyRelease>',
                            lambda e: self.update_counter(self.ner_input,
                                                          self.ner_counter))

        # Example hint
        hint = "💡 Example: 'Apple Inc. was founded by Steve Jobs in California on April 1, 1976.'"
        Label(content_frame, text=hint,
              bg='#2C3E50', fg='#95A5A6',
              font=('Arial', 9, 'italic'),
              wraplength=450).pack(pady=5)

        # Buttons
        button_frame = Frame(content_frame, bg='#2C3E50')
        button_frame.pack(pady=15)

        analyze_btn = self.create_styled_button(button_frame,
                                                '🔍 Extract Entities',
                                                self.do_ner,
                                                '#27AE60')
        analyze_btn.pack(side=LEFT, padx=5)

        clear_btn = self.create_styled_button(button_frame,
                                              '🗑️ Clear',
                                              lambda: self.ner_input.delete('1.0', END),
                                              '#E67E22')
        clear_btn.pack(side=LEFT, padx=5)

        # Result frame
        result_frame = Frame(content_frame, bg='#34495E',
                             relief=GROOVE, bd=3)
        result_frame.pack(pady=15, fill=BOTH, expand=True)

        Label(result_frame, text='📊 Extracted Entities:',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(15, 5), anchor=W, padx=15)

        # Scrollable result
        result_text_frame = Frame(result_frame, bg='#34495E')
        result_text_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        self.ner_result = scrolledtext.ScrolledText(result_text_frame,
                                                    width=50, height=8,
                                                    font=('Arial', 10),
                                                    bg='#34495E', fg='#BDC3C7',
                                                    relief=FLAT,
                                                    wrap=WORD)
        self.ner_result.pack(fill=BOTH, expand=True)
        self.ner_result.insert('1.0', 'Your results will appear here...')
        self.ner_result.config(state=DISABLED)

        # Export button
        self.ner_export_btn = self.create_styled_button(result_frame,
                                                        '💾 Export Result',
                                                        lambda: self.export_result('ner'),
                                                        '#7F8C8D')

        # Back button
        back_btn = self.create_styled_button(content_frame,
                                             '← Back to Home',
                                             self.home_gui,
                                             '#7F8C8D')
        back_btn.pack(pady=10)
        self.add_footer()

    def emotion_gui(self):
        self.clear()

        # Header
        header_frame = Frame(self.root, bg='#9B59B6', height=90)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        Label(header_frame, text='💭 Emotion Prediction',
              bg='#9B59B6', fg='white',
              font=('Arial', 24, 'bold')).pack(pady=25)

        # Main content
        content_frame = Frame(self.root, bg='#2C3E50')
        content_frame.pack(pady=20, padx=30, fill=BOTH, expand=True)

        Label(content_frame, text='Enter your text below:',
              bg='#2C3E50', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(5, 5), anchor=W)

        # Text input
        self.emotion_input = scrolledtext.ScrolledText(content_frame,
                                                       width=50, height=6,
                                                       font=('Arial', 11),
                                                       wrap=WORD,
                                                       relief=SOLID, bd=1)
        self.emotion_input.pack(pady=5, fill=BOTH, expand=True)
        self.emotion_input.focus()

        # Character counter
        self.emotion_counter = Label(content_frame,
                                     text='Words: 0 | Characters: 0',
                                     bg='#2C3E50', fg='#95A5A6',
                                     font=('Arial', 9))
        self.emotion_counter.pack(pady=5, anchor=E)

        self.emotion_input.bind('<KeyRelease>',
                                lambda e: self.update_counter(self.emotion_input,
                                                              self.emotion_counter))

        # Example hint
        hint = "💡 Example: 'I'm so excited and happy! This is the best day ever!'"
        Label(content_frame, text=hint,
              bg='#2C3E50', fg='#95A5A6',
              font=('Arial', 9, 'italic')).pack(pady=5)

        # Buttons
        button_frame = Frame(content_frame, bg='#2C3E50')
        button_frame.pack(pady=15)

        analyze_btn = self.create_styled_button(button_frame,
                                                '🔍 Predict Emotion',
                                                self.do_emotion_prediction,
                                                '#27AE60')
        analyze_btn.pack(side=LEFT, padx=5)

        clear_btn = self.create_styled_button(button_frame,
                                              '🗑️ Clear',
                                              lambda: self.emotion_input.delete('1.0', END),
                                              '#E67E22')
        clear_btn.pack(side=LEFT, padx=5)

        # Result frame
        result_frame = Frame(content_frame, bg='#34495E',
                             relief=GROOVE, bd=3)
        result_frame.pack(pady=15, fill=BOTH, expand=True)

        Label(result_frame, text='📊 Detected Emotions:',
              bg='#34495E', fg='white',
              font=('Arial', 11, 'bold')).pack(pady=(15, 5), anchor=W, padx=15)

        self.emotion_result = Label(result_frame,
                                    text='Your results will appear here...',
                                    bg='#34495E', fg='#BDC3C7',
                                    font=('Arial', 11),
                                    wraplength=450,
                                    justify=LEFT)
        self.emotion_result.pack(pady=20, padx=20)

        # Export button
        self.emotion_export_btn = self.create_styled_button(result_frame,
                                                            '💾 Export Result',
                                                            lambda: self.export_result('emotion'),
                                                            '#7F8C8D')

        # Back button
        back_btn = self.create_styled_button(content_frame,
                                             '← Back to Home',
                                             self.home_gui,
                                             '#7F8C8D')
        back_btn.pack(pady=10)
        self.add_footer()

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get("1.0", END).strip()

        if not text:
            messagebox.showwarning('⚠️ Empty Input',
                                   'Please enter some text to analyze!')
            return

        if len(text) < 3:
            messagebox.showwarning('⚠️ Too Short',
                                   'Please enter at least a few words!')
            return

        try:
            result = self.apio.sentiment_analysis(text)
            sentiment_data = result['sentiment']

            # Emoji mapping
            emoji_map = {
                'Positive': '😊',
                'Negative': '😞',
                'Neutral': '😐'
            }

            sentiment = sentiment_data['sentiment']
            emoji = emoji_map.get(sentiment, '📊')
            confidence = sentiment_data['confidence']
            polarity = sentiment_data.get('polarity', 0)

            txt = f"{emoji} {sentiment}\n\nConfidence: {confidence}\nPolarity Score: {polarity}"

            self.sentiment_result['text'] = txt

            # Color coding
            color_map = {
                'Positive': '#2ECC71',
                'Negative': '#E74C3C',
                'Neutral': '#F39C12'
            }
            self.sentiment_result['fg'] = color_map.get(sentiment, 'white')

            # Show export button
            self.sentiment_export_btn.pack(pady=(0, 15))

            # Save to history
            self.save_to_history('Sentiment Analysis', text, txt)

        except Exception as e:
            messagebox.showerror('❌ Error', f'An error occurred: {str(e)}')

    def do_ner(self):
        text = self.ner_input.get("1.0", END).strip()

        if not text:
            messagebox.showwarning('⚠️ Empty Input',
                                   'Please enter some text to analyze!')
            return

        if len(text) < 5:
            messagebox.showwarning('⚠️ Too Short',
                                   'Please enter more text for better results!')
            return

        try:
            result = self.apio.ner(text)
            entities = result['entities']

            self.ner_result.config(state=NORMAL)
            self.ner_result.delete('1.0', END)

            if entities:
                # Entity type emojis
                entity_emojis = {
                    'PERSON': '👤',
                    'ORG': '🏢',
                    'GPE': '🌍',
                    'DATE': '📅',
                    'TIME': '⏰',
                    'MONEY': '💰',
                    'PERCENT': '📊',
                    'FAC': '🏛️',
                    'LOC': '📍',
                    'PRODUCT': '📦',
                    'EVENT': '🎉',
                    'WORK_OF_ART': '🎨',
                    'LAW': '⚖️',
                    'LANGUAGE': '🗣️',
                    'NORP': '👥',
                    'CARDINAL': '🔢',
                    'ORDINAL': '#️⃣'
                }

                result_text = ""
                for entity_type, entity_list in entities.items():
                    emoji = entity_emojis.get(entity_type, '🏷️')
                    result_text += f"{emoji} {entity_type}:\n"
                    for entity in entity_list:
                        result_text += f"   • {entity}\n"
                    result_text += "\n"

                self.ner_result.insert('1.0', result_text)

                # Show export button
                self.ner_export_btn.pack(pady=(0, 15))

                # Save to history
                self.save_to_history('Named Entity Recognition', text, result_text)
            else:
                self.ner_result.insert('1.0',
                                       '❌ No entities found in the text.\n\nTry including names, places, dates, or organizations.')

            self.ner_result.config(state=DISABLED)

        except Exception as e:
            messagebox.showerror('❌ Error', f'An error occurred: {str(e)}')

    def do_emotion_prediction(self):
        text = self.emotion_input.get("1.0", END).strip()

        if not text:
            messagebox.showwarning('⚠️ Empty Input',
                                   'Please enter some text to analyze!')
            return

        if len(text) < 3:
            messagebox.showwarning('⚠️ Too Short',
                                   'Please enter at least a few words!')
            return

        try:
            result = self.apio.emotion_prediction(text)
            emotions = result['emotion']

            # Emotion emojis
            emotion_emojis = {
                'joy': '😄',
                'sadness': '😢',
                'anger': '😠',
                'fear': '😨',
                'surprise': '😲',
                'disgust': '🤢',
                'love': '❤️',
                'neutral': '😐'
            }

            txt = "Top Emotions Detected:\n\n"
            count = 0
            for emotion, score in emotions.items():
                emoji = emotion_emojis.get(emotion.lower(), '💭')
                txt += f"{emoji} {emotion.capitalize()}: {score}\n"
                count += 1
                if count == 5:  # Show top 5
                    break

            self.emotion_result['text'] = txt
            self.emotion_result['fg'] = '#2ECC71'

            # Show export button
            self.emotion_export_btn.pack(pady=(0, 15))

            # Save to history
            self.save_to_history('Emotion Prediction', text, txt)

        except Exception as e:
            messagebox.showerror('❌ Error', f'An error occurred: {str(e)}')

    def update_counter(self, text_widget, counter_label):
        """Update word and character counter"""
        text = text_widget.get("1.0", END).strip()
        words = len(text.split()) if text else 0
        chars = len(text)
        counter_label['text'] = f"Words: {words} | Characters: {chars}"

    def save_to_history(self, analysis_type, text, result):
        """Save analysis to history file"""
        try:
            history_entry = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'user': self.current_user,
                'type': analysis_type,
                'text': text[:200],  # Save first 200 chars
                'result': result[:500]  # Save first 500 chars of result
            }

            try:
                with open('history.json', 'r') as f:
                    history = json.load(f)
            except:
                history = []

            history.append(history_entry)

            # Keep only last 50 entries
            history = history[-50:]

            with open('history.json', 'w') as f:
                json.dump(history, f, indent=2)
        except:
            pass  # Silently fail if history can't be saved

    def show_history(self):
        """Show analysis history in a new window"""
        try:
            with open('history.json', 'r') as f:
                history = json.load(f)
        except:
            messagebox.showinfo('📜 History', 'No history available yet.')
            return

        if not history:
            messagebox.showinfo('📜 History', 'No history available yet.')
            return

        # Create history window
        history_window = Toplevel(self.root)
        history_window.title('Analysis History')
        history_window.geometry('600x500')
        history_window.configure(bg='#2C3E50')

        # Header
        Label(history_window, text='📜 Your Analysis History',
              bg='#2C3E50', fg='white',
              font=('Arial', 18, 'bold')).pack(pady=15)

        # Scrollable text area
        text_frame = Frame(history_window, bg='#2C3E50')
        text_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        history_text = scrolledtext.ScrolledText(text_frame,
                                                 width=70, height=20,
                                                 font=('Arial', 10),
                                                 bg='#34495E', fg='white',
                                                 wrap=WORD)
        history_text.pack(fill=BOTH, expand=True)

        # Display history (reverse order - newest first)
        for entry in reversed(history):
            if self.current_user and entry.get('user') != self.current_user:
                continue  # Only show current user's history

            history_text.insert(END, f"{'=' * 60}\n", 'separator')
            history_text.insert(END, f"🕐 {entry['timestamp']}\n", 'timestamp')
            history_text.insert(END, f"📋 Type: {entry['type']}\n", 'type')
            history_text.insert(END, f"\n📝 Text: {entry['text']}\n", 'text')
            history_text.insert(END, f"\n📊 Result: {entry['result']}\n\n", 'result')

        # Tags for styling
        history_text.tag_config('separator', foreground='#7F8C8D')
        history_text.tag_config('timestamp', foreground='#3498DB', font=('Arial', 9, 'bold'))
        history_text.tag_config('type', foreground='#2ECC71', font=('Arial', 10, 'bold'))
        history_text.tag_config('text', foreground='#ECF0F1')
        history_text.tag_config('result', foreground='#F39C12')

        history_text.config(state=DISABLED)

        # Close button
        close_btn = self.create_styled_button(history_window,
                                              '✖ Close',
                                              history_window.destroy,
                                              '#E74C3C')
        close_btn.pack(pady=15)

    def export_result(self, analysis_type):
        """Export analysis result to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=f"{analysis_type}_result.txt"
        )

        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"NLPApp - {analysis_type.title()} Result\n")
                    f.write(f"{'=' * 50}\n")
                    f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                    if analysis_type == 'sentiment':
                        text = self.sentiment_input.get("1.0", END).strip()
                        result = self.sentiment_result['text']
                    elif analysis_type == 'ner':
                        text = self.ner_input.get("1.0", END).strip()
                        result = self.ner_result.get("1.0", END).strip()
                    elif analysis_type == 'emotion':
                        text = self.emotion_input.get("1.0", END).strip()
                        result = self.emotion_result['text']

                    f.write(f"Input Text:\n{text}\n\n")
                    f.write(f"Analysis Result:\n{result}\n")

                messagebox.showinfo('✅ Success', 'Result exported successfully!')
            except Exception as e:
                messagebox.showerror('❌ Error', f'Failed to export: {str(e)}')

    def validate_email(self, email):
        """Validate email format"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def perform_registration(self):
        name = self.name_input.get().strip()
        email = self.email_input.get().strip()
        password = self.password_input.get()

        # Validation
        if not name:
            messagebox.showerror('❌ Error', 'Name cannot be empty!')
            return

        if len(name) < 2:
            messagebox.showerror('❌ Error', 'Please enter your full name!')
            return

        if not self.validate_email(email):
            messagebox.showerror('❌ Error', 'Please enter a valid email address!')
            return

        if len(password) < 6:
            messagebox.showerror('❌ Error', 'Password must be at least 6 characters long!')
            return

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('✅ Success',
                                f'Welcome {name}!\n\nYour account has been created successfully.\nYou can now login.')
            self.login_gui()
        else:
            messagebox.showerror('❌ Error',
                                 'This email is already registered!\n\nPlease use a different email or login.')

    def perform_login(self):
        email = self.email_input.get().strip()
        password = self.password_input.get()

        if not email or not password:
            messagebox.showerror('❌ Error', 'Please fill in all fields!')
            return

        response = self.dbo.search(email, password)

        if response:
            self.current_user = response  # response contains the name
            messagebox.showinfo('✅ Success', f'Welcome back, {self.current_user}!')
            self.home_gui()
        else:
            messagebox.showerror('❌ Error', 'Incorrect email or password!\n\nPlease try again.')

    def clear(self):
        """Clear all widgets from the window"""
        for widget in self.root.pack_slaves():
            widget.destroy()


if __name__ == '__main__':
    nlp = NLPApp()