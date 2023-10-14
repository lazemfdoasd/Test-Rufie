# напиши здесь свое приложение
# программа с двумя экранами

import time

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from instruction import *
from ruffier import *
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.core.window import Window

p1 = 0
p2 = 0
p3 = 0



class Clock1(Label):
    a = NumericProperty(15)  
 
    def start(self):
        Animation.cancel_all(self)  
        self.anim = Animation(a = 0, duration = self.a)
        self.anim.start(self)
 
    def on_a(self, instance, value):
        self.text = str(round(value, 1))

class Clock2(Label):
    a = NumericProperty(45)  
 
    def start(self):
        Animation.cancel_all(self)  
        self.anim = Animation(a = 0, duration = self.a)
        self.anim.start(self)
 
    def on_a(self, instance, value):
        self.text = str(round(value, 1))

class Clock3(Label):
    a = NumericProperty(60)  
 
    def start(self):
        Animation.cancel_all(self)  
        self.anim = Animation(a = 0, duration = self.a)
        self.anim.start(self)
 
    def on_a(self, instance, value):
        self.text = str(round(value, 1))

class FirstScr(Screen):
    def __init__(self, name='first'):

        super().__init__(name=name)
        self.lab1 = Label(text = 'Предлагаем Вашему вниманию пройти тест Руфье и узнать уровень здоровья сердечно-сосудистой системы', pos_hint={'center_x': 0.4, 'center_y': 0.7}, text_size=(250, 300))

        self.btn1 = Button(text = 'Тест', size_hint=(.2, .2), pos_hint={'center_x': 0.8, 'center_y': 0.8})
        self.btn2 = Button(text = 'Инструкция', size_hint=(.2, .2), pos_hint={'center_x': 0.8, 'center_y': 0.5})
        self.btn3 = Button(text = 'Выход', size_hint=(.2, .2), pos_hint={'center_x': 0.8, 'center_y': 0.2})

        self.btn1.on_press = self.next
        self.btn2.on_press = self.ins
        self.btn3.on_press = self.exit

        self.add_widget(self.lab1) 
        self.add_widget(self.btn1) 
        self.add_widget(self.btn2) 
        self.add_widget(self.btn3) 

    def next(self):
        self.manager.transition.direction = 'left' 
                                                   
        self.manager.current = 'second'

    def ins(self):
        self.manager.transition.direction = 'left' 
                                                   
        self.manager.current = 'third'

    def exit(self):
        Window.close()



