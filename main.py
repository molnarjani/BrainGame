from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window
from kivy.properties import ObjectProperty,  NumericProperty, ReferenceListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import random



class AddButtonLayout(BoxLayout):

	Window.clearcolor = (0, 0.1686,0.2117,1)
	
	COLOR_NAME_TABLE = ('RED', 'GREEN','BLUE','YELLOW')
	COLOR_VALUE_TABLE = ((0.862,0.196,0.184), (0.521,0.6,0),(0.149,0.545,0.824),(0.710, 0.537, 0))
	
	hint_opacity = NumericProperty(1)
	counter = 0
	
	playerscore =  NumericProperty(0)
	
	#Middle text label properties:
	colortext =  ObjectProperty(None)
	random_value = NumericProperty(0)
	colorvalue1 = NumericProperty(0)
	colorvalue2 = NumericProperty(0)
	colorvalue3 = NumericProperty(0)
	colorvalue = ReferenceListProperty(colorvalue1, colorvalue2, colorvalue3)
	
	random_btn = NumericProperty(0)
	
	#Btn1(left) button properties:
	btn1_color = ObjectProperty(None)
	btn1_colorvalue1 = NumericProperty(0)
	btn1_colorvalue2 = NumericProperty(0)
	btn1_colorvalue3 = NumericProperty(0)
	btn1_text_color = ReferenceListProperty(btn1_colorvalue1, btn1_colorvalue2, btn1_colorvalue3)
	
	#Btn2(right) button properties:
	btn2_color = ObjectProperty(None)
	btn2_colorvalue1 = NumericProperty(0)
	btn2_colorvalue2 = NumericProperty(0)
	btn2_colorvalue3 = NumericProperty(0)
	btn2_text_color = ReferenceListProperty(btn2_colorvalue1, btn2_colorvalue2, btn2_colorvalue3)
	
	btn1_text = ObjectProperty(None)
	btn2_text = ObjectProperty(None)
	button_texts = ReferenceListProperty(btn1_text,btn2_text)
	
	def update(self, dt):
		self.counter += 1 / 60
		if self.counter > 10:
			self.hint_opacity *= 0.95

	def jarakeksz(self, text):
		if(text == 'RED' and (self.colorvalue1,self.colorvalue2,self.colorvalue3) == self.COLOR_VALUE_TABLE[0]):
			self.playerscore += 1
		elif(text == 'GREEN' and  (self.colorvalue1,self.colorvalue2,self.colorvalue3) == self.COLOR_VALUE_TABLE[1]):
			self.playerscore += 1
		elif(text == 'BLUE' and  (self.colorvalue1,self.colorvalue2,self.colorvalue3) == self.COLOR_VALUE_TABLE[2]):
			self.playerscore += 1
		elif(text == 'YELLOW' and  (self.colorvalue1,self.colorvalue2,self.colorvalue3) == self.COLOR_VALUE_TABLE[3]):
			self.playerscore += 1
		else:
			self.playerscore -= 1
			
	def select_random(self):
		#random color for middle label
		self.colortext = random.choice(self.COLOR_NAME_TABLE)
		self.random_value = random.randint(0,3)
		if self.random_value == 0:
			self.colorvalue1 = self.COLOR_VALUE_TABLE[0][0]
			self.colorvalue2 = self.COLOR_VALUE_TABLE[0][1]
			self.colorvalue3 = self.COLOR_VALUE_TABLE[0][2]
		elif self.random_value == 1:
			self.colorvalue1 = self.COLOR_VALUE_TABLE[1][0]
			self.colorvalue2 = self.COLOR_VALUE_TABLE[1][1]
			self.colorvalue3 = self.COLOR_VALUE_TABLE[1][2]
		elif self.random_value == 2:
			self.colorvalue1 = self.COLOR_VALUE_TABLE[2][0]
			self.colorvalue2 = self.COLOR_VALUE_TABLE[2][1]
			self.colorvalue3 = self.COLOR_VALUE_TABLE[2][2]
		elif self.random_value == 3:
			self.colorvalue1 = self.COLOR_VALUE_TABLE[3][0]
			self.colorvalue2 = self.COLOR_VALUE_TABLE[3][1]
			self.colorvalue3 = self.COLOR_VALUE_TABLE[3][2]
			
		#makes sure the buttons text labels never match
		self.random_btn = random.randint(0,1)
		if self.random_btn == 0:
			self.btn1_text = self.COLOR_NAME_TABLE[self.random_value] 
			self.btn2_text = random.choice(self.COLOR_NAME_TABLE)
		else:
			self.btn1_text = random.choice(self.COLOR_NAME_TABLE)
			self.btn2_text = self.COLOR_NAME_TABLE[self.random_value]
			
		#random color for btn1
		self.btn1_color = random.choice(self.COLOR_NAME_TABLE)
		if self.btn1_color == 'RED':
			self.btn1_colorvalue1 = self.COLOR_VALUE_TABLE[0][0]
			self.btn1_colorvalue2 = self.COLOR_VALUE_TABLE[0][1]
			self.btn1_colorvalue3 = self.COLOR_VALUE_TABLE[0][2]
		elif self.btn1_color == 'GREEN':
			self.btn1_colorvalue1 = self.COLOR_VALUE_TABLE[1][0]
			self.btn1_colorvalue2 = self.COLOR_VALUE_TABLE[1][1]
			self.btn1_colorvalue3 = self.COLOR_VALUE_TABLE[1][2]
		elif self.btn1_color == 'BLUE':
			self.btn1_colorvalue1 = self.COLOR_VALUE_TABLE[2][0]
			self.btn1_colorvalue2 = self.COLOR_VALUE_TABLE[2][1]
			self.btn1_colorvalue3 = self.COLOR_VALUE_TABLE[2][2]
		elif self.btn1_color == 'YELLOW':
			self.btn1_colorvalue1 = self.COLOR_VALUE_TABLE[3][0]
			self.btn1_colorvalue2 = self.COLOR_VALUE_TABLE[3][1]
			self.btn1_colorvalue3 = self.COLOR_VALUE_TABLE[3][2]
		
		#random color for btn2
		self.btn2_color = random.choice(self.COLOR_NAME_TABLE)
		if self.btn2_color == 'RED':
			self.btn2_colorvalue1 = self.COLOR_VALUE_TABLE[0][0]
			self.btn2_colorvalue2 = self.COLOR_VALUE_TABLE[0][1]
			self.btn2_colorvalue3 = self.COLOR_VALUE_TABLE[0][2]
		elif self.btn2_color == 'GREEN':
			self.btn2_colorvalue1 = self.COLOR_VALUE_TABLE[1][0]
			self.btn2_colorvalue2 = self.COLOR_VALUE_TABLE[1][1]
			self.btn2_colorvalue3 = self.COLOR_VALUE_TABLE[1][2]
		elif self.btn2_color == 'BLUE':
			self.btn2_colorvalue1 = self.COLOR_VALUE_TABLE[2][0]
			self.btn2_colorvalue2 = self.COLOR_VALUE_TABLE[2][1]
			self.btn2_colorvalue3 = self.COLOR_VALUE_TABLE[2][2]
		elif self.btn2_color == 'YELLOW':
			self.btn2_colorvalue1 = self.COLOR_VALUE_TABLE[3][0]
			self.btn2_colorvalue2 = self.COLOR_VALUE_TABLE[3][1]
			self.btn2_colorvalue3 = self.COLOR_VALUE_TABLE[3][2]
			
			
class BrainGame(App):
	def build(self):
		game = AddButtonLayout()
		game.select_random()
		Clock.schedule_interval(game.update, 1.0 / 60.0)
		return game
	
if __name__ == '__main__':
		BrainGame().run()