class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        
        btn1 = Button(text="Включить таймер", size_hint=(.2, .1), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        btn2 = Button(text="Далее", size_hint=(.2, .17), pos_hint={'center_x': 0.7, 'center_y': 0.2})

        btn1.on_press = self.timer
        btn2.on_press = self.next

        self.lab1 = Label(text="В спокойном состоянии измерьте пульс в течении 15 секунди запишите результат в окошке справа", text_size=(150, 150), pos_hint={'center_x': 0.3, 'center_y': 0.6})

        self.ti = TextInput(size_hint=(.2, .05), pos_hint={'center_x': 0.7, 'center_y': 0.35})

        self.clock = Clock1(pos_hint={'center_x': 0.7, 'center_y': 0.7})


        self.add_widget(btn1) 
        self.add_widget(btn2) 
        self.add_widget(self.lab1) 
        self.add_widget(self.ti) 
        self.add_widget(self.clock)

    def next(self):
        global p1
        p1 = int(self.ti.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'four'

    def timer(self):
        self.clock.start()

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name) 
        lab = Label(text = txt_instruction, pos_hint={'center_x': 0.52, 'center_y': 0.7})

        button1 = Button(text='Приступить к тесту', size_hint=(.2, .2), pos_hint={'center_x': 0.3, 'center_y': 0.2})
        button2 = Button(text='Назад', size_hint=(.2, .2), pos_hint={'center_x': 0.6, 'center_y': 0.2})

        button1.on_press = self.next
        button2.on_press = self.back

        self.add_widget(lab)
        self.add_widget(button1)
        self.add_widget(button2)

    def next(self):
        self.manager.transition.direction = 'left' 
                                                   
        self.manager.current = 'second'

    def back(self):
        self.manager.transition.direction = 'left' 
                                                   
        self.manager.current = 'first'

class FourScr(Screen):
    def __init__(self, name='four'):
        super().__init__(name=name)
        
        btn1 = Button(text="Включить таймер", size_hint=(.2, .1), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        btn3 = Button(text="Включить таймер на 45 секунд", size_hint=(.3, .1), pos_hint={'center_x': 0.4, 'center_y': 0.8})
        btn2 = Button(text="Далее", size_hint=(.2, .17), pos_hint={'center_x': 0.7, 'center_y': 0.2})

        btn1.on_press = self.timer1
        btn3.on_press = self.timer2
        btn2.on_press = self.next

        self.lab1 = Label(text="Теперь в течении 45 секунд выполняйте любую физическую нагрузку и опять измерьте пульс за 15 секунд. Результат внесите в окошко справа", text_size=(150, 150), pos_hint={'center_x': 0.2, 'center_y': 0.5})

        self.ti = TextInput(size_hint=(.2, .05), pos_hint={'center_x': 0.7, 'center_y': 0.35})

        self.clock = Clock1(pos_hint={'center_x': 0.7, 'center_y': 0.7})
        self.clock2 = Clock2(pos_hint={'center_x': 0.4, 'center_y': 0.7})

        self.add_widget(btn1) 
        self.add_widget(btn2) 
        self.add_widget(btn3) 
        self.add_widget(self.lab1) 
        self.add_widget(self.ti) 
        self.add_widget(self.clock)
        self.add_widget(self.clock2)

    def next(self):
        global p2
        p2 = int(self.ti.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'five'

    def timer1(self):
        self.clock.start()
 
    def timer2(self):
        self.clock2.start()

class FiveScr(Screen):
    def __init__(self, name='five'):
        super().__init__(name=name)
        
        btn1 = Button(text="Включить таймер", size_hint=(.2, .1), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        btn2 = Button(text="Далее", size_hint=(.2, .17), pos_hint={'center_x': 0.7, 'center_y': 0.2})

        btn1.on_press = self.timer
        btn2.on_press = self.next

        self.lab1 = Label(text="Теперь отдохните минуту, расслабьтесь, подумайте о чем-то хорошем и переходите к завершительному этапу", text_size=(150, 150), pos_hint={'center_x': 0.3, 'center_y': 0.6})

        
        self.clock = Clock3(pos_hint={'center_x': 0.7, 'center_y': 0.7})


        self.add_widget(btn1) 
        self.add_widget(btn2) 
        self.add_widget(self.lab1) 
        self.add_widget(self.clock)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'six'

    def timer(self):
        self.clock.start()

class SixScr(Screen):
    def __init__(self, name='six'):
        super().__init__(name=name)
        
        btn1 = Button(text="Включить таймер", size_hint=(.2, .1), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        btn2 = Button(text="Далее", size_hint=(.2, .17), pos_hint={'center_x': 0.7, 'center_y': 0.2})

        btn1.on_press = self.timer
        btn2.on_press = self.next

        self.lab1 = Label(text="Теперь снова измерьте пульс в течении 15 секунди запишите результат в окошке справа", text_size=(150, 150), pos_hint={'center_x': 0.3, 'center_y': 0.6})

        self.ti = TextInput(size_hint=(.2, .05), pos_hint={'center_x': 0.7, 'center_y': 0.35})

        self.clock = Clock1(pos_hint={'center_x': 0.7, 'center_y': 0.7})


        self.add_widget(btn1) 
        self.add_widget(btn2) 
        self.add_widget(self.lab1) 
        self.add_widget(self.ti) 
        self.add_widget(self.clock)

    def next(self):
        global p3
        global itog 

        p3 = int(self.ti.text)
        self.manager.transition.direction = 'left'
        self.manager.current = 'final'
        itog = ((p1+p2+p3)*4-200)/10
    



    
    def timer(self):
        self.clock.start()




class Final(Screen):
    def __init__(self, name='final'):
        super().__init__(name=name)
        self.on_enter = self.test

    def test(self):
        self.lab = Label(text=f'Ваш результат: {itog}', pos_hint={'center_x': 0.3, 'center_y': 0.7})

        if itog >= 15:
            self.lab3 = Label(text=f'низкая. Срочно обратитесь к врачу!', pos_hint={'center_x': 0.3, 'center_y': 0.5})
        
        if itog < 15 and itog >= 11:
            self.lab3 = Label(text=f'удовлетворительная. Обратитесь к врачу!', pos_hint={'center_x': 0.3, 'center_y': 0.5})

        if itog < 11 and itog >= 6:
            self.lab3 = Label(text=f'средняя. Возможно, стоит дополнительно обследоваться у врача.', pos_hint={'center_x': 0.3, 'center_y': 0.5})

        if itog < 6 and itog >= 0.5:
            self.lab3 = Label(text=f'Выше среднего', pos_hint={'center_x': 0.3, 'center_y': 0.5})

        if itog < 0.5:
            self.lab3 = Label(text=f'Высокая', pos_hint={'center_x': 0.3, 'center_y': 0.5})

        self.btn1 = Button(text='Пройти тест еще раз', size_hint = (.2, .1), pos_hint={'center_x': 0.5, 'center_y': 0.1})

        self.btn1.on_press = self.test_zanovo

        self.add_widget(self.lab)
        self.add_widget(self.lab3)
        self.add_widget(self.btn1)

    def test_zanovo(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourScr())
        sm.add_widget(FiveScr())
        sm.add_widget(SixScr())  
        sm.add_widget(Final())  
        return sm



app = MyApp()

app.run()
